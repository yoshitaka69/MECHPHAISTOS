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
                    <li v-for="(value, index) in monthlyBenefit" :key="index" :class="{ negative: value < 0 }">{{ months[index] }}: {{ formatBenefit(value) }}</li>
                </ul>
            </div>
            <div class="benefit" v-if="yearlyBenefit.length > 0">
                <h3>Annual Profit</h3>
                <ul>
                    <li v-for="(value, index) in yearlyBenefit" :key="index" :class="{ negative: value < 0 }">{{ years[index] }}: {{ formatBenefit(value) }}</li>
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

// 11年分のデータを扱うように修正
const thisYear = new Date().getFullYear(); // 現在の年
const years = Array.from({ length: 11 }, (_, i) => thisYear + i); // 11年先までのデータ
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

const monthlyLayout = {
    title: {
        text: 'Monthly Cost Graph',
        font: {
            size: 24,
            weight: 'bold'
        }
    },
    xaxis: {
        title: 'Month',
        tickvals: Array.from({ length: 12 }, (_, i) => i),
        ticktext: months
    },
    yaxis: {
        title: 'Cost',
        rangemode: 'tozero',
        showline: true,
        showgrid: true,
        zeroline: true
    },
    paper_bgcolor: '#fffde7',
    plot_bgcolor: '#ffffff',
    showlegend: true
};

const totalCostLayout = {
    title: {
        text: 'Total Cost Graph',
        font: {
            size: 24,
            weight: 'bold'
        }
    },
    xaxis: {
        title: 'Year',
        tickvals: Array.from({ length: 11 }, (_, i) => thisYear + i), // 11年間
        ticktext: years
    },
    yaxis: {
        title: 'Total Cost',
        rangemode: 'tozero',
        showline: true,
        showgrid: true,
        zeroline: true
    },
    paper_bgcolor: '#fffde7',
    plot_bgcolor: '#ffffff',
    showlegend: true
};

const config = {
    responsive: true,
    displayModeBar: false
};

const monthlyBenefit = ref([]);
const yearlyBenefit = ref([]);

const calculateBenefit = (base, sim) => {
  if (!base || !sim || base.length === 0 || sim.length === 0) {
    console.error('Base or simulation data is invalid:', base, sim);
    return [];
  }

  if (base.length !== sim.length) {
    console.error('Base and simulation data lengths do not match:', base.length, sim.length);
    return [];
  }

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
        console.error('API Error: ', error);
    }
};

const fetchMonthlyData = async () => {
    const userStore = useUserStore();
    const url = `http://127.0.0.1:8000/api/calculation/summedPlannedCostByCompany/?companyCode=${userStore.companyCode}`;
    try {
        const response = await axios.get(url);
        processMonthlyData(response.data);
    } catch (error) {
        console.error('API Error: ', error);
    }
};

const processPPMData = (data) => {
    const ppmData = [];
    data.forEach((item) => {
        item.EventYearPPMList.forEach((event) => {
            const plantName = item.plant;
            for (let i = 0; i < 11; i++) {
                const yearKey = `PPM${i}YearCost`;
                if (event[yearKey] !== undefined) {
                    ppmData.push({
                        x: thisYear + i,
                        y: parseFloat(event[yearKey])
                    });
                }
            }
            totalCostBaseData.value.push({
                x: ppmData.map((d) => d.x),
                y: ppmData.map((d) => d.y),
                type: 'scatter',
                mode: 'lines+markers',
                name: `${plantName} Base Data`
            });
        });
    });
    drawTotalCostChart();
    console.log('Total Cost Base Data:', totalCostBaseData.value);
};

const processMonthlyData = (data) => {
    const monthlyBase = [];
    data.forEach((company) => {
        company.summedPlannedCostList.forEach((record) => {
            const plantName = record.plant;
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
                    name: `${plantName} Base Data`
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
      const { totalCostData: totalCostRawData, monthlyCostData, simulationNumber } = newData;

      if (!monthlyCostData || monthlyCostData.length !== 12 || !totalCostRawData || totalCostRawData.length !== 11) {
        console.error('Received invalid cost data:', newData);
        return;
      }

      yearlyBenefit.value = calculateBenefit(totalCostBaseData.value[0].y, totalCostRawData);
      monthlyBenefit.value = calculateBenefit(monthlyBaseData.value[0].y, monthlyCostData);

      const simName = simulationNumber !== null ? `Simulation ${simulationNumber}` : 'Simulation';
      totalCostData.value.push({
        x: years,
        y: totalCostRawData,
        type: 'scatter',
        mode: 'lines+markers',
        line: { dash: 'dot' },
        name: `Total Cost - ${simName}`
      });
      monthlyData.value.push({
        x: months,
        y: monthlyCostData,
        type: 'scatter',
        mode: 'lines+markers',
        line: { dash: 'dot' },
        name: `Monthly Cost - ${simName}`
      });

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
    background-color: #fffde7;
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
