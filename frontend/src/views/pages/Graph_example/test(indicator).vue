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
		type : "indicator",
		mode : "number+gauge+delta",
		value : 180,
		delta : { reference : 200},
		domain : { x : [0.25, 1], y : [0.08, 0.25]},
		title : { text : "Revenue"},
		gauge : {
			shape : "bullet",
			axis : { range :[ null, 300]},
			threshold : {
				line : { color : "black", width : 2},
				thickness : 0.75,
				value : 170
			},
			steps : [
				{range : [0, 150], color : "gray"},
				{
					range : [150, 250],
					color : "lightgray"
				}
			],
			bar : { color : "black"}
		}
	};

	let data2 = {
		type : "indicator",
		mode : "number+gauge+delta",
		value : 35,
		delta : { reference : 200},
		domain : { x : [0.25, 1], y : [0.4, 0.6]},
		title : { text : "Profit"},
		gauge : {
			shape : "bullet",
			axis : { range :[ null, 100]},
			threshold : {
				line : { color : "black", width : 2},
				thickness : 0.75,
				value : 50
			},
			steps : [
				{ range : [0, 25], color : "gray" },
				{ range : [25, 75], color : "lightgray" }
			],
			bar : { color : "black"}
		}
	};

	let data3 = {
		type : "indicator",
		mode : "number+gauge+delta",
		value : 220,
		delta : { reference : 200},
		domain : { x : [0.25, 1], y : [0.7, 0.9]},
		title : { text : "Satisfaction"},
		gauge : {
			shape : "bullet",
			axis : { range :[ null, 300]},
			threshold : {
				line : { color : "black", width : 2},
				thickness : 0.75,
				value : 210
			},
			steps : [
				{ range : [0, 150], color : "gray" },
				{ range : [150, 250], color : "lightgray" }
			],
			bar : { color : "black"}
		}
	};


    const layout = {
		width : 600, 
		height : 250,
		margin : { t:10, r:25, l:25, b:10}
	};

    Plotly.newPlot('slc', [data1, data2, data3], layout)
  }
}


</script>

