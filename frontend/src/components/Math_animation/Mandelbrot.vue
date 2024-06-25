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
        maxIterations: 100,
      };
    },
    mounted() {
      this.context = this.$refs.canvas.getContext('2d');
      this.context.fillStyle = 'black';
      this.context.fillRect(0, 0, this.width, this.height);
      this.drawMandelbrot();
    },
    methods: {
      drawMandelbrot() {
        for (let x = 0; x < this.width; x++) {
          for (let y = 0; y < this.height; y++) {
            const belongsToSet = this.checkMandelbrot(x / 200 - 2, y / 200 - 1);
            this.context.fillStyle = belongsToSet ? 'white' : 'black';
            this.context.fillRect(x, y, 1, 1);
          }
        }
      },
      checkMandelbrot(x, y) {
        let real = x;
        let imaginary = y;
        for (let i = 0; i < this.maxIterations; i++) {
          const tempReal = real * real - imaginary * imaginary + x;
          imaginary = 2 * real * imaginary + y;
          real = tempReal;
          if (real * imaginary > 5) {
            return false;
          }
        }
        return true;
      },
    },
  };
  </script>
  
  <style scoped>
  canvas {
    border: 1px solid #000;
  }
  </style>
  