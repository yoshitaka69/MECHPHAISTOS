<template>
	<div>
	  <v-flex>
		<v-card>
		  <v-card-title>Repairing Cost</v-card-title>
		  <div id="parallel"></div>
		</v-card>
	  </v-flex>
	</div>
  </template>


<script>
import Plotly from "plotly.js-dist-min";

export default {
  mounted() {
    let data = {
		type : "parcoords",
		line : {
			color : 'blue'
		},
		dimensions : [{
			range : [1,5],
			constraintrange : [1, 2],
			label : 'A',
			values : [1, 4]
		},{
			range : [1, 5],
			label : 'B',
			values : [3, 1.5],
			tickvals : [1.5, 3, 4.5]
		},{
			range : [1,5],
			label : 'C',
			values : [2,4],
			tickvals : [1, 2,  4, 5],
			ticktext : ['text1','text2','text4','text5']
		},{
			range : [1,5],
			label : 'D',
			values : [4,2],
		}]
	};

    Plotly.newPlot('parallel', [data])
  }
}


</script>

