<template>
    <div id="app">
        <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
        <button @click="saveData">保存</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Handsontable from 'handsontable';
  import { defineComponent } from 'vue';
  import { HotTable } from '@handsontable/vue3';
  import { registerAllModules } from 'handsontable/registry';
  import 'handsontable/dist/handsontable.full.css';
  
  registerAllModules();
  
  export default defineComponent({
    components: {
        HotTable
    },
    data() {
        return {
            hotSettings: {
                data: [], // 初期データを空配列に設定
                colHeaders: ['TestNo', 'Name', 'Price', 'Quantity'], // TestNoを一番左に配置
                columns: [
                    { data: 'testNo', readOnly: true }, // TestNo列を読み取り専用に設定
                    { data: 'name' }, // 名前列
                    { data: 'price', type: 'numeric', numericFormat: { pattern: '0,0.00' } }, // 数値列 (Price)
                    { data: 'quantity', type: 'numeric' } // 数値列 (Quantity)
                ],
                rowHeaders: true,
                minSpareRows: 1,
                contextMenu: true
            }
        };
    },
    mounted() {
        this.fetchData(); // コンポーネントがマウントされたときにデータを取得
    },
    methods: {
        fetchData() {
            axios
                .get('http://127.0.0.1:8000/api/products/')
                .then((response) => {
                    console.log('Fetched data:', response.data); // データ取得のログ
                    this.hotSettings.data = response.data; // 取得したデータをテーブルに設定
                    this.$refs.hotTableComponent.hotInstance.loadData(this.hotSettings.data); // テーブルにデータをロード
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        },
  
        saveData() {
      const hotInstance = this.$refs.hotTableComponent.hotInstance;
      const dataToSave = hotInstance.getData().filter(row => row[1] || row[2] || row[3]);
  
      const formattedData = dataToSave.map(row => {
          const postData = {
              name: row[1],
              price: parseFloat(row[2]),
              quantity: parseInt(row[3])
          };
          if (row[0] !== null && row[0] !== undefined) {
              postData.testNo = row[0];
          }
          return postData;
      });
  
      axios
          .post('http://127.0.0.1:8000/api/products/', formattedData)
          .then(response => {
              console.log('Successfully processed data:', response.data);
              this.fetchData();  // テーブルを再度読み込み、削除が反映された最新の状態を取得
          })
          .catch(error => {
              if (error.response) {
                  console.error('Server responded with status code:', error.response.status);
                  console.error('Response data:', error.response.data);
              } else if (error.request) {
                  console.error('No response received:', error.request);
              } else {
                  console.error('Error in setting up the request:', error.message);
              }
          });
  }
  
    }
  });
  </script>
  
  <style scoped>
  button {
    margin-top: 20px;
    padding: 10px;
    background-color: #4caf50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>
  