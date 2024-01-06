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
    let money = {
      x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      y: [10000, 21000, 15000, 35000, 20000, 40000, 33000, 55000, 28000, 12000, 46000, 9000],
      name: '金額',
      hovertext: "",
      hovertemplate: "%{y:.f}円<extra></extra>",
      type: 'scatter',
      mode: 'lines+markers',
      line: {
        color: '#ff1493'
      }
    };

    let times = {
      x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      y: [7, 2, 3, 2, 4, 5, 1, 3, 4, 6, 3, 3],
      name: '回数',
      hovertemplate: "%{y}回",
      type: 'bar',
      yaxis: 'y2',
      width: 0.5,
      marker: {
        color: '#90ee90'
      }
    };

    const layout = {
      hovermode:'closest',
      title: 'Repairing Cost',
      xaxis: {
        tickmode: "linear",
        tick0: 1,
        dtick: 1,
      },
      yaxis: {
        title: '金 額',
        overlaying: 'y2',
        tickformat: ".f"
      },
      yaxis2: {
        title: '回 数',
        side: 'right'
      }
    };

    const config = {
      responsive: true,
      displaylogo: false,
      //displayModeBar: false,
      toImageButtonOptions: {
        format: 'svg',
        filename: 'event_cost',
        scale: 1
      },
      modeBarButtonsToAdd: [
        {
          name: 'Download CSV',
          icon: Plotly.Icons.disk,
          click() {
            alert("Make download process!!")
          }
        }
      ]
    }

    Plotly.newPlot('slc', [money, times], layout, config)

    let slcPlot = document.getElementById('slc')
    slcPlot.on('plotly_hover', function(data){
      console.log("Hover Point X:" + data.points[0].x)
    })
  }
}
</script>