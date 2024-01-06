<template>
	<div>
	  <v-flex>
		<v-card>
		  <v-card-title></v-card-title>
		  <div id="slc"></div>
		</v-card>
	  </v-flex>
	</div>
  </template>


<script>
import Plotly from "plotly.js-dist-min";

export default {

	mounted() {
		let values = [['Salaries','Office','Merchandise','Legal','<b>Total<br>EXPENSES</b>'],["test1","test2","test3","test4","test5"]];

		let data = {
			type: 'table',
			columnorder: [1,2],
			columwidth: [80,400],
			header: {
				values:[["<b>EXPENSES</b><br>as of July 2017"],["<b>DESCRIPTION</b>"]],
					align: ["left", "center"],
					height: 40,
				line: {width: 1, color: "#506784"},
				fill: {color: '#119DFF'},
				font: {family: "Arial", size: 12, color: "white"}
			},
			cells: {
				values: values,
				align: ["left","center"],
					height: 30,
				line: {color: '#506784', width: 1},
					fill: {color: ["#25FEFD", 'white']},
				font: {family: "Arial", size: 11, color: ["#506784"]}
			}
		};

		Plotly.newPlot('slc', [data],)

	}
}


</script>

