<template>
	<div>
	  <v-flex>
		<v-card>
		  <v-card-title>Repairing Cost</v-card-title>
		  <div id="slc"></div>
		</v-card>
	  </v-flex>
	</div>
  </template>


<script>
import Plotly from "plotly.js-dist-min";

export default {
  mounted() {
    let data1 = {
		type : "scatterpolar",
		r : [39, 28, 8, 7, 28, 39],
		theta : ['A', 'B', 'C', 'D', 'E', 'A'],
		fill : 'toself',
		name : 'Group A',
	};

	let data2 = {
		type : "scatterpolar",
		r : [1.5, 10, 39, 31, 15, 1.5],
		theta : ['A', 'B', 'C', 'D', 'E', 'A'],
		fill : 'toself',
		name : 'Group B',
	};

    const layout = {
		polor : {
			radialaxis : {
				visible : true,
				range : [0, 50]
			}
		}
	};

    Plotly.newPlot('slc', [data1, data2], layout)
  }
}


</script>

