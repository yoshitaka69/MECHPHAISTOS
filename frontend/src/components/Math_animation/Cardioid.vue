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
        a: 150,
        trail: [],
        maxTrailLength: 1000
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
        
        const theta = this.t;
        const r = this.a * (1 - Math.cos(theta));
        const x = this.width / 2 + r * Math.cos(theta);
        const y = this.height / 2 + r * Math.sin(theta);
  
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
  
        this.t += 0.01;
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
  