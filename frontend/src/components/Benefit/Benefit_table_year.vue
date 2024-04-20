<template>
	<div>
	  <v-flex>
		<v-card>
		  <v-card-title></v-card-title>
		  <div id="table"></div>
		</v-card>
	  </v-flex>
	</div>
  </template>


<script>
import Plotly from "plotly.js-dist-min";

export default {

	mounted() {
		let values = [['Salaries','Office','Merchandise','Legal','<b>Total</b>'],
					  ["test1","test2","test3","test4","test5"],
					  ["test1","test2","test3","test4","test5"],
					  ["test1","test2","test3","test4","test5"],
					  ["test1","test2","test3","test4","test5"],
					];

		let headerColor = "grey";
		let rowEventColor = "lightgrey";
		let rowOddColor = "white";

		let data = {
			type: 'table',
			header: {
				values:[["<b>EXPENSES</b>"],
						["<b>Q1</b>"],
						["<b>Q2</b>"],
						["<b>Q3</b>"],
						["<b>Q4</b>"],
					],
					align: "center",
					line: {width: 1, color: "black"},
					fill: {color: headerColor},
					font: {family: "Arial", size: 12, color: "white"}
			},
			cells: {
				values: values,
				align: "center",
				line: {color: 'black', width: 1},
				fill: {color: [rowOddColor, rowEventColor, rowOddColor, rowEventColor, rowOddColor]},
				font: {family: "Arial", size: 11, color: ["black"]}
			}
		};

		Plotly.newPlot('table', [data],)

	}
}


</script>

