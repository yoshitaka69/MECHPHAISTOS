<template>
  <div class="container">
    <div class="content">
      <h2>Plan Optimization Benefit</h2>
      <div class="content-container">
        <div class="result-display">
          <p>Initial Repair Cost: <span>{{ initialCost }}</span></p>
          <p>Updated Repair Cost: <span>{{ updatedCost }}</span></p>
        </div>
        <div class="result-group">
          <p>Initial Repair Cost: <span>{{ initialCost }}</span></p>
          <p>Updated Repair Cost: <span>{{ updatedCost }}</span></p>
          <p>Benefit: <span>{{ benefit }}</span></p>
        </div>
        <div class="scale-wrapper">
          <RatingScale />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch, onUnmounted } from 'vue';
import RatingScale from '@/components/Benefit/Rating_Scale.vue';

export default {
  name: 'PlanOptimizationBenefit',
  components: {
    RatingScale,
  },
  setup() {
    const initialCost = ref(5000); // サンプルデータ
    const updatedCost = ref(3000); // サンプルデータ

    const benefit = computed(() => {
      return initialCost.value - updatedCost.value;
    });

    onMounted(() => {
      console.log('PlanOptimizationBenefit Component Mounted');
      console.log('Initial Cost:', initialCost.value);
      console.log('Updated Cost:', updatedCost.value);
      console.log('Benefit:', benefit.value);
    });

    onUnmounted(() => {
      console.log('PlanOptimizationBenefit Component Unmounted');
    });

    watch(
      [initialCost, updatedCost],
      ([newInitialCost, newUpdatedCost]) => {
        console.log('Initial Cost changed to:', newInitialCost);
        console.log('Updated Cost changed to:', newUpdatedCost);
        console.log('Benefit changed to:', benefit.value);
      }
    );

    return {
      initialCost,
      updatedCost,
      benefit,
    };
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  background-color: #ffffff;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.content {
  margin: 20px; /* 上下と両側に隙間を追加 */
}

.content h2 {
  margin-bottom: 20px;
  text-align: left;
  font-size: 2em; /* フォントサイズを大きくする */
  padding-left: 10px; /* 左側にスペースを追加 */
}

.content-container {
  display: flex;
  flex-direction: column;
}

.result-display,
.result-group {
  padding: 0 20px; /* 両側にスペースを追加 */
  margin-bottom: 20px;
}

.result-display p,
.result-group p {
  font-size: 1.2em;
  margin: 12px 0;
}

.result-group span,
.result-display span {
  font-weight: bold;
  color: #007bff;
}

.scale-wrapper {
  margin-top: 20px;
  text-align: center;
  overflow-x: hidden; /* 横に溢れないようにする */
}

:deep(.rating-scale) {
  transform: scale(0.8);
  width: 100%; /* 横いっぱいに広げる */
  max-width: 100%;
}
</style>
