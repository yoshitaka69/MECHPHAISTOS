<template>
	<div>
		<v-flex>
			<v-card>
				<v-card-title>Event Cost</v-card-title>
				<div id="slc"></div>
			</v-card>
		</v-flex>
	</div>
</template>
  
<script>
import Plotly from "plotly.js-dist-min";

export default {
	mounted() {
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

		Plotly.newPlot('slc', [trace1, trace2], layout)

	}
}
</script>
