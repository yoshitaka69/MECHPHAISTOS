<template>
	<div id="PM05actualtable">
	  <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
	  <p>*You cannot enter the same plant name and year more than once.</p>
	  <Button label="Update Data" severity="secondary" raised class="updateData" @click="updateData"/>
	</div>
</template>

<script>
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';
import axios from "axios";
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

// register Handsontable's modules
registerAllModules();

// totalCostの計算と表示のためのカスタムレンダラー
function totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties) {
	const rowData = instance.getDataAtRow(row);
	const totalCost = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'commitment']
		.map(month => parseFloat(rowData[monthColumnIndices[month]]) || 0)
		.reduce((sum, amount) => sum + amount, 0);

	td.innerText = totalCost.toFixed(2); // 2桁の小数点で表示
	td.style.backgroundColor = '#f0f0f0'; // より薄い灰色
	return td;
}

const monthColumnIndices = {
	jan: 2, feb: 3, mar: 4, apr: 5, may: 6, jun: 7, jul: 8, aug: 9, sep: 10, oct: 11, nov: 12, dec: 13, commitment: 14
};

const TableComponent = defineComponent({
	data() {
		return {
			hotSettings: {
				data: [
					['', '', "", "", "", "", "", "", "", "", "", "", "", "", ""],
				],
				colHeaders: ['Plant', 'Year', 'Jan', "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "commitment", "Total"],
				columns: [
					{ type: "text" }, // 'Plant'
					{ type: 'numeric' }, // 'Year'
					{ type: 'numeric' }, // 'Jan'
					{ type: 'numeric' }, // 'Feb'
					{ type: 'numeric' }, // 'Mar'
					{ type: 'numeric' }, // 'Apr'
					{ type: 'numeric' }, // 'May'
					{ type: 'numeric' }, // 'Jun'
					{ type: 'numeric' }, // 'Jul'
					{ type: 'numeric' }, // 'Aug'
					{ type: 'numeric' }, // 'Sep'
					{ type: 'numeric' }, // 'Oct'
					{ type: 'numeric' }, // 'Nov'
					{ type: 'numeric' }, // 'Dec'
					{ type: 'numeric' }, // 'commitment'
					{ type: 'numeric', readOnly: true, renderer: (instance, td, row, col, prop, value, cellProperties) => totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties) } // 'Total'
				],

				afterGetColHeader: (col, TH) => {
					if (col === -1) {  // ヘッダー行の場合
						return;
					}
					// 特定の列インデックスまたはすべてのヘッダーに適用したい場合
					TH.style.backgroundColor = '#FFCC99'; // 薄いオレンジ色
					TH.style.color = 'black';
					TH.style.fontWeight = 'bold';  // テキストを太字に設定
				},
				rowHeaders: true, // 行ヘッダーを有効化
				width: '100%',
				height: 'auto',
				contextMenu: true, // コンテキストメニュー
				autoWrapRow: true,
				autoWrapCol: true,
				fixedRowsTop: 2, // 列固定
				manualColumnFreeze: true, // コンテキストメニュー手動でコラム解除
				manualColumnResize: true, // 手動での列幅調整
				manualRowResize: true, // 列の手動高さ調整
				filters: true,
				dropdownMenu: true,
				comments: true, // コメントの有り無し
				fillHandle: {
					autoInsertRow: true
				},
				licenseKey: 'non-commercial-and-evaluation',
				afterChange: (changes, source) => {
					if (source !== 'loadData' && changes) {
						changes.forEach(([row, prop, oldValue, newValue]) => {
							const instance = this.$refs.hotTableComponent.hotInstance;
							const cell = instance.getCell(row, instance.propToCol(prop));
							if (newValue === null || newValue === '') {
								cell.style.backgroundColor = ''; // 空欄の場合は背景色をリセット
							} else if (isNaN(newValue)) {
								cell.style.backgroundColor = '#ffcccc'; // 薄い赤色
							} else {
								cell.style.backgroundColor = ''; // 正しい値の場合は背景色をリセット
							}
						});
					}
				}
			}
		};
	},

	created() {
		this.getDataAxios();
	},

	methods: {

		addRow() {
			const hotInstance = this.$refs.hotTableComponent.hotInstance;
			hotInstance.alter('insert_row', hotInstance.countRows());
		},

		getDataAxios() {
			const userStore = useUserStore();
			const userCompanyCode = userStore.companyCode;

			if (!userCompanyCode) {
				console.error("Error: No company code found for the user.");
				return;
			}

			const url = `http://127.0.0.1:8000/api/repairingCost/APM05ByCompany/?format=json&companyCode=${userCompanyCode}`;
			console.log("Request URL:", url); // コンソールログを追加

			axios.get(url, {
				headers: {
					"Content-Type": "application/json"
				},
				withCredentials: true
			})
				.then(response => {
					const actualCostData = response.data;

					// データ抽出
					const months = ["year", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "commitment"];
					const tableData = actualCostData.flatMap(companyData =>
						companyData.actualPM05List.flatMap(plantData =>
							plantData.actualPM05.map(yearData => {
								const rowData = { plant: plantData.plant, year: yearData.year };
								months.forEach(month => {
									rowData[month] = parseFloat(yearData[month]) || 0;
								});
								rowData["totalCost"] = parseFloat(yearData["totalCost"]) || 0;
								return rowData;
							})
						)
					);

					// columns の設定
					const columns = [
						{ data: "plant" },
						{ data: "year" },
						{ data: "jan" },
						{ data: "feb" },
						{ data: "mar" },
						{ data: "apr" },
						{ data: "may" },
						{ data: "jun" },
						{ data: "jul" },
						{ data: "aug" },
						{ data: "sep" },
						{ data: "oct" },
						{ data: "nov" },
						{ data: "dec" },
						{ data: "commitment" },
						{ data: 'total', readOnly: true, renderer: (instance, td, row, col, prop, value, cellProperties) => totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties) },
					];
					console.log("Table Data:", tableData); // テーブルデータをログに出力
					// 空行を追加
					const blankRows = Array.from({ length: 5 }, () => ({}));
					const newData = tableData.concat(blankRows);

					// table setting
					this.$refs.hotTableComponent.hotInstance.updateSettings({
						data: newData,
						columns,
					});
				})
				.catch(error => {
					console.error("Error fetching data:", error);
				});
		},

		// updateDataメソッドでのデータ確認
		updateData: function () {
			const userStore = useUserStore();
			const userCompanyCode = userStore.companyCode;

			if (!userCompanyCode) {
				console.error("Error: No company code found for the user.");
				return;
			}

			const tableData = this.$refs.hotTableComponent.hotInstance.getData();
			console.log("Table Data to be posted:", tableData); // ポストするデータをログに出力

			let actualPM05List = {};
			let deletedRows = [];

			tableData.forEach(row => {
				let plantName = row[0];
				if (!plantName) {
					// plantNameがnullまたは空の場合はスキップ
					return;
				}

				if (!actualPM05List[plantName]) {
					actualPM05List[plantName] = {
						plant: plantName,
						actualPM05: []  // このプラントに関するすべての年次データを保持
					};
				}

				// 年次データを追加
				const yearData = {
					companyCode: userCompanyCode,
					plant: plantName,
					year: row[1],
					jan: row[2] || 0,
					feb: row[3] || 0,
					mar: row[4] || 0,
					apr: row[5] || 0,
					may: row[6] || 0,
					jun: row[7] || 0,
					jul: row[8] || 0,
					aug: row[9] || 0,
					sep: row[10] || 0,
					oct: row[11] || 0,
					nov: row[12] || 0,
					dec: row[13] || 0,
					commitment: row[14] || 0,
					totalCost: row.slice(2, 15).reduce((acc, val) => acc + (parseFloat(val) || 0), 0) // Janからcommitmentまでの合計
				};

				actualPM05List[plantName].actualPM05.push(yearData);
			});

			// 削除された行を収集
			const physicalRowCount = this.$refs.hotTableComponent.hotInstance.countRows();
			for (let i = 0; i < physicalRowCount; i++) {
				const row = this.$refs.hotTableComponent.hotInstance.getDataAtRow(i);
				if (!row[0] && !row[1]) {
					// plantNameとyearがnullまたは空の場合は削除対象
					continue;
				}
				if (!actualPM05List[row[0]]) {
					deletedRows.push({
						companyCode: userCompanyCode,
						plant: row[0],
						year: row[1]
					});
				}
			}

			let postData = {
				companyCode: userCompanyCode,
				actualPM05List: Object.values(actualPM05List),
				deletedRows: deletedRows
			};
			console.log("Post Data:", postData); // ポストデータをログに出力

			axios.post('http://127.0.0.1:8000/api/repairingCost/APM05ByCompany/save_actual_pm05/', postData)
				.then(response => {
					console.log("Data posted successfully", response.data);
					console.log("Posted Data:", postData); // POSTしたデータをログに出力
				})
				.catch(error => {
					console.error("Error in posting data", error);
					console.log("Posted Data:", postData); // POSTしたデータをログに出力
					console.log("Response Error Data:", error.response.data); // エラーレスポンスをログに出力
				});
		}

	},
	components: {
		HotTable,
	},
});

export default TableComponent;
</script>
