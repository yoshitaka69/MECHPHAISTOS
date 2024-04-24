<template>
  <div id="hot"></div> <!-- Handsontableを表示するためのdiv -->
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue';
import Handsontable from 'handsontable'; // Handsontableライブラリをインポート
import 'handsontable/dist/handsontable.full.css'; // Handsontableのスタイルをインポート
import axios from 'axios'; // axiosライブラリをインポート、HTTPリクエストに使用

export default defineComponent({
  setup() {
    const hotInstance = ref(null); // Handsontableインスタンスを保持するためのref

    const headerMappings = { // 表示するヘッダー名をマッピングするオブジェクト
      "PPM0YearCost": "2024",
      "PPM1YearCostAgo": "2023",
      "PPM10YearCostAgo": "2014",
      // 他のマッピングも同様に
    };

    // データと初期ヘッダーを取得し、Handsontableを設定する非同期関数
    const loadData = async () => {
      try {
        const response = await axios.get('your/api/endpoint'); // APIからデータを取得
        const data = response.data; // レスポンスからデータを抽出
        const headers = Object.keys(data[0]); // データから列ヘッダーを抽出

        // Handsontableインスタンスを生成
        hotInstance.value = new Handsontable(document.getElementById('hot'), {
          data: data,
          colHeaders: headers,
          afterGetColHeader: (col, TH) => {
            // カスタムヘッダー名を設定するためのフック
            if (headers[col] in headerMappings) {
              TH.innerText = headerMappings[headers[col]];
            }
          },
          rowHeaders: true,
          width: '100%',
          height: 'auto',
          licenseKey: 'non-commercial-and-evaluation' // ライセンスキー設定
        });
      } catch (error) {
        console.error('Failed to load data:', error); // データロード失敗時のエラー処理
      }
    };

    onMounted(() => {
      loadData(); // コンポーネントがマウントされた後にデータロードを実行
    });

    return {
      hotInstance
    };
  }
});
</script>
