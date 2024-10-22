<template>
    <div class="card card-light-yellow custom-height"> <!-- 背景色を黄色に変更 -->
        <div class="flex-column justify-content-between mb-3" style="height: auto;">
            <ClockComponent />
            <div class="info-container">
                <div class="message-container">
                    <Button v-if="currentWarning === 'Warning'" label="Warning" class="warning-button" severity="danger" />
                    <Button v-else label="Be Safe" class="safe-button" severity="success" />
                </div>
                <div class="description-box">WarningTIME means when accidents and injuries occur the most</div>
            </div>
        </div>
    </div>
</template>

<script>
import ClockComponent from './ClockComponent.vue';
import Button from 'primevue/button';

export default {
    components: {
        ClockComponent,
        Button
    },
    data() {
        return {
            currentWarning: 'Be Safe'
        };
    },
    methods: {
        checkCurrentWarning() {
            const currentHour = new Date().getHours();
            const isInWarningZone = [
                { start: 7, end: 10 },
                { start: 15, end: 17 }
            ].some(zone => currentHour >= zone.start && currentHour < zone.end);
            this.currentWarning = isInWarningZone ? 'Warning' : 'Be Safe';
        }
    },
    mounted() {
        setInterval(() => {
            this.checkCurrentWarning();
        }, 1000);
    }
};
</script>

<style scoped>

/* カード全体の高さを設定 */
.custom-height {
    height: 250px; /* カスタム高さを指定 */
}

/* カード背景色 */
.card-light-yellow {
    background-color: #fffae6; /* 淡い黄色の背景色 */
}

/* ClockComponent のスタイル */
.clock-container {
    display: flex;
    align-items: center;
    width: 100%;
    height: 250px; /* 他のカードと高さを合わせる */
}

.clock-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #fff9c4;
    position: relative;
    padding: 2%;
    margin: 0 2%;
    flex: 1;
}

.clock-face {
    width: 100%;
    height: auto;
    background-color: #f0f0f0;
    border-radius: 50%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* 時計の針やテキストのスタイル */
.clock-border {
    fill: none;
    stroke: #333;
    stroke-width: 2;
}

.hand {
    stroke-linecap: round;
    transform-origin: center;
}

.hour-hand, .minute-hand, .second-hand {
    fill: #333;
}

.center-dot {
    fill: #333;
}

.hour-text {
    font-size: 0.6em;
    text-anchor: middle;
    fill: #333;
}

.warning-text {
    font-size: 0.55em;
    fill: #ff0000;
    font-weight: bold;
}

/* 他のカードコンポーネントのスタイル */
.large-bold-text {
    font-size: 4rem; /* 件数を大きく強調 */
    font-weight: bold; /* 太字 */
    margin-top: 1rem; /* 上に余白を追加して改行の間隔を調整 */
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 見出しを太字に設定 */
    font-size: 2rem; /* フォントサイズを大きく */
    color: black; /* 文字色を黒に設定 */
}

/* アイコンを中央に配置 */
.icon-wrapper {
    width: 3rem; 
    height: 3rem;
    margin-top: 1rem; /* 余白を追加 */
}

.pi-map-marker {
    font-size: 2rem; /* アイコンサイズ */
    color: orange; /* アイコンの色 */
}

/* アイコンと件数を横並びにするためのスタイル */
.pi-exclamation-circle {
    margin-right: 10px; /* アイコンとテキストの間に余白 */
}



</style>