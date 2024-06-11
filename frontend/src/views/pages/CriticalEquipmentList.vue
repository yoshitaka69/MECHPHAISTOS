<template>
  <div id="CeList">
    <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
    <button v-on:click="emitData" class="controls">Emit Data</button>
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

function applyBaseStyle(td) {
  if (td) {
    td.style.backgroundColor = '#F0F0F0'; // さらに薄い灰色
    td.style.color = 'black';
  }
}

function customRenderer(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments);
  applyBaseStyle(td);
  const impactColIndex = 15;
  if (col === impactColIndex) {
    if (value === 'High+') {
      td.style.backgroundColor = '#FF0000';
    } else if (value === 'High') {
      td.style.backgroundColor = '#FFC000';
    } else if (value === 'Low') {
      td.style.backgroundColor = '#00B050';
    }
  }
}

function customRendererForProbability(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments);
  applyBaseStyle(td);
  const probabilityColIndex = 16;
  if (col === probabilityColIndex) {
    switch (value) {
      case '要対策':
        td.style.backgroundColor = '#FF0000';
        break;
      case '対策検討':
        td.style.backgroundColor = '#FFC000';
        break;
      case '適切':
        td.style.backgroundColor = '#92D050';
        break;
      case '見直検討':
        td.style.backgroundColor = '#00B050';
        break;
    }
  }
}

function customRendererForAssessment(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments);
  applyBaseStyle(td);
  switch (value) {
    case '対策済':
      td.style.backgroundColor = '#92D050';
      break;
    case '見直検討':
      td.style.backgroundColor = '#00B050';
      break;
    case '保全タスク':
      td.style.backgroundColor = '#FFFF00';
      break;
  }
  const probabilityOfFailureColIndex = 16;
  const probabilityOfFailureValue = instance.getDataAtCell(row, probabilityOfFailureColIndex);
  const impactForProductionColIndex = 15;
  const impactForProductionValue = instance.getDataAtCell(row, impactForProductionColIndex);

  if (value === '対策済' || value === '見直検討' || value === '保全タスク') {
  } else if (impactForProductionValue === 'High+' || probabilityOfFailureValue === '要対策') {
    td.style.backgroundColor = '#FF0000';
  } else if (impactForProductionValue === 'High' || probabilityOfFailureValue === '対策検討') {
    td.style.backgroundColor = '#FFC000';
  }
}

function customRendererForSituation(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.TextRenderer.apply(this, arguments);
  applyBaseStyle(td);
  if (value === '遅延') {
    td.style.backgroundColor = '#FFFF00';
  }
}

function customRendererForMttr(instance, td, row, col, prop, value, cellProperties) {
  if (td) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
  }

  const constructionPeriodColIndex = 5;
  const partsDeliveryDateColIndex = 6;
  const constructionPeriod = instance.getDataAtCell(row, constructionPeriodColIndex);
  const partsDeliveryDate = instance.getDataAtCell(row, partsDeliveryDateColIndex);
  const mttrValue = Math.max(constructionPeriod, partsDeliveryDate);

  if (td) { // nullチェックを追加
    td.innerHTML = mttrValue === 0 ? '' : mttrValue;
  }

  return mttrValue; // MTTR値を返す
}

