<template>
    <div class="container">
      <!-- 描画ツールのボタン -->
      <div class="toolbar">
        <!-- 描画モードが選択されているボタンに "active" クラスを付与 -->
        <button :class="{ active: drawingMode === 'line' }" @click="setDrawingMode('line')">Draw Line</button>
        <button :class="{ active: drawingMode === 'spline' }" @click="setDrawingMode('spline')">Draw Spline</button>
        <button :class="{ active: drawingMode === 'circle' }" @click="setDrawingMode('circle')">Draw Circle</button>
        <button :class="{ active: drawingMode === 'rect' }" @click="setDrawingMode('rect')">Draw Rectangle</button>
        <button :class="{ active: drawingMode === 'text' }" @click="setDrawingMode('text')">Draw Text</button>
        <button @click="zoomIn">Zoom In</button>
        <button @click="zoomOut">Zoom Out</button>
      </div>
      <div class="main-content">
        <!-- キャンバスエリアとサイドバーは変更なし -->
        <div class="sidebar">
          <img :src="pumpIconSrc" @click="addPumpIconToCanvas" class="icon" alt="Pump Icon" />
        </div>
        <div class="canvas-container">
          <v-stage ref="stage" :config="stageConfig">
            <v-layer ref="layer">
              <v-rect :config="backgroundConfig" />
              <v-line v-for="(line, index) in lines" :key="index" :config="line" @dragend="onDragEnd(index, 'line')" draggable />
              <v-rect v-for="(rect, index) in rects" :key="index" :config="rect" @dragend="onDragEnd(index, 'rect')" draggable />
              <v-circle v-for="(circle, index) in circles" :key="index" :config="circle" @dragend="onDragEnd(index, 'circle')" draggable />
              <v-text v-for="(text, index) in texts" :key="index" :config="text" @dragend="onDragEnd(index, 'text')" draggable />
              <v-image v-for="(pump, index) in pumps" :key="index" :config="pump.config" @dragend="onDragEnd(index, 'pump')" />
            </v-layer>
          </v-stage>
        </div>
      </div>
  
      <!-- フッター領域に選択された描画モードを表示 -->
      <div class="footer">
        <p>現在の描画モード: <strong>{{ drawingModeDisplay }}</strong></p>
      </div>
    </div>
</template>

<script>
import pumpIcon from '@/assets/pump_icon.png';

