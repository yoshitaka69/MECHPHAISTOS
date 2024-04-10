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
    let data = {
		type : "parcats",
		dimensions : [
			{label : 'Hair',
			values : ['Black', 'Brown', 'Brown', 'Brown', 'Red'] 
			},
			{label : 'Eyes',
			values : ['Brown', 'Brown', 'Brown', 'Blue', 'Blue']
			},
			{label : 'sex',
			values : ['Female', 'Male', 'Female', 'Male', 'Male']}
		],
		counts : [6, 10, 40, 23, 7]
		};


    const layout = {
		width : 600, 
	};

    Plotly.newPlot('slc', [data], layout)
  }
}


</script>