<template>
    <div class="table-container custom-work-order-table-v2">
        <p class="description-text">
            This is the Work Order page. Here, you can issue work orders for maintenance tasks such as repair requests, modification work, and inspections. <br>The more detailed you fill out the work order form, the more accurate the equipment
            information and equipment lifespan data will be.
        </p>
        <div class="header-container-v2">
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
                :global-filter-fields="['workOrderNo', 'registrationDate', 'plant', 'equipment', 'workOrderDesc', 'status', 'title', 'failureTypes', 'failureModes', 'failureDescription', 'failureDate', 'description']"
                filter-display="menu"
                @page="onPage"
                @sort="onSort"
                @filter="onFilter"
                :rows-per-page-options="[5, 10, 20, 50]"
                class="p-datatable-custom custom-work-order-table-v2"
                :sort-field="sortField"
                :sort-order="sortOrder"
                style="width: 100%"
            >
                <template #header>
                    <div class="header-content">
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                        </span>
                        <Button type="button" label="New Work Order" @click="showNewEntryForm" class="new-work-order-button" />
                    </div>
                </template>
                <Column field="workOrderNo" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center">Work Order<br />No</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Work Order No" />
                    </template>
                </Column>

                <Column field="registrationDate" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center">Registration<br />Date</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Registration Date" />
                    </template>
                </Column>
                <Column field="plant" header="Plant" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Plant" />
                    </template>
                </Column>
                <Column field="equipment" header="Equipment" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Equipment" />
                    </template>
                </Column>
                <Column field="workOrderDesc" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center">Work Order<br />Description</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Work Order Description" />
                    </template>
                </Column>
                <Column field="status" header="Status" sortable filter filterMatchMode="contains">
                    <template #body="slotProps">
                        <Tag :value="slotProps.data.status" :severity="getStatusLabel(slotProps.data.status)" />
                    </template>
                    <template #filter="{ filterModel }">
                        <Dropdown v-model="filterModel.value" :options="statuses" optionLabel="label" optionValue="value" placeholder="Select a Status" />
                    </template>
                </Column>
                <Column field="title" header="Title" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Title" />
                    </template>
                </Column>
                <Column field="failureTypes" header="Failure Types" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Failure Types" />
                    </template>
                </Column>
                <Column field="failureModes" header="Failure Modes" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Failure Modes" />
                    </template>
                </Column>
                <Column field="failureDescription" header="Failure Description" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Failure Description" />
                    </template>
                </Column>
                <Column field="failureDate" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center">Failure<br />Date</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Failure Date" />
                    </template>
                </Column>
                <Column field="description" header="Description" sortable filter filterMatchMode="contains">
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Description" />
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
        <Dialog v-model:visible="isDeleteModalVisible" modal>
            <template #header>削除確認</template>
            <div>
                本当に {{ currentEntry?.workOrderNo }} を削除しますか？
            </div>
            <template #footer>
                <Button label="いいえ" @click="isDeleteModalVisible = false" />
                <Button label="はい" @click="deleteItem" class="p-button-danger" />
            </template>
        </Dialog>
        </div>
        <WorkOrderForm v-if="isModalVisible && currentEntry" v-model:visible="isModalVisible" :statuses="statuses" :entry="currentEntry" @submit="onSubmit" @cancel="onCancel" />
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Tag from 'primevue/tag';
import Dropdown from 'primevue/dropdown';
import WorkOrderForm from '@/components/Work_order/Work_order_form.vue'; // 修正: WorkOrderFormをインポート

const userStore = useUserStore(); // Piniaストアを使用

const products = ref([]);
const editingRows = ref([]);
const statuses = ref([
    { label: 'Completed', value: 'COMPLETED' },
    { label: 'Ongoing', value: 'Ongoing' },
    { label: 'Delayed', value: 'Delayed' }
]);

const currentEntry = ref(null); // 編集するエントリー
const isModalVisible = ref(false); // モーダル表示の状態
const isDeleteModalVisible = ref(false); // 削除確認モーダルの表示状態を管理するフラグ
const isAddingNew = ref(false);
const isEditing = ref(false);
const newEntry = ref({
    workOrderNo: '',
    plant: '',
    equipment: '',
    workOrderDesc: '',
    status: '',
    title: '',
    failureTypes: [],
    failureModes: [],
    failureDescription: '',
    failureDate: null,
    description: '',
    registrationDate: null // 登録日を追加
});
const editingItem = ref({});

onMounted(async () => {
    const response = await axios.get(`http://127.0.0.1:8000/api/workOrder/workOrderByCompany/?format=json&companyCode=${userStore.companyCode}`);
    const flattenedData = response.data.flatMap((company) => company.workOrderList);
    products.value = flattenedData; // データをproductsにセット
});


const serverItemsLength = computed(() => products.value.length);
const serverOptions = ref({
    page: 1,
    rowsPerPage: 30
});
const loading = ref(false);
const sortField = ref(null);
const sortOrder = ref(null);
const filters = ref({
    global: { value: null, matchMode: 'contains' },
    workOrderNo: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    registrationDate: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] }, // 登録日フィルターを追加
    plant: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    equipment: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    workOrderDesc: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    status: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    title: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    failureTypes: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    failureModes: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    failureDescription: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    failureDate: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    description: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] }
});

