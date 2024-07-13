<template>
  <div id="app">
    <div>
      <label for="backgroundColor">Select Background Color:</label>
      <select v-model="backgroundColor" @change="drawChart">
        <option value="white">White</option>
        <option value="lightblue">Light Blue</option>
        <option value="lightgreen">Light Green</option>
        <option value="lightyellow">Light Yellow</option>
      </select>
    </div>
    <svg ref="svg" :style="{ backgroundColor: backgroundColor }" width="800" height="800"></svg>
  </div>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'HierarchicalEdgeBundling',
  data() {
    return {
      backgroundColor: 'white', // デフォルトの背景色
      selectedNode: null, // 現在選択されているノード
    };
  },
  mounted() {
    this.drawChart();
  },
  methods: {
    drawChart() {
      const data = {
        name: "Root",
        children: [
          {
            name: "Group 1",
            children: [
              { name: "Leaf G1-1" },
              { name: "Leaf G1-2" },
              { name: "Leaf G1-3" }
            ]
          },
          {
            name: "Group 2",
            children: [
              { name: "Leaf G2-1" },
              { name: "Leaf G2-2" },
              { name: "Leaf G2-3" },
              { name: "Leaf G2-4" }
            ]
          },
          {
            name: "Group 3",
            children: [
              { name: "Leaf G3-1" },
              { name: "Leaf G3-2" }
            ]
          },
          {
            name: "Group 4",
            children: [
              { name: "Leaf G4-1" },
              { name: "Leaf G4-2" },
              { name: "Leaf G4-3" },
              { name: "Leaf G4-4" },
              { name: "Leaf G4-5" }
            ]
          }
        ]
      };

      const links = [
        { source: "Leaf G1-1", target: "Leaf G2-2" },
        { source: "Leaf G1-2", target: "Leaf G3-1" },
        { source: "Leaf G1-3", target: "Leaf G4-3" },
        { source: "Leaf G2-1", target: "Leaf G3-2" },
        { source: "Leaf G2-3", target: "Leaf G4-1" },
        { source: "Leaf G2-4", target: "Leaf G4-4" },
        { source: "Leaf G3-1", target: "Leaf G4-2" },
        { source: "Leaf G3-2", target: "Leaf G4-5" }
      ];

      const svg = d3.select(this.$refs.svg);
      svg.selectAll('*').remove(); // 既存の描画をクリア

      const width = +svg.attr("width");
      const height = +svg.attr("height");
      const radius = Math.min(width, height) / 2;

      const g = svg.append("g")
        .attr("transform", `translate(${width / 2},${height / 2})`);

      const cluster = d3.cluster()
        .size([2 * Math.PI, radius - 100]);

      const root = d3.hierarchy(data)
        .sum(d => d.size);

      cluster(root);

      const line = d3.radialLine()
        .curve(d3.curveBundle.beta(0.85))
        .radius(d => d.y)
        .angle(d => d.x);

      const link = g.selectAll(".link")
        .data(links)
        .enter().append("path")
        .attr("class", "link")
        .attr("d", d => {
          const source = root.descendants().find(n => n.data.name === d.source);
          const target = root.descendants().find(n => n.data.name === d.target);
          return line(source.path(target));
        })
        .attr("fill", "none")
        .attr("stroke", "#ccc")
        .attr("stroke-width", 1.5);

      const node = g.selectAll(".node")
        .data(root.descendants())
        .enter().append("g")
        .attr("class", "node")
        .attr("transform", d => `
          rotate(${d.x * 180 / Math.PI - 90})
          translate(${d.y},0)
        `)
        .on("click", (event, d) => {
          this.selectedNode = this.selectedNode === d ? null : d;
          this.updateHighlight(links, root);
        });

      node.append("circle")
        .attr("r", 4)
        .attr("fill", "#999");

      node.append("text")
        .attr("dy", ".31em")
        .attr("x", d => d.x < Math.PI === !d.children ? 6 : -6)
        .style("text-anchor", d => d.x < Math.PI === !d.children ? "start" : "end")
        .attr("transform", d => d.x >= Math.PI ? "rotate(180)" : null)
        .text(d => d.data.name);

      svg.call(d3.zoom().on("zoom", (event) => {
        g.attr("transform", event.transform);
      }));

      this.updateHighlight = (links, root) => {
        const selectedLinks = links.filter(l => {
          return this.selectedNode && (l.source === this.selectedNode.data.name || l.target === this.selectedNode.data.name);
        });

        link.attr("stroke", d => {
          const source = root.descendants().find(n => n.data.name === d.source);
          const target = root.descendants().find(n => n.data.name === d.target);
          const isHighlighted = selectedLinks.some(l => l.source === source.data.name && l.target === target.data.name);
          return isHighlighted ? "red" : "#ccc";
        });

        link.attr("stroke-width", d => {
          const source = root.descendants().find(n => n.data.name === d.source);
          const target = root.descendants().find(n => n.data.name === d.target);
          const isHighlighted = selectedLinks.some(l => l.source === source.data.name && l.target === target.data.name);
          return isHighlighted ? 2.5 : 1.5;
        });

        node.selectAll("circle").attr("fill", d => {
          if (!this.selectedNode) return "#999";
          const isConnected = selectedLinks.some(l => l.source === d.data.name || l.target === d.data.name);
          return isConnected || d === this.selectedNode ? "red" : "#ccc";
        });

        node.selectAll("text").style("fill", d => {
          if (!this.selectedNode) return "#000";
          const isConnected = selectedLinks.some(l => l.source === d.data.name || l.target === d.data.name);
          return isConnected || d === this.selectedNode ? "red" : "#ccc";
        });

        // Highlight paths from the root to the selected node
        g.selectAll(".link-to-selected")
          .data(root.descendants().slice(1))
          .enter().append("path")
          .attr("class", "link-to-selected")
          .attr("d", d => {
            return line(d.path(root));
          })
          .attr("fill", "none")
          .attr("stroke", "#ccc")
          .attr("stroke-width", 1.5)
          .attr("display", d => {
            const isAncestor = this.selectedNode && d.ancestors().includes(this.selectedNode);
            return isAncestor ? "block" : "none";
          });

        g.selectAll(".link-to-selected")
          .attr("stroke", d => {
            const isAncestor = this.selectedNode && d.ancestors().includes(this.selectedNode);
            return isAncestor ? "red" : "#ccc";
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
