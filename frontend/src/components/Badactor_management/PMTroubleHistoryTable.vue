<template>
  <div>
    <DataTable 
      v-model:filters="filters" 
      :value="filteredTroubles" 
      paginator 
      :rows="10" 
      dataKey="date"
      filterDisplay="menu"
      :globalFilterFields="['pmType']"
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
import SelectButton from 'primevue/selectbutton';

const pmTypeOptions = [
  { label: 'PM03', value: 'PM03' },
  { label: 'PM04', value: 'PM04' }
];

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  pmType: { value: null, matchMode: FilterMatchMode.EQUALS },
});

const troubles = ref([
  { date: '2024-07-01', pmType: 'PM03', description: 'Description 1', failureType: 'Type 1', failureCauses: 'Cause 1', repairingType: 'Repair 1', tag: '#001' },
  { date: '2024-07-02', pmType: 'PM04', description: 'Description 2', failureType: 'Type 2', failureCauses: 'Cause 2', repairingType: 'Repair 2', tag: '#002' },
  // ここに他の行データを追加できます
]);

const filteredTroubles = ref([...troubles.value]);

const emit = defineEmits(['update-timeline']);

const initFilters = () => {
  filters.value = {
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    pmType: { value: null, matchMode: FilterMatchMode.EQUALS },
  };
};

const clearFilter = () => {
  console.log("Clear filter");
  initFilters();
  filteredTroubles.value = [...troubles.value];
  emit('update-timeline', JSON.parse(JSON.stringify(filteredTroubles.value)));  // Proxyから純粋なオブジェクトに変換
};

const formatDate = (value) => {
  if (!value) return '';
  const date = new Date(value);
  return date.toLocaleDateString('en-CA'); // Format as YYYY-MM-DD
};

const onFilter = (event) => {
  console.log("Filter event:", event);
  filteredTroubles.value = event.filteredValue || [];
  console.log("Filtered troubles:", filteredTroubles.value);
  emit('update-timeline', JSON.parse(JSON.stringify(filteredTroubles.value)));  // Proxyから純粋なオブジェクトに変換
};

watch(filteredTroubles, (newVal) => {
  console.log("Filtered troubles updated:", newVal);
  emit('update-timeline', JSON.parse(JSON.stringify(newVal)));  // Proxyから純粋なオブジェクトに変換
});

onMounted(() => {
  console.log("Initial load, emitting all troubles");
  emit('update-timeline', JSON.parse(JSON.stringify(filteredTroubles.value)));  // Proxyから純粋なオブジェクトに変換
});
</script>

<style scoped>
.p-datatable .p-datatable-thead > tr > th {
  background-color: #d3e0ea !important; /* ヘッダーの背景色を統一 */
}
</style>
