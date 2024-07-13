<template>
    <div>
      <DataTable 
        v-model:filters="filters" 
        :value="filteredEvents" 
        paginator 
        :rows="10" 
        dataKey="date"
        filterDisplay="menu"
        :globalFilterFields="['plant', 'event']"
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
          field="plant" 
          header="Plant" 
          sortable 
          filter 
          :filterMenuStyle="{ width: '12rem' }"
          :showFilterMatchModes="false"
          :headerStyle="{ backgroundColor: '#a4c3b2' }"
        >
          <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" placeholder="Search by Plant" />
          </template>
        </Column>
        <Column 
          field="event" 
          header="Event" 
          sortable 
          filter 
          :filterMenuStyle="{ width: '12rem' }"
          :showFilterMatchModes="false"
          :headerStyle="{ backgroundColor: '#a4c3b2' }"
        >
          <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" placeholder="Search by Event" />
          </template>
        </Column>
        <Column 
          field="date" 
          header="Date" 
          :headerStyle="{ backgroundColor: '#d3e0ea' }"
          :showFilterMatchModes="false"
        >
          <template #body="{ data }">
            {{ formatDate(data.date) }}
          </template>
        </Column>
      </DataTable>
    </div>
  </template>
  
  <script setup>
  import { ref, watch, defineEmits, onMounted } from 'vue';
  import { FilterMatchMode } from 'primevue/api';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import Button from 'primevue/button';
  import InputText from 'primevue/inputtext';
  
  const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    plant: { value: null, matchMode: FilterMatchMode.CONTAINS },
    event: { value: null, matchMode: FilterMatchMode.CONTAINS },
  });
  
  const events = ref([
    { plant: 'Plant1', event: 'Event1', date: '2024-07-01' },
    { plant: 'Plant2', event: 'Event2', date: '2024-07-02' },
    // ここに他の行データを追加できます
  ]);
  
  const filteredEvents = ref([...events.value]);
  
  const emit = defineEmits(['update-timeline']);
  
  const initFilters = () => {
    filters.value = {
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
      plant: { value: null, matchMode: FilterMatchMode.CONTAINS },
      event: { value: null, matchMode: FilterMatchMode.CONTAINS },
    };
  };
  
  const clearFilter = () => {
    console.log("Clear filter");
    initFilters();
    filteredEvents.value = [...events.value];
    emit('update-timeline', JSON.parse(JSON.stringify(filteredEvents.value)));  // Proxyから純粋なオブジェクトに変換
  };
  
  const formatDate = (value) => {
    if (!value) return '';
    const date = new Date(value);
    return date.toLocaleDateString('en-CA'); // Format as YYYY-MM-DD
  };
  
  const onFilter = (event) => {
    console.log("Filter event:", event);
    filteredEvents.value = event.filteredValue || [];
    console.log("Filtered events:", filteredEvents.value);
    emit('update-timeline', JSON.parse(JSON.stringify(filteredEvents.value)));  // Proxyから純粋なオブジェクトに変換
  };
  
  watch(filteredEvents, (newVal) => {
    console.log("Filtered events updated:", newVal);
    emit('update-timeline', JSON.parse(JSON.stringify(newVal)));  // Proxyから純粋なオブジェクトに変換
  });
  
  onMounted(() => {
    console.log("Initial load, emitting all events");
    emit('update-timeline', JSON.parse(JSON.stringify(filteredEvents.value)));  // Proxyから純粋なオブジェクトに変換
  });
  </script>
  
  <style scoped>
  .p-datatable .p-datatable-thead > tr > th {
    background-color: #d3e0ea !important; /* ヘッダーの背景色を統一 */
  }
  </style>
  