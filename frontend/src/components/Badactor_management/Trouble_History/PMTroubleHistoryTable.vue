<template>
  <div class="unique-trouble-datatable-container-v2">
    <DataTable 
      v-model:filters="filters" 
      :value="filteredTroubles" 
      paginator 
      :rows="10" 
      dataKey="date"
      filterDisplay="menu"
      :globalFilterFields="['pmType']"
      @filter="onFilter"
      class="unique-trouble-datatable-v2"
    >
      <template #header>
        <div class="flex justify-between unique-header-v2">
          <Button type="button" icon="pi pi-filter-slash" label="Clear" outlined @click="clearFilter()" />
          <div class="unique-search-container-v2">
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
      <Column 
        field="failureContent" 
        header="Description" 
        sortable 
        :headerStyle="{ backgroundColor: '#d3e0ea' }"
      />
      <Column 
        field="failureType" 
        header="Failure Type" 
        sortable 
        :headerStyle="{ backgroundColor: '#d3e0ea' }"
      />
      <Column 
        field="rootCause" 
        header="Failure Causes" 
        sortable 
        :headerStyle="{ backgroundColor: '#d3e0ea' }"
      />
      <Column 
        field="repairMethod" 
        header="Repairing Type" 
        sortable 
        :headerStyle="{ backgroundColor: '#d3e0ea' }"
      />
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
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Pinia store

const pmTypeOptions = [
  { label: 'PM03', value: 'PM03' },
  { label: 'PM04', value: 'PM04' }
];

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  pmType: { value: null, matchMode: FilterMatchMode.EQUALS },
});

const troubles = ref([]);

const filteredTroubles = ref([...troubles.value]);

const emit = defineEmits(['update-timeline']);

const userStore = useUserStore();
const companyCode = userStore.companyCode;

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

const fetchTroubles = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/reliability/troubleHistoryByCompany/', {
      params: { companyCode }
    });
    console.log("API response data:", response.data);
    const data = response.data.find(item => item.companyCode === companyCode);
    troubles.value = data ? data.troubleHistory : [];
    filteredTroubles.value = [...troubles.value];
    emit('update-timeline', JSON.parse(JSON.stringify(filteredTroubles.value)));  // Proxyから純粋なオブジェクトに変換
  } catch (error) {
    console.error('Error fetching troubles:', error);
  }
};

watch(filteredTroubles, (newVal) => {
  console.log("Filtered troubles updated:", newVal);
  emit('update-timeline', JSON.parse(JSON.stringify(newVal)));  // Proxyから純粋なオブジェクトに変換
});

onMounted(() => {
  console.log("Initial load, fetching troubles");
  fetchTroubles();
});
</script>

<style scoped>
/* データテーブル全体のコンテナ */
.unique-trouble-datatable-container-v2 {
  margin: 20px; /* コンテナにマージンを追加 */
  padding: 10px;
  border: 1px solid #ccc; /* 全体の境界線を追加 */
  border-radius: 8px; /* 角を少し丸くする */
  background-color: #f5f5f5; /* 背景色を柔らかく */
}

/* テーブルのヘッダー部分 */
.unique-header-v2 {
  padding-bottom: 10px;
  margin-bottom: 10px;
  border-bottom: 1px solid #ddd; /* ヘッダーとコンテンツを分ける境界線 */
}

/* サーチボックスのコンテナ */
.unique-search-container-v2 {
  display: flex;
  align-items: center;
}

.unique-search-container-v2 i {
  margin-right: 5px;
}

/* テーブル全体のデザイン */
.unique-trouble-datatable-v2 .p-datatable-thead > tr > th {
  background-color: #d3e0ea !important; /* ヘッダーの背景色を統一 */
  font-weight: bold; /* ヘッダーのテキストを太字に */
  text-align: center; /* ヘッダーのテキストを中央揃え */
  padding: 12px; /* 余白を広げる */
}

/* 各列のセルのデザイン */
.unique-trouble-datatable-v2 .p-datatable-tbody > tr > td {
  padding: 10px; /* 各セルの余白を調整 */
  text-align: center; /* テキストを中央揃え */
}

/* 奇数行と偶数行の色分け */
.unique-trouble-datatable-v2 .p-datatable-tbody > tr:nth-child(odd) {
  background-color: #f9f9f9; /* 奇数行の背景色 */
}

.unique-trouble-datatable-v2 .p-datatable-tbody > tr:nth-child(even) {
  background-color: #ffffff; /* 偶数行の背景色 */
}

/* テーブルに境界線を追加 */
.unique-trouble-datatable-v2 .p-datatable-tbody > tr > td,
.unique-trouble-datatable-v2 .p-datatable-thead > tr > th {
  border: 1px solid #ddd; /* 各セルに境界線 */
}

/* ボタンのカスタマイズ */
.unique-trouble-datatable-container-v2 .p-button {
  background-color: #007bff;
  color: white;
  border-radius: 4px;
}

.unique-trouble-datatable-container-v2 .p-button:hover {
  background-color: #0056b3;
}

</style>
