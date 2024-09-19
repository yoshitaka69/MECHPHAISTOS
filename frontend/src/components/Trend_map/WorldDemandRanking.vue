<template>
    <div class="ranking-table">
      <h3>World Demand Ranking</h3>
      <table>
        <thead>
          <tr>
            <th>Country</th>
            <th>Demand</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in rankingData" :key="item.country">
            <td>{{ item.country }}</td>
            <td>{{ item.demand }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const rankingData = ref([
    { country: 'USA', demand: 1200 },
    { country: 'China', demand: 1100 },
    { country: 'Germany', demand: 900 },
    { country: 'Japan', demand: 800 },
    { country: 'India', demand: 700 }
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
  