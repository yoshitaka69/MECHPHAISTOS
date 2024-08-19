<template>
    <div id="SparePartsList">
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
        <Button label="Add Rows" severity="primary" @click="addRows" />
        <Button label="Save Data" severity="secondary" raised class="saveData" @click="saveData" />
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
    data() {
      return {
        hotSettings: {
          data: [
            [
              'image_url',
              '1',
              '1',
              'Motor',
              'Standard',
              'RX-78-5.7',
              '12345-98',
              'Change motor',
              900000,
              1,
              'pieces',
              'warehouse1',
              '8',
              'order',
              false,
              'classification',
              'inventoryTurnover',
              'when we change No.1 agitator, we have to change this motor too'
            ],
            // 以下、初期データ
          ],
          colHeaders: [
            'Image',
            'parts No',
            'BOM <br>Code.',
            'Parts Name',
            'Category',
            'Model',
            'Serial Number',
            'Task Code',
            'Price',
            'Number <br>of ~',
            'Unit',
            'Location',
            'Delivery <br>Time',
            'Alert <br>order',
            'Order <br>situation',
            'classification',
            'inventoryTurnover',
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
              source: ['Standard', 'Inventory', 'consumables']
            },
            {
              //Model
              data: 'partsModel',
              type: 'text'
            },
            {
              //SerialNumber
              data: 'serialNumber',
              type: 'text',
              className: 'htRight'
            },
            {
              //TaskCode
              data: 'taskCode',
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
              type: 'numeric',
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
              width: 100,
              className: 'htCenter',
              type: 'text',
              renderer: customRendererForAlertOrder,
              readOnly: true
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
              type: 'text'
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
                  const alertOrderValue = this.getDataAtCell(row, 13);
                  if (newValue === true && alertOrderValue === 'order') {
                    this.setDataAtCell(row, 13, 'ordered');
                  } else if (newValue === false && alertOrderValue === 'ordered') {
                    this.setDataAtCell(row, 13, 'order');
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
        sparePartsDataStore: [] // データストア
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
                'bomCode',
                'partsName',
                'category',
                'partsModel',
                'serialNumber',
                'taskCode',
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
            image: '',
            partsNo: '',
            bomCode: '',
            partsName: '',
            category: '',
            partsModel: '',
            serialNumber: '',
            taskCode: '',
            partsCost: 0,
            numberOf: 0,
            unit: '',
            location: '',
            partsDeliveryTime: 0,
            orderAlert: '',
            orderSituation: false,
            classification: '',
            inventoryTurnover: '',
            partsDescription: ''
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
            partsNo: row[1],
            bomCode: row[2],
            partsName: row[3],
            category: row[4],
            partsModel: row[5],
            serialNumber: row[6],
            taskCode: row[7],
            partsCost: row[8],
            numberOf: row[9],
            unit: row[10],
            location: row[11],
            partsDeliveryTime: row[12],
            orderAlert: row[13],
            orderSituation: row[14] !== null ? row[14] : false,  // null を false に変換
            classification: row[15],
            inventoryTurnover: row[16],
            partsDescription: row[17],
        };
    });

    console.log("送信するデータ:", JSON.stringify(formattedData, null, 2));

    const url = `http://127.0.0.1:8000/api/spareParts/spareParts/`;

    axios
        .post(url, formattedData, {
            headers: {
                'Content-Type': 'application/json',
            },
            withCredentials: true,
        })
        .then((response) => {
            console.log("Data saved successfully:", response.data);
        })
        .catch((error) => {
            console.error("Error saving data:", error);

            if (error.response) {
                console.error("Error response status:", error.response.status);
                console.error("Error response headers:", error.response.headers);
                console.error("Error response data:", error.response.data);
            } else if (error.request) {
                console.error("Error request data:", error.request);
            } else {
                console.error("Error message:", error.message);
            }

            console.error("Error config:", error.config);
        });
},






    },
  
    components: {
      HotTable
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
  </style>
  