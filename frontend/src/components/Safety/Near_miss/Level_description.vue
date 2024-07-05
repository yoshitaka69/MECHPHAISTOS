<template>
	<div class="table-container">
	  <table id="LvDescription">
		<thead>
		  <tr>
			<th>Level</th>
			<th>Injured Lv</th>
			<th>Equipment Damage Lv</th>
			<th>Affect Of Environment</th>
			<th>News Coverage</th>
			<th>Measures</th>
		  </tr>
		</thead>
		<tbody>
		  <tr>
			<td><b>A</b></td>
			<td>Death</td>
			<td>Explosion, Destruction of critical assets</td>
			<td>Massive irreversible damage</td>
			<td>International media coverage</td>
			<td>Something needs to be done urgently</td>
		  </tr>
		  <tr>
			<td><b>B</b></td>
			<td>Visceral disorder, Lv3 Burn, Amputation</td>
			<td>Limited destruction or fire that takes more than a week to repair</td>
			<td>1 year of ecological damage</td>
			<td>Local media coverage</td>
			<td>Some kind of soft or hard response is required within a few days.</td>
		  </tr>
		  <tr>
			<td><b>C</b></td>
			<td>Eye injury, Lv2 Burn, fracture</td>
			<td>Minor damage within 1 week to repair</td>
			<td>Short-term effects around the leak location</td>
			<td>No media coverage. However, it is necessary to report to the government agency.</td>
			<td>In addition to considering hard measures.</td>
		  </tr>
		  <tr>
			<td><b>D</b></td>
			<td>First aid that does not interfere with work, Lv1 Burn</td>
			<td>Minor damage that can be repaired within 1 day</td>
			<td>There is no effect on biological systems, but coloring and odor are generated.</td>
			<td>No media coverage. However, there is no need to report to government agencies.</td>
			<td>Consider measures such as reviewing methods and rules (soft).</td>
		  </tr>
		  <tr>
			<td><b>E</b></td>
			<td>Minor scratches not applicable</td>
			<td>Minor damage not applicable to the above</td>
			<td>Minor environmental damage that does not fall under the above categories</td>
			<td>Not applicable to the above</td>
			<td>No measures needed</td>
		  </tr>
		</tbody>
	  </table>
	</div>
  </template>
  
  <script>
  export default {
	mounted() {
	  // Additional JavaScript if needed
	}
  }
  </script>
  
  <style scoped>
  .table-container {
	width: 100%;
	max-width: 800px; /* 任意の最大幅に調整 */
	margin: 0 auto; /* 中央に配置 */
	overflow-x: auto; /* 水平方向のスクロールを可能に */
  }
  
  #LvDescription {
	width: 100%;
	border-collapse: collapse;
  }
  
  #LvDescription th,
  #LvDescription td {
	border: 1px solid black;
	padding: 8px;
	text-align: center;
  }
  
  #LvDescription th {
	background-color: grey;
	color: white;
  }
  
  #LvDescription tr:nth-child(even) {
	background-color: lightgrey;
  }
  
  #LvDescription tr:nth-child(odd) {
	background-color: white;
  }
  </style>
  