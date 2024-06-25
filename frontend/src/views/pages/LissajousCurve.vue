<template>
  <div>
    <canvas ref="canvas" :width="width" :height="height"></canvas>
  </div>
</template>

<script>
export default {
  data() {
    return {
      width: 800,
      height: 400,
      context: null,
      t: 0,
      A: 100,
      B: 100,
      a: 3,
      b: 2,
      delta: Math.PI / 2,
      trail: [],  // 軌跡を保存するための配列
      maxTrailLength: 1000 // 軌跡の最大長さ
    };
  },
  mounted() {
    this.context = this.$refs.canvas.getContext('2d');
    this.context.fillStyle = 'black';
    this.context.fillRect(0, 0, this.width, this.height);
    this.animate();
  },
  methods: {
    animate() {
      this.context.fillStyle = 'black';
      this.context.fillRect(0, 0, this.width, this.height);
      this.context.strokeStyle = 'white';
      this.context.beginPath();
      
      const x = this.width / 2 + this.A * Math.sin(this.a * this.t + this.delta);
      const y = this.height / 2 + this.B * Math.sin(this.b * this.t);

      this.trail.push({ x, y });
      if (this.trail.length > this.maxTrailLength) {
        this.trail.shift();
      }

      for (let i = 0; i < this.trail.length; i++) {
        const point = this.trail[i];
        if (i === 0) {
          this.context.moveTo(point.x, point.y);
        } else {
          this.context.lineTo(point.x, point.y);
        }
      }

      this.context.stroke();

      this.t += 0.02; // 時間の進行速度を調整
      requestAnimationFrame(this.animate);
    },
  },
};
</script>

<style scoped>
canvas {
  border: 1px solid #000;
}
</style>
