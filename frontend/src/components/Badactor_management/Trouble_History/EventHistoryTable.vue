<template>
    <div class="unique-datatable-container-v2">
        <DataTable v-model:filters="filters" :value="filteredEvents" paginator :rows="10" dataKey="date" filterDisplay="menu" :globalFilterFields="['plant', 'event']" @filter="onFilter" class="unique-datatable-v2">
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
            <Column field="plant" header="Plant" sortable filter :filterMenuStyle="{ width: '12rem' }" :showFilterMatchModes="false" :headerStyle="{ backgroundColor: '#a4c3b2' }">
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" placeholder="Search by Plant" />
                </template>
            </Column>
            <Column field="event" header="Event" sortable filter :filterMenuStyle="{ width: '12rem' }" :showFilterMatchModes="false" :headerStyle="{ backgroundColor: '#a4c3b2' }">
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" placeholder="Search by Event" />
                </template>
            </Column>
            <Column field="date" header="Date" :headerStyle="{ backgroundColor: '#d3e0ea' }" :showFilterMatchModes="false">
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
    event: { value: null, matchMode: FilterMatchMode.CONTAINS }
});

const events = ref([
    { plant: 'Plant1', event: 'Event1', date: '2024-07-01' },
    { plant: 'Plant2', event: 'Event2', date: '2024-07-02' }
    // ここに他の行データを追加できます
]);

const filteredEvents = ref([...events.value]);

const emit = defineEmits(['update-timeline']);

const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        plant: { value: null, matchMode: FilterMatchMode.CONTAINS },
        event: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};

const clearFilter = () => {
    console.log('Clear filter');
    initFilters();
    filteredEvents.value = [...events.value];
    emit('update-timeline', JSON.parse(JSON.stringify(filteredEvents.value))); // Proxyから純粋なオブジェクトに変換
};

const formatDate = (value) => {
    if (!value) return '';
    const date = new Date(value);
    return date.toLocaleDateString('en-CA'); // Format as YYYY-MM-DD
};

const onFilter = (event) => {
    console.log('Filter event:', event);
    filteredEvents.value = event.filteredValue || [];
    console.log('Filtered events:', filteredEvents.value);
    emit('update-timeline', JSON.parse(JSON.stringify(filteredEvents.value))); // Proxyから純粋なオブジェクトに変換
};

watch(filteredEvents, (newVal) => {
    console.log('Filtered events updated:', newVal);
    emit('update-timeline', JSON.parse(JSON.stringify(newVal))); // Proxyから純粋なオブジェクトに変換
});

onMounted(() => {
    console.log('Initial load, emitting all events');
    emit('update-timeline', JSON.parse(JSON.stringify(filteredEvents.value))); // Proxyから純粋なオブジェクトに変換
});
</script>

<style scoped>
/* データテーブル全体のコンテナ */
.unique-datatable-container-v2 {
    margin: 20px; /* コンテナにマージンを追加 */
    padding: 10px;
    border: 1px solid #ccc; /* 全体の境界線を追加 */
    border-radius: 8px; /* 角を少し丸くする */
    background-color: #f5f5f5; /* 背景色を少し柔らかく */
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
.unique-datatable-v2 .p-datatable-thead > tr > th {
    background-color: #d3e0ea !important; /* ヘッダーの背景色を統一 */
    font-weight: bold; /* ヘッダーのテキストを太字に */
    text-align: center; /* ヘッダーのテキストを中央揃え */
    padding: 12px; /* 余白を広げる */
}

/* 各列のセルのデザイン */
.unique-datatable-v2 .p-datatable-tbody > tr > td {
    padding: 10px; /* 各セルの余白を調整 */
    text-align: center; /* テキストを中央揃え */
}

/* 奇数行と偶数行の色分け */
.unique-datatable-v2 .p-datatable-tbody > tr:nth-child(odd) {
    background-color: #f9f9f9; /* 奇数行の背景色 */
}

.unique-datatable-v2 .p-datatable-tbody > tr:nth-child(even) {
    background-color: #ffffff; /* 偶数行の背景色 */
}

/* テーブルに境界線を追加 */
.unique-datatable-v2 .p-datatable-tbody > tr > td,
.unique-datatable-v2 .p-datatable-thead > tr > th {
    border: 1px solid #ddd; /* 各セルに境界線 */
}

/* ボタンのカスタマイズ */
.unique-datatable-container-v2 .p-button {
    background-color: #007bff;
    color: white;
    border-radius: 4px;
}

.unique-datatable-container-v2 .p-button:hover {
    background-color: #0056b3;
}
</style>
