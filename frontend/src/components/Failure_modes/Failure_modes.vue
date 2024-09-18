<template>
    <div>
      <h2>Failure Modes in Factories</h2>
      <table>
        <thead>
          <tr>
            <th>No</th>
            <th>Failure Mode</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(failure, index) in failureModes" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ failure.name }}</td>
            <td>{{ failure.description }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        failureModes: [
          { name: "Wear", description: "Surface wears down due to friction, reducing functionality." },
          { name: "Fatigue Failure", description: "Repeated stress causes cracks and eventually failure." },
          { name: "Corrosion", description: "Material deteriorates through chemical reactions, especially rusting in metals." },
          { name: "Overheating", description: "Excessive temperatures cause deterioration of machinery or electronics." },
          { name: "Inadequate Lubrication", description: "Insufficient lubrication leads to increased friction and equipment damage." },
          { name: "Seal Failure", description: "Damaged seals cause leaks, affecting efficiency or safety." },
          { name: "Overload", description: "Exceeding design limits causes parts to break." },
          { name: "Vibration", description: "Excessive vibration loosens or damages components." },
          { name: "Electrical Insulation Failure", description: "Insulation deteriorates, leading to short circuits or fires." },
          { name: "Short Circuit", description: "Electrical circuits fail due to unintended connections." },
          { name: "Mechanical Shock", description: "Sudden impacts cause parts to break." },
          { name: "Thermal Fatigue", description: "Repeated temperature changes cause material cracks and failure." },
          { name: "Cavitation", description: "Bubbles form and collapse, damaging surface materials." },
          { name: "Frictional Wear", description: "Surfaces wear down due to frictional contact." },
          { name: "Stress Corrosion Cracking", description: "Tensile stress and corrosive environments lead to material breakdown." },
          { name: "Erosion", description: "Surface material is worn away by fast-moving fluids or gases." },
          { name: "Oxidation", description: "High temperatures cause metals to degrade via oxygen reactions." },
          { name: "Cable Breakage", description: "Cables break due to repeated bending or external damage." },
          { name: "Bearing Failure", description: "Bearings fail due to wear, poor lubrication, or overload." },
          { name: "Electronic Component Failure", description: "Semiconductors or capacitors fail due to overload or overheating." },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  table {
    width: 100%;
    border-collapse: collapse;
    background-color: white; /* Set background color to white */
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
  }
  
  th {
    background-color: #f2f2f2;
    text-align: left;
  }
  
  tbody tr:nth-child(odd) {
    background-color: white; /* Set background color for odd rows to white */
  }
  
  tbody tr:nth-child(even) {
    background-color: white; /* Ensure even rows are also white */
  }
  </style>
  