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
  
  export default {
    mounted() {
      let map = {
        type: 'scattergeo',
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
  
  
  
      const layout = {
        'geo': {
          'scope': 'europe',
          'resolution': 50
        }
      };
  
  
      Plotly.newPlot('TRmap', [map], layout)
    }
  }
  
  </script>