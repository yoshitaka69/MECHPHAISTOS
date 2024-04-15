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
        const repairingCostData = ref([]);
        const actualCostData = ref([]);

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

            const url = `http://127.0.0.1:8000/api/calculation/summedByCompany/?format=json&companyCode=${companyCode}`;
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

        onMounted(async () => {
            await getRepairingCostData();
            await getActualCostData();
            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Commitment', 'TotalCost'];
            const lineTraces = repairingCostData.value.map((plant) => {
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

            const barTraces = actualCostData.value.map((costData) => {
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


            


            const layout = {
                title: 'Total Graph (Planned vs Actual)',
                barmode: 'stack',
                height: 400,
                width: 900
            };

            Plotly.newPlot('Totalrpc', [...lineTraces, ...barTraces], layout);
        });

        return {
            repairingCostData,
            actualCostData
        };
    }
};
</script>
