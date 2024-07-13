<!-- components/TroubleHistoryTable.vue -->
<template>
  <div>
    <DataTable :value="troubleHistories" :stripedRows="true">
      <Column field="date" header="Date" />
      <Column field="pmType" header="PM Type" />
      <Column field="failureContent" header="Failure Content" />
      <Column field="failureType" header="Failure Type" />
      <Column field="repairCost" header="Repair Cost" />
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
    const troubleHistories = ref([]);
    const userStore = useUserStore();
    const companyCode = computed(() => userStore.companyCode);

    const fetchTroubleHistories = async () => {
      try {
        console.log('Fetching trouble histories with companyCode:', companyCode.value);
        const response = await axios.get('http://127.0.0.1:8000/api/reliability/troubleHistoryByCompany/', {
          params: {
            companyCode: companyCode.value,
          },
        });
        console.log('Response data:', response.data);

        const today = new Date();
        const oneYearAgo = new Date(today);
        oneYearAgo.setFullYear(today.getFullYear() - 1);
        const oneYearFromNow = new Date(today);
        oneYearFromNow.setFullYear(today.getFullYear() + 1);

        // companyCode に対応する troubleHistory を抽出し、日付をフィルタリング
        const companyData = response.data.find(item => item.companyCode === companyCode.value);
        if (companyData && companyData.troubleHistory) {
          troubleHistories.value = companyData.troubleHistory.filter(item => {
            const itemDate = new Date(item.date);
            return itemDate >= oneYearAgo && itemDate <= oneYearFromNow;
          }).map(item => ({
            date: item.date,
            pmType: item.pmType,
            failureContent: item.failureContent,
            failureType: item.failureType,
            repairCost: item.repairCost,
          }));
        }
        console.log('Filtered TroubleHistories:', troubleHistories.value);
      } catch (error) {
        console.error('Failed to fetch trouble histories:', error);
      }
    };

    onMounted(fetchTroubleHistories);

    return {
      troubleHistories,
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
