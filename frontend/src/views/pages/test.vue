<template>
    <div id="app" style="display: flex">
        <div style="margin-right: 20px; display: flex; flex-direction: column">
            <label for="backgroundColor">Select Background Color:</label>
            <p-dropdown v-model="backgroundColor" :options="backgroundColorOptions" optionLabel="label" @change="drawChart"></p-dropdown>
        </div>
        <svg ref="svg" :style="{ backgroundColor: backgroundColor, border: '1px solid black' }" width="800" height="800"></svg>
    </div>
</template>

<script>
import * as d3 from 'd3';
import axios from 'axios';
import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/saga-blue/theme.css';
import 'primeicons/primeicons.css';
import Dropdown from 'primevue/dropdown';

export default {
    name: 'HierarchicalEdgeBundling',
    components: {
        'p-dropdown': Dropdown
    },
    data() {
        return {
            backgroundColor: 'white', // デフォルトの背景色
            selectedNode: null, // 現在選択されているノード
            backgroundColorOptions: [
                { label: 'White', value: 'white' },
                { label: 'Light Blue', value: 'lightblue' },
                { label: 'Light Green', value: 'lightgreen' },
                { label: 'Light Yellow', value: 'lightyellow' }
            ],
            chartData: null, // Djangoから取得するデータを保存
            links: [] // グラフ内のリンクを保存
        };
    },
    mounted() {
        this.fetchChartData(); // マウント時にデータを取得してグラフを描画
    },
    methods: {
        fetchChartData() {
            axios
                .get('http://localhost:8000/api/tree-data/') // Djangoからデータを取得
                .then((response) => {
                    this.chartData = response.data; // データを保存
                    console.log('Received data:', this.chartData); // デバッグ用
                    this.drawChart(); // データ取得後にグラフを描画
                })
                .catch((error) => {
                    console.error('Error fetching chart data:', error);
                });
        },
        drawChart() {
            const data = this.chartData;

            if (!data) {
                console.error('No data available for drawing the chart.');
                return;
            }

            const links = [
                { source: 'Leaf G1-1', target: 'Leaf G2-2' },
                { source: 'Leaf G1-2', target: 'Leaf G3-1' },
                { source: 'Leaf G1-3', target: 'Leaf G4-3' },
                { source: 'Leaf G2-1', target: 'Leaf G3-2' },
                { source: 'Leaf G2-3', target: 'Leaf G4-1' },
                { source: 'Leaf G2-4', target: 'Leaf G4-4' },
                { source: 'Leaf G3-1', target: 'Leaf G4-2' },
                { source: 'Leaf G3-2', target: 'Leaf G4-5' }
            ];

            const svg = d3.select(this.$refs.svg);
            svg.selectAll('*').remove(); // 既存の描画をクリア

            const width = +svg.attr('width');
            const height = +svg.attr('height');
            const radius = Math.min(width, height) / 2;

            const g = svg.append('g').attr('transform', `translate(${width / 2},${height / 2})`);

            const cluster = d3.cluster().size([2 * Math.PI, radius - 100]);

            const root = d3.hierarchy(data).sum((d) => d.size);

            cluster(root);

            const line = d3
                .radialLine()
                .curve(d3.curveBundle.beta(0.85))
                .radius((d) => d.y)
                .angle((d) => d.x);

            const link = g
                .selectAll('.link')
                .data(links)
                .enter()
                .append('path')
                .attr('class', 'link')
                .attr('d', (d) => {
                    const source = root.descendants().find((n) => n.data.name === d.source);
                    const target = root.descendants().find((n) => n.data.name === d.target);

                    // source または target が見つからない場合のエラーチェック
                    if (!source || !target) {
                        console.error('Source or target not found for link:', d);
                        return null;
                    }

                    return line(source.path(target));
                })
                .attr('fill', 'none')
                .attr('stroke', '#ccc')
                .attr('stroke-width', 1.5);

            const node = g
                .selectAll('.node')
                .data(root.descendants())
                .enter()
                .append('g')
                .attr('class', 'node')
                .attr(
                    'transform',
                    (d) => `
      rotate(${(d.x * 180) / Math.PI - 90})
      translate(${d.y},0)
    `
                )
                .on('click', (event, d) => {
                    this.selectedNode = this.selectedNode === d ? null : d;
                    this.updateHighlight(links, root);
                });

            node.append('circle').attr('r', 4).attr('fill', '#999');

            node.append('text')
                .attr('dy', '.31em')
                .attr('x', (d) => (d.x < Math.PI === !d.children ? 6 : -6))
                .style('text-anchor', (d) => (d.x < Math.PI === !d.children ? 'start' : 'end'))
                .attr('transform', (d) => (d.x >= Math.PI ? 'rotate(180)' : null))
                .text((d) => d.data.name);

            svg.call(
                d3.zoom().on('zoom', (event) => {
                    g.attr('transform', event.transform);
                })
            );

            this.updateHighlight = (links, root) => {
                const selectedLinks = links.filter((l) => {
                    return this.selectedNode && (l.source === this.selectedNode.data.name || l.target === this.selectedNode.data.name);
                });

                link.attr('stroke', (d) => {
                    const source = root.descendants().find((n) => n.data.name === d.source);
                    const target = root.descendants().find((n) => n.data.name === d.target);
                    const isHighlighted = selectedLinks.some((l) => l.source === source.data.name && l.target === target.data.name);
                    return isHighlighted ? 'red' : '#ccc';
                });

                link.attr('stroke-width', (d) => {
                    const source = root.descendants().find((n) => n.data.name === d.source);
                    const target = root.descendants().find((n) => n.data.name === d.target);
                    const isHighlighted = selectedLinks.some((l) => l.source === source.data.name && l.target === target.data.name);
                    return isHighlighted ? 2.5 : 1.5;
                });

                node.selectAll('circle').attr('fill', (d) => {
                    if (!this.selectedNode) return '#999';
                    const isConnected = selectedLinks.some((l) => l.source === d.data.name || l.target === d.data.name);
                    return isConnected || d === this.selectedNode ? 'red' : '#ccc';
                });

                node.selectAll('text').style('fill', (d) => {
                    if (!this.selectedNode) return '#000';
                    const isConnected = selectedLinks.some((l) => l.source === d.data.name || l.target === d.data.name);
                    return isConnected || d === this.selectedNode ? 'red' : '#ccc';
                });
            };
        }
    }
};
</script>

<style>
.link {
    fill: none;
    stroke: #ccc;
    stroke-width: 1.5px;
}
.node circle {
    fill: #999;
}
.node text {
    font: 12px sans-serif;
}
</style>
