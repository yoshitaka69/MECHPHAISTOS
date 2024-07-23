<template>
  <div>
    <div class="graphs-container">
      <div id="MonthlyGraph" class="graph"></div>
      <div id="TotalCostGraph" class="graph"></div>
    </div>
    <div class="benefits-container">
      <div class="benefit" v-if="monthlyBenefit.length > 0">
        <h3>Monthly Profit</h3>
        <ul>
          <li v-for="(value, index) in monthlyBenefit" :key="index" :class="{ negative: value < 0 }">
            {{ months[index] }}: {{ formatBenefit(value) }}
          </li>
        </ul>
      </div>
      <div class="benefit" v-if="yearlyBenefit.length > 0">
        <h3>Annual Profit</h3>
        <ul>
          <li v-for="(value, index) in yearlyBenefit" :key="index" :class="{ negative: value < 0 }">
            {{ years[index] }}: {{ formatBenefit(value) }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

const props = defineProps(['costData']);

const monthlyBaseData = ref([]);
const totalCostBaseData = ref([]);
const monthlyData = ref([]);
const totalCostData = ref([]);

const thisYear = new Date().getFullYear();
const years = Array.from({ length: 10 }, (_, i) => thisYear + i);
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

const monthlyLayout = { 
  title: 'Monthly Cost Graph',
  xaxis: { title: 'Month', tickvals: Array.from({ length: 12 }, (_, i) => i), ticktext: months },
  yaxis: { rangemode: 'tozero' }
};
const totalCostLayout = { 
  title: 'Total Cost Graph',
  xaxis: { title: 'Year', tickvals: Array.from({ length: 10 }, (_, i) => thisYear + i), ticktext: years },
  yaxis: { rangemode: 'tozero' }
};
const config = { responsive: true };

const monthlyBenefit = ref([]);
const yearlyBenefit = ref([]);

const calculateBenefit = (base, sim) => {
  return base.map((value, index) => sim[index] - value);
};

const formatBenefit = (value) => {
  return value < 0 ? `-${Math.abs(value)}` : value.toString();
};

const fetchPPMData = async () => {
  const userStore = useUserStore();
  const url = `http://127.0.0.1:8000/api/junctionTable/eventYearPPMByCompany/?format=json&companyCode=${userStore.companyCode}`;
  try {
    const response = await axios.get(url);
    processPPMData(response.data);
  } catch (error) {
    console.error("API Error: ", error);
  }
};

const fetchMonthlyData = async () => {
  const userStore = useUserStore();
  const url = `http://127.0.0.1:8000/api/calculation/summedPlannedCostByCompany/?companyCode=${userStore.companyCode}`;
  try {
    const response = await axios.get(url);
    processMonthlyData(response.data);
  } catch (error) {
    console.error("API Error: ", error);
  }
};

const processPPMData = (data) => {
  const ppmData = [];
  data.forEach(item => {
    item.EventYearPPMList.forEach(event => {
      for (let i = 0; i < 10; i++) {
        const yearKey = `PPM${i}YearCost`;
        if (event[yearKey] !== undefined) {
          ppmData.push({
            x: thisYear + i,
            y: parseFloat(event[yearKey])
          });
        }
      }
    });
  });
  totalCostBaseData.value = [
    { x: ppmData.map(d => d.x), y: ppmData.map(d => d.y), type: 'scatter', mode: 'lines+markers', name: 'Base Data' }
  ];
  drawTotalCostChart();
  console.log('Total Cost Base Data:', totalCostBaseData.value);
};

const processMonthlyData = (data) => {
  const monthlyBase = [];
  data.forEach(company => {
    company.summedPlannedCostList.forEach(record => {
      if (record.year === thisYear) {
        monthlyBase.push({
          x: months,
          y: [
            parseFloat(record.sumJan),
            parseFloat(record.sumFeb),
            parseFloat(record.sumMar),
            parseFloat(record.sumApr),
            parseFloat(record.sumMay),
            parseFloat(record.sumJun),
            parseFloat(record.sumJul),
            parseFloat(record.sumAug),
            parseFloat(record.sumSep),
            parseFloat(record.sumOct),
            parseFloat(record.sumNov),
            parseFloat(record.sumDec)
          ],
          type: 'scatter',
          mode: 'lines+markers',
          name: record.plant
        });
      }
    });
  });
  monthlyBaseData.value = monthlyBase;
  drawMonthlyChart();
  console.log('Monthly Base Data:', monthlyBaseData.value);
};

const drawTotalCostChart = () => {
  Plotly.newPlot('TotalCostGraph', [...totalCostBaseData.value, ...totalCostData.value], totalCostLayout, config);
};

const drawMonthlyChart = () => {
  Plotly.newPlot('MonthlyGraph', [...monthlyBaseData.value, ...monthlyData.value], monthlyLayout, config);
};

onMounted(() => {
  fetchPPMData();
  fetchMonthlyData();
});

watch(
  () => props.costData,
  (newData) => {
    if (newData) {
      const { totalCostData: totalCostRawData, monthlyCostData } = newData;
      
      yearlyBenefit.value = calculateBenefit(totalCostBaseData.value[0].y, totalCostRawData[0]);
      monthlyBenefit.value = calculateBenefit(monthlyBaseData.value[0].y, monthlyCostData[0]);

      totalCostData.value = [
        { x: years, y: totalCostRawData[0], type: 'scatter', mode: 'lines+markers', line: { dash: 'dot' }, name: 'Total Cost' }
      ];
      monthlyData.value = [
        { x: months, y: monthlyCostData[0], type: 'scatter', mode: 'lines+markers', line: { dash: 'dot' }, name: 'Monthly Cost' }
      ];

      console.log('Monthly Data:', monthlyData.value);
      console.log('Total Cost Data:', totalCostData.value);

      drawTotalCostChart();
      drawMonthlyChart();
    }
  },
  { immediate: true }
);
</script>

<style>
.graphs-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}
.graph {
  width: 48%;
}
.benefits-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
.benefit {
  width: 48%;
}
.negative {
  color: red;
}
</style>
