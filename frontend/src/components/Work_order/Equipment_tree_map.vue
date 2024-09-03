<template>
  <div ref="treeMap" class="tree-map-container"></div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import * as d3 from 'd3';

const treeMap = ref(null);

// サンプルデータとして設備を準備
const data = {
  name: "root",
  children: [
    { name: "Pump", value: 180 },
    { name: "Valve", value: 120 },
    { name: "Compressor", value: 90 },
    {
      name: "Heat Exchanger", children: [
        { name: "Tube Bundle", value: 50 },
        { name: "Shell", value: 70 },
        { name: "Baffle", value: 30 },
      ]
    },
    { name: "Boiler", value: 100 },
    { name: "Cooling Tower", value: 60 }
  ]
};

onMounted(() => {
  const container = treeMap.value;
  const width = container.clientWidth;
  const height = container.clientHeight;

  const root = d3.hierarchy(data)
    .sum(d => d.value)
    .sort((a, b) => b.value - a.value);

  d3.treemap()
    .size([width, height])
    .padding(1)
    (root);

  // カスタムカラーのスケールを定義
  const color = d3.scaleOrdinal()
    .domain(root.leaves().map(d => d.data.name))
    .range(d3.schemeCategory10);  // ここで使用する色のパレットを指定

  const svg = d3.select(treeMap.value)
    .append("svg")
    .attr("width", "100%")
    .attr("height", "100%")
    .attr("viewBox", `0 0 ${width} ${height}`)
    .attr("preserveAspectRatio", "xMidYMid meet");

  const leaf = svg.selectAll("g")
    .data(root.leaves())
    .enter().append("g")
    .attr("transform", d => `translate(${d.x0},${d.y0})`);

  leaf.append("rect")
    .attr("id", d => d.data.name)
    .attr("width", d => d.x1 - d.x0)
    .attr("height", d => d.y1 - d.y0)
    .attr("fill", d => color(d.data.name));  // カラーを適用

  leaf.append("text")
    .attr("x", 5)
    .attr("y", 20)
    .text(d => `${d.data.name} (${d.data.value}件)`); // 名前と件数を表示
});
</script>

<style>
.tree-map-container {
  width: 100%;
  height: 100%;
  /* 必要に応じて高さを指定する */
}

rect {
  stroke: #fff;
}
</style>
