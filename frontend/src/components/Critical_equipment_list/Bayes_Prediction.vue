<template>
  <div class="container">
    <h1>Bayesian Prediction for Failure Rate</h1>
    <div class="content">
      <form @submit.prevent="submitForm" class="form">
        <div>
          <label for="sampleData">Select Sample Data:</label>
          <select @change="loadSampleData($event)">
            <option value="" disabled selected>Select a sample data set</option>
            <option value="sample1">Sample Data 1</option>
            <option value="sample2">Sample Data 2</option>
          </select>
        </div>
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
      <div class="chart-container">
        <svg id="chart" width="800" height="400"></svg>
      </div>
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
  mounted() {
    // 初期状態でグラフを描画
    this.renderChart([], [], [], []);
  },
  methods: {
    loadSampleData(event) {
      const sampleData = {
        sample1: {
          times: "1,2,3,4",
          failures: "0,1,0,1",
          failureTypes: "mechanical,electrical,mechanical,electrical",
          failureCauses: "overload,wear,overload,wear",
          maintenanceTypes: "regular,preventive,regular,preventive",
          maintenanceResults: "checked,replaced,checked,replaced",
          windowSize: 3
        },
        sample2: {
          times: "1,2,3,4,5",
          failures: "0,1,0,1,0",
          failureTypes: "mechanical,electrical,mechanical,electrical,mechanical",
          failureCauses: "overload,wear,overload,wear,overload",
          maintenanceTypes: "regular,preventive,regular,preventive,regular",
          maintenanceResults: "checked,replaced,checked,replaced,checked",
          windowSize: 3
        }
      };
      const selectedSample = sampleData[event.target.value];
      this.times = selectedSample.times;
      this.failures = selectedSample.failures;
      this.failureTypes = selectedSample.failureTypes;
      this.failureCauses = selectedSample.failureCauses;
      this.maintenanceTypes = selectedSample.maintenanceTypes;
      this.maintenanceResults = selectedSample.maintenanceResults;
      this.windowSize = selectedSample.windowSize;
    },
    async submitForm() {
      const payload = {
        times: this.times.split(',').map(Number),
        failures: this.failures.split(',').map(Number),
        failure_types: this.failureTypes.split(','),
        failure_causes: this.failureCauses.split(','),
        maintenance_types: this.maintenanceTypes.split(','),
        maintenance_results: this.maintenanceResults.split(','),
        window_size: this.windowSize
      };
      
      console.log('Sending data to the server:', payload);

      try {
        const response = await axios.post('http://127.0.0.1:8000/api/reliability/BayesianPrediction/', payload);
        console.log('Server response:', response.data);
        this.predictedFailureRates = response.data.predicted_failure_rates;
        this.rateChanges = response.data.rate_changes;
        this.predictedPhases = response.data.predicted_phases;
        this.$nextTick(() => {
          this.renderChart(response.data.times, response.data.predicted_failure_rates, response.data.rate_changes, response.data.predicted_phases);
        });
      } catch (error) {
        console.error('Error:', error);
        if (error.response) {
          console.error('Server response:', error.response.data);
        }
      }
    },
    renderChart(times, predictedFailureRates, rateChanges, predictedPhases) {
      const svg = d3.select("#chart");
      svg.selectAll("*").remove(); // Clear previous chart

      const width = +svg.attr("width");
      const height = +svg.attr("height");
      const margin = { top: 40, right: 40, bottom: 50, left: 60 };

      const x = d3.scaleLinear().domain([0, d3.max(times) || 1]).range([margin.left, width - margin.right]);
      const y = d3.scaleLinear().domain([0, d3.max(predictedFailureRates) || 1]).range([height - margin.bottom, margin.top]);

      const line = d3.line()
        .x((d, i) => x(times[i]))
        .y(d => y(d));

      // X軸とY軸のグリッド線
      const xAxis = g => g
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(x).ticks(width / 80).tickSize(-height + margin.top + margin.bottom))
        .call(g => g.select(".domain").remove());

      const yAxis = g => g
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(y).ticks(height / 40).tickSize(-width + margin.left + margin.right))
        .call(g => g.select(".domain").remove());

      svg.append("g")
        .call(xAxis);

      svg.append("g")
        .call(yAxis);

      svg.append("path")
        .datum(predictedFailureRates)
        .attr("fill", "none")
        .attr("stroke", "blue")
        .attr("stroke-width", 2)
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

      // グラフタイトル
      svg.append("text")
        .attr("x", (width - margin.left - margin.right) / 2 + margin.left)
        .attr("y", margin.top / 2)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("font-weight", "bold")
        .text("Predicted Failure Rate Over Time");

      // X軸ラベル
      svg.append("text")
        .attr("x", (width - margin.left - margin.right) / 2 + margin.left)
        .attr("y", height - 10)
        .attr("text-anchor", "middle")
        .style("font-size", "12px")
        .text("Time");

      // Y軸ラベル
      svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 15)
        .attr("x", -(height - margin.top - margin.bottom) / 2 - margin.top)
        .attr("text-anchor", "middle")
        .style("font-size", "12px")
        .text("Failure Rate");
    }
  }
};
</script>

<style>
.container {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 1200px;
  margin: 0 auto;
}

.content {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.form {
  flex: 1;
  max-width: 300px;
  margin-right: 20px;
}

.form div {
  margin-bottom: 10px;
}

.form label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form input,
.form select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.form button {
  background-color: #007bff;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.form button:hover {
  background-color: #0056b3;
}

.chart-container {
  flex: 2;
}

#chart {
  width: 100%;
  height: 400px;
}
</style>
