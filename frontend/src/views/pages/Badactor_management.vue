<template>
    <div>
      <TargetPlot :sampleDataX="sampleDataX" :sampleDataY="sampleDataY" />
      <Histogram :sampleDataX="sampleDataX" />
    </div>
  </template>
  
  <script>
  import Histogram from '@/components/Badactor_management/Histogram.vue';
  import TargetPlot from '@/components/Badactor_management/TargetPlot.vue';
  
  export default {
    components: {
      Histogram,
      TargetPlot,
    },
    data() {
      return {
        sampleDataX: [],
        sampleDataY: [],
      };
    },
    mounted() {
      this.generateSampleData();
    },
    methods: {
      generateSampleData() {
        this.sampleDataX = Array.from({ length: 100 }, () => Math.random() * 2 - 1);
        this.sampleDataY = Array.from({ length: 100 }, () => Math.random() * 2 - 1);
      },
    },
  };
  </script>
  