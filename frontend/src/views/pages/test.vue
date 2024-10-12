<template>
    <div class="table-container custom-work-order-table-v2">
        <p class="description-text">
            This is the Work Order page. Here, you can issue work orders for maintenance tasks such as repair requests, modification work, and inspections. <br />The more detailed you fill out the work order form, the more accurate the equipment
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
                <!-- Work Order No 列 -->
                <Column field="workOrderNo" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Work Order<br />No</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Work Order No" />
                    </template>
                </Column>

                <!-- Registration Date 列 -->
                <Column field="registrationDate" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Registration<br />Date</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Registration Date" />
                    </template>
                </Column>

                <!-- Plant 列 -->
                <Column field="plant" header="Plant" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Plant</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Plant" />
                    </template>
                </Column>

                <!-- Equipment 列 -->
                <Column field="equipment" header="Equipment" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Equipment</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Equipment" />
                    </template>
                </Column>

                <!-- Work Order Description 列 -->
                <Column field="workOrderDesc" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Work Order<br />Description</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Work Order Description" />
                    </template>
                </Column>

                <!-- Status 列 -->
                <Column field="status" header="Status" sortable filter filterMatchMode="contains">
                    <template #body="slotProps">
                        <Tag :value="slotProps.data.status" :class="getStatusLabel(slotProps.data.status)" />
                    </template>
                    <template #filter="{ filterModel }">
                        <Dropdown v-model="filterModel.value" :options="statuses" optionLabel="label" optionValue="value" placeholder="Select a Status" />
                    </template>
                </Column>

                <!-- Title 列 -->
                <Column field="title" header="Title" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Title</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Title" />
                    </template>
                </Column>

                <!-- Failure Types 列 -->
                <Column field="failureTypes" header="Failure Types" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Failure Types</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Failure Types" />
                    </template>
                </Column>

                <!-- Failure Modes 列 -->
                <Column field="failureModes" header="Failure Modes" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Failure Modes</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Failure Modes" />
                    </template>
                </Column>

                <!-- Failure Description 列 -->
                <Column field="failureDescription" header="Failure Description" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Failure Description</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Failure Description" />
                    </template>
                </Column>

                <!-- Failure Date 列 -->
                <Column field="failureDate" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Failure<br />Date</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Failure Date" />
                    </template>
                </Column>

                <!-- Remark 列 -->
                <Column field="remark" header="Remark" sortable filter filterMatchMode="contains">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Remark</div>
                    </template>
                    <template #filter="{ filterModel }">
                        <InputText v-model="filterModel.value" type="text" placeholder="Search by Remark" />
                    </template>
                </Column>

                <!-- Picture 1 列 -->
                <Column field="picture1" header="Picture 1">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Picture 1</div>
                    </template>
                    <template #body="slotProps">
                        <span v-if="slotProps.data.picture1">
                            <img :src="slotProps.data.picture1" class="thumbnail" alt="Picture 1" />
                        </span>
                        <span v-else>No picture</span>
                    </template>
                </Column>

                <!-- Picture 2 列 -->
                <Column field="picture2" header="Picture 2">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Picture 2</div>
                    </template>
                    <template #body="slotProps">
                        <span v-if="slotProps.data.picture2">
                            <img :src="slotProps.data.picture2" class="thumbnail" alt="Picture 2" />
                        </span>
                        <span v-else>No picture</span>
                    </template>
                </Column>

                <!-- Operation 列 -->
                <Column header="Operation">
                    <template #header>
                        <div style="text-align: center; font-weight: bold">Operation</div>
                    </template>
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
                <div>本当に {{ currentEntry?.workOrderNo }} を削除しますか？</div>
                <template #footer>
                    <Button label="いいえ" @click="isDeleteModalVisible = false" />
                    <Button label="はい" @click="deleteItem" class="p-button-danger" />
                </template>
            </Dialog>
        </div>
        <WorkOrderForm v-if="isModalVisible" :visible="isModalVisible" :entry="currentEntry" @submit="onSubmit" @cancel="onCancel" @update:visible="isModalVisible = $event" />
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
import WorkOrderForm from '@/components/Work_order/Work_order_form.vue'; // WorkOrderFormをインポート

