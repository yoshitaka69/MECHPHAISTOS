<template>
	<div>
		<v-flex>
			<v-card>
				<v-card-title>Safety Measure trend</v-card-title>
				<div id="smt"></div>
			</v-card>
		</v-flex>
	</div>
</template>
  
<script>
import Plotly from "plotly.js-dist-min";

export default {
	data(){
		return {
			x:{},
			y:{},
		};
	},


	mounted() {
        axios.get("http://localhost:3000/NearMiss")
    .then(response => {
        const measureArray = response.data.map(item => item['Measure']);

        this.values = measureArray.reduce((accumulator, measure) => {
            accumulator[measure] = (accumulator[measure] || 0) + 1;
            return accumulator;
        }, {});


		let trace1 = {
			x: ['giraffes', 'orangutans', 'monkeys'],
			y: [20, 14, 23],
			name: 'SF Zoo',
			type: 'bar'
		};

		let trace2 = {
			x: ['giraffes', 'orangutans', 'monkeys'],
			y: [12, 18, 29],
			name: 'LA Zoo',
			type: 'bar'
		};

		const layout = { barmode: 'stack' };

		Plotly.newPlot('smt', [trace1, trace2], layout)

	}
}
</script>