const CriticalEquipmentList = defineComponent({
  data() {
    return {
      hotSettings: {
        data: [
          ['', 'PlantA', 'モーターA', 'N401/A plant__', '4', '10', '6', '10', '4', '今年', '2022-10-02', '3', '2019-11-01', '0', '', 'High+', '', '対策済', 'A plant/変換器室 変換器盤1-3パワーサプライ交換', '10000', '3', '2025', '', 'Standard', '', '', '', '', '',], //1
          ['', 'PlantA', 'モーターA', 'N401/A plant__/OX2_', '3', '10', '6', '10', '4', '', '', '4', '2018-08-10', '', '', 'High', '対策検討', '', '', '750000', '3', '', '遅延', '', '', '', '', '', '',], //2
          ['', 'PlantB', 'Attach系機械設備', 'N401/A plant__/OX2_/A', '3', '10', '6', '10', '今年', '2', '2022-05-20', '0', '', '', '', '', '注意', '', 'A plant/Di槽撹拌機交換（A）', '5000', '', '', '', '', '', '', '', '', '',], //3
          ['', 'PlantC', '回収温水熱交', 'N401/A plant__/OX2_/A/5E-09', '3', '10', '60', '10', '4', '', '', '', '', '', '', 'Low', '見直検討', '', '', '', '', '', '', '', '', '', '', '', '',], //4
        ],
        nestedHeaders: [
          ["", "", "", "", { label: "Impact", colspan: 5 }, { label: "Probability of failure", colspan: 6 }, { label: "Critical equipment Level", colspan: 3 }, "", "", "", "", "", { label: "Spare parts", colspan: 2 }, { label: "Status of measures", colspan: 4 }, { label: "Order", colspan: 2 }],
          ["CeListNo", "Plant", "Equipment", "Machine", "Level set <br>value", "Construction <br>period", "Parts <br>delivery date", "MTTR", "PossibilityOf<br>ContinuousProduction", "Count <br>of PM02", "Latest <br>PM02", "Count <br>of PM03", "Latest <br>PM03", "Count <br>of PM04", "Latest <br>PM04", "Impact for <br>production", "Probability <br>of failure", "Assessment", "Typical Task", "Labor <br>Cost(PM02)", "Period", "Next <br>event year", "situation", "BomCode", "Stock", "RCA or <br>Replace(hard)", "Spear parts or <br>Alternative(soft)", "Covered <br>from task", "Two <br>ways"],
        ],

        columns: [
          { data: "ceListNo", type: "text", readOnly: true },
          { data: "plant", type: "text" },
          { data: "equipment", type: "text" },
          { data: "machineName", type: "text" },
          {
            data: "levelSetValue",
            type: 'dropdown',
            source: ['Low', 'Middle', 'High']
          },
          { data: "typicalConstPeriod", type: 'numeric' },
          { data: "maxPartsDeliveryTimeInBom", type: 'numeric' },
          { data: "mttr", type: 'numeric', renderer: customRendererForMttr },
          {
            data: "possibilityOfContinuousProduction",
            type: 'dropdown',
            source: [1, 2, 3, 4, 5],
            className: 'htRight',
            readOnly: false
          },
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
    },

    emitData() {
      const hotInstance = this.$refs.hotTableComponent.hotInstance;
      const rows = hotInstance.countRows();
      const emittedData = [];

      for (let row = 0; row < rows; row++) {
        const levelSetValue = hotInstance.getDataAtCell(row, 4); // levelSetValueの値を取得
        const mttr = customRendererForMttr(hotInstance, null, row, 7); // MTTRの値を取得するためにcustomRendererForMttrを呼び出す
        const possibilityOfContinuousProduction = hotInstance.getDataAtCell(row, 8); // possibilityOfContinuousProductionの値を取得
        const countOfPM02 = hotInstance.getDataAtCell(row, 9); // countOfPM02の値を取得
        const countOfPM03 = hotInstance.getDataAtCell(row, 11); // countOfPM03の値を取得
        const countOfPM04 = hotInstance.getDataAtCell(row, 13); // countOfPM04の値を取得

        emittedData.push({ levelSetValue, mttr, possibilityOfContinuousProduction, countOfPM02, countOfPM03, countOfPM04 });
      }

      console.log('Emitting Data:', emittedData);
      this.$emit('data-emitted', emittedData);
    },

    updateImpactForProduction({ index, impactForProduction }) {
      console.log(`Updating impactForProduction at row ${index} with value ${impactForProduction}`);
      this.$refs.hotTableComponent.hotInstance.setDataAtCell(index, 15, impactForProduction);
    },

    updateProbabilityOfFailure({ index, probabilityOfFailure }) {
      console.log(`Updating probabilityOfFailure at row ${index} with value ${probabilityOfFailure}`);
      this.$refs.hotTableComponent.hotInstance.setDataAtCell(index, 16, probabilityOfFailure);
    }
  },

  components: {
    HotTable,
  },
});

export default CriticalEquipmentList;
</script>

<style scoped>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
