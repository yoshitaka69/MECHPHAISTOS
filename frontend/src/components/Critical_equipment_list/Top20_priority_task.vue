<template>
  <div class="card">
      <DataTable :value="sortedTasks" tableStyle="min-width: 50rem">
          <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header"></Column>
      </DataTable>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

const priorityTasks = ref([]);
const columns = [
  { field: 'typicalTaskName', header: 'Top20 Priority Tasks' },
  { field: 'plant', header: 'Plant' },
  { field: 'typicalTaskCost', header: 'Cost' },
  { field: 'assessment', header: 'Assessment' },
];

const userStore = useUserStore();
const companyCode = userStore.companyCode;

const priorityMap = {
  'Very High': 1,
  'High': 2,
  'Middle': 3,
  'Low': 4,
  'Very Low': 5
};

onMounted(async () => {
  if (!companyCode) {
    console.error("No company code found.");
    return;
  }
  
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${companyCode}`);
    if (response.data && response.data.length > 0) {
      const masterData = response.data.find(d => d.companyCode === companyCode);
      if (masterData && masterData.MasterDataTable) {
        priorityTasks.value = masterData.MasterDataTable.map(item => ({
          typicalTaskName: item.typicalTaskName || 'ー',
          plant: item.plant || 'ー',
          typicalTaskCost: item.typicalTaskCost !== null ? item.typicalTaskCost : 'ー',
          assessment: item.assessment || 'ー'
        }));
      }
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});

const sortedTasks = computed(() => {
  return priorityTasks.value
    .sort((a, b) => {
      return (priorityMap[a.assessment] || 6) - (priorityMap[b.assessment] || 6);
    })
    .slice(0, 25);
});
</script>
