<template>
  <div>
    <table id="LvDescriptionImpact" class="impact-table">
      <thead>
        <tr>
          <th>1 - Operator recovery possible</th>
          <th>2 - Spare parts and replacement machines are available, allowing for quick recovery.</th>
          <th>3 - Recovery that requires specialized contractors and involves irregularities</th>
          <th>4 - Temporary recovery in situations where production schedule or quality is affected</th>
          <th>5 - Recovery not possible</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>・Recovery possible by operator・Replacement device or easy recovery possible・Equipment is divided into two lines, making recovery easy.Spare parts are on hand and restoration is easily possible with WI</td>
          <td>・Recovery within 1 day・Recovery by operator is not possible・Restoration by knowledgeable and professional contractors.Spare parts and replacement machines available・Parts delivery time for restoration is within 3 days</td>
          <td>・Recovery within 1 to 3 days・Recovery by operator is not possible・Restoration by knowledgeable and professional contractors.No spare parts or replacement equipment available・The parts delivery time required for restoration is between 1 and 3 days。</td>
          <td>・Recovery within 3 to 14 days・Manufacturing by changing manufacturing conditions such as single-lung operation・Irregular operations by operators occur after provisional recovery・Special parts are required and the parts delivery time is 3 days or more。</td>
          <td>・Due to severe equipment damage, recovery with replacement equipment is not possible.・Individual response is required after coordinating with each department</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ImpactTable'
}
</script>

<style scoped>
.impact-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.impact-table th, .impact-table td {
  border: 1px solid black;
  padding: 10px;
  text-align: center;
  font-family: Arial, sans-serif;
}

.impact-table th {
  background-color: grey;
  color: white;
}

.impact-table tr:nth-child(even) {
  background-color: lightgrey;
}

.impact-table tr:nth-child(odd) {
  background-color: white;
}

.impact-table td {
  vertical-align: top;
}
</style>
