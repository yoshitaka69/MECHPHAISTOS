<template>

    <div class="card mb-0">
      <div class="flex justify-content-between mb-3">
        <div>
          <span class="block text-500 font-medium mb-3">Number of near misses</span>
          <div class="text-900 font-medium text-xl">{{ nearMissTotal }}件</div>
        </div>
        <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
          style="width: 2.5rem; height: 2.5rem">
          <i class="pi pi-map-marker text-orange-500 text-xl"></i>
        </div>
      </div>
      <span class="text-green-500 font-medium">%52+ </span>
      <span class="text-500">since last month</span>
    </div>

</template>


<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート


export default {
  setup() {
    const nearMissTotal = ref(0);
    const userStore = useUserStore();

    const fetchNearMissData = async () => {
      try {
        console.log("Fetching data with companyCode:", userStore.companyCode); // リクエストのログ
        const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/safetyIndicatorsByCompany/`, {
          params: { companyCode: userStore.companyCode }
        });
        console.log("Response data:", response.data); // レスポンスのログ
        const data = response.data.find(d => d.companyCode === userStore.companyCode);
        if (data && data.safetyIndicatorsList.length > 0) {
          nearMissTotal.value = data.safetyIndicatorsList[0].totalOfNearMiss;
        } else {
          console.log("No matching data found for companyCode:", userStore.companyCode);
        }
      } catch (error) {
        console.error('Error fetching data:', error); // エラーのログ
      }
    };

    onMounted(fetchNearMissData);

    return { nearMissTotal };
  },
};
</script>
