<template>
  <div id="app">
    <SimulationGraph :costData="costData" />
    <Simulation_table @update-cost-data="handleUpdateCostData" />
  </div>
</template>

<script>
import { ref } from 'vue';
import Simulation_table from './Simulation_table.vue';
import SimulationGraph from './SimulationGraph.vue';

export default {
  name: 'App',
  components: {
    Simulation_table,
    SimulationGraph,
  },
  setup() {
    const costData = ref(null);

    const handleUpdateCostData = (data) => {
      costData.value = data;
    };

    return {
      costData,
      handleUpdateCostData,
    };
  },
};
</script>
