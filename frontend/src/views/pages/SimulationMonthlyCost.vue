<template>
  <div id="monthlyCostTable">
    <hot-table ref="monthlyCostTableComponent" :settings="monthlyCostSettings"></hot-table>
  </div>
</template>

<script>
import { HotTable } from '@handsontable/vue3';

export default {
  name: 'SimulationMonthlyCost',
  props: {
    monthlyCostSettings: {
      type: Object,
      required: true
    }
  },
  components: {
    HotTable
  }
};
</script>

<style scoped>
#monthlyCostTable {
  width: 100%;
  height: 150px;
}
</style>
