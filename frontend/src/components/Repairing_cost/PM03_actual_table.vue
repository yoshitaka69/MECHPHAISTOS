<template>
	<div id="PM03actualtable">
		<hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
		<button v-on:click="updateData" class="controls">Update Data</button>
		<div>
			<input type="text" v-model="newPlantName" placeholder="Enter new plant name">
			<button v-on:click="postNewPlant">Add New Plant</button>
		</div>
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
  return td;
}

const monthColumnIndices = {
  jan: 3, feb: 4, mar: 5, jun:6, jul:7, aug:8, sep:9, oct:10, nov:11, dec:12, commitment:13// ... 各月のカラムインデックス...
};



const TableComponent = defineComponent({
	data() {
		return {
			newPlantName: '', // 新しいplant名を格納
			plantDropdownData: [], // ドロップダウンのデータ
			hotSettings: {
				data: [
					['', '', "", "", "", "", "", "", "", "", "", "", ""],
				],
				colHeaders: ['Plant', 'Year', 'Jan', "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "commitment", "Total"],
				columns: [
					{//'Plant'
						type: "text",

					},
					{//'Jan'
						type: 'numeric',

					},
					{//'Jan'
						type: 'numeric',

					},
					{//"Feb"
						type: 'numeric',

					},
					{//"Mar"
						type: 'numeric',

					},
					{//"Apr"
						type: 'numeric',
					},

					{//"May"
						type: 'numeric',

					},
					{//"Jun"
						type: 'numeric',

					},
					{//"Jul"
						type: 'numeric',

					},
					{//"Aug"
						type: 'numeric',

					},
					{//"Sep"
						type: 'numeric',

					},
					{//"Oct"
						type: 'numeric',

					},
					{//"Nov"
						type: 'numeric',

					},
					{//"Dec"
						type: 'numeric',

					},
					{//"Dec"
						type: 'numeric',
					},
					{//"Total"
						type: 'numeric',
					},

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

				width: '100%',
				height: 'auto',
				contextMenu: true,//コンテキストメニュー
				autoWrapRow: true,
				autoWrapCol: true,
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
				licenseKey: 'non-commercial-and-evaluation',

			}
		};
	},

	created() {
    this.getPlantDropdownData();
    this.getDataAxios();
  },

	methods: {


		async getPlantDropdownData() {
			const userStore = useUserStore();
			const userCompanyCode = userStore.companyCode;
			if (!userCompanyCode) {
				console.error("Error: No company code found for the user.");
				return;
			}
			try {
				const response = await axios.get(`http://127.0.0.1:8000/api/accounts/companyPlant/?companyCode=${userCompanyCode}`);
				this.plantDropdownData = response.data.flatMap(company => company.plantList.map(plant => plant.plant));
				console.log("Fetched plantDropdownData:", this.plantDropdownData);

				// Update the 'Plant' column with the fetched dropdown data
				this.hotSettings = {
					...this.hotSettings,
					columns: this.hotSettings.columns.map((column, index) => {
						if (index === 0) {
							return { ...column, type: 'dropdown', source: this.plantDropdownData };
						}
						return column;
					}),
				};
				console.log("Updated hotSettings:", this.hotSettings);
			} catch (error) {
				console.error('Error fetching dropdown data:', error);
			}
		},

		




		postNewPlant() {
			if (!this.newPlantName) {
				alert("Please enter a plant name.");
				return;
			}

			const userStore = useUserStore();
			const postData = {
				companyCode: userStore.companyCode,
				plant: this.newPlantName,
			};

			axios.post('http://127.0.0.1:8000/api/accounts/plant/', postData)
				.then(response => {
					console.log("Plant added successfully:", response.data);
					// 成功時の処理をここに追加（例: リストの更新、通知の表示など）
				})
				.catch(error => {
					console.error("Error in adding plant:", error);
				});

			// フォームをリセット
			this.newPlantName = '';
		},



		getDataAxios() {
			const userStore = useUserStore();
			const userCompanyCode = userStore.companyCode;

			if (!userCompanyCode) {
				console.error("Error: No company code found for the user.");
				return;
			}

			const url = `http://127.0.0.1:8000/api/repairingCost/APM03ByCompany/?format=json&companyCode=${userCompanyCode}`;

			axios.get(url, {
				headers: {
					"Content-Type": "application/json"
				},
				withCredentials: true
			})
				.then(response => {
					const actualCostData = response.data;

					//データ抽出
					const months = ["year", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "commitment",];
					const tableData = actualCostData.flatMap(companyData =>
						companyData.actualPM03List.flatMap(plantData =>
							plantData.actualPM03.map(yearData => {
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
						{
							data: "plant", type: 'dropdown',
							source: this.plantDropdownData,
						},
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
						{ data: 'total', readOnly: true, renderer: (instance, td, row, col, prop, value, cellProperties) => totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties), },
					];
					
					console.log("Table Data:", tableData); // テーブルデータをログに出力

					// 空行を追加
					const blankRows = Array.from({ length: 5 }, () => ({}));
					const newData = tableData.concat(blankRows);

					//table setting
					this.$refs.hotTableComponent.hotInstance.updateSettings({
						data: newData,
						columns,
					});
				})
				.catch(error => {
					console.error("Error fetching data:", error);
				});
		},


		updateData: function () {
			const userStore = useUserStore();
			const userCompanyCode = userStore.companyCode;

			if (!userCompanyCode) {
				console.error("Error: No company code found for the user.");
				return;
			}

			const tableData = this.$refs.hotTableComponent.hotInstance.getData();

			let actualPM03List = {};

			tableData.forEach(row => {
				let plantName = row[0];
				if (!actualPM03List[plantName]) {
					actualPM03List[plantName] = {
						plant: plantName,
						actualPM03: []  // このプラントに関するすべての年次データを保持
					};
				}

				// 年次データを追加
				actualPM03List[plantName].actualPM03.push({
					companyCode: userCompanyCode,
					plant: plantName,
					year: row[1],
					jan: row[2],
					feb: row[3],
					mar: row[4],
					apr: row[5],
					may: row[6],
					jun: row[7],
					jun: row[8],
					aug: row[9],
					sep: row[10],
					oct: row[11],
					nov: row[12],
					dec: row[13],
					commitment: row[14],
					totalCost: row[15]
				});
			});

			let postData = {
				companyCode: userCompanyCode,
				actualPM03List: Object.values(actualPM03List)
			};
			console.log("postData", postData);

			axios.post('http://127.0.0.1:8000/api/repairingCost/APM03ByCompany/', postData)
				.then(response => {
					console.log("Data posted successfully", response.data);
				})
				.catch(error => {
					console.error("Error in posting data", error);
				});
		}

	},
	components: {
		HotTable,
	},
});

export default TableComponent;
</script>