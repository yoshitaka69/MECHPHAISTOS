<style scoped>
.swing {
  display: inline-block;
  animation: swing ease-in-out 1s infinite alternate;
}

@keyframes swing {
  0% {
    transform: rotate(-10deg);
  }
  100% {
    transform: rotate(10deg);
  }
}

.vibrate {
  display: inline-block;
  animation: vibrate 0.5s infinite alternate;
}

@keyframes vibrate {
  0% {
    transform: translateY(-5px);
  }
  100% {
    transform: translateY(5px);
  }
}

.large-bold-text {
  font-size: 2rem;
  /* 更に大きいフォントサイズに調整 */
  font-weight: bold;
  /* 太字 */
}

.block.text-500.font-medium.mb-3 {
  font-weight: bold;
  /* 太字に設定 */
  font-size: 1.5em;
  /* 現在のフォントサイズの2倍 */
  color: black;
  /* 文字色を黒に設定 */
}
</style>

<template>

  <div class="card mb-0">
    <div class="flex justify-content-between mb-3" style="height: 65px">
      <div>
        <span class="block text-500 font-medium mb-3">Action Items</span>
        <!-- countOfActionItemsの表示 -->
        <div class="large-bold-text">Action Items: {{ countOfActionItems }} &nbsp;&nbsp;Solved Action Items: {{
          countOfSolvedActionItems }}</div>

        <!-- rateOfActionItemsの表示 -->
        <div class="large-bold-text">Rate of Action Items: {{ rateOfActionItems }}%</div>
      </div>
      <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
        style="width: 2.5rem; height: 2.5rem">
        <i class="pi pi-map-marker text-orange-500 text-xl"></i>
      </div>
      
      <i class="pi pi-thumbs-up swing" style="font-size: 3rem"></i>

    </div>
  </div>
</template>




<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';

export default {
  setup() {
    const countOfActionItems = ref(0);
    const countOfSolvedActionItems = ref(0);
    const rateOfActionItems = ref('');

    const userStore = useUserStore();

    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/nearMiss/safetyIndicatorsByCompany/', {
          params: { companyCode: userStore.companyCode }
        });
        const dataList = response.data;

        // 対象のcompanyCodeを持つオブジェクトを見つける
        const targetData = dataList.find(data => data.companyCode === userStore.companyCode);

        // 対象のsafetyIndicatorsListが存在し、要素があるかをチェック
        if (targetData && targetData.safetyIndicatorsList && targetData.safetyIndicatorsList.length > 0) {
          const firstItem = targetData.safetyIndicatorsList[0];
          countOfActionItems.value = firstItem.countOfActionItems;
          countOfSolvedActionItems.value = firstItem.countOfSolvedActionItems;
          rateOfActionItems.value = firstItem.rateOfActionItems;
        } else {
          console.log('No safety indicators data available for the specified companyCode');
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

