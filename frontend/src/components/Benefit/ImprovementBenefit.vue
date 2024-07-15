<template>
  <div class="container">
    <div class="header">
      <h2>ImprovementBenefit</h2>
    </div>
    <div class="content">
      <div class="input-group">
        <label for="investment-benefit">Investment Benefit: </label>
        <input id="investment-benefit" v-model="investmentBenefit" type="text" />
      </div>
      <div class="input-group">
        <label for="improvement-benefit">Improvement Benefit: </label>
        <input id="improvement-benefit" v-model="improvementBenefit" type="text" />
      </div>
      <div class="result-group">
        <p>Investment Benefit: <span>{{ investmentBenefit }}</span></p>
        <p>Improvement Benefit: <span>{{ improvementBenefit }}</span></p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'ImprovementBenefit',
  setup() {
    const investmentBenefit = ref('Sample Investment Benefit');
    const improvementBenefit = ref('Sample Improvement Benefit');

    return {
      investmentBenefit,
      improvementBenefit
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
