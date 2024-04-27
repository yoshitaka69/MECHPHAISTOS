<template>
    <div id="SparePartsList">
      <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
      <button v-on:click="updateData" class="controls">Update Data</button>
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
  
  
  const SparePartsComponent = defineComponent({
    data() {
      return {
        hotSettings: {
          data: [
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//1
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//2
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//3
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//4
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//5
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//6
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//7
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//8
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//9
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//10
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//11
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//12
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//13
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//14
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//15
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//16
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//17
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//18
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//19
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "",],//20
  
          ],
          colHeaders: [
            "Image", "BOM <br>Code.", "Parts Name", "Category", "Model", "Serial Number", "Task Code", "Price", "Number <br>of ~", "Unit", "Location", "Delivery <br>Time", 'classification', "Description"
          ],
  
          columns: [
  
            {//Image
            },
            {//BOM Code.
              type: "numeric",
            },
            {//PartsName
              type: "text",
              className: 'htCenter',
            },
            {//Category
              className: 'htRight',
              type: 'dropdown',
              source: ['','Standard', 'Inventory', 'consumables'],
              correctFormat: false,
            },
            {//Model
              type: 'text',
            },
            {//SerialNumber
              type: 'text',
              className: 'htRight',
            },
            {//TaskCode
              type: 'text',
              className: 'htCenter',
            },
            {//PartsCost
              type: 'numeric',
              className: 'htRight',
            },
            {//Number of ~
              width: 60,
              className: 'htRight',
              type: 'numeric',
            },
            {//Unit
              width: 60,
              type: 'numeric',
              className: 'htRight',
            },
            {//Location
              className: 'htRight',
              type: 'text',
              className: 'htRight',
            },
            {//Delivery Parts time
              width: 60,
              className: 'htRight',
              type: 'numeric',
            },
            {//Classification
              width: 100,
              className: 'htCenter',
              type: 'dropdown',
              source: ['','Long lead Time Items', 'High Expensive Items', 'Sleeping Stock'],
              correctFormat: false,
            },
            {//Description
              width: 100,
              className: 'htCenter',
              type: 'text'
            },
          ],
  
          afterGetColHeader: (col, TH) => {
            if (col === -1) {  // ヘッダー行の場合
              return;
            }
            // 全ヘッダーセルに薄い青色の背景を設定
            TH.style.backgroundColor = '#E6F7FF'; // 薄い青色
            TH.style.color = 'black';  // テキスト色を黒に設定
            TH.style.fontWeight = 'bold';  // テキストを太字に設定
          },
  
  
          width: '100%',
          height: 'auto',
          stretchH: 'all', // 'none' is default 様子見
          contextMenu: true,//コンテキストメニュー
          autoWrapRow: true,
          autoWrapCol: true,
          fixedColumnsStart: 2,//カラム固定
          fixedRowsTop: 2,//列固定
          manualColumnFreeze: true,//コンテキストメニュー手動でコラム解除
          manualColumnResize: true,//手動での列幅調整
          manualRowResize: true,//列の手動高さ調整
          filters: true,
          dropdownMenu: true,
          comments: true,//コメントの有り無し
          fillHandle: {
            autoInsertRow: true
          },
  
          licenseKey: 'non-commercial-and-evaluation'
  
        }
      };
    },
  
  
  
    updateData: function () {
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;
  
      if (!userCompanyCode) {
        console.error("Error: No company code found for the user.");
        return;
      }
  
      const tableData = this.$refs.hotTableComponent.hotInstance.getData();
      let sparePartsList = [];
  
      tableData.forEach(row => {
        let partsNo = row[0]; // partsナンバー
        let image = row[1]; // 画像
        let bomCode = row[2]; // BOMコード
        let partsName = row[3]; // パーツネーム
        let category = row[4]; // カテゴリー
        let partsModel = row[5]; // 型式
        let serialNumber = row[6]; // シリアルナンバー
        let taskCode = row[7]; // タスクコード
        let partsCost = row[8]; // パーツコスト
        let numberOf = row[9]; // 個数
        let unit = row[10]; // カテゴリー
        let location = row[11]; // 型式
        let partsDeliveryTime = row[12]; // シリアルナンバー
        let orderAlert = row[13]; // タスクコード
        let orderSituation = row[14]; // パーツコスト
        let classification = row[15]; // 区分
        let inventoryTurnover = row[16]; // 在庫回転率
        let partsDescription = row[17]; // 詳細
  
        sparePartsList.push({
          companyCode: userCompanyCode,
          partsNo: partsNo,
          image: image,
          bomCode: bomCode,
          partsName: partsName,
          category: category,
          partsModel: partsModel,
          serialNumber: serialNumber,
          taskCode: taskCode,
          partsCost: partsCost,
          numberOf: numberOf,
          unit: unit,
          location: location,
          partsDeliveryTime: partsDeliveryTime,
          orderAlert: orderAlert,
          orderSituation: orderSituation,
          classification: classification,
          inventoryTurnover: inventoryTurnover,
          partsDescription: partsDescription
        });
      });
  
      let postData = {
        companyCode: userCompanyCode,
        sparePartsList: sparePartsList
      };
      console.log("postData", postData)
  
      const backendUrl = `http://127.0.0.1:8000/api/spareParts/sparePartsByCompany/?format=json&companyCode=${userCompanyCode}`;
      axios.post(backendUrl, postData)
        .then(response => {
          console.log("Data posted successfully", response.data);
        })
        .catch(error => {
          console.error("Error in posting data", error);
        });
    },
  
  components: {
      HotTable,
    },
  });
  
  export default SparePartsComponent;
  
  </script>