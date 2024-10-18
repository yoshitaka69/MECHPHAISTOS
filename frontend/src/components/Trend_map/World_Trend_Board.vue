<template>
    <div class="ranking-table">
      <h3>World Trend Board</h3>
      <table>
        <thead>
          <tr>
            <th>Logo</th> <!-- LOGO項目を追加 -->
            <th>Parts Name</th>
            <th>Model</th>
            <th>Manufacturer</th>
            <th>Demand of count</th>
            <th>Trend</th>
            <th>Alert Date</th>
            <th>Country</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in trendData" :key="item.country">
            <td><img :src="item.logo" alt="Logo" class="logo-img" /></td> <!-- ロゴを表示 -->
            <td>{{ item.partsName }}</td>
            <td>{{ item.model }}</td>
            <td>{{ item.manufacturer }}</td>
            <td>{{ item.demandCount }}</td>
            <td>
              <span :style="{ color: getTrendColor(item.trendChange), fontSize: '24px', fontWeight: 'bold' }">
                {{ getTrendArrow(item.trendChange) }}
              </span>
            </td>
            <td>{{ item.alertDate }}</td>
            <td>{{ item.country }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  // サンプルデータ
  const trendData = ref([
    { logo: 'https://via.placeholder.com/50', partsName: 'Engine', model: 'X100', manufacturer: 'Company A', demandCount: 500, trendChange: 2, alertDate: '2024-10-15', country: 'USA' },
    { logo: 'https://via.placeholder.com/50', partsName: 'Battery', model: 'B200', manufacturer: 'Company B', demandCount: 400, trendChange: 1, alertDate: '2024-09-12', country: 'China' },
    { logo: 'https://via.placeholder.com/50', partsName: 'Brakes', model: 'Z300', manufacturer: 'Company C', demandCount: 350, trendChange: 0, alertDate: '2024-08-23', country: 'Germany' },
    { logo: 'https://via.placeholder.com/50', partsName: 'Transmission', model: 'T400', manufacturer: 'Company D', demandCount: 250, trendChange: -1, alertDate: '2024-07-18', country: 'Japan' },
    { logo: 'https://via.placeholder.com/50', partsName: 'Tires', model: 'Q500', manufacturer: 'Company E', demandCount: 300, trendChange: -2, alertDate: '2024-06-10', country: 'India' }
  ]);
  
  // トレンドの矢印を取得する関数
  const getTrendArrow = (change) => {
    if (change > 1) return '↑';        // 大きな上昇
    if (change === 1) return '↗';      // 小さな上昇
    if (change === 0) return '→';      // 変化なし
    if (change === -1) return '↘';     // 小さな下降
    return '↓';                        // 大きな下降
  };
  
  // 矢印の色を取得する関数
  const getTrendColor = (change) => {
    if (change > 1) return 'green';      // 大きな上昇: 緑
    if (change === 1) return 'yellow';   // 小さな上昇: 黄色
    if (change === 0) return 'gray';     // 変化なし: 灰色
    if (change === -1) return 'orange';  // 小さな下降: オレンジ
    return 'red';                        // 大きな下降: 赤
  };
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
  