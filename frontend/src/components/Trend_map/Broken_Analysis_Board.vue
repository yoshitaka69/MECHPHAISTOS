<template>
    <div class="ranking-table">
      <h3>Broken Analysis Board</h3>
      <table>
        <thead>
          <tr>
            <th>Logo</th> <!-- LOGO項目 -->
            <th>Parts Name</th>
            <th>Model</th>
            <th>Manufacturer</th>
            <th>Demand of count</th>
            <th>Country</th>
            <th>Situation</th> <!-- Situation項目 -->
            <th>Notes</th> <!-- 備考を英語に変更 -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in brokenData" :key="item.country">
            <td><img :src="item.logo" alt="Logo" class="logo-img" /></td> <!-- ロゴを表示 -->
            <td>{{ item.partsName }}</td>
            <td>{{ item.model }}</td>
            <td>{{ item.manufacturer }}</td>
            <td>{{ item.demandCount }}</td>
            <td>{{ item.country }}</td>
            <td>{{ item.situation }}</td> <!-- Situationを表示 -->
            <td>{{ item.notes }}</td> <!-- Notesを表示 -->
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  // サンプルデータ
  const brokenData = ref([
    { logo: 'https://via.placeholder.com/50', partsName: 'Engine', model: 'X100', manufacturer: 'Company A', demandCount: 500, country: 'USA', situation: 'Broken', notes: 'Under investigation' },
    { logo: 'https://via.placeholder.com/50', partsName: 'Battery', model: 'B200', manufacturer: 'Company B', demandCount: 400, country: 'China', situation: 'Fixed', notes: 'Replaced last month' },
    { logo: 'https://via.placeholder.com/50', partsName: 'Brakes', model: 'Z300', manufacturer: 'Company C', demandCount: 350, country: 'Germany', situation: 'Pending', notes: 'Repaired successfully' },
    { logo: 'https://via.placeholder.com/50', partsName: 'Transmission', model: 'T400', manufacturer: 'Company D', demandCount: 250, country: 'Japan', situation: 'Awaiting parts', notes: 'Waiting for parts' },
    { logo: 'https://via.placeholder.com/50', partsName: 'Tires', model: 'Q500', manufacturer: 'Company E', demandCount: 300, country: 'India', situation: 'Operational', notes: 'No issues reported' }
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
  
  h3 {
    color: yellow; /* タイトルのフォントカラーを黄色に設定 */
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 8px 12px;
    text-align: left;
    color: yellow; /* フォントカラーを黄色に設定 */
    border: 1px solid #777; /* セルに境界線を追加 */
  }
  
  th {
    background-color: #222; /* ヘッダーの背景色を濃く */
    border-bottom: 3px solid yellow; /* ヘッダーのボーダーを太くし、目立たせる */
  }
  
  tbody tr:nth-child(odd) {
    background-color: #555;
  }
  
  span {
    font-size: 24px; /* 矢印のフォントサイズを大きく */
    font-weight: bold; /* 矢印を太字にして強調 */
  }
  
  /* ロゴの画像をスタイル */
  .logo-img {
    width: 50px;
    height: 50px;
    object-fit: contain;
  }
  </style>
  