<template>
    <div>
      <h1>Bayesian Prediction for Failure Rate</h1>
      <form @submit.prevent="submitForm">
        <div>
          <label for="times">Times (comma separated):</label>
          <input type="text" v-model="times" required>
        </div>
        <div>
          <label for="failures">Failures (comma separated):</label>
          <input type="text" v-model="failures" required>
        </div>
        <div>
          <label for="failure_types">Failure Types (comma separated):</label>
          <input type="text" v-model="failureTypes" required>
        </div>
        <div>
          <label for="failure_causes">Failure Causes (comma separated):</label>
          <input type="text" v-model="failureCauses" required>
        </div>
        <div>
          <label for="maintenance_types">Maintenance Types (comma separated):</label>
          <input type="text" v-model="maintenanceTypes" required>
        </div>
        <div>
          <label for="maintenance_results">Maintenance Results (comma separated):</label>
          <input type="text" v-model="maintenanceResults" required>
        </div>
        <div>
          <label for="window_size">Window Size for Moving Average:</label>
          <input type="number" v-model="windowSize" required>
        </div>
        <button type="submit">Submit</button>
      </form>
      <div v-if="predictedFailureRates.length">
        <h2>Results:</h2>
        <svg id="chart" width="800" height="400"></svg>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import * as d3 from 'd3';
  
  export default {
    data() {
      return {
        times: '',
        failures: '',
        failureTypes: '',
        failureCauses: '',
        maintenanceTypes: '',
        maintenanceResults: '',
        windowSize: 3,
        predictedFailureRates: [],
        rateChanges: [],
        predictedPhases: []
      };
    },
    methods: {
      async submitForm() {
        try {
          console.log('Sending data to the server:', {
            times: this.times.split(',').map(Number),
            failures: this.failures.split(',').map(Number),
            failure_types: this.failureTypes.split(','),
            failure_causes: this.failureCauses.split(','),
            maintenance_types: this.maintenanceTypes.split(','),
            maintenance_results: this.maintenanceResults.split(','),
            window_size: this.windowSize
          });
          const response = await axios.post('http://127.0.0.1:8000/api/reliability/BayesianPrediction/', {
            times: this.times.split(',').map(Number),
            failures: this.failures.split(',').map(Number),
            failure_types: this.failureTypes.split(','),
            failure_causes: this.failureCauses.split(','),
            maintenance_types: this.maintenanceTypes.split(','),
            maintenance_results: this.maintenanceResults.split(','),
            window_size: this.windowSize
          });
          console.log('Server response:', response.data);
          this.predictedFailureRates = response.data.predicted_failure_rates;
          this.rateChanges = response.data.rate_changes;
          this.predictedPhases = response.data.predicted_phases;
          this.renderChart(response.data.times, response.data.predicted_failure_rates, response.data.rate_changes, response.data.predicted_phases);
        } catch (error) {
          console.error('Error:', error);
        }
      },
      renderChart(times, predictedFailureRates, rateChanges, predictedPhases) {
        const svg = d3.select("#chart");
        svg.selectAll("*").remove(); // Clear previous chart
  
        const width = +svg.attr("width");
        const height = +svg.attr("height");
        const margin = { top: 20, right: 20, bottom: 30, left: 50 };
  
        const x = d3.scaleLinear().domain([0, d3.max(times)]).range([margin.left, width - margin.right]);
        const y = d3.scaleLinear().domain([0, d3.max(predictedFailureRates)]).range([height - margin.bottom, margin.top]);
  
        const line = d3.line()
          .x((d, i) => x(times[i]))
          .y(d => y(d));
  
        svg.append("g")
          .attr("transform", `translate(0,${height - margin.bottom})`)
          .call(d3.axisBottom(x));
        svg.append("g")
          .attr("transform", `translate(${margin.left},0)`)
          .call(d3.axisLeft(y));
  
        svg.append("path")
          .datum(predictedFailureRates)
          .attr("fill", "none")
          .attr("stroke", "blue")
          .attr("stroke-width", 1.5)
          .attr("d", line);
  
        const phaseColor = d3.scaleOrdinal()
          .domain([0, 1, 2])
          .range(["red", "green", "orange"]);
  
        svg.selectAll("circle")
          .data(predictedPhases)
          .enter()
          .append("circle")
          .attr("cx", (d, i) => x(times[i + 1]))
          .attr("cy", (d, i) => y(predictedFailureRates[i + 1]))
          .attr("r", 5)
          .attr("fill", d => phaseColor(d));
      }
    }
  };
  </script>
  
  <style>
  #chart {
    width: 100%;
    height: 400px;
  }
  </style>
  