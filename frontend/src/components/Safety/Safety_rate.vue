<template>
	<div>
	  <v-flex>
		<v-card>
		  <v-card-title>Safety factor</v-card-title>
		  <div id="Rate"></div>
		</v-card>
	  </v-flex>
	</div>
  </template>


<script>
import Plotly from "plotly.js-dist-min";

export default {
  mounted() {
    let data = {
		type : "pie",
		values : [2, 3, 4, 4],
		labels : ["Wages", "Operating expenses", "Cost of sales", "Insurance"],
		textinfo : "label+percent",
		insidetextorientation : "radial"
	};

    const layout = {
		height : 700,
		width : 700
	};

    Plotly.newPlot('Rate', [data], layout)
  }
}


</script>

