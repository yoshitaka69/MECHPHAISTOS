<template>
  <div id="app">
    <LissajousCurve />
    <RoseCurve /> 
    <Spirograph />
    <Cardioid />
    <Lemniscate />
    <Mandelbrot />
    <Astroid />
  </div>
</template>

<script>
import LissajousCurve from './LissajousCurve.vue';
import RoseCurve from './RoseCurve.vue';
import Spirograph from './Spirograph.vue';
import Cardioid from './Cardioid.vue';
import Lemniscate from './Lemniscate.vue';
import Mandelbrot from './Mandelbrot.vue';
import Astroid from './Astroid.vue';

export default {
  name: 'App',
  components: {
    LissajousCurve,
    RoseCurve,
    Spirograph,
    Cardioid,
    Lemniscate,
    Mandelbrot,
    Astroid,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