const sortedItems = computed(() => {
    let items = [...products.value];
    if (sortField.value) {
        items.sort((a, b) => {
            let result = 0;
            if (a[sortField.value] < b[sortField.value]) result = -1;
            else if (a[sortField.value] > b[sortField.value]) result = 1;
            return sortOrder.value === 1 ? result : -result;
        });
    }
    while (items.length < serverOptions.value.rowsPerPage) {
        items.push({
            id: '',
            workOrderNo: '',
            registrationDate: null, // 登録日を追加
            plant: '',
            equipment: '',
            workOrderDesc: '',
            status: '',
            title: '',
            failureTypes: [],
            failureModes: [],
            failureDescription: '',
            failureDate: null,
            description: ''
        });
    }
    return items;
});


// 削除確認モーダルを表示
const confirmDelete = (item) => {
    currentEntry.value = { ...item }; // 削除するエントリーをセット
    isDeleteModalVisible.value = true; // 削除確認モーダルを表示
};

// データ削除処理
const deleteItem = async () => {
    try {
        await axios.delete(`http://127.0.0.1:8000/api/workOrder/workOrder/${currentEntry.value.id}/`);
        products.value = products.value.filter(item => item.id !== currentEntry.value.id); // リストから削除
        isDeleteModalVisible.value = false; // モーダルを閉じる
        currentEntry.value = null; // currentEntryをリセット
        console.log('Deleted item successfully');
    } catch (error) {
        console.error('Error deleting item:', error);
    }
};


const onSort = (event) => {
    sortField.value = event.sortField;
    sortOrder.value = event.sortOrder;
};

const onFilter = (event) => {
    filters.value = event.filters;
};

// 編集アイテムを設定し、モーダルを開く
const editItem = (item) => {
    const existingEntry = products.value.find((i) => i.workOrderNo === item.workOrderNo); // workOrderNoで既存データを検索
    if (existingEntry) {
        currentEntry.value = { ...existingEntry }; // 編集するエントリーをセット
        isEditing.value = true; // 編集フラグをセット
        isModalVisible.value = true; // モーダルを表示
        console.log('Editing existing item:', currentEntry.value);
    } else {
        console.error('Work Order No not found:', item.workOrderNo);
    }
};



const onSubmit = (entry) => {
    if (isEditing.value) {
        const item = products.value.find((i) => i.id === entry.id);
        if (item) {
            Object.assign(item, entry);
        }
        isEditing.value = false;
    } else {
        products.value.push({ ...entry, id: products.value.length + 1 });
        isAddingNew.value = false;
    }
    isModalVisible.value = false; // モーダルを閉じる
};

const onCancel = () => {
    isModalVisible.value = false; // モーダルを閉じる
};



const showNewEntryForm = () => {
    isAddingNew.value = true;
    currentEntry.value = {
        workOrderNo: '',
        registrationDate: null, // 登録日を初期化
        plant: '',
        equipment: '',
        workOrderDesc: '',
        status: '',
        title: '',
        failureTypes: [],
        failureModes: [],
        failureDescription: '',
        failureDate: null,
        description: ''
    };
    isModalVisible.value = true; // 新規エントリ用のモーダルを表示
};

const onPage = (event) => {
    serverOptions.value.page = event.page + 1;
    serverOptions.value.rowsPerPage = event.rows;
};

const clearFilter = () => {
    filters.value = {
        global: { value: null, matchMode: 'contains' },
        workOrderNo: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        registrationDate: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] }, // 登録日フィルターを追加
        plant: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        equipment: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        workOrderDesc: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        status: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        title: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        failureTypes: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        failureModes: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        failureDescription: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        failureDate: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        description: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] }
    };
};

const rowClass = (data, index) => {
    return index % 2 === 0 ? 'even-row' : 'odd-row';
};

const getStatusLabel = (status) => {
    switch (status) {
        case 'COMPLETED':
            return 'success';

        case 'Ongoing':
            return 'warning';

        case 'Delayed':
            return 'danger';

        default:
            return null;
    }
};

const onRowEditSave = (event) => {
    let { newData, index } = event;
    products.value[index] = newData;
};
</script>

<style>
.description-text {
    font-size: 16px;
    line-height: 1.5;
    margin-bottom: 20px;
    color: #333;
}

.table-container.custom-work-order-table-v2 .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px; /* リストとボタンの間に隙間を追加 */
}

.table-container.custom-work-order-table-v2 .new-work-order-button {
    margin-left: auto; /* ボタンを右上に配置 */
}

.table-container.custom-work-order-table-v2 .p-datatable-thead > tr > th {
    background-color: #b2d8b2 !important; /* ヘッダーの色を薄い緑色に変更 */
    color: black !important; /* ヘッダーの文字色を黒に変更 */
}

.table-container.custom-work-order-table-v2 .p-datatable {
    border: none; /* 黒い枠線を削除 */
}

.table-container.custom-work-order-table-v2 .p-datatable-tbody > tr:nth-child(odd) > td {
    background-color: #ffffff !important; /* 奇数行は白色 */
}

.table-container.custom-work-order-table-v2 .p-datatable-tbody > tr:nth-child(even) > td {
    background-color: #d3d3d3 !important; /* 偶数行は明るい灰色 */
}

.table-container.custom-work-order-table-v2 .p-datatable-tbody > tr > td {
    border-right: none;
}

.table-container.custom-work-order-table-v2 .p-datatable-thead > tr > th {
    border-right: none;
}
</style>
