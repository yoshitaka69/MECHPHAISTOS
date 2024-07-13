<template>
    <div>
      <h2>PM Trouble history</h2>
      <DataTable 
        v-model:filters="filters" 
        :value="troubles" 
        paginator 
        :rows="10" 
        dataKey="date"
        filterDisplay="menu"
        :globalFilterFields="['pmType', 'description', 'failureType', 'failureCauses', 'repairingType', 'tag']"
        @filter="onFilter"
      >
        <template #header>
          <div class="flex justify-between">
            <Button type="button" icon="pi pi-filter-slash" label="Clear" outlined @click="clearFilter()" />
            <div>
              <i class="pi pi-search" />
              <InputText v-model="filters.global.value" placeholder="Keyword Search" />
            </div>
          </div>
        </template>
        <template #empty>No records found.</template>
        <Column 
          field="date" 
          header="Date" 
          :headerStyle="{ backgroundColor: '#d3e0ea' }"
          :showFilterMatchModes="false"
        >
          <template #body="{ data }">
            {{ formatDate(data.date) }}
          </template>
          <template #filter="{ filterModel }">
            <Calendar v-model="filterModel.value" dateFormat="yy-mm-dd" placeholder="YYYY-MM-DD" />
          </template>
        </Column>
        <Column 
          field="pmType" 
          header="PM type" 
          sortable 
          filter 
          :filterMenuStyle="{ width: '12rem' }"
          :showFilterMatchModes="false"
          :headerStyle="{ backgroundColor: '#a4c3b2' }"
        >
          <template #filter="{ filterModel }">
            <SelectButton v-model="filterModel.value" :options="pmTypeOptions" optionLabel="label" optionValue="value" placeholder="Select PM type" showClear />
          </template>
        </Column>
        <Column field="description" header="Description" :headerStyle="{ backgroundColor: '#f5d5cb' }">
          <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by description" />
          </template>
        </Column>
        <Column field="failureType" header="Failure type" :headerStyle="{ backgroundColor: '#f5b7b1' }" :showFilterMatchModes="false">
          <template #filter="{ filterModel }">
            <SelectButton v-model="filterModel.value" :options="failureTypeOptions" optionLabel="label" optionValue="value" placeholder="Select Failure Type" showClear />
          </template>
        </Column>
        <Column field="failureCauses" header="Failure Causes" :headerStyle="{ backgroundColor: '#c5e1a5' }" :showFilterMatchModes="false">
          <template #filter="{ filterModel }">
            <SelectButton v-model="filterModel.value" :options="failureCausesOptions" optionLabel="label" optionValue="value" placeholder="Select Failure Causes" showClear />
          </template>
        </Column>
        <Column field="repairingType" header="Repairing Type" :headerStyle="{ backgroundColor: '#ffe0b2' }" :showFilterMatchModes="false">
          <template #filter="{ filterModel }">
            <SelectButton v-model="filterModel.value" :options="repairingTypeOptions" optionLabel="label" optionValue="value" placeholder="Select Repairing Type" showClear />
          </template>
        </Column>
        <Column field="tag" header="#tag" :headerStyle="{ backgroundColor: '#ce93d8' }">
          <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by tag" />
          </template>
        </Column>
      </DataTable>
      <div v-if="filteredTroubles.length">
        <h3>Filtered Results</h3>
        <ul>
          <li v-for="trouble in filteredTroubles" :key="trouble.date">
            {{ trouble.date }} - {{ trouble.pmType }} - {{ trouble.description }} - {{ trouble.failureType }} - {{ trouble.failureCauses }} - {{ trouble.repairingType }} - {{ trouble.tag }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { FilterMatchMode, FilterOperator } from 'primevue/api';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import Button from 'primevue/button';
  import InputText from 'primevue/inputtext';
  import Calendar from 'primevue/calendar';
  import SelectButton from 'primevue/selectbutton';
  
  const pmTypeOptions = [
    { label: 'PM03', value: 'PM03' },
    { label: 'PM04', value: 'PM04' }
  ];
  
  const failureTypeOptions = [
    { label: 'Type 1', value: 'Type 1' },
    { label: 'Type 2', value: 'Type 2' }
  ];
  
  const failureCausesOptions = [
    { label: 'Cause 1', value: 'Cause 1' },
    { label: 'Cause 2', value: 'Cause 2' }
  ];
  
  const repairingTypeOptions = [
    { label: 'Repair 1', value: 'Repair 1' },
    { label: 'Repair 2', value: 'Repair 2' }
  ];
  
  const filters = ref();
  const troubles = ref([
    { date: '2024-07-01', pmType: 'PM03', description: 'Description 1', failureType: 'Type 1', failureCauses: 'Cause 1', repairingType: 'Repair 1', tag: '#001' },
    { date: '2024-07-02', pmType: 'PM04', description: 'Description 2', failureType: 'Type 2', failureCauses: 'Cause 2', repairingType: 'Repair 2', tag: '#002' },
    // ここに他の行データを追加できます
  ]);
  
  const filteredTroubles = ref([...troubles.value]);
  
  const initFilters = () => {
    filters.value = {
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
      date: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.DATE_IS }] },
      pmType: { value: null, matchMode: FilterMatchMode.IN },
      description: { value: null, matchMode: FilterMatchMode.CONTAINS },
      failureType: { value: null, matchMode: FilterMatchMode.IN },
      failureCauses: { value: null, matchMode: FilterMatchMode.IN },
      repairingType: { value: null, matchMode: FilterMatchMode.IN },
      tag: { value: null, matchMode: FilterMatchMode.CONTAINS },
    };
  };
  
  initFilters();
  
  const clearFilter = () => {
    initFilters();
    filteredTroubles.value = [...troubles.value]; // Clear the filtered results to show all data
  };
  
  const formatDate = (value) => {
    if (!value) return '';
    const date = new Date(value);
    return date.toLocaleDateString('en-CA'); // Format as YYYY-MM-DD
  };
  
  const onFilter = (event) => {
    filteredTroubles.value = event.filteredValue;
  };
  </script>
  
  <style scoped>
  h2 {
    color: #333;
  }
  
  th {
    background-color: #d3e0ea; /* 適切な色に変更 */
  }
  
  .p-datatable .p-datatable-thead > tr > th {
    background-color: #d3e0ea !important; /* ヘッダーの背景色を統一 */
  }
  </style>
  