PM03
<template>
    <div>
      <table id="PlantMaintenanceType" class="impact-table">
        <thead>
          <tr>
            <th>1 - PM01 <br>(Plant Maintenance type1)</th>
            <th>2 - PM02 <br>(Plant Maintenance type2)</th>
            <th>3 - PM03 <br>(Plant Maintenance type3)</th>
            <th>4 - PM04 <br>(Plant Maintenance type4)</th>
            <th>5 - PM05 <br>(Plant Maintenance type5)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>・PM01 is a maintenance category such as inspection and investigation methods. Please categorize costs such as obtaining estimates, design costs, and preliminary survey costs into this category. </td>
            <td>・PM02 is preventive maintenance. Basically, it is assigned as a planned and periodic maintenance task.</td>
            <td>・PM03 is corrective maintenance. This is maintenance performed in response to repair requests from other departments or when equipment breaks down.</td>
            <td>・Like PM03, PM04 is also in the corrective maintenance. <br>The major difference from PM03 is corrective maintenance that involves equipment stoppage (BreakDownTrouble). Therefore, I am a maintenance type who is required to respond quickly.</td>
            <td>・PM05 is maintenance based on improvement activities. Maintenance is something that brings some kind of benefit by performing maintenance activities or modifying equipment.</td>
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
  