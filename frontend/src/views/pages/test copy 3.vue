<template>
  <div id="app">
    <SimulationGraph :costData="costData" />
    <Simulation_table @update-cost-data="handleUpdateCostData" />
  </div>
</template>

<script>
import { ref } from 'vue';
import Simulation_table from '../../components/Repairing_cost/Simulations/Simulation_table.vue';
import SimulationGraph from '../../components/Repairing_cost/Simulations/Simulation_graph.vue';

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
