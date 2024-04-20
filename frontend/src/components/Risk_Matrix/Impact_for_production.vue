<template>
	<div>
		  <div id="LvDescriptionImpact" style="width: 800px;"></div>
	</div>
</template>

<script>
import Plotly from "plotly.js-dist-min";

export default {

	mounted() {
		let values = [['・Recovery possible by operator・Replacement device or easy recovery possible・Equipment is divided into two lines, making recovery easy.Spare parts are on hand and restoration is easily possible with WI'],
					  ["・Recovery within 1 day・Recovery by operator is not possible・Restoration by knowledgeable and professional contractors.Spare parts and replacement machines available・Parts delivery time for restoration is within 3 days"],
					  ["・Recovery within 1 to 3 days・Recovery by operator is not possible・Restoration by knowledgeable and professional contractors.No spare parts or replacement equipment available・The parts delivery time required for restoration is between 1 and 3 days."],
					  ["・Recovery within 3 to 14 days・Manufacturing by changing manufacturing conditions such as single-lung operation・Irregular operations by operators occur after provisional recovery・Special parts are required and the parts delivery time is 3 days or more."],
					  ["・Due to severe equipment damage, recovery with replacement equipment is not possible.・Individual response is required after coordinating with each department"],
					];

		let headerColor = "grey";
		let rowEventColor = "lightgrey";
		let rowOddColor = "white";


		let data = {
			type: 'table',
			columnwidth: [400,400,400,400,400],
			header: {
				values:[["<b>1 - Operator recovery possible</b>"],
						["<b>2 - Spare parts and replacement machines are available, allowing for quick recovery.</b>"],
						["<b>3 - Recovery that requires specialized contractors and involves irregularities</b>"],
						["<b>4 - Temporary recovery in situations where production schedule or quality is affected</b>"],
						["<b>5 - Recovery not possible</b>"],
					],
					align: "center",
					line: {width: 1, color: "black"},
					fill: {color: headerColor},
					font: {family: "Arial", size: 12, color: "white"}
			},
			cells: {
				values: values,
				align: ["center"],
				fill: {color: [rowOddColor, rowEventColor, rowOddColor, rowEventColor, rowOddColor]},
				font: {family: "Arial", size: 12, color: ["black"]}
			}
		};

		const layout = {
      title:"Definition of impact for production",
			height: 500,
            width: 780,
			margin: { t: 40, r: 10, b: 0, l: 10 },
			displayModeBar: false,
			displaylogo: false
		}

		const config = { responsive: true }

		Plotly.newPlot('LvDescriptionImpact', [data],layout,config,)

	}
}


</script>