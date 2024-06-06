<template>
  <div>
    Total Graph (Planned vs Actual)
    <div id="Totalrpc" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import { onMounted, onUnmounted, ref } from 'vue';

export default {
  setup() {
    const userStore = useUserStore();
    const repairingCostData = ref([]);
    const actualCostData = ref([]);
    const plannedCostDataStack = ref([]);
    const actualCostDataStack = ref([]);

    const getRepairingCostData = async () => {
      const companyCode = userStore.companyCode;
      if (!companyCode) {
        console.error('No company code found.');
        return;
      }

      const url = `http://127.0.0.1:8000/api/repairingCost/PPM02ByCompany/?format=json&companyCode=${companyCode}`;
      try {
        const response = await axios.get(url);
        if (response.data[0]?.plannedPM02List) {
          repairingCostData.value = response.data[0].plannedPM02List.filter((plant) => plant.plannedPM02 && plant.plannedPM02.length > 0);
        }
      } catch (error) {
        console.error('Error fetching Repairing Cost data:', error);
      }
    };

    const getActualCostData = async () => {
      const companyCode = userStore.companyCode;
      if (!companyCode) {
        console.error('No company code found.');
        return;
      }

      const url = `http://127.0.0.1:8000/api/calculation/summedActualCostByCompany/?format=json&companyCode=${companyCode}`;
      try {
        const response = await axios.get(url);
        const currentYear = new Date().getFullYear().toString();
        if (response.data.length > 0 && response.data[0].summedActualCostList) {
          actualCostData.value = response.data[0].summedActualCostList.filter((item) => item.year.toString() === currentYear);
        }
      } catch (error) {
        console.error('Error fetching actual cost data:', error);
      }
    };

    const fetchData = async () => {
      const companyCode = userStore.companyCode;
      if (!companyCode) {
        console.error('No company code found.');
        return;
      }

      const currentYear = new Date().getFullYear().toString();
      const plannedURL = `http://127.0.0.1:8000/api/calculation/summedPlannedCostByCompany/?format=json&companyCode=${companyCode}`;
      const actualURL = `http://127.0.0.1:8000/api/calculation/summedActualCostByCompany/?format=json&companyCode=${companyCode}`;

      try {
        const [plannedResponse, actualResponse] = await Promise.all([axios.get(plannedURL), axios.get(actualURL)]);

        plannedCostDataStack.value = plannedResponse.data.flatMap((company) => company.summedPlannedCostList.filter((item) => item.year.toString() === currentYear));

        actualCostDataStack.value = actualResponse.data.flatMap((company) => company.summedActualCostList.filter((item) => item.year.toString() === currentYear));
      } catch (error) {
        console.error('Error fetching cost data:', error);
      }
    };

    const updateGraphSize = () => {
      const graphContainer = document.getElementById('Totalrpc').parentElement;
      graphContainer.style.height = window.innerHeight + 'px';
      const layout = {
        title: 'Total Graph (Planned vs Actual)',
        barmode: 'stack',
        height: graphContainer.offsetHeight,
        width: graphContainer.offsetWidth
      };

      Plotly.newPlot('Totalrpc', [...lineTraces, ...barTraces, ...barTracesStack], layout);
    };

    let lineTraces = [];
    let barTraces = [];
    let barTracesStack = [];

    onMounted(async () => {
      await getRepairingCostData();
      await getActualCostData();
      await fetchData();

      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Commitment', 'TotalCost'];
      lineTraces = repairingCostData.value.map((plant) => {
        const pmData = plant.plannedPM02[0];
        const yValues = months.map((month) => (pmData[`sum${month}`] ? parseFloat(pmData[`sum${month}`]) : 0));
        return {
          x: months,
          y: yValues,
          type: 'scatter',
          mode: 'lines+markers',
          name: plant.plant
        };
      });

      barTraces = actualCostData.value.map((costData) => {
        const xValues = Object.keys(costData).filter((key) => key.startsWith('sum') || key === 'totalActualCost');
        const formattedXValues = xValues.map((key) => key.replace('sum', '').replace('totalActualCost', 'TotalCost'));
        const yValues = xValues.map((key) => parseFloat(costData[key] || 0));

        return {
          x: formattedXValues,
          y: yValues,
          type: 'bar',
          name: costData.plant || 'Total Cost'
        };
      });

      barTracesStack = [];

      plannedCostDataStack.value.forEach((data) => {
        barTracesStack.push({
          x: ['Planned'],
          y: [parseFloat(data.totalPlannedPM02)],
          name: 'Planned PM02',
          type: 'bar'
        });
        barTracesStack.push({
          x: ['Planned'],
          y: [parseFloat(data.totalPlannedPM03)],
          name: 'Planned PM03',
          type: 'bar'
        });
        barTracesStack.push({
          x: ['Planned'],
          y: [parseFloat(data.totalPlannedPM05)],
          name: 'Planned PM05',
          type: 'bar'
        });
      });

      actualCostDataStack.value.forEach((data) => {
        barTracesStack.push({
          x: ['Actual'],
          y: [parseFloat(data.totalActualPM02)],
          name: 'Actual PM02',
          type: 'bar'
        });
        barTracesStack.push({
          x: ['Actual'],
          y: [parseFloat(data.totalActualPM03)],
          name: 'Actual PM03',
          type: 'bar'
        });
        barTracesStack.push({
          x: ['Actual'],
          y: [parseFloat(data.totalActualPM04)],
          name: 'Actual PM04',
          type: 'bar'
        });
        barTracesStack.push({
          x: ['Actual'],
          y: [parseFloat(data.totalActualPM05)],
          name: 'Actual PM05',
          type: 'bar'
        });
      });

      console.log([...lineTraces, ...barTraces, ...barTracesStack]);

      // Call once to set initial size
      updateGraphSize();
      window.addEventListener('resize', updateGraphSize);
    });

    onUnmounted(() => {
      window.removeEventListener('resize', updateGraphSize);
    });

    return {
      repairingCostData,
      actualCostData,
      plannedCostDataStack,
      actualCostDataStack
    };
  }
};
</script>
