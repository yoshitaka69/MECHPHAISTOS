<template>
  <div id="SparePartsList">
      <!-- 成功時または失敗時のアラート表示 -->
      <Save_Alert v-if="showAlert" :type="alertType" :message="alertMessage" :errorMessages="errorMessages" />

      <div class="legend">
          <div class="legend-item">
              <div class="color-box" style="background-color: #f0a0a0"></div>
              <span>Form input format is incorrect</span>
          </div>
          <div class="legend-item">
              <div class="color-box" style="background-color: #f0f0f0"></div>
              <span>Input not allowed. Value is automatically filled.</span>
          </div>
      </div>

      <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>

      <div class="button-container">
          <input type="number" v-model="rowsToAdd" placeholder="Number of rows" />
          <Button label="Add Rows" icon="pi pi-plus" class="p-button-primary blue-button" @click="addRows" />
          <Button label="Save Data" icon="pi pi-save" class="p-button-primary blue-button ml-3" @click="saveData" />
      </div>
  </div>
</template>

<script>
import axios from 'axios';
import Handsontable from 'handsontable';
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
import Save_Alert from '@/components/Alert/Save_Alert.vue'; // 新しいアラートコンポーネントをインポート
import Button from 'primevue/button'; // PrimeVue Button コンポーネントをインポート

// register Handsontable's modules
registerAllModules();

function customRendererForAlertOrder(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments); // 常に基本のテキストレンダラーを適用
  if (value === 'order') {
      td.style.backgroundColor = '#FF0000'; // 注文が必要な場合は赤色
      td.style.color = 'black';
  } else if (value === 'ordered') {
      td.style.backgroundColor = '#00FF00'; // 注文済みの場合は緑色
      td.style.color = 'black';
  } else if (cellProperties.readOnly) {
      td.style.backgroundColor = '#f5f5f5'; // 読み取り専用のセルは薄い灰色
  }
}

function imageRenderer(instance, td, row, col, prop, value, cellProperties) {
  td.innerHTML = ''; // セルをクリア

  const partsNo = instance.getDataAtRowProp(row, 'partsNo'); // partsNo を取得
  const link = document.createElement('a');
  link.href = `/spare_parts_detail/${partsNo}`;
  link.target = '_blank';

  if (partsNo && value) {
      const img = document.createElement('img');
      img.src = value;
      img.style.width = '50px';
      img.style.height = '50px';
      link.appendChild(img);

      const url = document.createElement('div');
      url.innerText = value; // 画像のURLを表示
      url.style.fontSize = '10px';
      link.appendChild(url);
  } else if (partsNo) {
      link.innerText = 'no image';
  }

  td.appendChild(link);
}

function imageEditor(instance, td, row, col, prop, value, cellProperties) {
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = 'image/*';
  input.style.display = 'none';

  input.addEventListener('change', (event) => {
      const file = event.target.files[0];
      const formData = new FormData();
      formData.append('image', file);

      axios
          .post('http://127.0.0.1:8000/api/spareParts/upload_image/', formData, {
              headers: {
                  'Content-Type': 'multipart/form-data'
              }
          })
          .then((response) => {
              const imageUrl = response.data.imageUrl;
              instance.setDataAtCell(row, col, imageUrl);
          })
          .catch((error) => {
              console.error('Image upload failed:', error);
          });
  });

  td.appendChild(input);
  input.click();
}

