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

	let rawData = [
		{Critical_Equipment: 50, Repairing_Cost: 50, Maintenance_Task: 50, label: 'point 1'},
    ];

	let data = {
		type: 'scatterternary',
		mode: 'markers',
		a: rawData.map(function(d){ return d.Critical_Equipment;}),
		b: rawData.map(function(d){ return d.Repairing_Cost;}),
		c: rawData.map(function(d){ return d.Maintenance_Task;}),
		text: rawData.map(function(d){ return d.label;}),
		marker: {
			symbol: 100,
			color: '#DB7365',
			size: 14,
			line: { width: 2}
		},
	};

	let ternary = {
		sum: 100,
		aaxis: this.makeAxis('Critical Equipment',0),
		baxis: this.makeAxis('<br>Repairing Cost',45),
		caxis: this.makeAxis('<br>Maintenance Task',-45),
		bgcolor: '#fff1e0'
	};

	let annotations = {
		showarrow: false,
		text:'test',
		x: 1.0,
		y: 1.3,
		font: { size: 15},
		paper_bgcolor: '#fff1e0'
	};
    Plotly.newPlot('slc', [data], {ternary, annotations})
  },

  methods:{
	makeAxis(title,tickangle){
		return {
			title:title,
			titlefont: { size:20 } ,
			tickangle: tickangle,
			tickfont: { size:15 },
			tickcolor: 'rgba(0,0,0,0)',
			ticklen: 5,
			showline: true,
			showgrid: true,
		};
	}
  }
};

</script>