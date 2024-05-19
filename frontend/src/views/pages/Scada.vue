<template>
  <div id="app">
    <Canvas />
    <Pipeline />
  </div>
</template>

<script>
import Canvas from './Canvas.vue';
import Pipeline from './Pipeline.vue';

export default {
  name: 'App',
  components: {
    Canvas,
    Pipeline
  }
};
</script>

<style>
#app {
  width: 100vw;
  height: 100vh;
  position: relative;
}
</style>
