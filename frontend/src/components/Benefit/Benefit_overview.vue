<template>
	<div>
	  <v-flex>
		<v-card>
		  <v-card-title>Benefit Overview</v-card-title>
		  <div id="overview"></div>
		</v-card>
	  </v-flex>
	</div>
  </template>


<script>
import Plotly from "plotly.js-dist-min";

export default {
  mounted() {
    let data = {
		name : "2018",
		type : "waterfall",
		orientation : "v",
		measure : [
			"relative",
			"relative",
			"total",
			"relative",
			"relative",
			"total"
		],

		x : [
			"Sales",
			"Consulting",
			"Net revenue",
			"Purchases",
			"Other expenses",
			"Profit before tax",
		],
		textposition : "outside",
		text : [
			"+60",
			"+80",
			"",
			"-40",
			"-20",
			"Total"
		],

		y:[
			60,
			80,
			0,
			-40,
			-20,
			0
		],
		connector : {
			line : {
				color : "rgb(63, 63, 63)"
			}
		},

	};

    const layout = {
		title : {
			text : "Profit and loss statement 2018"
		},

		xaxis : {
			type : "category"
		},

		yaxis : {
			type : "liner"
		},
		autosize : true,
		showlegend : true
    };

    Plotly.newPlot('overview', [data], layout)
  }
}


</script>

