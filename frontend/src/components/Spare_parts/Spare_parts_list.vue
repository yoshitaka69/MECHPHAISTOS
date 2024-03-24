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
	Handsontable.renderers.TextRenderer.apply(this, arguments);
	if (value === 'order') {
		td.style.backgroundColor = '#FF0000'; // 赤
		td.style.color = 'black';
	}
}


const SparePartsComponent = defineComponent({
	data() {
		return {
			hotSettings: {
				data: [
					["", 1, "Motor", "Standard", "RX-78-5.7", "12345-98", "Change motor", 900000, 1, "pieces", "warehouse1", "8", "", "", "when we change No.1 agitator, we have to change this motor too"],//1
					["", 2, "Agitator", "Inventory", "ag89-78-5.7", "1233333-9", "Replace agitator", 180000, 4, "pieces", "warehouse2", "14", "", "", "This agitator is bad actor,we keep this agitator every time"],//2
					["", 3, "Pump", "Standard", "zew99-0045", "135455333-9", "Exchange pump", 550000, 2, "pieces", "plantA", "60", "", "", "This pump is needed exchange by operator"],//3
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//4
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//5
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//6
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//7
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//8
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//9
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//10
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//11
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//12
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//13
					["", "", "", "", "", "", "", "", "", "", "", "", ""],//14
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//15
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//16
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//17
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//18
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//19
					["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],//20

				],
				colHeaders: [
					"Image", "BOM <br>No.", "Parts Name", "Category", "Model", "Serial Number", "Task Name", "Price", "Number <br>of ~", "Unit", "Location", "Delivery <br>Time", "Alert <br>order", "Order <br>situation", "Description"
				],

				columns: [
					{//Image


					},
					{//BOM No.
						type: "numeric",

					},
					{//PartsName
						type: "text",
						className: 'htCenter',

					},
					{//Category
						className: 'htRight',
						type: 'dropdown',
						source: ['Standard', 'Inventory', 'consumables']

					},
					{//Model
						type: 'text',

					},
					{//SerialNumber
						type: 'text',
						className: 'htRight',

					},
					{//TaskName
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
					{//Alert order
						width: 100,
						className: 'htCenter',
						type: "text",
						renderer: customRendererForAlertOrder
					},
					{//Order situation
						width: 100,
						className: 'htCenter',
						type: 'checkbox'
					},
					{//Description
						className: 'htCenter',
						type: 'text',
					},
				],

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
		this.getData();
	},

	methods: {
		swapHotData: function () {
			console.log("swapHotData: Loading new data into Handsontable");
			// 新しいデータをロード
			this.$refs.hotTableComponent.hotInstance.loadData([['new', 'data']]);
		},

		getData: function () {
			console.log("getData: Initiating data retrieval");

			const userStore = useUserStore();
			const userCompanyCode = userStore.companyCode;

			if (!userCompanyCode) {
				console.error("getData Error: No company code found for the user.");
				return;
			}

			console.log("getData: Using company code", userCompanyCode);

			const url = `http://127.0.0.1:8000/api/spareParts/sparePartsByCompany/?format=json&companyCode=${userCompanyCode}`;
			console.log("getData: Requesting data from", url);

			axios.get(url)
				.then(response => {
					console.log("getData: Data retrieved successfully", response.data);

					// 応答データの初期処理
					const sparePartsData = response.data;



					// データ抽出
					const index = ['image', 'bomCode', 'partsName', 'category', 'partsModel', 'serialNumber', 'taskCode', 'partsCost', 'numberOf', 'unit', 'location', 'partsDeliveryTime', 'orderAlert', 'orderSituation', 'classification'];

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

					// columns の設定
					const columns = [
						{ data: "image" },
						{ data: "bomCode" },
						{ data: "partsName" },
						{ data: "category" },
						{ data: "partsModel" },
						{ data: "serialNumber" },
						{ data: "taskCode" },
						{ data: "partsCost" },
						{ data: "numberOf" },
						{ data: "unit" },
						{ data: "location" },
						{ data: "partsDeliveryTime" },
						{ data: "overAlert" },
						{ data: "orderSituation" },
						{ data: "classification" },
						{ data: "inventoryTurnover" },
					];
					console.log("Table Data:", tableData); // テーブルデータをログに出力

					//table setting
					this.$refs.hotTableComponent.hotInstance.updateSettings({
						data: tableData,
						columns,
					});
				})
				.catch(error => {
					console.error("Error fetching data:", error);
				});
		},



		updateData: function () {
			console.log("updateData: Initiating data update");

			const userStore = useUserStore();
			const userCompanyCode = userStore.companyCode;

			if (!userCompanyCode) {
				console.error("updateData Error: No company code found for the user.");
				return;
			}

			console.log("updateData: Using company code", userCompanyCode);

			const jsonData = this.$refs.hotTableComponent.hotInstance.getData();
			console.log("updateData: Data to be sent", jsonData);

			const backendUrl = `http://127.0.0.1:8000/api/spareParts/sparePartsByCompany/?format=json&companyCode=${userCompanyCode}`;
			console.log("updateData: Sending data to", backendUrl);

			axios.post(backendUrl, jsonData)
				.then(response => {
					console.log("updateData: Data updated successfully", response.data);
				})
				.catch(error => {
					console.error("updateData Error: An error occurred during the request", error);
					if (error.response) {
						console.error("updateData Error: Server response", error.response);
					}
				});
		}
	},

	components: {
		HotTable,
	},
});

export default SparePartsComponent;
</script>