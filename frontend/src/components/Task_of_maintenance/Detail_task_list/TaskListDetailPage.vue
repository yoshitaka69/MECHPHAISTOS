<template>
    <div>
      <div class="surface-ground px-4 py-8 md:px-6 lg:px-8">
        <div class="p-fluid flex flex-column lg:flex-row">
          <ul
            class="list-none m-0 p-0 flex flex-row lg:flex-column justify-content-evenly md:justify-content-between lg:justify-content-start mb-5 lg:pr-8 lg:mb-0"
          >
            <li>
              <a
                @click="selectTab('detailTaskList')"
                :class="[
                  'flex align-items-center cursor-pointer p-3 border-round',
                  selectedTab === 'detailTaskList' ? 'text-primary' : 'text-800',
                  'hover:surface-hover transition-duration-150 transition-colors',
                  'font-bold'
                ]"
              >
                <i class="pi pi-list md:mr-2"></i>
                <span class="font-medium hidden md:block">Detail Task List</span>
              </a>
            </li>
          </ul>
          <div class="surface-card p-5 shadow-2 border-round flex-auto">
            <DetailTaskList v-if="selectedTab === 'detailTaskList'" />
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import DetailTaskList from "@/components/Task_of_maintenance/Detail_task_list/DetailTaskList.vue";
  
  export default {
    components: {
      DetailTaskList,
    },
    setup() {
      const selectedTab = ref("detailTaskList");
  
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
  