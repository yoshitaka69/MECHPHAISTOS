<template>
  <DataTable :value="sortedTasks" tableStyle="min-width: 50rem" class="striped-table">
      <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" sortable></Column>
  </DataTable>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

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

const defaultTask = () => ({
typicalTaskName: 'ー',
plant: 'ー',
typicalTaskCost: 'ー',
assessment: 'ー'
});

const priorityTasks = ref([]);

onMounted(async () => {
if (!companyCode) {
console.error("No company code found.");
priorityTasks.value = Array(20).fill(defaultTask());
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

<style>
.striped-table .p-datatable-thead > tr > th {
background-color: #2d3a4f;
color: white;
}

.striped-table .p-datatable-tbody > tr:nth-child(even) {
background-color: #e0e0e0; /* ここを変更して濃い灰色に設定 */
}

.striped-table .p-datatable-tbody > tr:nth-child(odd) {
background-color: white;
}

.striped-table .p-datatable {
border: 1px solid black;
}
</style>
