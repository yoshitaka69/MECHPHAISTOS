<template>
  <div>
    <div class="text-900 font-semibold text-lg mt-3">
      Evaluate Equipment
    </div>
    <Divider />
    <MTTR_MTBF />
    <Bayes_Prediction /> <!-- Bayes_Predictionコンポーネントを追加 -->
  </div>
</template>

<script>
import Divider from "primevue/divider";
import MTTR_MTBF from "@/components/Critical_equipment_list/MTTR_MTBF.vue";
import Bayes_Prediction from "@/components/Critical_equipment_list/Bayes_Prediction.vue"; // Bayes_Predictionコンポーネントをインポート

export default {
  components: {
    Divider,
    MTTR_MTBF,
    Bayes_Prediction, // コンポーネントを登録
  },
  setup() {
    // ここで必要なロジックやデータを追加できます
  },
};
</script>

<style scoped>
/* 必要に応じてスタイルを追加 */
</style>
