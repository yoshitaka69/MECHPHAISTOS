
<template>
  <div class="col-12 lg:col-6 xl:col-4">
    <div class="card mb-0">
      <div class="flex justify-content-between mb-3">
        <div>
          <span class="block text-500 font-medium mb-3">Number of near misses</span>
                <!-- countOfActionItemsの表示 -->
      <div class="text-900 font-medium text-xl">Action Items: {{ countOfActionItems }}</div>

      <!-- countOfSolvedActionItemsの表示 -->
      <div class="text-900 font-medium text-xl">Solved Action Items: {{ countOfSolvedActionItems }}</div>

      <!-- rateOfActionItemsの表示 -->
      <div class="text-900 font-medium text-xl">Rate of Action Items: {{ rateOfActionItems }}</div>
        </div>
        <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
          style="width: 2.5rem; height: 2.5rem">
          <i class="pi pi-map-marker text-orange-500 text-xl"></i>
        </div>
      </div>
      <span class="text-green-500 font-medium">%52+ </span>
      <span class="text-500">since last month</span>
    </div>
  </div>
</template>




<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

export default {
  setup() {
    const countOfActionItems = ref(0);
    const countOfSolvedActionItems = ref(0);
    const rateOfActionItems = ref('');

    const userStore = useUserStore();

    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/nearMiss/trendSafetyIndicatorsByCompany/', {
          params: { companyCode: userStore.companyCode }
        });
        const data = response.data;
        if (data && data.safetyIndicatorsList && data.safetyIndicatorsList.length > 0) {
          const firstItem = data.safetyIndicatorsList[0];
          countOfActionItems.value = firstItem.countOfActionItems;
          countOfSolvedActionItems.value = firstItem.countOfSolvedActionItems;
          rateOfActionItems.value = firstItem.rateOfActionItems;
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    onMounted(fetchData);

    return { countOfActionItems, countOfSolvedActionItems, rateOfActionItems };
  },
};
</script>
