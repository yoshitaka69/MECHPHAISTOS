<template>
  <div id="app">
    <LissajousCurve />
  </div>
</template>

<script>
import LissajousCurve from './LissajousCurve.vue';

export default {
  name: 'App',
  components: {
    LissajousCurve,
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