const userStore = useUserStore(); // Piniaストアを使用
const products = ref([]); // サーバーから取得するWork Orderのリスト
const statuses = ref([
    { label: 'Completed', value: 'COMPLETED' },
    { label: 'Ongoing', value: 'Ongoing' },
    { label: 'Delayed', value: 'Delayed' }
]);

const currentEntry = ref(null); // 編集または削除するエントリー
const isModalVisible = ref(false); // モーダル表示の状態
const isDeleteModalVisible = ref(false); // 削除確認モーダルの表示状態
const isEditing = ref(false); // 編集中かどうかのフラグ
const serverItemsLength = computed(() => products.value.length); // サーバー上のアイテム数
const serverOptions = ref({ page: 1, rowsPerPage: 30 });
const loading = ref(false); // ローディング状態の管理
const sortField = ref(null); // ソート対象のフィールド
const sortOrder = ref(null); // ソート順序
const filters = ref({
    global: { value: null, matchMode: 'contains' },
    workOrderNo: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    registrationDate: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    plant: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    equipment: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    workOrderDesc: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    status: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    title: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    failureTypes: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    failureModes: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    failureDescription: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    failureDate: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    remark: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] }
});

onMounted(async () => {
    const response = await axios.get(`http://127.0.0.1:8000/api/workOrder/workOrderByCompany/?format=json&companyCode=${userStore.companyCode}`);
    const flattenedData = response.data.flatMap((company) => company.workOrderList);
    products.value = flattenedData; // データをproductsにセット
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
            registrationDate: null,
            plant: '',
            equipment: '',
            workOrderDesc: '',
            status: '',
            title: '',
            failureTypes: [],
            failureModes: [],
            failureDescription: '',
            failureDate: null,
            remark: '',
            picture1: null,
            picture2: null
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
        products.value = products.value.filter((item) => item.id !== currentEntry.value.id); // リストから削除
        isDeleteModalVisible.value = false; // モーダルを閉じる
        currentEntry.value = null; // currentEntryをリセット
        console.log('Deleted item successfully');
    } catch (error) {
        console.error('Error deleting item:', error);
    }
};

// ソート処理
const onSort = (event) => {
    sortField.value = event.sortField;
    sortOrder.value = event.sortOrder;
};

// フィルター処理
const onFilter = (event) => {
    filters.value = event.filters;
};

// 編集アイテムを設定し、モーダルを開く
const editItem = (item) => {
    const existingEntry = products.value.find((i) => i.workOrderNo === item.workOrderNo);
    if (existingEntry) {
        currentEntry.value = { ...existingEntry };
        isEditing.value = true;
        isModalVisible.value = true;
        console.log('Editing existing item:', currentEntry.value);
    } else {
        console.error('Work Order No not found:', item.workOrderNo);
    }
};

// 保存・更新処理
const onSubmit = (entry) => {
    if (isEditing.value) {
        const item = products.value.find((i) => i.id === entry.id);
        if (item) {
            Object.assign(item, entry); // エントリーを更新
        }
        isEditing.value = false;
    } else {
        products.value.push({ ...entry, id: products.value.length + 1 });
    }
    isModalVisible.value = false;
};

// モーダルを閉じる
const onCancel = () => {
    isModalVisible.value = false;
};

// 新規エントリーフォームを表示
const showNewEntryForm = () => {
    currentEntry.value = {
        workOrderNo: '',
        registrationDate: null,
        plant: '',
        equipment: '',
        workOrderDesc: '',
        status: '',
        title: '',
        failureTypes: [],
        failureModes: [],
        failureDescription: '',
        failureDate: null,
        remark: '',
        picture1: null,
        picture2: null
    };
    isModalVisible.value = true;
};

// ページ処理
const onPage = (event) => {
    serverOptions.value.page = event.page + 1;
    serverOptions.value.rowsPerPage = event.rows;
};

// フィルターをクリア
const clearFilter = () => {
    filters.value = {
        global: { value: null, matchMode: 'contains' },
        workOrderNo: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        registrationDate: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        plant: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        equipment: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        workOrderDesc: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        status: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        title: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        failureTypes: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        failureModes: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        failureDescription: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        failureDate: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
        remark: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] }
    };
};

