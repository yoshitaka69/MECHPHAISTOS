<template>

<div id="example1">
  <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br/>
  <button v-on:click="swapHotData" class="controls">Load new data</button>
</div>

</template>


<script>
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';

// register Handsontable's modules
registerAllModules();

const ExampleComponent = defineComponent({
  data() {
    return {
      hotSettings: {
        data: [
          ['A1', 'B1', 'C1', 'D1','E1','F1','G1','H1','I1','J1','K1','L1','M1','N1','O1','P1','Q1','R1','S1','T1','U1','V1','W1','X1','Y1','Z1','AA1','AB1','AC1','AD1'],
          ['A2', 'B2', 'C2', 'D2','E2','F2','G2','H2','I2','J2','K2','L2','M2','N2','O2','P2','Q2','R2','S2','T2','U2','V2','W2','X2','Y2','Z2','AA2','AB2','AC2','AD2'],
          ['A3', 'B3', 'C3', 'D3','E3','F3','G3','H3','I3','J3','K3','L3','M3','N3','O3','P3','Q3','R3','S3','T3','U3','V3','W3','X3','Y3','Z3','AA3','AB3','AC3','AD3'],
          ['A4', 'B4', 'C4', 'D4','E4','F4','G4','H4','I4','J4','K4','L4','M4','N4','O4','P4','Q4','R4','S4','T4','U4','V4','W4','X4','Y4','Z4','AA4','AB4','AC4','AD4'],
        ],
        nestedHeaders: [
          ["","","",{label:"Impact", colspan:5},{label:"Probability of failure", colspan:6},{label:"Critical equipment Level", colspan:3},"","","","","",{label:"Spare parts", colspan:2},{label:"Status of measures", colspan:4},{label:"Order", colspan:2},],
          ["Plant","Equipment","Function","Level set value","Construction period", "Parts delivery date","MTTR","Possibility of production","Count of PM02","Latest PM02","Count of PM03","Latest PM03","Count of PM04","Latest PM04","Impact for production","Probability of failure","Assessment","Task of PM02","Cost(PM02)","Period","Next event year","situation","Category","Stock","RCA or Replace(hard)","Spear parts or Alternative(soft)","Covered from task","Two ways","Alert order","Order situation"],
      ],
        width: '100%',
        height: 'auto',
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
        licenseKey: 'non-commercial-and-evaluation'
      }
    };
  },
  methods: {
    swapHotData: function() {
      //load new data
      // The Handsontable instance is stored under the `hotInstance` property of the wrapper component.
      this.$refs.hotTableComponent.hotInstance.loadData([['new', 'data']]);
    }
  },

  components: {
    HotTable,
  }
});

export default ExampleComponent;

</script>