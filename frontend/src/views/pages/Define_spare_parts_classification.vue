<template>
    <div class="container">
      <h2>Spare Parts Inventory Classification</h2>
      <DataTable :value="stockItems" responsiveLayout="scroll">
        <Column field="category" header="Classification" :sortable="true"></Column>
        <Column field="definition" header="Definition"></Column>
        <Column field="features" header="Features"></Column>
        <Column field="action" header="Actions"></Column>
      </DataTable>
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  
  export default defineComponent({
    name: 'StockClassificationTable',
    components: {
      DataTable,
      Column
    },
    data() {
      return {
        stockItems: [
          {
            category: 'Long-Term Stock Items',
            definition: 'Parts that have not been used for a long time but are important and need to be kept in stock.',
            features: 'Low usage frequency, but critical parts that need to be kept for unexpected failures. Long lead-time parts are included here.',
            action: 'Regularly check inventory and perform maintenance to ensure there is no deterioration.'
          },
          {
            category: 'Short-Term Stock Items',
            definition: 'Parts with a high inventory turnover rate and are regularly used.',
            features: 'Consumables and common parts that need frequent replenishment due to daily wear and tear.',
            action: 'Implement an automatic ordering system and set optimal safety stock levels to prevent stockouts.'
          },
          {
            category: 'Dead Stock Items',
            definition: 'Parts that have not been used for a long time and are not expected to be used in the future.',
            features: 'Parts for discontinued machines or parts that were over-ordered, occupying storage space and driving up costs.',
            action: 'Regularly review inventory and dispose of unnecessary stock or consider reallocating it to other departments.'
          },
          {
            category: 'Critical Stock Items',
            definition: 'High-priority parts that must always be in stock to ensure immediate replacement when needed.',
            features: 'Essential for preventing system downtime. Often includes parts with long lead times.',
            action: 'Create a list of critical parts and regularly check stock levels.'
          },
          {
            category: 'Safety Stock Items',
            definition: 'Extra stock held in addition to normal ordering quantities to account for demand fluctuations and supply delays.',
            features: 'Consumables and parts that are difficult to obtain quickly, held to meet variable demand.',
            action: 'Optimize safety stock levels to avoid stockouts.'
          },
          {
            category: 'Irregular Use Stock Items',
            definition: 'Parts that are used infrequently and may not be used for extended periods, but are sometimes needed unexpectedly.',
            features: 'Challenging to adjust stock levels due to unpredictable usage patterns.',
            action: 'Review inventory levels based on historical usage data and shorten lead times where necessary.'
          }
        ]
      };
    }
  });
  </script>
  
  <style scoped>
  h2 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  /* Use :deep() to target deep child components */
  :deep(.p-datatable thead th) {
    background-color: #d3d3d3 !important;
  }
  
  .container {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
</style>

  