<template>
  <div>
    <div class="surface-ground px-4 py-8 md:px-6 lg:px-8">
      <div class="p-fluid flex flex-column lg:flex-row">
        <ul
          class="list-none m-0 p-0 flex flex-row lg:flex-column justify-content-evenly md:justify-content-between lg:justify-content-start mb-5 lg:pr-8 lg:mb-0"
        >
          <li>
            <a
              @click="selectTab('annualCost')"
              :class="[
                'flex align-items-center cursor-pointer p-3 border-round',
                selectedTab === 'annualCost' ? 'text-primary' : 'text-800',
                'hover:surface-hover transition-duration-150 transition-colors',
                'font-bold'
              ]"
            >
              <i class="pi pi-calendar md:mr-2"></i>
              <span class="font-medium hidden md:block">Annual Cost</span>
            </a>
          </li>
          <li>
            <a
              @click="selectTab('costByPlant')"
              :class="[
                'flex align-items-center cursor-pointer p-3 border-round',
                selectedTab === 'costByPlant' ? 'text-primary' : 'text-800',
                'hover:surface-hover transition-duration-150 transition-colors',
                'font-bold'
              ]"
            >
              <i class="pi pi-chart-bar md:mr-2"></i>
              <span class="font-medium hidden md:block">Cost by Plant</span>
            </a>
          </li>
          <li>
            <a
              @click="selectTab('vsPlantCost')"
              :class="[
                'flex align-items-center cursor-pointer p-3 border-round',
                selectedTab === 'vsPlantCost' ? 'text-primary' : 'text-800',
                'hover:surface-hover transition-duration-150 transition-colors',
                'font-bold'
              ]"
            >
              <i class="pi pi-chart-line md:mr-2"></i>
              <span class="font-medium hidden md:block">Vs Plant Cost</span>
            </a>
          </li>
          <li>
            <a
              @click="selectTab('simulationResult')"
              :class="[
                'flex align-items-center cursor-pointer p-3 border-round',
                selectedTab === 'simulationResult' ? 'text-primary' : 'text-800',
                'hover:surface-hover transition-duration-150 transition-colors',
                'font-bold'
              ]"
            >
              <i class="pi pi-cog md:mr-2"></i>
              <span class="font-medium hidden md:block">Result of Simulation</span>
            </a>
          </li>
        </ul>
        <div class="surface-card p-5 shadow-2 border-round flex-auto">
          <AnnualCostChart v-if="selectedTab === 'annualCost'" />
          <CostByPlantChart v-else-if="selectedTab === 'costByPlant'" />
          <VsPlantCostChart v-else-if="selectedTab === 'vsPlantCost'" />
          <SimulationResultChart v-else-if="selectedTab === 'simulationResult'" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import AnnualCostChart from "@/components/Repairing_cost/Repairing_cost_detail/AnnualCostChart.vue";
import CostByPlantChart from "@/components/Repairing_cost/Repairing_cost_detail/CostByPlantChart.vue";
import VsPlantCostChart from "@/components/Repairing_cost/Repairing_cost_detail/VsPlantCostChart.vue";
import SimulationResultChart from "@/components/Repairing_cost/Repairing_cost_detail/SimulationResultChart.vue";

export default {
  components: {
    AnnualCostChart,
    CostByPlantChart,
    VsPlantCostChart,
    SimulationResultChart,
  },
  setup() {
    const selectedTab = ref("annualCost");

    const selectTab = (tab) => {
      selectedTab.value = tab;
    };

    return {
      selectedTab,
      selectTab,
    };
  },
};
</script>

<style scoped>
.surface-ground {
  /* 背景色を薄い橙色に設定 */
  background-color: #FFEDD5 !important;
}

.font-bold {
  font-weight: bold;
}

.cursor-pointer {
  cursor: pointer;
}

.border-round {
  border-radius: 4px;
}

.transition-duration-150 {
  transition-duration: 150ms;
}

.transition-colors {
  transition-property: color, background-color;
}

.hover\:surface-hover:hover {
  background-color: var(--surface-hover);
}
</style>
