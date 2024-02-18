<template>
	<div>
		  <div id="LvDescription" style="width: 800px; margin-left: auto;"></div>
	</div>
</template>

<script>
import Plotly from "plotly.js-dist-min";

export default {

	mounted() {
		let values = [['<b>A</b>','<b>B</b>','<b>C</b>','<b>D</b>','<b>E</b>'],
					  ["Death","Visceral disorder, Lv3 Burn, Amputation","Eye injury, Lv2 Burn, fracture","First aid that does not interfere with work, Lv1 Burn","Minor scratches not applicable"],
					  ["Explosion, Destruction of critical assets","Limited destruction or fire that takes more than a week to repair","Minor damage within 1 week to repair","Minor damage that can be repaired within 1 day","Minor damage not applicable to the above"],
					  ["Massive irreversible damage","1 year of ecological damage","Short-term effects around the leak location","There is no effect on biological systems, but coloring and odor are generated.","Minor environmental damage that does not fall under the above categories"],
					  ["International media coverage","Local media coverage","No media coverage. However, it is necessary to report to the government agency.","No media coverage. However, there is no need to report to government agencies.","Not applicable to the above"],
					  ["Something needs to be done urgently","Some kind of soft or hard response is required within a few days.","In addition to considering hard measures.","Consider measures such as reviewing methods and rules (soft).","No measures needed"],
					];

		let headerColor = "grey";
		let rowEventColor = "lightgrey";
		let rowOddColor = "white";


		let data = {
			type: 'table',
			columnwidth: [150,400,400,400,400,400],
			header: {
				values:[["<b>Level</b>"],
						["<b>Injured Lv</b>"],
						["<b>Equipment Damage Lv</b>"],
						["<b>Affect Of Enviroment</b>"],
						["<b>NewsCoverage</b>"],
						["<b>Measures</b>"],
					],
					align: "center",
					line: {width: 1, color: "black"},
					fill: {color: headerColor},
					font: {family: "Arial", size: 12, color: "white"}
			},
			cells: {
				values: values,
				align: ["center","left"],
				fill: {color: [rowOddColor, rowEventColor, rowOddColor, rowEventColor, rowOddColor,rowEventColor,]},
				font: {family: "Arial", size: 12, color: ["black"]}
			}
		};

		const layout = {
			height: 550,
            width: 780,
			margin: { t: 40, r: 0, b: 0, l: 10 },
			displayModeBar: false,
			displaylogo: false
		}

		const config = { responsive: true }

		Plotly.newPlot('LvDescription', [data],layout,config,)

	}
}


</script>

