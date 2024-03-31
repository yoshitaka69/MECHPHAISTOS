<template>
  <div id="PM03actualtable">
      <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
	  <button v-on:click="updateData" class="controls">Update Data</button>
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
  
  
  const TableComponent = defineComponent({
    data() {
      return {
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
						{ data: "totalCost", readOnly: true },
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
          year: Number(row[1]),
          jan: Number(row[2]),
          feb: Number(row[3]),
          mar: Number(row[4]),
          apr: Number(row[5]),
          may: Number(row[6]),
          jun: Number(row[7]),
          jul: Number(row[8]),
          aug: Number(row[9]),
          sep: Number(row[10]),
          oct: Number(row[11]),
          nov: Number(row[12]),
          dec: Number(row[13]),
          commitment: Number(row[14]),
          totalCost: Number(row[15])
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