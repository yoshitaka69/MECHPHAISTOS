<template>
  <div>
    <v-card>
      <v-card-title>Total Graph (Planned vs Actual)</v-card-title>
      <div id="Totalrpc" style="width: 100%; height: 100%"></div>
    </v-card>
  </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import { onMounted, ref } from 'vue';

export default {
    setup() {
        const userStore = useUserStore();
        const plannedCostData = ref([]);
        const actualCostData = ref([]);

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
                const [plannedResponse, actualResponse] = await Promise.all([
                    axios.get(plannedURL),
                    axios.get(actualURL)
                ]);

                plannedCostData.value = plannedResponse.data.flatMap(company =>
                    company.summedPlannedCostList.filter(item => item.year.toString() === currentYear)
                );

                actualCostData.value = actualResponse.data.flatMap(company =>
                    company.summedActualCostList.filter(item => item.year.toString() === currentYear)
                );
            } catch (error) {
                console.error('Error fetching cost data:', error);
            }
        };

        onMounted(async () => {
            await fetchData();
            const barTraces = [];

            plannedCostData.value.forEach(data => {
                barTraces.push({
                    x: ['Planned'],
                    y: [parseFloat(data.totalPlannedPM02)],
                    name: 'Planned PM02',
                    type: 'bar'
                });
                barTraces.push({
                    x: ['Planned'],
                    y: [parseFloat(data.totalPlannedPM03)],
                    name: 'Planned PM03',
                    type: 'bar'
                });
                barTraces.push({
                    x: ['Planned'],
                    y: [parseFloat(data.totalPlannedPM05)],
                    name: 'Planned PM05',
                    type: 'bar'
                });
            });

            actualCostData.value.forEach(data => {
                barTraces.push({
                    x: ['Actual'],
                    y: [parseFloat(data.totalActualPM02)],
                    name: 'Actual PM02',
                    type: 'bar'
                });
                barTraces.push({
                    x: ['Actual'],
                    y: [parseFloat(data.totalActualPM03)],
                    name: 'Actual PM03',
                    type: 'bar'
                });
                barTraces.push({
                    x: ['Actual'],
                    y: [parseFloat(data.totalActualPM04)],
                    name: 'Actual PM04',
                    type: 'bar'
                });
                barTraces.push({
                    x: ['Actual'],
                    y: [parseFloat(data.totalActualPM05)],
                    name: 'Actual PM05',
                    type: 'bar'
                });
            });

            const layout = {
                title: 'Total Graph (Planned vs Actual)',
                barmode: 'stack',
                height: 400,
                width: 900
            };

            Plotly.newPlot('Totalrpc', barTraces, layout);
        });

        return {
            plannedCostData,
            actualCostData
        };
    }
};
</script>
