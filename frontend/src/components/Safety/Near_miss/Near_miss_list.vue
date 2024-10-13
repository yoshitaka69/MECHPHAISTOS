<template>
    <div class="table-container">
        <div class="header-container">
            <DataTable
                v-model:filters="filters"
                :value="sortedItems"
                :loading="loading"
                paginator
                showGridlines
                :rows="serverOptions.rowsPerPage"
                :total-records="serverItemsLength"
                :lazy="true"
                :resizable-columns="true"
                :global-filter-fields="['nearMissNo', 'userName.userName', 'department', 'description']"
                filter-display="menu"
                @page="onPage"
                @sort="onSort"
                @filter="onFilter"
                :rows-per-page-options="[5, 10, 20, 50]"
                class="p-datatable-custom custom-near-miss-table"
                :sort-field="sortField"
                :sort-order="sortOrder"
                style="width: 100%"
            >
                <!-- ヘッダーとカラム定義 -->
                <template #header>
                    <div class="flex justify-between items-center">
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                        </span>
                        <Button type="button" label="New Entry" @click="openNewEntry" />
                    </div>
                </template>
                <!-- カラム定義 -->
                <Column field="nearMissNo" header="NearMiss No." sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by NearMiss No." />
                    </template>
                </Column>
                <Column field="userName.userName" header="Name" sortable filter filterMatchMode="contains">
                    <template #body="slotProps">
                        {{ slotProps.data.userName.userName }}
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Name" />
                    </template>
                </Column>
                <Column field="department" header="Department" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Department" />
                    </template>
                </Column>
                <Column field="dateOfOccurrence" header="Date" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <Calendar v-model="filterModel.value" dateFormat="yy-mm-dd" placeholder="Select a Date" />
                    </template>
                </Column>
                <Column field="placeOfOccurrence" header="Where?" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Place of Occurrence" />
                    </template>
                </Column>
                <Column field="typeOfAccident" header="Type of Accident" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Type of Accident" />
                    </template>
                </Column>
                <Column field="description" header="Description" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Description" />
                    </template>
                </Column>
                <Column field="factor" header="Factor" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Factor" />
                    </template>
                </Column>
                <Column field="injuredLv" header="Injured Lv." sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Injured Lv." />
                    </template>
                </Column>
                <Column field="equipmentDamageLv" header="Equipment Damage Lv." sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Equipment Damage Lv." />
                    </template>
                </Column>
                <Column field="affectOfEnviroment" header="Effect on Environment" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Effect on Environment" />
                    </template>
                </Column>
                <Column field="newsCoverage" header="News Coverage" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by News Coverage" />
                    </template>
                </Column>
                <Column field="measures" header="Measures">
                    <template #body="slotProps">
                        <Tag :value="slotProps.data.measures" :class="getMeasuresClass(slotProps.data.measures)" class="wide-tag" />
                    </template>
                </Column>
                <Column field="actionItems" header="Action Items" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Action Items" />
                    </template>
                </Column>
                <Column field="solvedActionItems" header="Solved Action Items">
                    <template #body="slotProps">
                        <input type="checkbox" :checked="slotProps.data.solvedActionItems" readonly />
                    </template>
                </Column>
                <Column field="updateDay" header="Update Day" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Update Day" />
                    </template>
                </Column>
                <Column header="Operation">
                    <template #body="slotProps">
                        <div>
                            <i class="pi pi-pencil" @click="editItem(slotProps.data)" style="margin-right: 10px; cursor: pointer"></i>
                            <i class="pi pi-trash" @click="confirmDelete(slotProps.data)" style="cursor: pointer"></i>
                        </div>
                    </template>
                </Column>
            </DataTable>

            <!-- 削除確認モーダル -->
            <Dialog header="Delete Confirmation" v-model:visible="showDeleteDialog" :modal="true" :closable="false">
                <p>Are you sure you want to delete this item?</p>
                <div class="flex justify-content-end">
                    <Button label="No" icon="pi pi-times" @click="showDeleteDialog = false" class="p-button-text" />
                    <Button label="Yes" icon="pi pi-check" @click="deleteItemConfirmed" class="p-button-danger" />
                </div>
            </Dialog>
        </div>

        <div class="edit-item" v-if="isEditing">
            <h3>Edit Near Miss Entry</h3>
            <form @submit.prevent="submitEdit">
                <label>
                    NearMiss No:
                    <input type="text" v-model="editingItem.nearMissNo" readonly />
                </label>
                <label>
                    Name:
                    <input type="text" v-model="editingItem.userName.userName" />
                </label>
                <label>
                    Department:
                    <input type="text" v-model="editingItem.department" />
                </label>
                <label>
                    Date of Occurrence:
                    <input type="date" v-model="editingItem.dateOfOccurrence" />
                </label>
                <label>
                    Measures:
                    <input type="text" v-model="editingItem.measures" />
                </label>
                <button type="submit">Save</button>
                <button type="button" @click="cancelEdit">Cancel</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Pinia storeのインポート
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Checkbox from 'primevue/checkbox';
import Dropdown from 'primevue/dropdown';
import Calendar from 'primevue/calendar';
import Tag from 'primevue/tag';
import Dialog from 'primevue/dialog';


