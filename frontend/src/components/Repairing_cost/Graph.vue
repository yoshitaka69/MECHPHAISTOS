<template>
  <div>
      <v-flex>
          <v-card>
              <v-card-title>Repairing Cost</v-card-title>
              <div id="rpc"></div>
          </v-card>
      </v-flex>
  </div>
</template>

<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";

export default {
  data() {
      return {
          y: [],
          error: null,
          message: null,
      };
  },

  mounted() {
      axios
          .get("http://localhost:3000/PlannedPM02")
          .then(response => {
              this.y = response.data.PlantA.cost;
              let trace1 = {
                  x: ["Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."],
                  y: this.y
              };

              const layout = {
                  height: 500,
                  width: 600
              };

              Plotly.newPlot('rpc', [trace1], layout);
          })
          .catch(error => {
              this.error = error;
          });
  },

};
</script>