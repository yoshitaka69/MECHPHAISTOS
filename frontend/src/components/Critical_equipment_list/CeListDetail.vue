<template>
  <div>
    <div class="surface-ground px-4 py-8 md:px-6 lg:px-8">
      <div class="p-fluid flex flex-column lg:flex-row">
        <ul
          class="list-none m-0 p-0 flex flex-row lg:flex-column justify-content-evenly md:justify-content-between lg:justify-content-start mb-5 lg:pr-8 lg:mb-0"
        >
          <li>
            <a
              @click="selectTab('criticalEquipment')"
              :class="[
                'flex align-items-center cursor-pointer p-3 border-round',
                selectedTab === 'criticalEquipment' ? 'text-primary' : 'text-800',
                'hover:surface-hover transition-duration-150 transition-colors'
              ]"
            >
              <i class="pi pi-database md:mr-2"></i>
              <span class="font-medium hidden md:block">Critical Equipment</span>
            </a>
          </li>
          <li>
            <a
              @click="selectTab('evaluateEquipment')"
              :class="[
                'flex align-items-center cursor-pointer p-3 border-round',
                selectedTab === 'evaluateEquipment' ? 'text-primary' : 'text-800',
                'hover:surface-hover transition-duration-150 transition-colors'
              ]"
            >
              <i class="pi pi-chart-line md:mr-2"></i>
              <span class="font-medium hidden md:block">Evaluate Equipment</span>
            </a>
          </li>
          <li>
            <a
              @click="selectTab('taskList')"
              :class="[
                'flex align-items-center cursor-pointer p-3 border-round',
                selectedTab === 'taskList' ? 'text-primary' : 'text-800',
                'hover:surface-hover transition-duration-150 transition-colors'
              ]"
            >
              <i class="pi pi-list md:mr-2"></i>
              <span class="font-medium hidden md:block">Task List</span>
            </a>
          </li>
          <li>
            <a
              @click="selectTab('partsList')"
              :class="[
                'flex align-items-center cursor-pointer p-3 border-round',
                selectedTab === 'partsList' ? 'text-primary' : 'text-800',
                'hover:surface-hover transition-duration-150 transition-colors'
              ]"
            >
              <i class="pi pi-box md:mr-2"></i>
              <span class="font-medium hidden md:block">Parts List</span>
            </a>
          </li>
          <li>
            <a
              @click="selectTab('workingRecord')"
              :class="[
                'flex align-items-center cursor-pointer p-3 border-round',
                selectedTab === 'workingRecord' ? 'text-primary' : 'text-800',
                'hover:surface-hover transition-duration-150 transition-colors'
              ]"
            >
              <i class="pi pi-book md:mr-2"></i>
              <span class="font-medium hidden md:block">Working Record</span>
            </a>
          </li>
        </ul>
        <div class="surface-card p-5 shadow-2 border-round flex-auto">
          <CriticalEquipment v-if="selectedTab === 'criticalEquipment'" />
          <EvaluateEquipment v-else-if="selectedTab === 'evaluateEquipment'" />
          <TaskList v-else-if="selectedTab === 'taskList'" />
          <PartsList v-else-if="selectedTab === 'partsList'" />
          <WorkingRecord v-else-if="selectedTab === 'workingRecord'" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import CriticalEquipment from "@/components/Critical_equipment_list/CriticalEquipment.vue";
import EvaluateEquipment from "@/components/Critical_equipment_list/EvaluateEquipment";
import TaskList from "@/components/Critical_equipment_list/TaskList";
import PartsList from "@/components/Critical_equipment_list/PartsList";
import WorkingRecord from "@/components/Critical_equipment_list/WorkingRecord";

export default {
  components: {
    CriticalEquipment,
    EvaluateEquipment,
    TaskList,
    PartsList,
    WorkingRecord,
  },
  setup() {
    const selectedTab = ref("criticalEquipment");

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
