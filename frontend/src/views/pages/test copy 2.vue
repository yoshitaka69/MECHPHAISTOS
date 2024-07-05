<template>
    <div>
      <DataTable :value="products" dataKey="id">
        <Column field="name" header="Name">
          <template #body="slotProps">
            <div v-if="slotProps.data.editing">
              <input v-model="slotProps.data.name" @blur="finishEdit(slotProps.data)" />
            </div>
            <div v-else>
              {{ slotProps.data.name }}
            </div>
          </template>
        </Column>
        <Column header="Check">
          <template #body="slotProps">
            <Checkbox v-model="slotProps.data.checked" :binary="true" />
          </template>
        </Column>
        <Column header="Actions">
          <template #body="slotProps">
            <div>
              <i class="pi pi-pencil" @click="editRow(slotProps.data)" style="margin-right: 10px; cursor: pointer;"></i>
              <i class="pi pi-trash" @click="deleteRow(slotProps.data)" style="cursor: pointer;"></i>
            </div>
          </template>
        </Column>
      </DataTable>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import Checkbox from 'primevue/checkbox';
  
  export default {
    components: {
      DataTable,
      Column,
      Checkbox,
    },
    setup() {
      const products = ref([
        { id: 1, name: 'Product 1', checked: false, editing: false },
        { id: 2, name: 'Product 2', checked: false, editing: false },
      ]);
  
      const editRow = (rowData) => {
        rowData.editing = true;
      };
  
      const finishEdit = (rowData) => {
        rowData.editing = false;
      };
  
      const deleteRow = (rowData) => {
        products.value = products.value.filter(product => product.id !== rowData.id);
      };
  
      return {
        products,
        editRow,
        finishEdit,
        deleteRow,
      };
    },
  };
  </script>
  
  <style>
  /* 任意でスタイルを追加できます */
  </style>
  