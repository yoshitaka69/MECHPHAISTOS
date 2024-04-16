<template>
    <div>
        <v-card>
            Demand trend Map
            <div id="TRmap" style="width: 100%; height: 100%"></div>
        </v-card>
    </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';

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

        const layout = {
            mapbox: { style: 'light', center: { lat: 20 } },
            width: 800,
            height: 600,
            margin: {
                l: 50, // 左側のマージン
                r: 50, // 右側のマージン
                b: 50, // 下側のマージン
                t: 50, // 上側のマージン
                pad: 4 // グラフ領域と軸の周りの余白
            }
        };
        const config = {
            mapboxAccessToken: 'pk.eyJ1IjoieW9zaGl0YWthNjkiLCJhIjoiY2xyd2hjNmFoMDNwajJrbnU5NWV4ODh2ZiJ9.4QE8gwFBapcj7kO3_gtkNw'
        };

        Plotly.newPlot('TRmap', [map], layout, config);
    }
};
</script>
