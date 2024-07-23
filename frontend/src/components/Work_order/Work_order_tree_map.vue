<template>
  <div ref="treeMap"></div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import * as d3 from 'd3';

const treeMap = ref(null);

const data = {
  name: "root",
  children: [
    { name: "A", value: 100 },
    { name: "B", value: 300 },
    { name: "C", value: 200 },
    {
      name: "D", children: [
        { name: "D1", value: 50 },
        { name: "D2", value: 100 },
        { name: "D3", value: 150 },
      ]
    }
  ]
};

onMounted(() => {
  const width = 800;
  const height = 400;

  const root = d3.hierarchy(data)
    .sum(d => d.value)
    .sort((a, b) => b.value - a.value);

  d3.treemap()
    .size([width, height])
    .padding(1)
    (root);

  const svg = d3.select(treeMap.value)
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  const leaf = svg.selectAll("g")
    .data(root.leaves())
    .enter().append("g")
    .attr("transform", d => `translate(${d.x0},${d.y0})`);

  leaf.append("rect")
    .attr("id", d => d.data.name)
    .attr("width", d => d.x1 - d.x0)
    .attr("height", d => d.y1 - d.y0)
    .attr("fill", d => d3.scaleOrdinal(d3.schemeCategory10)(d.data.name));

  leaf.append("text")
    .attr("x", 5)
    .attr("y", 20)
    .text(d => d.data.name);
});
</script>

<style>
rect {
  stroke: #fff;
}
</style>
