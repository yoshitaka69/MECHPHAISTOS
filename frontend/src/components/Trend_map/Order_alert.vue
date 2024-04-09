<template>
	<div id="OrderAlerttable">
		<hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
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
					["", "", "", "", "", "", ],
				],
				colHeaders: ['Order Alert', 'Parts Name', 'Delivery Time', 'Event Date', "Location", "Check",],
				columns: [
					{//'Order Alert'
						type: "text",
            readOnly : true,

					},
					{//'Parts Name'
						type: 'text',
            readOnly : true,

					},
          {//"Delivery Time"
						type: 'numeric',
            readOnly : true,
					},
					{//'Event Date'
          type: 'date',
          dateFormat: 'YYYY-MM-DD',
            readOnly : true,

					},
					{//"Location"
						type: 'text',
            readOnly : true,

					},

					{//"Check"
						type: 'checkbox',
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

    // URLの更新
    const url = `http://127.0.0.1:8000/api/junctionTable/alertScheduleByCompany/?format=json&companyCode=${userCompanyCode}`;

    axios.get(url, {
        headers: {
            "Content-Type": "application/json"
        },
        withCredentials: true
    })
    .then(response => {
        const alertScheduleList = response.data.AlertScheduleList;

        // データ抽出
        const tableData = alertScheduleList.map(schedule => ({
            partsName: schedule.partsName,
            eventDate: schedule.eventDate,
            location: schedule.location,
            deliveryTime: schedule.deliveryTime,
            orderAlertDate: schedule.orderAlertDate
        }));

        // columns の設定
        const columns = [
            { data: "partsName" },
            { data: "eventDate" },
            { data: "location" },
            { data: "deliveryTime" },
            { data: "orderAlertDate" }
        ];
        console.log("Table Data:", tableData); // テーブルデータをログに出力

        // 空行を追加
        const blankRows = Array.from({ length: 20 }, () => ({}));
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
}
	components: {
		HotTable,
	},
});

export default TableComponent;
</script>
