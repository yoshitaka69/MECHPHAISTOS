<!-- components/PM02TaskTable.vue -->
<template>
  <div>
    <DataTable :value="taskPlan" :stripedRows="true">
      <Column field="date" header="Date" />
      <Column field="pmType" header="PM Type" />
      <Column field="pMContent" header="Prevent Maintenance Content" />
      <Column field="maintenanceCategory" header="Maintenance Category" />
      <Column field="laborCost" header="Maintenance Cost" :body="formatCost" />
    </DataTable>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import { useUserStore } from '@/stores/userStore'; // インポートの確認

export default {
  components: {
    DataTable,
    Column,
  },
  setup() {
    const taskPlan = ref([]);
    const userStore = useUserStore();
    const companyCode = computed(() => userStore.companyCode);

    const fetchPM02TaskPlan = async () => {
      try {
        console.log('Fetching PM02 task plan with companyCode:', companyCode.value);

        // PPM02のAPIエンドポイントからデータを取得
        const response = await axios.get('http://127.0.0.1:8000/api/task/taskListPPM02ByCompany/', {
          params: {
            companyCode: companyCode.value,
          },
        });

        console.log('Response data PM02:', response.data);

        if (!response.data || !Array.isArray(response.data)) {
          console.error('Unexpected response format:', response.data);
          return;
        }

        // companyCode に対応する taskListPPM02 を抽出
        const companyData = response.data.find(item => item.companyCode === companyCode.value);
        if (!companyData || !Array.isArray(companyData.taskListPPM02)) {
          console.error('No taskListPPM02 found for companyCode:', companyCode.value);
          return;
        }

        // データを整形してPM02としてテーブルに追加
        const pm02Data = companyData.taskListPPM02.map(item => ({
          date: item.nextEventDate,
          pmType: 'PM02',
          pMContent: item.pM02Content,
          maintenanceCategory: item.maintenanceCategory,
          laborCost: parseFloat(item.laborCostOfPPM02).toFixed(2),
        }));

        taskPlan.value.push(...pm02Data);

        console.log('Processed PM02TaskPlan:', taskPlan.value);
      } catch (error) {
        console.error('Failed to fetch PM02 task plan:', error);
      }
    };

    const fetchPM03TaskPlan = async () => {
      try {
        console.log('Fetching PM03 task plan with companyCode:', companyCode.value);

        // PPM03のAPIエンドポイントからデータを取得
        const response = await axios.get('http://127.0.0.1:8000/api/task/taskListPPM03ByCompany/', {
          params: {
            companyCode: companyCode.value,
          },
        });

        console.log('Response data PM03:', response.data);

        if (!response.data || !Array.isArray(response.data)) {
          console.error('Unexpected response format:', response.data);
          return;
        }

        // companyCode に対応する taskListPPM03 を抽出
        const companyData = response.data.find(item => item.companyCode === companyCode.value);
        if (!companyData || !Array.isArray(companyData.taskListPPM03)) {
          console.error('No taskListPPM03 found for companyCode:', companyCode.value);
          return;
        }

        // データを整形してPM03としてテーブルに追加
        const pm03Data = companyData.taskListPPM03.map(item => ({
          date: item.nextEventDate,
          pmType: 'PM03',
          pMContent: item.pM03Content,
          maintenanceCategory: item.maintenanceCategory,
          laborCost: parseFloat(item.laborCostOfPPM03).toFixed(2),
        }));

        taskPlan.value.push(...pm03Data);

        console.log('Processed PM03TaskPlan:', taskPlan.value);
      } catch (error) {
        console.error('Failed to fetch PM03 task plan:', error);
      }
    };

    const formatCost = (rowData) => {
      return parseFloat(rowData.laborCost).toFixed(2);
    };

    onMounted(async () => {
      await fetchPM02TaskPlan();
      await fetchPM03TaskPlan();
      // データを日付順にソート
      taskPlan.value.sort((a, b) => new Date(a.date) - new Date(b.date));
      console.log('Final sorted task plan:', taskPlan.value);
    });

    return {
      taskPlan,
      formatCost,
    };
  },
};
</script>

<style>
.p-datatable .p-datatable-tbody > tr:nth-child(odd) {
  background-color: #f9f9f9;
}

.p-datatable .p-datatable-tbody > tr:nth-child(even) {
  background-color: #ffffff;
}

.p-datatable .p-datatable-tbody > tr:hover {
  background-color: #f1f1f1;
}
</style>