const SparePartsComponent = defineComponent({
  components: {
      HotTable,
      Save_Alert,
      Button // PrimeVue Button コンポーネントを登録
  },

  data() {
      return {
          hotSettings: {
              data: [], // **修正**: 初期データを空に設定しました
              colHeaders: [
                  'Image',
                  'Parts No',
                  'Plant', // **追加**: 新しい列を追加
                  'BOM <br>Code.',
                  'Parts Name',
                  'Category',
                  'Model',
                  'Manufacturer',
                  'Serial Number',
                  'Task <br>List No', // **リネーム**: Task CodeをTask list Noにリネーム
                  'Price',
                  'Number <br>of ~',
                  'Unit',
                  'Location',
                  'Delivery <br>Time',
                  'Alert <br>Order',
                  'Order <br>Situation',
                  'classification',
                  'Inventory<br>Turnover',
                  'Description'
              ],
              rowHeaders: true, // ここで行ヘッダーを有効にします
              columns: [
                  {
                      //Image
                      data: 'image',
                      renderer: imageRenderer,
                      editor: imageEditor
                  },
                  {
                      //Parts No
                      data: 'partsNo',
                      type: 'text',
                      readOnly: true,
                      renderer: function (instance, td, row, col, prop, value, cellProperties) {
                          Handsontable.renderers.TextRenderer.apply(this, arguments);
                          td.style.backgroundColor = '#f5f5f5'; // 背景色を灰色に設定
                          td.style.color = 'black'; // テキスト色を黒に設定
                      }
                  },
                  {
                      //Plant (新規追加)
                      data: 'plant',
                      type: 'text'
                  },
                  {
                      //BOM Code.
                      data: 'bomCode',
                      type: 'text'
                  },
                  {
                      //PartsName
                      data: 'partsName',
                      type: 'text',
                      className: 'htCenter'
                  },
                  {
                      //Category
                      data: 'category',
                      className: 'htRight',
                      type: 'dropdown',
                      source: ['Inventory', 'Standard', 'Consumables']
                  },
                  {
                      //Model
                      data: 'partsModel',
                      type: 'text'
                  },
                  {
                      //Manufacturer
                      data: 'manufacturer',
                      type: 'text'
                  },
                  {
                      //SerialNumber
                      data: 'serialNumber',
                      type: 'text',
                      className: 'htRight'
                  },
                  {
                      //Task list No (リネーム)
                      data: 'taskListNo',
                      type: 'text',
                      className: 'htCenter'
                  },
                  {
                      //PartsCost
                      data: 'partsCost',
                      type: 'numeric',
                      className: 'htRight'
                  },
                  {
                      //Number of ~
                      data: 'numberOf',
                      width: 60,
                      className: 'htRight',
                      type: 'numeric'
                  },
                  {
                      //Unit
                      data: 'unit',
                      width: 60,
                      type: 'text',
                      className: 'htRight'
                  },
                  {
                      //Location
                      data: 'location',
                      className: 'htRight',
                      type: 'text',
                      className: 'htRight'
                  },
                  {
                      //Delivery Parts time
                      data: 'partsDeliveryTime',
                      width: 60,
                      className: 'htRight',
                      type: 'numeric'
                  },
                  {
                      //Alert order
                      data: 'orderAlert',
                      width: 80,
                      className: 'htCenter',
                      type: 'text',
                      renderer: customRendererForAlertOrder,
                  },
                  {
                      //Order situation
                      data: 'orderSituation',
                      width: 100,
                      className: 'htCenter',
                      type: 'checkbox'
                  },
                  {
                      //classification
                      data: 'classification',
                      width: 100,
                      className: 'htCenter',
                      type: 'dropdown',
                      source: ['','Long-Term Stock Items', 'Short-Term Stock Items', 'Dead Stock Items','Critical Stock Items','Safety Stock Items','Irregular Use Stock Items']
                  },
                  {
                      //inventoryTurnover
                      data: 'inventoryTurnover',
                      width: 100,
                      className: 'htCenter',
                      type: 'text'
                  },
                  {
                      //Description
                      data: 'partsDescription',
                      className: 'htCenter',
                      type: 'text'
                  }
              ],

              afterGetColHeader: (col, TH) => {
                  if (col === -1) {
                      // ヘッダー行の場合
                      return;
                  }
                  // 全ヘッダーセルに薄い青色の背景を設定
                  TH.style.backgroundColor = '#E6F7FF'; // 薄い青色
                  TH.style.color = 'black'; // テキスト色を黒に設定
                  TH.style.fontWeight = 'bold'; // テキストを太字に設定
              },

              afterChange: function (changes, source) {
                  if (changes) {
                      changes.forEach(([row, prop, oldValue, newValue]) => {
                          if (prop === 'orderSituation') {
                              const alertOrderValue = this.getDataAtCell(row, 14);
                              if (newValue === true && alertOrderValue === 'order') {
                                  this.setDataAtCell(row, 14, 'ordered');
                              } else if (newValue === false && alertOrderValue === 'ordered') {
                                  this.setDataAtCell(row, 14, 'order');
                              }
                          }
                      });
                  }
              },

              cells: function (row, col, prop) {
                  const cellProperties = {};
                  const readOnlyColumns = ['inventoryTurnover'];

                  if (readOnlyColumns.includes(this.columns[col].data)) {
                      cellProperties.readOnly = true; // 列を読み取り専用に設定
                      cellProperties.renderer = customRendererForAlertOrder; // すべての読み取り専用列にカスタムレンダラーを適用
                  }
                  return cellProperties;
              },

              width: '100%',
              height: 'auto',
              stretchH: 'all', // 'none' is default 様子見
              contextMenu: true, //コンテキストメニュー
              autoWrapRow: true,
              autoWrapCol: true,
              fixedColumnsStart: 2, //カラム固定
              fixedRowsTop: 2, //列固定
              manualColumnFreeze: true, //コンテキストメニュー手動でコラム解除
              manualColumnResize: true, //手動での列幅調整
              manualRowResize: true, //列の手動高さ調整
              filters: true,
              dropdownMenu: true,
              comments: true, //コメントの有り無し
              fillHandle: {
                  autoInsertRow: true
              },

              licenseKey: 'non-commercial-and-evaluation'
          },
          rowsToAdd: 1, // 追加する行数のデフォルト値
          sparePartsDataStore: [], // データストア
          showAlert: false, // アラート表示用のフラグ
          alertType: 'success', // 'success' か 'error' を指定
          alertMessage: 'データが正常に保存されました。',
          errorMessages: [] // エラーメッセージのリスト
      };
  },

  created() {
      this.getDataAxios();
  },

  methods: {
      getDataAxios() {
          const userStore = useUserStore();
          const userCompanyCode = userStore.companyCode;

          if (!userCompanyCode) {
              console.error('Error: No company code found for the user.');
              return;
          }

          const url = `http://127.0.0.1:8000/api/spareParts/sparePartsByCompany/?format=json&companyCode=${userCompanyCode}`;

          axios
              .get(url, {
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  withCredentials: true
              })
              .then((response) => {
                  const sparePartsData = response.data;

                  const index = [
                      'image',
                      'partsNo',
                      'plant', // **追加**: Plant列を含むように修正
                      'bomCode',
                      'partsName',
                      'category',
                      'partsModel',
                      'manufacturer',
                      'serialNumber',
                      'taskListNo', // **リネーム**: Task Code を Task list No に修正
                      'partsCost',
                      'numberOf',
                      'unit',
                      'location',
                      'partsDeliveryTime',
                      'orderAlert',
                      'orderSituation',
                      'classification',
                      'inventoryTurnover',
                      'partsDescription'
                  ];

                  const tableData = sparePartsData.flatMap((companyData) =>
                      companyData.sparePartsList.flatMap((partData) => {
                          const rowData = {};
                          index.forEach((key) => {
                              rowData[key] = key === 'partsCost' || key === 'numberOf' ? parseFloat(partData[key]) || 0 : partData[key];
                              if (key === 'image' && !partData[key]) {
                                  rowData[key] = ''; // 画像がない場合は空文字に設定
                              }
                          });
                          return rowData;
                      })
                  );

                  // partsNoでソート
                  tableData.sort((a, b) => (parseInt(a.partsNo, 10) || 0) - (parseInt(b.partsNo, 10) || 0));

                  this.sparePartsDataStore = tableData;

                  // もしデータが10行未満の場合のみダミーデータを追加
                  if (tableData.length < 10) {
                      const blankRows = Array.from({ length: 10 - tableData.length }, () => ({}));
                      const newData = tableData.concat(blankRows);

                      this.$refs.hotTableComponent.hotInstance.updateSettings({
                          data: newData
                      });
                  } else {
                      this.$refs.hotTableComponent.hotInstance.updateSettings({
                          data: tableData
                      });
                  }
              })
              .catch((error) => {
                  console.error('Error fetching data:', error);
              });
      },

      addRows() {
          const hotInstance = this.$refs.hotTableComponent.hotInstance;
          const blankRows = Array.from({ length: this.rowsToAdd }, () => {
              return {
                  companyCode: userCompanyCode,
                  partsNo: row[1],
                  plant: row[2], // **追加**: Plant列をPOSTリクエストに含める
                  bomCode: row[3],
                  partsName: row[4],
                  category: row[5],
                  partsModel: row[6],
                  manufacturer: row[7],
                  serialNumber: row[8],
                  taskListNo: row[9], // **リネーム**: Task Code を Task list No に修正
                  partsCost: row[10],
                  numberOf: row[11],
                  unit: row[12],
                  location: row[13],
                  partsDeliveryTime: row[14],
                  orderAlert: row[15],
                  orderSituation: row[16] !== null ? row[16] : false, // null を false に変換
                  classification: row[17],
                  inventoryTurnover: row[18],
                  partsDescription: row[19]
              };
          });

          this.sparePartsDataStore = this.sparePartsDataStore.concat(blankRows);

          const newData = this.sparePartsDataStore;

          hotInstance.updateSettings({
              data: newData
          });
      },

      saveData() {
          const userStore = useUserStore();
          const userCompanyCode = userStore.companyCode;

          if (!userCompanyCode) {
              console.error('Error: No company code found for the user.');
              return;
          }

          const hotInstance = this.$refs.hotTableComponent.hotInstance;
          const tableData = hotInstance.getData();

          const formattedData = tableData.map((row) => {
              return {
                  companyCode: userCompanyCode,
                  partsNo: row[1], // parts No
                  plant: row[2], // **追加**: Plant フィールドを追加
                  bomCode: row[3], // BOM Code
                  partsName: row[4], // Parts Name
                  category: row[5], // Category
                  partsModel: row[6], // Model
                  manufacturer: row[7], // Manufacturer
                  serialNumber: row[8], // Serial Number
                  taskListNo: row[9], // **リネーム**: Task Code を Task list No に修正
                  partsCost: row[10], // Price (Parts Cost)
                  numberOf: row[11], // Number of
                  unit: row[12], // Unit
                  location: row[13], // Location
                  partsDeliveryTime: row[14], // Delivery Time
                  orderAlert: row[15], // Alert Order
                  orderSituation: row[16] !== null ? row[16] : false, // Order Situation
                  classification: row[17], // Classification
                  inventoryTurnover: row[18], // Inventory Turnover
                  partsDescription: row[19] // Description
              };
          });

          console.log('送信するデータ:', JSON.stringify(formattedData, null, 2));

          const url = `http://127.0.0.1:8000/api/spareParts/spareParts/`;

          axios
              .post(url, formattedData, {
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  withCredentials: true
              })
              .then((response) => {
                  console.log('Data saved successfully:', response.data);
                  this.alertType = 'success';
                  this.alertMessage = 'データが正常に保存されました。';
                  this.showAlert = true;
                  setTimeout(() => {
                      this.showAlert = false;
                  }, 3000); // 3秒後にアラートを非表示にする
              })
              .catch((error) => {
                  console.error('Error saving data:', error);
                  this.alertType = 'error';
                  this.alertMessage = 'データの保存に失敗しました。エラーを確認してください。';
                  this.errorMessages = ['エラーが発生しました。再度試してください。'];
                  this.showAlert = true;
                  setTimeout(() => {
                      this.showAlert = false;
                  }, 5000); // 5秒後にアラートを非表示にする
              });
      }
  }
});

export default SparePartsComponent;
</script>

<style scoped>
.button-container {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.legend {
  margin-bottom: 10px;
  display: flex;
  align-items: center;
}

.legend-item {
  display: flex;
  align-items: center;
  margin-right: 15px;
}

.color-box {
  width: 20px;
  height: 20px;
  margin-right: 10px;
  border: 1px solid #000;
}

.blue-button {
  background-color: #007bff;
  border-color: #007bff;
  color: white;
}
</style>
