<template>
    <div>
        <v-card>
            <v-card-title>Trend of Safety Indicators</v-card-title>
            <v-container>
                <v-row>
                    <v-col>
                        <div id="safetyDiv" style="height: 600px; width: 600px"></div>
                    </v-col>
                </v-row>
            </v-container>
        </v-card>
    </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';

export default {
    setup() {
        const userStore = useUserStore();
        const companyCode = userStore.companyCode;
        const data = ref([]);

        const safetyLevels = {
            'Very High': 5,
            'High': 4,
            'Middle': 3,
            'Low': 2,
            'Very Low': 1
        };

        onMounted(async () => {
    if (!companyCode) {
        console.error('No company code found.');
        return;
    }

    const url = `http://127.0.0.1:8000/api/nearMiss/trendSafetyIndicatorsByCompany/?format=json&companyCode=${companyCode}`;
    try {
        const response = await axios.get(url);
        console.log("Complete API Response:", response.data);  // Display full API response for debugging
        if (response.data && response.data.length > 0) {
            const companyData = response.data.find(item => item.companyCode === companyCode);
            if (companyData && companyData.trendSafetyIndicatorsList) {
                console.log("Filtered Trend Safety Indicators List:", companyData.trendSafetyIndicatorsList);
                data.value = companyData.trendSafetyIndicatorsList.map(item => {
                    const formattedDate = new Date(item.lastUpdateDay).toISOString().slice(0, 10); // Ensure the date is in ISO format
                    console.log("Formatted Date:", formattedDate); // Log the formatted date for debugging
                    return {
                        x: formattedDate,
                        y: safetyLevels[item.safetyIndicators] || null, // Fallback if mapping fails
                        type: 'scatter',
                        mode: 'lines+markers',
                        name: item.safetyIndicators
                    };
                });
                console.log("Prepared Data for Chart:", JSON.stringify(data.value, null, 2));  // Use JSON.stringify for better readability in logs

                generateChart(data.value);
            } else {
                console.log("No Trend Safety Indicators data found for this company");
            }
        }
    } catch (error) {
        console.error('Error fetching safety indicators data:', error);
    }
});

function generateChart(chartData) {
    const layout = {
        height: 600,
        width: 600,
        title: 'Trend of Safety Indicators',
        xaxis: {
            title: 'Date',
            type: 'date', // Ensure the x-axis is treated as dates
            range: ['2019-01-01', '2029-12-31'], // Adjust the range if necessary
            tickformat: '%Y-%m-%d' // Change to show full date for clarity
        },
        yaxis: {
            title: 'Safety Level',
            showgrid: true,
            showline: true, // Show lines for visibility
            tickmode: 'array',
            tickvals: [1, 2, 3, 4, 5],
            ticktext: ['Very Low', 'Low', 'Middle', 'High', 'Very High']
        }
    };
    Plotly.newPlot('safetyDiv', chartData, layout);
}


        return { data };
    }
};
</script>
