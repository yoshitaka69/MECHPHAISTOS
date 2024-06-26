<template>
  <div>
    <div>
        <span class="block text-500 font-medium mb-3">Safety Indicators</span>
        <!-- PrimeVue Buttonを利用してsafetyIndicatorsの表示 -->
        <Button :label="safetyIndicators" :class="['custom-button-style', ...buttonClass.split(' ')]" />
      </div>
    <br>
    <br>
      <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
        style="width: 2.5rem; height: 2.5rem">
        <i class="pi pi-map-marker text-orange-500 text-xl"></i>
    </div>
    <span class="text-green-500 font-medium">%52+ </span>
    <span class="text-500">since last month</span>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';
import Button from 'primevue/button';  // PrimeVue Buttonのインポート

export default {
  components: {
    Button  // コンポーネントにButtonを登録
  },
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

    const buttonClass = computed(() => {
      let classes = [];
      switch (safetyIndicators.value) {
        case 'Very High':
        case 'High':
          classes.push('p-button-danger', 'blinking'); // 'danger'は赤色, 'blinking'は点滅
          break;
        case 'Middle':
          classes.push('p-button-warning'); // 'warning'は黄色
          break;
        case 'Low':
        case 'Very Low':
          classes.push('p-button-success'); // 'success'は緑色
          break;
        default:
          classes.push('p-button-secondary'); // デフォルトのグレー
      }
      return classes.join(' ');
    });

    return { safetyIndicators, buttonClass };
  },
};
</script>


<style scoped>

@keyframes blink {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 太字に設定 */
    font-size: 1.5em; /* 現在のフォントサイズの2倍 */
    color: black; /* 文字色を黒に設定 */
}

.blinking {
  animation: blink 1.5s linear infinite;
}


.custom-button-style {
    width: 150px;       /* ボタンの幅 */
    height: 50px;       /* ボタンの高さ */
    font-size: 20px;    /* 文字のサイズ */
    line-height: 50px;  /* テキストの行高、ボタンの高さに合わせて中央揃え */
}

</style>
