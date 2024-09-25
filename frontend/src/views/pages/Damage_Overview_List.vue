<template>
    <div>
      <h2>Equipment Damage Overview List</h2>
      <table>
        <thead>
          <tr>
            <th>Damage Type</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in damageOverviews" :key="index">
            <td>{{ item.damageType }}</td>
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
        damageOverviews: [
          { damageType: "Leakage", description: "The unintended release of liquids, gases, or other substances from equipment or piping systems." },
          { damageType: "Wear and Tear / Stress Cracks", description: "Gradual degradation of equipment surfaces or structures due to friction, abrasion, or repeated stress, often resulting in cracks or breaks." },
          { damageType: "Cracks / Breakage", description: "The presence of fractures or complete breakage in equipment or components, which can compromise structural integrity." },
          { damageType: "Blockage / Clogging", description: "The obstruction of flow within pipes, filters, or equipment due to foreign objects or accumulated substances." },
          { damageType: "Seizure", description: "A condition where parts of equipment become stuck or immovable, usually due to a lack of lubrication or contamination." },
          { damageType: "Loosening", description: "The loss of tightness in connections or fasteners, which can lead to equipment malfunction or failure." },
          { damageType: "Deformation", description: "Alteration of the original shape of a component due to external forces or stress, impacting its functionality." },
          { damageType: "Misalignment", description: "The improper alignment of components, causing inefficient operation or excessive wear and tear." },
          { damageType: "Contamination", description: "The presence of unwanted substances, such as dirt, dust, or chemicals, that can degrade equipment performance or cause damage." },
          { damageType: "Corrosion", description: "The deterioration of materials, typically metals, due to chemical reactions with environmental elements like moisture or chemicals." },
          { damageType: "Fusion / Melting", description: "Damage caused by high temperatures leading to the fusion or melting of components, affecting their structural integrity." },
          { damageType: "Abnormal Noise", description: "Unusual or unexpected sounds emitted by equipment, often indicating internal damage or malfunction." },
          { damageType: "Abnormal Vibration", description: "Excessive or irregular vibrations in equipment, which can lead to further damage or failure." },
          { damageType: "Burn Damage", description: "Damage resulting from excessive heat or electrical faults, causing parts to char, melt, or deform." },
          { damageType: "Faulty Indication", description: "Incorrect or misleading readings from equipment indicators or gauges, which can lead to improper operation or maintenance." },
          { damageType: "Control Failure", description: "Malfunction in the control system, causing unintended operations or failure to respond to commands." },
          { damageType: "Sequencer Failure", description: "Issues with the sequencing or timing mechanisms in automated systems, disrupting normal operations." },
          { damageType: "No Damage", description: "No visible or identifiable damage present on the equipment or component." }
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
  