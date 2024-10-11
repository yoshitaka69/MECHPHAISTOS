<template>
  <DataTable :value="sortedTasks" tableStyle="min-width: 50rem" class="styled-table">
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
  { field: 'equipment', header: 'Equipment' },
  { field: 'machineName', header: 'Machine Name' },
  { field: 'pmType', header: 'PM Type' },
  { field: 'typicalTaskCost', header: 'Cost' },
  { field: 'assessment', header: 'Assessment' }
];

const userStore = useUserStore();
const companyCode = userStore.companyCode;

const defaultTask = () => ({
  typicalTaskName: 'ー',
  plant: 'ー',
  equipment: 'ー',
  machineName: 'ー',
  pmType: 'ー',
  typicalTaskCost: 'ー',
  assessment: 'ー'
});

const priorityTasks = ref([]);

onMounted(async () => {
  console.log('Mounted. Company code:', companyCode); 
  if (!companyCode) {
      console.error('No company code found.');
      priorityTasks.value = Array(20).fill(defaultTask());
      return;
  }

  try {
      const response = await axios.get(`http://127.0.0.1:8000/api/junctionTable/ceListAndTaskByCompany/?companyCode=${companyCode}`);
      console.log('API response:', response);
      if (response.data && response.data.length > 0) {
          const companyData = response.data.find((d) => d.companyCode === companyCode);
          console.log('Filtered companyData:', companyData);
          if (companyData && companyData.CeListAndTaskList) {
              if (companyData.CeListAndTaskList.length > 0) {
                  priorityTasks.value = companyData.CeListAndTaskList.map((item) => ({
                      typicalTaskName: item?.no1HighPriorityTaskName || 'ー',
                      plant: item?.plant || 'ー',
                      equipment: item?.equipment || 'ー',
                      machineName: item?.no1HighLevelMachine || 'ー',
                      pmType: 'ー',
                      typicalTaskCost: 'ー',
                      assessment: 'ー'
                  }));
              } else {
                  console.warn('CeListAndTaskList is empty. Setting default tasks.');
                  priorityTasks.value = Array(20).fill(defaultTask());
              }
          }
      }

      const itemsNeeded = 20 - priorityTasks.value.length;
      if (itemsNeeded > 0) {
          priorityTasks.value.push(...Array(itemsNeeded).fill(defaultTask()));
      }
  } catch (error) {
      console.error('Error fetching data:', error); 
      priorityTasks.value = Array(20).fill(defaultTask());
  }
});

const sortedTasks = computed(() => {
  return priorityTasks.value.slice(0, 20);
});
</script>

<style>
.styled-table .p-datatable-thead > tr > th {
  background-color: #003366;
  color: #ffffff;
  font-weight: bold;
  padding: 10px;
  text-align: center;
  border-bottom: 2px solid #006699;
}

.styled-table .p-datatable-tbody > tr:nth-child(even) {
  background-color: #f0f8ff;
}

.styled-table .p-datatable-tbody > tr:nth-child(odd) {
  background-color: #ffffff;
}

.styled-table .p-datatable-tbody > tr:hover {
  background-color: #cce7ff; /* Hover effect */
}

.styled-table .p-datatable {
  border-collapse: collapse;
  width: 100%;
  font-family: Arial, sans-serif;
  font-size: 14px;
  color: #333;
}

.styled-table .p-datatable-tbody > tr > td {
  padding: 12px 8px;
  text-align: left;
  border-bottom: 1px solid #dddddd;
}

.styled-table .p-datatable-tbody > tr > td:first-child {
  font-weight: bold;
}

.styled-table .p-datatable {
  border: 1px solid #cccccc;
}
</style>
