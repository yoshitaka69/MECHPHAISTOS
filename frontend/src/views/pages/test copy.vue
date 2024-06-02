<template>
  <div id="CeList">
    <div class="matrices-container">
      <RiskMatrixImpactForProductionOnlyMatrix />
      <RiskMatrixPossibilityOfFailureOnlyMatrix />
    </div>
    <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
    <button v-on:click="sendData" class="controls">Update Data</button>
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
import RiskMatrixImpactForProductionOnlyMatrix from './Risk_Matrix_impact_for_production_onlyMatrix.vue';
import RiskMatrixPossibilityOfFailureOnlyMatrix from './Risk_matrix_possibility_Of_Failure onlyMatrix.vue';

// register Handsontable's modules
registerAllModules();

function customRenderer(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments);
  td.style.backgroundColor = '#F5F5F5'; // 薄い灰色
  // 'Impact for production' 列のインデックス（0から始まる）
  const impactColIndex = 15;
  // インデックスが 'Impact for production' の列であり、値が 'High+' などの場合にスタイルを設定
  if (col === impactColIndex) {
    if (value === 'High+') {
      td.style.backgroundColor = '#FF0000'; // 赤
      td.style.color = 'black';
    } else if (value === 'High') {
      td.style.backgroundColor = '#FFC000'; // オレンジ
      td.style.color = 'black';
    } else if (value === 'Low') {
      td.style.backgroundColor = '#00B050'; // 緑
      td.style.color = 'black';
    }
    // 他の条件があれば、if ステートメントを拡張してください
  }
}

function customRendererForProbability(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments);
  td.style.backgroundColor = '#F5F5F5'; // 薄い灰色

  // 'Probability of failure' 列のインデックス
  const probabilityColIndex = 16;

  // インデックスが 'Probability of failure' の列であり、値に基づいてスタイルを設定
  if (col === probabilityColIndex) {
    // セル内の文字に基づいてスタイルを変更
    switch (value) {
      case '要対策':
        td.style.backgroundColor = '#FF0000';
        td.style.color = 'black';
        break;
      case '対策検討':
        td.style.backgroundColor = '#FFC000';
        td.style.color = 'black';
        break;
      case '適切':
        td.style.backgroundColor = '#92D050';
        td.style.color = 'black';
        break;
      case '見直検討':
        td.style.backgroundColor = '#00B050';
        td.style.color = 'black';
        break;
      // 他の条件があればここに追加
    }
  }
}

function customRendererForAssessment(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments);
  td.style.backgroundColor = '#F5F5F5'; // 薄い灰色

  // セル内の文字に基づいてスタイルを変更
  switch (value) {
    case '対策済':
      td.style.backgroundColor = '#92D050'; // 条件1
      td.style.color = 'black';
      break;
    case '見直検討':
      td.style.backgroundColor = '#00B050'; // 条件2
      td.style.color = 'black';
      break;
    case '保全タスク':
      td.style.backgroundColor = '#FFFF00'; // 条件3
      td.style.color = 'black';
      break;
    // 他の条件があればここに追加
  }

  // 'Probability of failure' 列の値に基づいてスタイルを変更
  const probabilityOfFailureColIndex = 16; // 'Probability of failure' 列のインデックス
  const probabilityOfFailureValue = instance.getDataAtCell(row, probabilityOfFailureColIndex);

  // 'Impact for production' 列の値に基づいてスタイルを変更
  const impactForProductionColIndex = 15; // 'Impact for production' 列のインデックス
  const impactForProductionValue = instance.getDataAtCell(row, impactForProductionColIndex);

  // 条件の優先順位を考慮してスタイルを適用
  if (value === '対策済' || value === '見直検討' || value === '保全タスク') {
    // 条件1, 2, 3 の場合
    // 何もしない（条件1, 2, 3が優先される）
  } else if (impactForProductionValue === 'High+' || probabilityOfFailureValue === '要対策') {
    // 条件4, 5 の場合
    td.style.backgroundColor = '#FF0000'; // 条件4, 5 が優先される
    td.style.color = 'black';
  } else if (impactForProductionValue === 'High' || probabilityOfFailureValue === '対策検討') {
    // 条件6, 7 の場合
    td.style.backgroundColor = '#FFC000'; // 条件6, 7 が優先される
    td.style.color = 'black';
  }
}

function customRendererForSituation(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments);
  td.style.backgroundColor = '#F5F5F5'; // 薄い灰色
  if (value === '遅延') {
    td.style.backgroundColor = '#FFFF00'; // 黄色
    td.style.color = 'black';
  }
}

function customRendererForMttr(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments);
  td.style.backgroundColor = '#F5F5F5'; // 薄い灰色

  const constructionPeriodColIndex = 5;  // Construction period の列のインデックス
  const partsDeliveryDateColIndex = 6;  // Parts delivery date の列のインデックス

  const constructionPeriod = instance.getDataAtCell(row, constructionPeriodColIndex);
  const partsDeliveryDate = instance.getDataAtCell(row, partsDeliveryDateColIndex);

  // Construction period と Parts delivery date の比較
  const mttrValue = Math.max(constructionPeriod, partsDeliveryDate);

  // MTTR セルに表示
  td.innerHTML = mttrValue === 0 ? '' : mttrValue;
}

