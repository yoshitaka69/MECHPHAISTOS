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
	Handsontable.renderers.TextRenderer.apply(this, arguments); // テキストレンダラーを基本に適用
	if (value) {
	  const img = document.createElement('img');
	  img.src = value;
	  img.style.width = '50px';
	  img.style.height = '50px';
	  td.appendChild(img);
	}
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
  
	  axios.post('http://127.0.0.1:8000/api/spareParts/upload_image/', formData, {
		headers: {
		  'Content-Type': 'multipart/form-data'
		}
	  }).then(response => {
		const imageUrl = response.data.imageUrl;
		instance.setDataAtCell(row, col, imageUrl);
	  }).catch(error => {
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
			["image_url", "1", "1", "Motor", "Standard", "RX-78-5.7", "12345-98", "Change motor", 900000, 1, "pieces", "warehouse1", "8", "order", false, "classification", "inventoryTurnover", "when we change No.1 agitator, we have to change this motor too"],//1
			["image_url", "2", "2", "Agitator", "Inventory", "ag89-78-5.7", "1233333-9", "Replace agitator", 180000, 4, "pieces", "warehouse2", "14", "order", false, "classification", "inventoryTurnover", "This agitator is bad actor,we keep this agitator every time"],//2
			["image_url", "3", "3", "Pump", "Standard", "zew99-0045", "135455333-9", "Exchange pump", 550000, 2, "pieces", "plantA", "60", "order", false, "classification", "inventoryTurnover", "This pump is needed exchange by operator"],//3
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//4
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//5
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//6
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//7
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//8
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//9
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//10
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//11
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//12
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//13
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//14
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//15
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//16
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//17
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//18
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//19
			["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//20
		  ],
		  colHeaders: [
			"Image", "parts No", "BOM <br>Code.", "Parts Name", "Category", "Model", "Serial Number", "Task Code", "Price", "Number <br>of ~", "Unit", "Location", "Delivery <br>Time", "Alert <br>order", "Order <br>situation", 'classification', 'inventoryTurnover', "Description"
		  ],
		  rowHeaders: true, // ここで行ヘッダーを有効にします
		  columns: [
			{//Image
			  data: 'image',
			  renderer: imageRenderer,
			  editor: imageEditor,
			},
			{//Parts No
			  data: 'partsNo',
			  type: "text",
			  readOnly: true,
			  renderer: function(instance, td, row, col, prop, value, cellProperties) {
				Handsontable.renderers.TextRenderer.apply(this, arguments);
				td.style.backgroundColor = '#f5f5f5'; // 背景色を灰色に設定
				td.style.color = 'black'; // テキスト色を黒に設定
			  }
			},
			{//BOM Code.
			  data: 'bomCode',
			  type: "text",
			},
			{//PartsName
			  data: 'partsName',
			  type: "text",
			  className: 'htCenter',
			},
			{//Category
			  data: 'category',
			  className: 'htRight',
			  type: 'dropdown',
			  source: ['Standard', 'Inventory', 'consumables']
			},
			{//Model
			  data: 'partsModel',
			  type: 'text',
			},
			{//SerialNumber
			  data: 'serialNumber',
			  type: 'text',
			  className: 'htRight',
			},
			{//TaskCode
			  data: 'taskCode',
			  type: 'text',
			  className: 'htCenter',
			},
			{//PartsCost
			  data: 'partsCost',
			  type: 'numeric',
			  className: 'htRight',
			},
			{//Number of ~
			  data: 'numberOf',
			  width: 60,
			  className: 'htRight',
			  type: 'numeric',
			},
			{//Unit
			  data: 'unit',
			  width: 60,
			  type: 'numeric',
			  className: 'htRight',
			},
			{//Location
			  data: 'location',
			  className: 'htRight',
			  type: 'text',
			  className: 'htRight',
			},
			{//Delivery Parts time
			  data: 'partsDeliveryTime',
			  width: 60,
			  className: 'htRight',
			  type: 'numeric',
			},
			{//Alert order
			  data: 'orderAlert',
			  width: 100,
			  className: 'htCenter',
			  type: 'text',
			  renderer: customRendererForAlertOrder,
			  readOnly: true,
			},
			{//Order situation
			  data: 'orderSituation',
			  width: 100,
			  className: 'htCenter',
			  type: 'checkbox',
			},
			{//classification
			  data: 'classification',
			  width: 100,
			  className: 'htCenter',
			  type: 'text'
			},
			{//inventoryTurnover
			  data: 'inventoryTurnover',
			  width: 100,
			  className: 'htCenter',
			  type: 'text'
			},
			{//Description
			  data: 'partsDescription',
			  className: 'htCenter',
			  type: 'text',
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
  
	created() {
	  this.getDataAxios();
	},
  
	methods: {
	  getDataAxios() {
		const userStore = useUserStore();
		const userCompanyCode = userStore.companyCode;
  
		if (!userCompanyCode) {
		  console.error("Error: No company code found for the user.");
		  return;
		}
  
		const url = `http://127.0.0.1:8000/api/spareParts/sparePartsByCompany/?format=json&companyCode=${userCompanyCode}`;
  
		axios.get(url, {
		  headers: {
			"Content-Type": "application/json"
		  },
		  withCredentials: true
		})
		  .then(response => {
			const sparePartsData = response.data;
  
			// データ抽出
			const index = ['image', 'partsNo', 'bomCode', 'partsName', 'category', 'partsModel', 'serialNumber', 'taskCode', 'partsCost', 'numberOf', 'unit', 'location', 'partsDeliveryTime', 'orderAlert', 'orderSituation', 'classification', "inventoryTurnover", "partsDescription"];
  
			const tableData = sparePartsData.flatMap(companyData =>
			  companyData.sparePartsList.flatMap(partData => {
				const rowData = {};
				index.forEach(key => {
				  // 数値データに対してはparseFloatを適用し、それ以外は直接代入
				  rowData[key] = (key === 'partsCost' || key === 'numberOf') ? parseFloat(partData[key]) || 0 : partData[key];
				});
				return rowData;
			  })
			);
  
			// partsNoでソート
			tableData.sort((a, b) => (parseInt(a.partsNo, 10) || 0) - (parseInt(b.partsNo, 10) || 0));
  
			const blankRows = Array.from({ length: 10 }, () => ({}));
			const newData = tableData.concat(blankRows);
  
			// table settings
			this.$refs.hotTableComponent.hotInstance.updateSettings({
			  data: newData,
			});
		  })
		  .catch(error => {
			console.error("Error fetching data:", error);
		  });
	  },
  
	  updateData() {
		const userStore = useUserStore();
		const userCompanyCode = userStore.companyCode;
  
		if (!userCompanyCode) {
		  console.error("Error: No company code found for the user.");
		  return;
		}
  
		const tableData = this.$refs.hotTableComponent.hotInstance.getData();
		let sparePartsList = [];
  
		tableData.forEach(row => {
		  let image = row[0]; // 画像
		  let partsNo = row[1]; // partsナンバー
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
		  let orderSituation = row[14] === true; // パーツコスト
		  let classification = row[15]; // 区分
		  let inventoryTurnover = row[16]; // 在庫回転率
		  let partsDescription = row[17]; // 詳細
  
		  // orderSituationを除外した全フィールドが空欄またはnullであるかを確認
		  const isRowEmpty = [image, partsNo, bomCode, partsName, category, partsModel, serialNumber, taskCode, partsCost, numberOf, unit, location, partsDeliveryTime, orderAlert, classification, inventoryTurnover, partsDescription].every(field => field === null || field === '');
  
		  if (!isRowEmpty) {
			sparePartsList.push({
			  companyCode: userCompanyCode,
			  image: image,
			  partsNo: partsNo,
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
		  }
		});
  
		let postData = {
		  sparePartsList: sparePartsList
		};
		console.log("postData", postData);
  
		const backendUrl = `http://127.0.0.1:8000/api/spareParts/sparePartsByCompany/?format=json`;
		axios.post(backendUrl, postData)
		  .then(response => {
			console.log("Data posted successfully", response.data);
		  })
		  .catch(error => {
			console.error("Error in posting data", error);
			console.error("Response data:", error.response.data);
		  });
	  },
	},
  
	components: {
	  HotTable,
	},
  });
  
  export default SparePartsComponent;
  </script>
  