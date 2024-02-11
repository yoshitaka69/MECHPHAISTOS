<template>
	<div>
		<v-flex>
			<v-card>
				<v-card-title></v-card-title>
				<div id="TRmap"></div>
			</v-card>
		</v-flex>
	</div>
</template>
  
<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";

export default {
	mounted() {
		let map = {
			type: 'scattermapbox',
			mode: 'markers',
			locations: ['FRA', 'DEU', 'RUS', 'ESP'],
			marker: {
				size: [20, 30, 15, 10],
				color: [10, 20, 40, 50],
				cmin: 0,
				cmax: 50,
				colorscale: 'Greens',
				colorbar: {
					title: 'Some rate',
					ticksuffix: '%',
					showticksuffix: 'last'
				},
				line: {
					color: 'black'
				}
			},
			name: 'europe data'
		};



		const layout = { mapbox: { style: 'light', center: { lat: 20 } }, width: 600, height: 500 };
		const config = {
			mapboxAccessToken: "pk.eyJ1IjoieW9zaGl0YWthNjkiLCJhIjoiY2xyd2hjNmFoMDNwajJrbnU5NWV4ODh2ZiJ9.4QE8gwFBapcj7kO3_gtkNw"
		};


		Plotly.newPlot('TRmap', [map], layout,config)
	}
}

</script>