const CriticalEquipmentComponent = defineComponent({
  components: {
    HotTable,
    RiskMatrixImpactForProductionOnlyMatrix,
    RiskMatrixPossibilityOfFailureOnlyMatrix
  },
  data() {
    return {
      hotSettings: {
        data: [
          // データをここに追加
        ],
        nestedHeaders: [
          ["", "", "", "", { label: "Impact", colspan: 5 }, { label: "Probability of failure", colspan: 6 }, { label: "Critical equipment Level", colspan: 3 }, "", "", "", "", "", { label: "Spare parts", colspan: 2 }, { label: "Status of measures", colspan: 4 }, { label: "Order", colspan: 2 },],
          ["CeListNo", "Plant", "Equipment", "Machine", "Level set <br>value", "Construction <br>period", "Parts <br>delivery date", "MTTR", "Possibility of <br>production Lv", "Count <br>of PM02", "Latest <br>PM02", "Count <br>of PM03", "Latest <br>PM03", "Count <br>of PM04", "Latest <br>PM04", "Impact for <br>production", "Probability <br>of failure", "Assessment", "Typical Task", "Labor <br>Cost(PM02)", "Period", "Next <br>event year", "situation", "BomCode", "Stock", "RCA or <br>Replace(hard)", "Spear parts or <br>Alternative(soft)", "Covered <br>from task", "Two <br>ways",],
        ],
        columns: [
          { data: "ceListNo", type: "text", readOnly: true },
          { data: "plant", type: "text" },
          { data: "equipment", type: "text" },
          { data: "machineName", type: "text" },
          { data: "levelSetValue", type: 'numeric' },
          { data: "typicalConstPeriod", type: 'numeric' },
          { data: "maxPartsDeliveryTimeInBom", type: 'numeric' },
          { data: "mttr", type: 'numeric', renderer: customRendererForMttr },
          { data: "probabilityOfFailure", type: 'numeric', className: 'htRight', readOnly: true },
          { data: "countOfPM02", width: 100, className: 'htRight', type: 'numeric' },
          { data: "latestPM02", width: 100, className: 'htRight', type: 'date', dateFormat: 'YYYY-MM-DD', correctFormat: false },
          { data: "countOfPM03", width: 100, className: 'htRight', type: 'numeric' },
          { data: "latestPM03", width: 100, className: 'htRight', type: 'date', dateFormat: 'YYYY-MM-DD', correctFormat: false },
          { data: "countOfPM04", width: 100, className: 'htRight', type: 'numeric' },
          { data: "latestPM04", width: 100, className: 'htRight', type: 'date', dateFormat: 'YYYY-MM-DD', correctFormat: false },
          { data: "impactForProduction", renderer: customRenderer, width: 100, className: 'htCenter', readOnly: true },
          { data: "probabilityOfFailure", renderer: customRendererForProbability, width: 100, className: 'htCenter', readOnly: true },
          { data: "assessment", renderer: customRendererForAssessment, readOnly: true, width: 100, className: 'htCenter' },
          { data: "typicalTaskName", type: "text" },
          { data: "typicalTaskCost", type: 'numeric' },
          { data: "typicalConstPeriod", type: 'numeric' },
          { data: "typicalNextEventDate", className: 'htRight', type: 'date', dateFormat: 'YYYY-MM-DD', correctFormat: false, readOnly: true },
          { data: "typicalSituation", className: 'htCenter', renderer: customRendererForSituation, readOnly: true },
          { data: "bomCode", className: 'htRight', type: 'dropdown', source: ['Standard', 'Inventory', 'consumables'] },
          { data: "bomStock", type: 'dropdown', source: ['有', '無'], className: 'htCenter' },
          { data: "rcaOrReplace", width: 100, className: 'htCenter', type: 'checkbox' },
          { data: "sparePartsOrAlternative", width: 100, className: 'htCenter', type: 'checkbox' },
          { data: "coveredFromTask", width: 100, className: 'htCenter', type: 'checkbox' },
          { data: "twoways", width: 100, className: 'htCenter', type: 'checkbox' },
        ],
        afterGetColHeader: (col, TH) => {
          if (col === -1) {
            return;
          }
          TH.style.backgroundColor = '#FFCC99';
          TH.style.color = 'black';
          TH.style.fontWeight = 'bold';
        },
        width: '100%',
        height: 'auto',
        stretchH: 'all',
        contextMenu: true,
        autoWrapRow: true,
        autoWrapCol: true,
        fixedColumnsStart: 2,
        fixedRowsTop: 2,
        manualColumnFreeze: true,
        manualColumnResize: true,
        manualRowResize: true,
        filters: true,
        dropdownMenu: true,
        comments: true,
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
    initHandsontable() {
      const container = this.$el;
      this.hot = new Handsontable(container, {
        afterChange: (changes, source) => {
          if (source !== 'loadData') {
            const data = this.hot.getData();
            this.updateData(data);
          }
        }
      });
    },
    getDataAxios() {
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;
      if (!userCompanyCode) {
        console.error("Error: No company code found for the user.");
        return;
      }
      const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${userCompanyCode}`;
      axios.get(url, {
        headers: {
          "Content-Type": "application/json"
        },
        withCredentials: true
      })
        .then(response => {
          const masterDataTable = response.data.flatMap(companyData => companyData.MasterDataTable);
          console.log("Fetched masterDataTable:", masterDataTable);
          const blankRows = Array.from({ length: 10 }, () => ({}));
          const newData = masterDataTable.concat(blankRows);
          this.$refs.hotTableComponent.hotInstance.loadData(newData);
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });
    },
    updateData(data) {
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;
      const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${userCompanyCode}`;
      const payload = { companyCode: userCompanyCode, masterDataTable: data };
      axios.post(url, payload)
        .then(response => console.log('Data successfully updated:', response))
        .catch(error => console.error('Error updating data:', error));
    },
    sendData() {
      const data = this.$refs.hotTableComponent.hotInstance.getSourceData();
      this.updateData(data);
    }
  }
});

export default CriticalEquipmentComponent;
</script>

<style scoped>
.matrices-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}
</style>