const itemsFromApi = ref([]);
const serverItemsLength = ref(0);
const serverOptions = ref({
    page: 1,
    rowsPerPage: 10
});
const loading = ref(false);
const isEditing = ref(false); // 編集モードかどうか
const editingItem = ref({}); // 編集対象のデータ
const sortField = ref(null);
const sortOrder = ref(null);
const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    nearMissNo: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    'userName.userName': { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    department: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    description: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }] },
    solvedActionItems: { value: null, matchMode: FilterMatchMode.EQUALS }
});

const getMeasuresClass = (measures) => {
    switch (measures) {
        case 'A':
            return 'measures-a'; // 一番危険
        case 'B':
            return 'measures-b';
        case 'C':
            return 'measures-c';
        case 'D':
            return 'measures-d';
        case 'E':
            return 'measures-e'; // 一番安全
        default:
            return '';
    }
};

// 削除対象とモーダルの状態を管理
const showDeleteDialog = ref(false);
const itemToDelete = ref(null);

const confirmDelete = (item) => {
    itemToDelete.value = item;
    showDeleteDialog.value = true;
};


// 編集モードで既存エントリをロードしてフォームを開く関数
const editItem = (item) => {
    isEditing.value = true; // 編集モードをオン
    Object.assign(editingItem.value, item); // クリックしたデータをセット
    localStorage.setItem('editingItem', JSON.stringify(editingItem.value)); // データを保存
    
    // フォームを開くためのロジック（例: 新しいタブ、モーダルなど）
    window.open('/near_miss_input_form', '_blank');
};



const deleteItemConfirmed = async () => {
    if (itemToDelete.value) {
        try {
            const deleteUrl = `http://127.0.0.1:8000/api/nearMiss/delete/?companyCode=${companyCode}&nearMissNo=${itemToDelete.value.nearMissNo}`;
            await axios.delete(deleteUrl);
            itemsFromApi.value = itemsFromApi.value.filter((i) => i.nearMissNo !== itemToDelete.value.nearMissNo); // ローカルで削除
            showDeleteDialog.value = false;
            itemToDelete.value = null;
            console.log('Item deleted successfully');
        } catch (error) {
            console.error('Failed to delete item:', error);
        }
    }
};

const userStore = useUserStore(); // Pinia storeの使用
const companyCode = userStore.companyCode; // companyCodeの取得