const getStatusLabel = (status) => {
    switch (status) {
        case 'COMPLETED':
            return 'status-completed';
        case 'Ongoing':
            return 'status-ongoing';
        case 'Delayed':
            return 'status-delayed';
        default:
            return null;
    }
};
</script>

<style>
/* テーブル全体の文字を太字に設定 */
.table-container.custom-work-order-table-v2 {
    font-weight: bold; /* テーブル内の全ての文字を太字に */
}

/* Completed ステータスのスタイル */
.table-container.custom-work-order-table-v2 .status-completed {
    background-color: #39ff14 !important; /* 蛍光グリーン */
    color: white !important; /* 白文字 */
    padding: 5px 10px; /* タグのサイズ調整 */
    border-radius: 5px; /* 角を丸く */
    font-size: 14px !important; /* フォントサイズ調整 */
    font-weight: bold !important; /* 太字 */
}

/* Ongoing ステータスのスタイル */
.table-container.custom-work-order-table-v2 .status-ongoing {
    background-color: #00ffff !important; /* 蛍光ブルー */
    color: black !important;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 14px !important;
    font-weight: bold !important; /* 太字 */
}

/* Delayed ステータスのスタイル */
.table-container.custom-work-order-table-v2 .status-delayed {
    background-color: #ff0000 !important; /* 赤色 */
    color: white !important; /* 白文字 */
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 14px !important;
    font-weight: bold !important; /* 太字 */
}

/* On Hold ステータスのスタイル */
.table-container.custom-work-order-table-v2 .status-on-hold {
    background-color: #ffd700 !important; /* ゴールド */
    color: black !important;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 14px !important;
    font-weight: bold !important; /* 太字 */
}

/* Temp Completed ステータスのスタイル */
.table-container.custom-work-order-table-v2 .status-temp-completed {
    background-color: #ff6347 !important; /* トマト色 */
    color: white !important;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 14px !important;
    font-weight: bold !important; /* 太字 */
}

/* Help ステータスのスタイル */
.table-container.custom-work-order-table-v2 .status-help {
    background-color: #ff4500 !important; /* オレンジレッド */
    color: white !important;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 14px !important;
    font-weight: bold !important; /* 太字 */
    animation: blink 2s step-start infinite; /* 点滅アニメーション */
    animation-iteration-count: 4;
}

/* テーブルヘッダーのスタイル */
.table-container.custom-work-order-table-v2 .p-datatable-thead > tr > th {
    background-color: #b2d8b2 !important; /* ヘッダー背景色 */
    color: black !important;
    font-weight: bold !important; /* ヘッダー文字も太字に */
}

/* テーブル本体のスタイル */
.table-container.custom-work-order-table-v2 .p-datatable {
    border: none; /* テーブルの黒枠線を削除 */
}

/* 奇数行の背景色 */
.table-container.custom-work-order-table-v2 .p-datatable-tbody > tr:nth-child(odd) > td {
    background-color: #ffffff !important; /* 白色 */
}

/* 偶数行の背景色 */
.table-container.custom-work-order-table-v2 .p-datatable-tbody > tr:nth-child(even) > td {
    background-color: #d3d3d3 !important; /* 灰色 */
}

/* テーブルセルのスタイル */
.table-container.custom-work-order-table-v2 .p-datatable-tbody > tr > td {
    border-right: none; /* 右側の境界線を削除 */
}

/* ヘッダーとセルのスタイル */
.table-container.custom-work-order-table-v2 .p-datatable-thead > tr > th,
.table-container.custom-work-order-table-v2 .p-datatable-tbody > tr > td {
    font-weight: bold !important; /* テーブル全体を太字に */
}

/* サムネイル画像のスタイル */
.thumbnail {
    width: 100px; /* サムネイルのサイズ */
    height: auto; /* アスペクト比を維持 */
    border: 1px solid #ccc; /* 枠線 */
    padding: 5px;
    cursor: pointer; /* カーソルをポインターに */
}

/* サムネイルのホバー時のスタイル */
.thumbnail:hover {
    border-color: #999; /* ホバー時の枠線色 */
}
</style>
