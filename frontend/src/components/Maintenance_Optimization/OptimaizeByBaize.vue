<template>
  <div class="optimaize-container">
    <h1 class="title">Summed Planned Cost Optimization</h1>
    <div class="content">
      <div class="indicator-container">
        <Maintenance_Indicator :width="350" :height="350" />
      </div>
      <div class="content-container">
        <div id="OptimaizeByBaize"></div>
      </div>
    </div>
    <form @submit.prevent="optimize" class="optimization-form">
      <div class="form-row">
        <label for="failureProb">Critical Equipment:</label>
        <input id="failureProb" v-model.number="failureProb" type="number" step="0.01" min="0" max="1" required>
      </div>
      <div class="form-row">
        <label for="repairCost">Work Order:</label>
        <input id="repairCost" v-model.number="repairCost" type="number" step="0.01" required>
      </div>
      <div class="form-row">
        <label for="impact">Mainte Task:</label>
        <input id="impact" v-model.number="impact" type="number" step="0.01" required>
      </div>
      <Button label="Run Bayesian Optimization" severity="secondary" raised class="submit-button"/>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import Plotly from 'plotly.js-dist-min';
import { useUserStore } from '@/stores/userStore'; // ストアのパスに応じて適宜変更してください
import { computed, ref, onMounted } from 'vue';
import Maintenance_Indicator from '@/components/Maintenance_Optimization/MaintenanceIndicator.vue';
import Button from 'primevue/button';

export default {
  components: {
    Maintenance_Indicator,
    Button
  },
  setup() {
    const userStore = useUserStore();
    const companyCode = computed(() => userStore.companyCode);
    const year = new Date().getFullYear();
    const graphData = ref(null);
    const optimizedData = ref(null);

    const failureProb = ref(0.1); // 初期値を適当に設定
    const repairCost = ref(1000); // 初期値を適当に設定
    const impact = ref(10); // 初期値を適当に設定

    onMounted(() => {
      fetchData();
    });

    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/calculation/summedPlannedCostByCompany/');
        const data = response.data;
        const companyData = data.find(item => item.companyCode === companyCode.value);
        
        if (companyData && companyData.summedPlannedCostList.length > 0) {
          const costData = companyData.summedPlannedCostList.find(item => item.year === year);
          if (costData) {
            plotGraph(costData, 'Planned vs Optimized Costs');
            graphData.value = costData;
          } else {
            console.error(`No data found for the specified company code and year ${year}.`);
          }
        } else {
          console.error('No data found for the specified company code.');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    const plotGraph = (costData, title, optimizedData = null) => {
      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      const plannedCosts = [
        parseFloat(costData.sumJan),
        parseFloat(costData.sumFeb),
        parseFloat(costData.sumMar),
        parseFloat(costData.sumApr),
        parseFloat(costData.sumMay),
        parseFloat(costData.sumJun),
        parseFloat(costData.sumJul),
        parseFloat(costData.sumAug),
        parseFloat(costData.sumSep),
        parseFloat(costData.sumOct),
        parseFloat(costData.sumNov),
        parseFloat(costData.sumDec),
      ];

      const traces = [
        {
          x: months,
          y: plannedCosts,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Planned Costs',
          marker: { color: 'blue' },
        },
      ];

      if (optimizedData) {
        const optimizedCosts = months.map(month => optimizedData[month]);

        traces.push({
          x: months,
          y: optimizedCosts,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Optimized Costs',
          marker: { color: 'red' },
        });

        // 探索領域を色付け
        const lowerBound = plannedCosts.map(cost => cost * 0.8); // 仮の下限値
        const upperBound = plannedCosts.map(cost => cost * 1.2); // 仮の上限値

        traces.push({
          x: [...months, ...months.reverse()],
          y: [...upperBound, ...lowerBound.reverse()],
          fill: 'toself',
          fillcolor: 'rgba(0, 100, 255, 0.2)',
          line: { color: 'transparent' },
          showlegend: false,
        });
      }

      const layout = {
        title: title,
        xaxis: { title: 'Month' },
        yaxis: { title: 'Cost (in units)' }
      };

      Plotly.newPlot('OptimaizeByBaize', traces, layout);
    };

    const optimize = async () => {
      if (graphData.value) {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/calculation/optimize-repair-cost/', {
            companyCode: companyCode.value,
            year: year,
            failureProb: failureProb.value,
            repairCost: repairCost.value,
            impact: impact.value
          });
          console.log('Optimization result:', response.data);
          optimizedData.value = response.data.optimized_costs;
          plotGraph(graphData.value, 'Planned vs Optimized Costs', optimizedData.value);
        } catch (error) {
          console.error('Error during optimization:', error);
        }
      } else {
        console.error('No data available to optimize.');
      }
    };

    return {
      companyCode,
      year,
      failureProb,
      repairCost,
      impact,
      graphData,
      optimizedData,
      fetchData,
      plotGraph,
      optimize
    };
  }
};
</script>

<style scoped>
.optimaize-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 20px;
}

.title {
  align-self: flex-start;
  margin-bottom: 10px;
}

.optimization-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}

.form-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.submit-button {
  width: auto; /* ボタンの幅を自動に設定 */
  align-self: flex-start; /* ボタンを左揃え */
}

.content {
  display: flex;
  width: 100%;
  gap: 20px;
}

.indicator-container {
  flex: 2; /* 2/5 */
}

.content-container {
  flex: 3; /* 3/5 */
}

#OptimaizeByBaize {
  width: 100%;
  height: 500px;
}
</style>
