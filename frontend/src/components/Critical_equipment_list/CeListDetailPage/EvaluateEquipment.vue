<template>
  <div class="bg-light-gray p-4">
      <div class="text-900 font-semibold text-lg mt-3">Evaluate Equipment</div>
      <Divider />
      <div class="flex flex-col md:flex-row gap-4">
          <!-- ワイブル分布を左上に配置 -->
          <div class="flex-1 overflow-hidden">
              <Weibull_distribution class="responsive-component" />
          </div>
          <!-- MTTRを右上に配置 -->
          <div class="flex-1 overflow-hidden">
              <MTTR_MTBF class="responsive-component" />
          </div>
      </div>
      <!-- ベイズ推定を下に配置 -->
      <div class="mt-4 overflow-hidden">
          <Bayesian_estimation class="responsive-component" />
      </div>
  </div>
</template>

<script>
import Divider from 'primevue/divider';
import MTTR_MTBF from '@/components/Critical_equipment_list/CeListDetailPage/MTTR_MTBF.vue';
import Bayesian_estimation from '@/components/Critical_equipment_list/CeListDetailPage/Bayesian_estimation/Bayesian_estimation.vue';
import Weibull_distribution from '@/components/Critical_equipment_list/CeListDetailPage/Weibull_distribution.vue';

export default {
  components: {
      Divider,
      MTTR_MTBF,
      Bayesian_estimation,
      Weibull_distribution
  },
  setup() {
      // ここで必要なロジックやデータを追加できます
  }
};
</script>

<style scoped>
.bg-light-gray {
  background-color: #f0f0f0; /* 薄い灰色の背景色 */
}

.p-4 {
  padding: 1rem; /* パディングを追加 */
}

.flex {
  display: flex;
}

.flex-1 {
  flex: 1;
  min-width: 0; /* flexboxの要素が縮小可能になる */
}

.flex-col {
  flex-direction: column;
}

.md\:flex-row {
  flex-direction: row;
}

.gap-4 {
  gap: 1rem;
}

.mt-4 {
  margin-top: 1rem;
}

.overflow-hidden {
  overflow: hidden; /* はみ出しを隠す */
}

.responsive-component {
  width: 100%;
  height: auto;
  max-width: 100%;
  box-sizing: border-box; /* パディングとボーダーを含めてサイズを計算 */
}
</style>
