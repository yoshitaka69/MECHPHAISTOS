<template>
  <div class="container">
    <div class="header">
      <h2>RiskAvoidanceBenefit</h2>
    </div>
    <div class="content">
      <div class="input-group">
        <label for="risk-avoidance-rate">リスク回避率: </label>
        <input id="risk-avoidance-rate" v-model="riskAvoidanceRate" type="text" />
      </div>
      <div class="input-group">
        <label for="cost-benefit">コストベネフィット: </label>
        <input id="cost-benefit" v-model="costBenefit" type="text" />
      </div>
      <div class="result-group">
        <p>リスク回避率: <span>{{ riskAvoidanceRate }}</span></p>
        <p>コストベネフィット: <span>{{ costBenefit }}</span></p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'RiskAvoidanceBenefit',
  setup() {
    const riskAvoidanceRate = ref('75%'); // サンプルデータ
    const costBenefit = ref('¥1,000,000'); // サンプルデータ

    return {
      riskAvoidanceRate,
      costBenefit
    };
  }
}
</script>

<style scoped>
.container {
  width: 100%;
  height: 100%;
  background-color: #f0f4f8;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.header {
  margin-bottom: 20px;
  text-align: center;
}

.header h2 {
  font-size: 1.8em;
  color: #333;
}

.input-group {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  align-items: start;
}

.input-group label {
  font-weight: bold;
  margin-bottom: 5px;
  color: #555;
}

.input-group input {
  width: 100%;
  max-width: 400px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-sizing: border-box;
  transition: border-color 0.3s;
}

.input-group input:focus {
  border-color: #007bff;
  outline: none;
}

.result-group p {
  font-size: 1.2em;
  margin: 10px 0;
  color: #333;
}

.result-group span {
  font-weight: bold;
  color: #007bff;
}

@media (min-width: 768px) {
  .input-group {
    flex-direction: row;
    align-items: center;
  }

  .input-group label {
    margin-right: 10px;
  }
}
</style>
