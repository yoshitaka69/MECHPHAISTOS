<template>

    <div class="card mb-0">
      <div class="flex justify-content-between mb-3">
        <div>
          <span class="block text-500 font-medium mb-3">Safety Indicators</span>
              <!-- safetyIndicatorsの表示 -->
    <div :class="safetyIndicatorsClass">{{ safetyIndicators }}</div>
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
import { ref, computed, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';

export default {
  setup() {
    const safetyIndicators = ref('');
    const userStore = useUserStore();

    const fetchSafetyIndicators = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/safetyIndicatorsByCompany/`, {
          params: { companyCode: userStore.companyCode }
        });
        const data = response.data.find(d => d.companyCode === userStore.companyCode);
        if (data && data.safetyIndicatorsList.length > 0) {
          safetyIndicators.value = data.safetyIndicatorsList[0].safetyIndicators; // safetyIndicatorsの設定
        }
      } catch (error) {
        console.error('Error fetching safety indicators:', error);
      }
    };

    onMounted(fetchSafetyIndicators);

    const safetyIndicatorsClass = computed(() => {
      switch (safetyIndicators.value) {
        case 'High':
          return 'text-red font-bold';
        case 'Middle':
          return 'text-yellow font-bold';
        case 'Low':
          return 'text-blue font-bold';
        default:
          return '';
      }
    });

    return { safetyIndicators, safetyIndicatorsClass };
  },
};
</script>
