<template>
  <div id="totalCostTable">
    <hot-table ref="totalCostTableComponent" :settings="totalCostSettings"></hot-table>
  </div>
</template>

<script>
import { HotTable } from '@handsontable/vue3';

export default {
  name: 'SimulationYearCost',
  props: {
    totalCostSettings: {
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
#totalCostTable {
  width: 100%;
  height: 150px;
}
</style>
