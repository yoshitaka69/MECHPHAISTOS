<template>
  <div class="card mb-0" v-if="filteredCosts.length > 0">
    <div v-for="(cost, index) in filteredCosts" :key="index">
      <div class="flex justify-content-between mb-3">
        <div>
          <span class="block text-500 font-medium mb-3">Repairing Cost/year</span>
          <div class="text-900 font-medium text-xl">Plant&nbsp;:&nbsp; {{ cost.plant }}</div>
          <div class="text-900 font-medium text-xl">Year&nbsp;:&nbsp;{{ cost.year }}</div>
          <div class="text-900 font-medium text-xl">Total Actual Cost&nbsp;:&nbsp;{{ cost.totalActualCost }}</div>
        </div>
        <div class="flex align-items-center justify-content-center bg-purple-100 border-round"
          style="width: 2.5rem; height: 2.5rem">
          <!--以下が右側のアイコン-->
          <i class="pi pi-comment text-purple-500 text-xl"></i>
        </div>
      </div>
      <span class="text-green-500 font-medium">85 </span>
      <span class="text-500">responded</span>
    </div>
  </div>
  <div class="card mb-0" v-else>
    <span>No Data</span>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';

export default {
  setup() {
    const filteredCosts = ref([]);

    const userStore = useUserStore();

    const fetchTotalActualCost = async () => {
      const currentYear = new Date().getFullYear();
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/calculation/summedActualCostByCompany/?format=json', {
          params: { companyCode: userStore.companyCode }
        });
        const companyData = response.data.find((company) => company.companyCode === userStore.companyCode);
        if (companyData && companyData.summedActualCostList) {
          const currentYearCosts = companyData.summedActualCostList.filter((item) => item.year === currentYear);
          if (currentYearCosts.length > 0) {
            filteredCosts.value = currentYearCosts; // 現在の年に一致するデータをセット
          } else {
            filteredCosts.value = []; // "No Data" を表示するために空の配列をセット
          }
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    onMounted(fetchTotalActualCost);

    return { filteredCosts };
  }
};
</script>
