<template>
  <div>
    <table id="LvDescriptionFailure" class="failure-table">
      <thead>
        <tr>
          <th style="background-color: #00B050;">1 - Extremely rare</th>
          <th style="background-color: #92D050;">2 - Rare</th>
          <th style="background-color: #FFFF00;">3 - Occasionally</th>
          <th style="background-color: #FFC000;">4 - Often</th>
          <th style="background-color: #FF0000;">5 - Frequently</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>・No failures have occurred in the past 5 years.・Equipment operating rate is low, and the possibility of failure occurring in the future is low。</td>
          <td>・Failures have occurred less than twice in the past five years。・Preventive maintenance has been performed in the past five years。・Countermeasures for past problems have been implemented through RCA, etc., and are showing sufficient effectiveness.Managed by preventive maintenance tasks, with regular maintenance observations and actions taken。</td>
          <td>・Failures have occurred 2 or more times but less than 3 times in the past 5 years。・It is managed by preventive maintenance tasks, and early abnormalities can be detected。・Countermeasures for past problems have been implemented through RCA, etc., and are showing sufficient effectiveness。・PM has not been implemented for a long time。</td>
          <td>・Failures have occurred 2 or more times but less than 3 times in the past 5 years.Although managed by preventive maintenance tasks, a certain number of failures occur.Countermeasures for past problems caused by RCA, etc. have not been implemented, or their effects have not been sufficiently effective。・The cause of the trouble is clear and its occurrence can be predicted。</td>
          <td>・Failures have occurred three or more times during repairs over the past five years.Not managed by preventive maintenance tasks, and initial abnormalities are not noticed.Countermeasures for past problems have not been implemented or their effects have not been sufficiently effective。The cause of the problem is not clear。</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ProbabilityOfFailure'
};
</script>

<style scoped>
.failure-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.failure-table th, .failure-table td {
  border: 1px solid black;
  padding: 10px;
  text-align: center;
  font-family: Arial, sans-serif;
}

.failure-table th {
  color: black;
}

.failure-table tr:nth-child(even) {
  background-color: lightgrey;
}

.failure-table tr:nth-child(odd) {
  background-color: white;
}

.failure-table td {
  vertical-align: top;
}
</style>