export default {
    data() {
        return {
            // 初期データ設定
            stageConfig: {
                width: window.innerWidth - 100,
                height: window.innerHeight - 100, // フッター領域分の高さを引く
                scaleX: 1,
                scaleY: 1
            },
            backgroundConfig: {
                x: 0,
                y: 0,
                width: window.innerWidth - 100,
                height: window.innerHeight - 100, // フッター領域分の高さを引く
                fill: 'white'
            },
            drawingMode: 'none',
            isDrawing: false,
            lines: [],
            rects: [],
            circles: [],
            texts: [],
            pumps: [],
            currentShape: null,
            pumpIconSrc: pumpIcon
        };
    },

    computed: {
        // 描画モードを日本語表記で返すコンピューテッドプロパティ
        drawingModeDisplay() {
            switch (this.drawingMode) {
                case 'line':
                    return '線を描画';
                case 'spline':
                    return 'スプラインを描画';
                case 'circle':
                    return '円を描画';
                case 'rect':
                    return '矩形を描画';
                case 'text':
                    return 'テキストを描画';
                default:
                    return 'なし';
            }
        }
    },
    methods: {
        setDrawingMode(mode) {
            this.drawingMode = mode;
        },
        // キャンバス上にアイコンを配置するメソッド
        addPumpIconToCanvas() {
            const stage = this.$refs.stage.getStage();
            const pointerPosition = stage.getPointerPosition();
            const img = new window.Image();
            img.src = this.pumpIconSrc;
            img.onload = () => {
                this.pumps.push({
                    config: {
                        x: pointerPosition.x,
                        y: pointerPosition.y,
                        image: img,
                        width: 50,
                        height: 50,
                        draggable: true
                    }
                });
            };
        },
        // 描画開始時の処理
        startDrawing(e) {
            if (this.drawingMode === 'none') return;
            this.isDrawing = true;
            const stage = this.$refs.stage.getStage();
            const pointerPosition = stage.getPointerPosition();

            if (this.drawingMode === 'line' || this.drawingMode === 'spline') {
                this.currentShape = [{ x: pointerPosition.x, y: pointerPosition.y }];
            } else if (this.drawingMode === 'rect') {
                this.currentShape = {
                    x: pointerPosition.x,
                    y: pointerPosition.y,
                    width: 0,
                    height: 0,
                    fill: 'transparent',
                    stroke: 'black',
                    strokeWidth: 2
                };
                this.rects.push(this.currentShape);
            } else if (this.drawingMode === 'circle') {
                this.currentShape = {
                    x: pointerPosition.x,
                    y: pointerPosition.y,
                    radius: 0,
                    fill: 'transparent',
                    stroke: 'black',
                    strokeWidth: 2
                };
                this.circles.push(this.currentShape);
            } else if (this.drawingMode === 'text') {
                this.currentShape = {
                    x: pointerPosition.x,
                    y: pointerPosition.y,
                    text: 'Sample Text',
                    fontSize: 20,
                    fill: 'black'
                };
                this.texts.push(this.currentShape);
            }
        },
        // 描画中の処理
        draw(e) {
            if (!this.isDrawing) return;
            const stage = this.$refs.stage.getStage();
            const pointerPosition = stage.getPointerPosition();

            if (this.drawingMode === 'line' || this.drawingMode === 'spline') {
                const startX = this.currentShape[0].x;
                const startY = this.currentShape[0].y;

                if (this.drawingMode === 'line') {
                    const dx = Math.abs(pointerPosition.x - startX);
                    const dy = Math.abs(pointerPosition.y - startY);
                    if (dx > dy) {
                        pointerPosition.y = startY; // 水平線
                    } else {
                        pointerPosition.x = startX; // 垂直線
                    }
                }

                // 線やスプラインの形を更新
                this.currentShape.push({ x: pointerPosition.x, y: pointerPosition.y });
                this.lines = [
                    ...this.lines.slice(0, -1),
                    {
                        points: this.currentShape.flatMap((point) => [point.x, point.y]),
                        stroke: 'black',
                        strokeWidth: 2,
                        lineCap: 'round',
                        lineJoin: this.drawingMode === 'spline' ? 'round' : 'miter'
                    }
                ];
            } else if (this.drawingMode === 'rect') {
                const rect = this.currentShape;
                rect.width = pointerPosition.x - rect.x;
                rect.height = pointerPosition.y - rect.y;
            } else if (this.drawingMode === 'circle') {
                const circle = this.currentShape;
                const dx = pointerPosition.x - circle.x;
                const dy = pointerPosition.y - circle.y;
                circle.radius = Math.sqrt(dx * dx + dy * dy);
            }
        },
        // 描画終了時の処理
        endDrawing() {
            if (!this.isDrawing) return;
            this.isDrawing = false;

            if (this.drawingMode === 'line' || this.drawingMode === 'spline') {
                this.lines.push({
                    points: this.currentShape.flatMap((point) => [point.x, point.y]),
                    stroke: 'black',
                    strokeWidth: 2,
                    lineCap: 'round',
                    lineJoin: this.drawingMode === 'spline' ? 'round' : 'miter'
                });
            }

            this.currentShape = null;
        },
        onDragEnd(index, type) {
            const shape = this[type + 's'][index].config;
            const stage = this.$refs.stage.getStage();
            const pointerPosition = stage.getPointerPosition();
            shape.x = pointerPosition.x;
            shape.y = pointerPosition.y;
        },
        zoomIn() {
            this.stageConfig.scaleX *= 1.2;
            this.stageConfig.scaleY *= 1.2;
        },
        zoomOut() {
            this.stageConfig.scaleX /= 1.2;
            this.stageConfig.scaleY /= 1.2;
        }
    },
    mounted() {
        const stage = this.$refs.stage.getStage();
        stage.on('mousedown touchstart', this.startDrawing);
        stage.on('mousemove touchmove', this.draw);
        stage.on('mouseup touchend', this.endDrawing);
    }
};
</script>

<style>
body {
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.container {
    display: flex;
    flex-direction: column;
    width: 100vw;
    height: 100vh;
}

.toolbar {
    width: 100%;
    height: 50px;
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 10px;
    border-bottom: 1px solid black;
}

.main-content {
    display: flex;
    flex-grow: 1;
}

.sidebar {
    width: 100px;
    background-color: #f0f0f0;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 20px;
    height: 100%;
    border-right: 1px solid black;
}

.icon {
    width: 50px;
    height: 50px;
    margin-bottom: 20px;
    cursor: pointer;
}

.canvas-container {
    flex-grow: 1;
}

.footer {
    width: 100%;
    height: 50px;
    background-color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    border-top: 1px solid black;
}
</style>