const fetchData = async () => {
    loading.value = true;
    console.log('Fetching data...');
    console.log(`API URL: http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?format=json&companyCode=${companyCode}&page=${serverOptions.value.page}&limit=${serverOptions.value.rowsPerPage}`);
    try {
        const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?format=json&companyCode=${companyCode}&page=${serverOptions.value.page}&limit=${serverOptions.value.rowsPerPage}`);
        console.log('API response:', response.data);

        // nearMissListを抽出
        const nearMissList = response.data.flatMap((company) => company.nearMissList);
        console.log('Extracted nearMissList:', nearMissList);

        if (nearMissList.length > 0) {
            itemsFromApi.value = nearMissList.map((item) => ({
                id: item.id,
                nearMissNo: item.nearMissNo,
                userName: { userName: item.userName.userName }, // userNameを正しく表示
                department: item.department,
                dateOfOccurrence: item.dateOfOccurrence,
                placeOfOccurrence: item.placeOfOccurrence,
                typeOfAccident: item.typeOfAccident,
                description: item.description,
                factor: item.factor,
                injuredLv: item.injuredLv,
                equipmentDamageLv: item.equipmentDamageLv,
                affectOfEnviroment: item.affectOfEnviroment,
                newsCoverage: item.newsCoverage,
                measures: item.measures,
                actionItems: item.actionItems,
                solvedActionItems: item.solvedActionItems,
                updateDay: item.updateDay,
                operation: item.operation
            }));
            serverItemsLength.value = nearMissList.length;
        } else {
            console.warn('API returned no data.');
            itemsFromApi.value = []; // データがない場合の処理
            serverItemsLength.value = 0;
        }
        console.log('Items from API:', itemsFromApi.value);
    } catch (error) {
        console.error('Error fetching data:', error);
    } finally {
        loading.value = false;
    }
};

onMounted(() => {
    // データのフェッチ処理
    fetchData(); // Near Miss リストをサーバーから取得

    // ローカルストレージから編集対象データを取得
    const editingItemData = localStorage.getItem('editingItem');
    if (editingItemData) {
        Object.assign(editingItem.value, JSON.parse(editingItemData)); // 編集アイテムのデータをセット
        console.log('Editing item loaded from localStorage:', editingItem.value);
    }
});

const sortedItems = computed(() => {
    let items = [...itemsFromApi.value];
    if (sortField.value) {
        items.sort((a, b) => {
            let result = 0;
            if (a[sortField.value] < b[sortField.value]) result = -1;
            else if (a[sortField.value] > b[sortField.value]) result = 1;
            return sortOrder.value === 1 ? result : -result;
        });
    }
    // 空の行を追加する処理
    while (items.length < serverOptions.value.rowsPerPage) {
        items.push({
            id: '',
            nearMissNo: '',
            userName: { userName: '' },
            department: '',
            dateOfOccurrence: '',
            placeOfOccurrence: '',
            typeOfAccident: '',
            description: '',
            factor: '',
            injuredLv: '',
            equipmentDamageLv: '',
            affectOfEnviroment: '',
            newsCoverage: '',
            measures: '',
            actionItems: '',
            solvedActionItems: false,
            updateDay: '',
            operation: ''
        });
    }
    return items;
});

const onSort = (event) => {
    sortField.value = event.sortField;
    sortOrder.value = event.sortOrder;
};

const onFilter = (event) => {
    filters.value = event.filters;
};

const submitEdit = async () => {
    try {
        await axios.put(`http://127.0.0.1:8000/api/nearMiss/${editingItem.value.nearMissNo}/`, editingItem.value);
        // 成功した場合にフロントエンドのデータを更新
        const index = itemsFromApi.value.findIndex((item) => item.nearMissNo === editingItem.value.nearMissNo);
        if (index !== -1) {
            itemsFromApi.value[index] = { ...editingItem.value };
        }
        isEditing.value = false; // 編集モードを終了
    } catch (error) {
        console.error('Failed to update item:', error);
    }
};


const cancelEdit = () => {
    isEditing.value = false;
    console.log('Edit cancelled');
};



const deleteItem = async (item) => {
    console.log('Deleting item:', item);
    const deleteUrl = `http://127.0.0.1:8000/api/nearMiss/${item.id}/`;
    console.log(`Delete URL: ${deleteUrl}`);
    try {
        await axios.delete(deleteUrl);
        itemsFromApi.value = itemsFromApi.value.filter((i) => i.id !== item.id);
        console.log('Item deleted successfully');
    } catch (error) {
        console.error('Failed to delete item:', error);
    }
};


// 新規エントリ作成用のフォームを開く関数
const openNewEntry = () => {
    isEditing.value = false; // 編集モードを解除（新規モード）
    editingItem.value = {
        nearMissNo: '',
        userName: { userName: '' },
        department: '',
        dateOfOccurrence: '',
        placeOfOccurrence: '',
        typeOfAccident: '',
        description: '',
        factor: '',
        injuredLv: '',
        equipmentDamageLv: '',
        affectOfEnviroment: '',
        newsCoverage: '',
        measures: '',
        actionItems: '',
        solvedActionItems: false,
        updateDay: ''
    };
    
    // フォームを開くためのロジック（例: 新しいタブ、モーダルなど）
    window.open('/near_miss_input_form', '_blank');
};


