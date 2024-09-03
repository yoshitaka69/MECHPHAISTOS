<template>
  <div>
    <table id="LvDescriptionImpact" class="impact-table">
      <thead>
        <tr>
          <th>1 - Low</th>
          <th>2 - Middle</th>
          <th>3 - High</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>・Equipment that has an impact on the entire factory
<br>(Compressor equipment, STM main pipe, IA main pipe, LPG auxiliary equipment)
<br>・Related to substation equipment
<br>・Process core line</td>
          <td>・Other than process core line</td>
          <td>(ex.)・The equipment must not affect production.
<br>・It must be related to buildings.
<br>・It must be related to on-site road construction.</td>
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
