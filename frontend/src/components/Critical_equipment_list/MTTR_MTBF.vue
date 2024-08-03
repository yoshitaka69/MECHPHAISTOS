<template>
    <div class="container">
      <div ref="chart" class="chart"></div>
    </div>
  </template>
  
  <script>
  import * as d3 from "d3";
  
  export default {
    name: "MTBFMTTRBar",
    data() {
      return {
        sampleData: {
          mtbf: 200, // MTBF in days
          mttr: 50,  // MTTR in days
        },
      };
    },
    mounted() {
      this.drawChart();
    },
    methods: {
      drawChart() {
        const margin = { top: 20, right: 30, bottom: 70, left: 30 }; // Increased bottom margin
        const width = 800 - margin.left - margin.right;
        const height = 60 - margin.top; // Height for bars and bounding box
  
        const svg = d3
          .select(this.$refs.chart)
          .append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr("transform", `translate(${margin.left},${margin.top})`);
  
        // Add a black border around the chart area
        svg.append("rect")
          .attr("x", 0)
          .attr("y", 0)
          .attr("width", width)
          .attr("height", height)
          .style("stroke", "black")
          .style("fill", "none")
          .style("stroke-width", 1);
  
        const now = new Date();
        const oneYearAgo = new Date(now);
        oneYearAgo.setFullYear(now.getFullYear() - 1);
        const oneYearLater = new Date(now);
        oneYearLater.setFullYear(now.getFullYear() + 1);
  
        const x = d3
          .scaleTime()
          .domain([oneYearAgo, oneYearLater])
          .range([0, width]);
  
        const xAxis = d3.axisBottom(x).ticks(d3.timeMonth.every(1)).tickFormat(d3.timeFormat("%b %Y"));
  
        svg
          .append("g")
          .attr("transform", `translate(0,${height})`)
          .call(xAxis)
          .selectAll("text")
          .attr("transform", "rotate(-45)")
          .style("text-anchor", "end");
  
        const mtbfStartDate = new Date(now);
        mtbfStartDate.setDate(now.getDate() - this.sampleData.mtbf);
        const mtbfEndDate = new Date(now);
  
        // Add MTBF bar
        svg
          .append("rect")
          .attr("x", x(mtbfStartDate))
          .attr("y", 0) // Align with the top of the bounding box
          .attr("width", x(mtbfEndDate) - x(mtbfStartDate))
          .attr("height", height) // Fill the entire height of the bounding box
          .attr("fill", "steelblue");
  
        // Add MTBF label
        svg
          .append("text")
          .attr("x", (x(mtbfStartDate) + x(mtbfEndDate)) / 2)
          .attr("y", height / 2)
          .attr("dy", ".35em")
          .attr("fill", "white")
          .attr("text-anchor", "middle")
          .text("MTBF");
  
        const mttrStartDate = new Date(now);
        const mttrEndDate = new Date(mttrStartDate);
        mttrEndDate.setDate(mttrStartDate.getDate() + this.sampleData.mttr);
  
        // Add MTTR bar
        svg
          .append("rect")
          .attr("x", x(mttrStartDate))
          .attr("y", 0) // Align with the top of the bounding box
          .attr("width", x(mttrEndDate) - x(mttrStartDate))
          .attr("height", height) // Fill the entire height of the bounding box
          .attr("fill", "orange");
  
        // Add MTTR label
        svg
          .append("text")
          .attr("x", (x(mttrStartDate) + x(mttrEndDate)) / 2)
          .attr("y", height / 2)
          .attr("dy", ".35em")
          .attr("fill", "black")
          .attr("text-anchor", "middle")
          .text("MTTR");
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .chart {
    width: 100%;
    height: auto;
  }
  </style>
  