<template>
  <div class="card mb-0">
    <div class="flex justify-content-between mb-3" style="height: 150px">
      <div>
        <span class="block text-500 font-medium mb-3">Relatively Dangerous Area</span>
        <div class="text-900 large-bold-text">{{ dangerArea }}</div>
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
import { useUserStore } from '@/stores/userStore';

export default {
  setup() {
    const dangerArea = ref('');
    const userStore = useUserStore();

    const fetchDangerArea = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/nearMiss/safetyIndicatorsByCompany/', {
          params: { companyCode: userStore.companyCode }
        });
        const dataList = response.data;

        // Find the object that contains the companyCode
        const targetData = dataList.find(data => data.companyCode === userStore.companyCode);

        // Check if safetyIndicatorsList exists and has elements
        if (targetData && targetData.safetyIndicatorsList && targetData.safetyIndicatorsList.length > 0) {
          dangerArea.value = targetData.safetyIndicatorsList[0].dangerArea;
        } else {
          console.log('Data is empty or does not contain safetyIndicatorsList for the specified companyCode');
        }
      } catch (error) {
        console.error('Error fetching danger area:', error);
      }
    };

    onMounted(fetchDangerArea);

    return { dangerArea };
  },
};
</script>

<style scoped>

.large-bold-text {
    font-size: 4rem; /* 更に大きいフォントサイズに調整 */
    font-weight: bold; /* 太字 */
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 太字に設定 */
    font-size: 1.5em; /* 現在のフォントサイズの2倍 */
    color: black; /* 文字色を黒に設定 */
}
</style>
