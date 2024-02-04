<template>
	<div>
		<v-flex>
			<v-card>
				<v-card-title>Location</v-card-title>
				<div id="RC"></div>
			</v-card>
		</v-flex>
	</div>
</template>
  
<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";

export default {
	data() {
		return {
			plannedData: null,
			actualData: null,
		};
	},

	mounted() {
		// Initialize data variables
		let data1, data2;

		// Fetch planned data
		axios.get("http://localhost:3000/PlannedPM02")
			.then(response => {
				this.plannedData = response.data;

				const plannedPlantCosts = Object.keys(this.plannedData).map(plant => {
					return parseInt(this.plannedData[plant].cost[this.plannedData[plant].cost.length - 1]);
				});

				data1 = {
					type: "scatterpolar",
					r: plannedPlantCosts,
					theta: Object.keys(this.plannedData),
					fill: 'toself',
					name: 'Planned',
				};

				// Fetch actual data
				return axios.get("http://localhost:3000/ActualPM03");
			})
			.then(response => {
				this.actualData = response.data;

				const actualPlantCosts = Object.keys(this.actualData).map(plant => {
					return parseInt(this.actualData[plant].cost[this.actualData[plant].cost.length - 1]);
				});

				data2 = {
					type: "scatterpolar",
					r: actualPlantCosts,
					theta: Object.keys(this.actualData),
					fill: 'toself',
					name: 'Actual',
				};

				// Compute max range
				const maxRange = Math.max(...[...data1.r, ...data2.r]) + 10;

				const layout = {
					polar: {
						radialaxis: {
							visible: true,
							range: [0, maxRange],
						},
					},
				};

				// Render the plot with both traces
				Plotly.newPlot('RC', [data1, data2], layout);
			})
			.catch(error => {
				console.error("Error fetching data:", error);
			});
	},
};
</script>
