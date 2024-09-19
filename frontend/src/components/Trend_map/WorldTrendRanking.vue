<template>
    <div class="ranking-table">
      <h3>World Trend Ranking</h3>
      <table>
        <thead>
          <tr>
            <th>Country</th>
            <th>Trend</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in trendData" :key="item.country">
            <td>{{ item.country }}</td>
            <td>{{ item.trend }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const trendData = ref([
    { country: 'USA', trend: 150 },
    { country: 'China', trend: 130 },
    { country: 'Germany', trend: 110 },
    { country: 'Japan', trend: 95 },
    { country: 'India', trend: 85 }
  ]);
  </script>
  
  <style scoped>
  .ranking-table {
    padding: 10px;
    background-color: #333;
    border-radius: 8px;
    color: white;
    overflow: auto;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 8px 12px;
    text-align: left;
    color: yellow; /* フォントカラーを黄色に設定 */
  }
  
  th {
    background-color: #444;
  }
  
  tbody tr:nth-child(odd) {
    background-color: #555;
  }
  </style>
  