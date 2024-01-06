<template>
	<div>
	  <v-flex>
		<v-card>
		  <div id="r-impact"></div>
		</v-card>
	  </v-flex>
	</div>
  </template>

<script>
import Plotly from "plotly.js-dist-min";

export default {
  mounted() {
    let data = {
		type: 'heatmap',
		z: [[1,null,30,50,1],[20,1,60,80,30],[30,60,1,-10,20]],
		x: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
		y: ['Morning', 'Afternoon', 'Evening'],
		hoverongaps: false,
	};

    Plotly.newPlot('r-impact', [data],)
  }
}

</script>