const onPage = (event) => {
    serverOptions.value.page = event.page + 1;
    serverOptions.value.rowsPerPage = event.rows;
    fetchData();
};

const clearFilter = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        nearMissNo: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
        'userName.userName': { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
        department: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
        description: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }] },
        solvedActionItems: { value: null, matchMode: FilterMatchMode.EQUALS }
    };
};
</script>

<style>
.table-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.header-container {
    flex: 0 1 auto;
    width: 100%;
}

.p-datatable-custom .p-datatable-thead > tr > th {
    background-color: #ffdab9; /* 薄いオレンジ色 */
    color: black; /* テキストの色を黒に設定 */
}

/* CSSで交互に背景色を設定 */
.custom-near-miss-table .p-datatable-tbody > tr:nth-child(odd) {
    background-color: #ffffff !important; /* 白色 */
}

.custom-near-miss-table .p-datatable-tbody > tr:nth-child(even) {
    background-color: #d3d3d3 !important; /* 薄い灰色 */
}

.p-input-icon-left .pi {
    left: 10px;
}

/* テーブルの本文の文字を太字にする */
.custom-near-miss-table .p-datatable-tbody > tr > td {
    font-weight: bold;
}

/* テーブルのヘッダーの文字を太字にする */
.p-datatable-thead > tr > th {
    font-weight: bold;
}

/* 特定のカラムに対して、ヘッダーのテキストを2行にするスタイル */
.p-datatable-thead th {
    white-space: normal; /* テキストを折り返し */
    text-align: center; /* テキストを中央揃え（オプション） */
}

/* Injured Lv, Equipment Damage Lv, Effect on Environmentのカラムに対応する */
.p-datatable-thead th[aria-label='Injured Lv.'] {
    white-space: normal;
}

.p-datatable-thead th[aria-label='Equipment Damage Lv.'] {
    white-space: normal;
}

.p-datatable-thead th[aria-label='Effect on Environment'] {
    white-space: normal;
}

.measures-a {
    background-color: red;
    color: black; /* 文字の色を黒に統一 */
    font-weight: bold !important; /* フォントを太字に強制 */
    font-size: 16px !important; /* フォントサイズを一回り大きく設定 */
    font-family: 'Arial', sans-serif; /* 任意のフォントを指定 */
}

.measures-b {
    background-color: orange;
    color: black; /* 文字の色を黒に統一 */
    font-weight: bold !important; /* フォントを太字に強制 */
    font-size: 16px !important; /* フォントサイズを一回り大きく設定 */
    font-family: 'Arial', sans-serif; /* 任意のフォントを指定 */
}

.measures-c {
    background-color: yellow;
    color: black; /* 文字の色を黒に統一 */
    font-weight: bold !important; /* フォントを太字に強制 */
    font-size: 16px !important; /* フォントサイズを一回り大きく設定 */
    font-family: 'Arial', sans-serif; /* 任意のフォントを指定 */
}

.measures-d {
    background-color: lightgreen;
    color: black; /* 文字の色を黒に統一 */
    font-weight: bold !important; /* フォントを太字に強制 */
    font-size: 16px !important; /* フォントサイズを一回り大きく設定 */
    font-family: 'Arial', sans-serif; /* 任意のフォントを指定 */
}

.measures-e {
    background-color: green;
    color: black; /* 文字の色を黒に統一 */
    font-weight: bold !important; /* フォントを太字に強制 */
    font-size: 16px !important; /* フォントサイズを一回り大きく設定 */
    font-family: 'Arial', sans-serif; /* 任意のフォントを指定 */
}

/* 横長のスタイルを適用し、文字の色を黒に変更 */
.wide-tag {
    display: inline-block;
    padding: 0.5rem 2rem;
    min-width: 120px;
    text-align: center;
    border-radius: 10px;
    color: black;
    font-weight: bold !important; /* 太字を強制 */
    font-size: 16px !important; /* フォントサイズを一回り大きく設定 */
    font-family: 'Arial', sans-serif; /* 任意のフォントを指定 */
}


</style>
