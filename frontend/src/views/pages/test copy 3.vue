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

const columns = [
  { field: 'orderAlertDate', header: 'Order Alert' },
  { field: 'partsName', header: 'Parts Name' },
  { field: 'deliveryTime', header: 'Delivery Time' },
  { field: 'eventDate', header: 'Event Date' },
  { field: 'location', header: 'Location' },
  { field: 'Check', header: 'Check' },
];

const userStore = useUserStore();
const companyCode = userStore.companyCode;


const defaultTask = () => ({
  orderAlertDate: 'ー',
  partsName: 'ー',
  deliveryTime: 'ー',
  eventDate: 'ー',
  location: 'ー',
  check: 'false',
});



onMounted(async () => {
  if (!companyCode) {
    console.error("No company code found.");
    priorityTasks.value = Array(20).fill(defaultTask());
    return;
  }

  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/junctionTable/alertScheduleByCompany/?format=json&companyCode=${companyCode}`);
    
    if (response.data && response.data.length > 0) {
      const masterData = response.data.find(d => d.companyCode === companyCode);
      if (masterData && masterData.MasterDataTable) {
        priorityTasks.value = masterData.MasterDataTable.map(item => ({
          typicalTaskName: item.typicalTaskName || 'ー',
          plant: item.plant || 'ー',
          typicalTaskCost: item.typicalTaskCost !== null ? item.typicalTaskCost.toString() : 'ー',
          assessment: item.assessment || 'ー'
        }));
      }
    }
    // APIから取得したデータが20件未満の場合、残りをデフォルトデータで補う
    const itemsNeeded = 20 - priorityTasks.value.length;
    if (itemsNeeded > 0) {
      priorityTasks.value.push(...Array(itemsNeeded).fill(defaultTask()));
    }
  } catch (error) {
    console.error("Error fetching data:", error);
    priorityTasks.value = Array(20).fill(defaultTask());
  }
});

const sortedTasks = computed(() => {
  return priorityTasks.value
    .sort((a, b) => (priorityMap[a.assessment] || 6) - (priorityMap[b.assessment] || 6))
    .slice(0, 20); // 20件に制限
});
</script>
