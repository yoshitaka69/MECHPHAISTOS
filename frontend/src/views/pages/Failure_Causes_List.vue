<template>
  <div>
    <h2>Equipment Failure Causes List</h2>
    <table>
      <thead>
        <tr>
          <th>Failure Cause</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in failureCauses" :key="index">
          <td>{{ item.cause }}</td>
          <td>{{ item.description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      failureCauses: [
        { cause: "Stress Fatigue", description: "A phenomenon where repeated stress on machinery or structures causes microcracks, eventually leading to failure." },
        { cause: "Overheating / Overload", description: "A condition where equipment or machinery is exposed to temperatures or loads beyond normal operating ranges, causing damage or deterioration." },
        { cause: "Misuse", description: "Occurs when equipment is operated in a manner that ignores its intended purpose or procedures, leading to malfunctions or failures." },
        { cause: "Operational Error", description: "Failures caused by incorrect operations or settings by the operator, resulting in equipment not functioning properly." },
        { cause: "Manufacturing Defect", description: "Issues that arise when parts or equipment are not manufactured to design specifications, causing problems during use." },
        { cause: "Poor Maintenance", description: "Failures due to inadequate regular inspections or repairs, leading to reduced functionality or equipment breakdown." },
        { cause: "Improper Installation", description: "Equipment does not operate normally due to improper installation or placement during setup." },
        { cause: "Material Defect", description: "Occurs when the materials used do not meet the required performance, causing the equipment to not function as expected." },
        { cause: "Progressive Damage", description: "Gradual damage to equipment due to repeated use or aging, leading to decreased performance." },
        { cause: "Corrosion", description: "Deterioration of metals or other materials caused by environmental factors, reducing strength and durability." },
        { cause: "Control Failure", description: "Abnormalities in the control system of equipment, causing unintended operations or shutdowns." },
        { cause: "Process Defect", description: "Issues in the manufacturing or operational process using the equipment, preventing the achievement of desired performance or quality." }
      ]
    };
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
  text-align: left;
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

tbody tr:hover {
  background-color: #f1f1f1;
}
</style>
