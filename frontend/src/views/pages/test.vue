<template>
    <div>
      <h1>Repair Cost Optimization</h1>
      <button @click="optimize">Optimize</button>
      <div v-if="result">
        <h2>Optimal Parameters</h2>
        <p>Failure Probability: {{ result.best_params[0] }}</p>
        <p>Impact of Failure: {{ result.best_params[1] }}</p>
        <p>Repair Cost: {{ result.best_params[2] }}</p>
        <p>Annual Repair Cost: {{ result.best_value }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { useUserStore } from '@/stores/userStore'; // ストアのパスに応じて適宜変更してください
  import { computed, ref } from 'vue';
  
  export default {
    setup() {
      const userStore = useUserStore();
      const companyCode = computed(() => userStore.companyCode);
      const year = new Date().getFullYear();
      const result = ref(null);
  
      const optimize = async () => {
        try {
          console.log('Optimization started');
          const response = await axios.post('http://localhost:8000/api/calculation/optimize-repair-cost/', {
            companyCode: companyCode.value,
            year: year
          });
          console.log('Optimization successful:', response.data);
          result.value = response.data;
        } catch (error) {
          console.error('Optimization failed:', error);
        }
      };
  
      return {
        companyCode,
        year,
        result,
        optimize
      };
    }
  };
  </script>
  