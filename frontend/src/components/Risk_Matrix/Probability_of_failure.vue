<template>
	<div>
		<div id="LvDescriptionFailure" style="width: 800px;"></div>
	</div>
</template>

<script>
import Plotly from "plotly.js-dist-min";

export default {

	mounted() {
		let values = [['・No failures have occurred in the past 5 years.・Equipment operating rate is low, and the possibility of failure occurring in the future is low.'],
		["・Failures have occurred less than twice in the past five years.・Preventive maintenance has been performed in the past five years.・Countermeasures for past problems have been implemented through RCA, etc., and are showing sufficient effectiveness.Managed by preventive maintenance tasks, with regular maintenance observations and actions taken."],
		["・Failures have occurred 2 or more times but less than 3 times in the past 5 years.・It is managed by preventive maintenance tasks, and early abnormalities can be detected.・Countermeasures for past problems have been implemented through RCA, etc., and are showing sufficient effectiveness.・PM has not been implemented for a long time."],
		["・Failures have occurred 2 or more times but less than 3 times in the past 5 years.Although managed by preventive maintenance tasks, a certain number of failures occur.Countermeasures for past problems caused by RCA, etc. have not been implemented, or their effects have not been sufficiently effective.・The cause of the trouble is clear and its occurrence can be predicted."],
		["- Failures have occurred three or more times during repairs over the past five years.Not managed by preventive maintenance tasks, and initial abnormalities are not noticed.Countermeasures for past problems have not been implemented or their effects have not been sufficiently effective.The cause of the problem is not clear."],
		];

		let rowEventColor = "lightgrey";
		let rowOddColor = "white";

		let data = {
			type: 'table',
			columnwidth: [400, 400, 400, 400, 400],
			header: {
				values: [["<b>1 - Extremely rare</b>"],
				["<b>2 - Rare</b>"],
				["<b>3 - Occasionally</b>"],
				["<b>4 - Often</b>"],
				["<b>5 - Frequently</b>"],
				],
				align: "center",
				line: { width: 1, color: "black" },
				fill: {
					color: ["#00B050", "#92D050", "#FFFF00", "#FFC000", "#FF0000"], // 色の指定
				},
				font: { family: "Arial", size: 12, color: "black" }
			},
			cells: {
				values: values,
				align: ["center"],
				fill: { color: [rowOddColor, rowEventColor, rowOddColor, rowEventColor, rowOddColor] },
				font: { family: "Arial", size: 12, color: ["black"] }
			}
		};

		const layout = {
			title: "Definition of probability of failure",
			height: 500,
			width: 780,
			margin: { t: 40, r: 10, b: 0, l: 10 },
			displayModeBar: false,
			displaylogo: false
		}

		const config = { responsive: true }

		Plotly.newPlot('LvDescriptionFailure', [data], layout, config,)

	}
}


</script>

