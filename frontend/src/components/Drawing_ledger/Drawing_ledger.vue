<template>
    <div class="table-container">
        <!-- ヘッダー部分。トグルボタンと新規エントリーボタンを配置 -->
        <div class="header-container flex justify-end items-center">
            <Button type="button" label="Toggle View" @click="toggleView" class="right-aligned-button custom-toggle-button" />
            <Button label="New Entry" @click="showNewEntryForm" class="custom-button" style="margin-left: 20px" />
        </div>

        <!-- DataTableのリスト表示。viewModeが'list'のときに表示 -->
        <DataTable
            v-if="viewMode === 'list'"
            v-model:filters="filters"
            :value="sortedItems"
            :loading="loading"
            paginator
            showGridlines
            :rows="serverOptions.rowsPerPage"
            :total-records="serverItemsLength"
            :lazy="true"
            :resizable-columns="true"
            :global-filter-fields="['project_name', 'name', 'uploaded_at', 'uploaded_by', 'tag']"
            filter-display="menu"
            @page="onPage"
            @sort="onSort"
            @filter="onFilter"
            :rows-per-page-options="[5, 10, 20, 50]"
            class="p-datatable-custom"
            :sort-field="sortField"
            :sort-order="sortOrder"
            :row-class="rowClass"
            style="width: 100%"
        >
            <!-- テーブルヘッダー -->
            <template #header>
                <div class="flex justify-between items-center custom-header">
                    <h2>ファイル一覧</h2>
                </div>
            </template>

            <!-- 各列の定義（プロジェクト名、ファイル、カテゴリ、ファイル名、登録日、登録者、タグ） -->
            <!-- プロジェクト名の列 -->
            <Column field="projectName" header="プロジェクト名" sortable filter filterMatchMode="contains">
                <template #body="slotProps">
                    {{ slotProps.data.projectName || 'N/A' }}
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Search by Project Name" class="custom-input" />
                </template>
            </Column>

            <Column field="file" header="ファイル" sortable filter filterMatchMode="contains">
                <template #body="slotProps">
                    <a v-if="slotProps.data.file" :href="`/api/cad_files/${slotProps.data.file}`" download class="file-link">{{ slotProps.data.file }}</a>
                    <span v-else>N/A</span>
                </template>
            </Column>

            <Column field="category" header="カテゴリ" sortable filter filterMatchMode="contains">
                <template #body="slotProps">
                    <span v-if="slotProps.data && slotProps.data.categories">{{ slotProps.data.categories.join(', ') }}</span>
                    <span v-else>N/A</span>
                </template>
            </Column>

            <Column field="name" header="ファイル名" sortable filter filterMatchMode="contains">
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Search by File Name" class="custom-input" />
                </template>
            </Column>

            <Column field="registrationDate" header="登録日" sortable filter filterMatchMode="contains">
                <template #body="slotProps">
                    {{ new Date(slotProps.data.registrationDate).toLocaleDateString() || 'N/A' }}
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Search by Registration Date" class="custom-input" />
                </template>
            </Column>

            <Column field="uploadedBy" header="登録者" sortable filter filterMatchMode="contains">
                <template #body="slotProps">
                    {{ slotProps.data.uploadedBy || 'N/A' }}
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Search by Uploader" class="custom-input" />
                </template>
            </Column>

            <Column field="tag" header="タグ" sortable filter filterMatchMode="contains">
                <template #body="slotProps">
                    {{ slotProps.data.tag || 'N/A' }}
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Search by Tag" class="custom-input" />
                </template>
            </Column>

            <!-- 操作列（編集、削除アイコンを含む） -->
            <Column header="操作">
                <template #body="slotProps">
                    <div>
                        <i class="pi pi-pencil custom-icon" @click="editItem(slotProps.data)" style="margin-right: 10px; cursor: pointer"></i>
                        <i class="pi pi-trash custom-icon" @click="deleteItem(slotProps.data)" style="cursor: pointer"></i>
                    </div>
                </template>
            </Column>
        </DataTable>

        <!-- カードビューの表示。viewModeが'card'のときに表示 -->
        <CardView
            v-else
            :files="sortedItems"
            :selectedBrand_1="selectedBrand_1"
            :rangeValues="rangeValues"
            :minDate="minDate"
            :maxDate="maxDate"
            :oneDay="oneDay"
            :formattedStartDate="formattedStartDate"
            :formattedEndDate="formattedEndDate"
            :selectedCategories="selectedCategories"
            :sizes="sizes"
            :selectedSizes1="selectedSizes1"
            @update:selectedBrand_1="updateSelectedBrand_1"
            @update:rangeValues="updateRangeValues"
            @update:selectedCategories="updateSelectedCategories"
            @update:selectedSizes1="updateSelectedSizes1"
        />

        <!-- データアップロードフォーム -->
        <DataUploadForm :visible="isEditing || isAddingNew" :entry="isEditing ? editingItem : newEntry" @update:visible="updateVisible" @submit="submitEntry" @cancel="cancelEntry" />
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'; // ref, onMounted, computedをインポート
import axios from 'axios'; // axiosをインポートしてAPIリクエストに使用
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
import DataUploadForm from '@/components/Drawing_ledger/Data_upload_form.vue'; // データアップロードフォームコンポーネント
import CardView from '@/components/Drawing_ledger/CardView.vue'; // カードビューコンポーネント

// Piniaストアのインスタンスを作成
const userStore = useUserStore();

// データと状態を管理する変数を定義
const files = ref([]); // ファイルデータのリスト
const editingRows = ref([]); // 編集中の行
const isAddingNew = ref(false); // 新規エントリーモードかどうか
const isEditing = ref(false); // 編集モードかどうか
const newEntry = ref({
    name: '',
    file: '',
    uploaded_at: '',
    uploaded_by: '',
    category: ''
});
const editingItem = ref({
    name: '',
    file: '',
    uploaded_at: '',
    uploaded_by: '',
    category: ''
});
const viewMode = ref('list'); // リスト表示かカード表示かを管理するフラグ

// カードビューに関連する状態変数
const selectedBrand_1 = ref([]);
const rangeValues = ref([new Date(2020, 0, 1).getTime(), new Date(2024, 11, 31).getTime()]);
const minDate = ref(new Date(2020, 0, 1));
const maxDate = ref(new Date(2024, 11, 31));
const oneDay = ref(24 * 60 * 60 * 1000); // 1日のミリ秒数
const formattedStartDate = ref('');
const formattedEndDate = ref('');
const selectedCategories = ref([]);
const selectedSizes1 = ref([]);

// ビューをトグルする関数
const toggleView = () => {
    viewMode.value = viewMode.value === 'list' ? 'card' : 'list';
};

// サーバーからファイルデータを取得する関数
const fetchFiles = async () => {
    loading.value = true;
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/projectManagement/projectManagementByCompany/', {
            params: {
                companyCode: userStore.companyCode // companyCodeをクエリパラメータとして設定
            }
        });
        console.log(response.data); // 取得したデータをログに表示
        if (response.data && response.data.length > 0) {
            const companyData = response.data[0];
            files.value = companyData.projectManagementList;
        }
    } catch (error) {
        console.error('Error fetching project management data:', error);
    } finally {
        loading.value = false;
    }
};

// サーバーデータに関する計算済みプロパティ
const serverItemsLength = computed(() => files.value.length); // データ数を計算
const serverOptions = ref({
    page: 1,
    rowsPerPage: 5 // デフォルトで5件表示
});
const loading = ref(false); // ロード状態のフラグ
const sortField = ref(null); // ソートに使用するフィールド
const sortOrder = ref(null); // ソートの順序
const filters = ref({
    global: { value: null, matchMode: 'contains' },
    name: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    uploaded_at: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    uploaded_by: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] }
});

// **sortedItemsの定義**
const sortedItems = computed(() => {
    let items = [...files.value];
    if (sortField.value) {
        items.sort((a, b) => {
            let result = 0;
            if (a[sortField.value] < b[sortField.value]) result = -1;
            else if (a[sortField.value] > b[sortField.value]) result = 1;
            return sortOrder.value === 1 ? result : -result;
        });
    }
    // ページあたりの表示数に合わせて空の行を追加
    while (items.length < serverOptions.value.rowsPerPage) {
        items.push({
            id: '',
            name: '',
            file: '',
            uploaded_at: '',
            uploaded_by: '',
            categories: [] // カテゴリも初期化
        });
    }
    return items;
});

// ソート処理
const onSort = (event) => {
    sortField.value = event.sortField;
    sortOrder.value = event.sortOrder;
};

// フィルタ処理
const onFilter = (event) => {
    filters.value = event.filters;
};

// アイテム編集処理
const editItem = (item) => {
    isEditing.value = true;
    editingItem.value = { ...item };
};

// エントリーを保存する処理
const submitEntry = (entry) => {
    if (isEditing.value) {
        const item = files.value.find((i) => i.id === entry.id);
        if (item) {
            Object.assign(item, entry);
        }
        isEditing.value = false;
    } else {
        files.value.push({ ...entry, id: files.value.length + 1 });
        isAddingNew.value = false;
    }
};

// エントリー編集をキャンセルする処理
const cancelEntry = () => {
    isEditing.value = false;
    isAddingNew.value = false;
};

// アイテム削除処理
const deleteItem = (item) => {
    files.value = files.value.filter((i) => i.id !== item.id);
};

// 新規エントリーフォーム表示処理
const showNewEntryForm = () => {
    isAddingNew.value = true;
    newEntry.value = {
        name: '',
        file: '',
        uploaded_at: '',
        uploaded_by: '',
        categories: []
    };
};

// ページネーション処理
const onPage = (event) => {
    serverOptions.value.page = event.page + 1;
    serverOptions.value.rowsPerPage = event.rows;
};

// 行のスタイルを設定
const rowClass = (data, index) => {
    return index % 2 === 0 ? 'even-row' : 'odd-row';
};

// フォームの表示状態を更新
const updateVisible = (value) => {
    isAddingNew.value = isEditing.value = value;
};

// サーバーからデータを取得する処理を実行
onMounted(fetchFiles);
</script>

<style>
/* テーブルの全体のスタイル */
.table-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
}

/* ヘッダーのスタイル */
.header-container {
    flex: 0 1 auto;
    width: 100%;
    display: flex;
    justify-content: flex-end;
    padding: 10px;
}

/* カスタムヘッダーのスタイル */
.custom-header {
    font-size: 1.5rem;
    font-weight: bold;
    color: #333;
}

/* DataTableのカスタムスタイル */
.p-datatable-custom .p-datatable-thead > tr > th {
    background-color: #2c3e50;
    color: white;
    font-weight: bold;
    border-right: 1px solid #333;
}

.p-datatable-custom .p-datatable-tbody > tr:nth-child(odd) > td {
    background-color: #ecf0f1;
}

.p-datatable-custom .p-datatable-tbody > tr:nth-child(even) > td {
    background-color: #f7f7f7;
}

.p-datatable-custom .p-datatable-tbody > tr > td {
    border-right: 1px solid #bdc3c7;
}

.p-datatable-custom .p-datatable-tbody > tr > td:last-child {
    border-right: none;
}

/* カスタムボタンのスタイル */
.custom-button {
    background-color: #1abc9c;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.custom-button:hover {
    background-color: #16a085;
}

/* カスタム入力フィールドのスタイル */
.custom-input {
    width: 100%;
    padding: 8px;
    border: 1px solid #bdc3c7;
    border-radius: 4px;
}

/* 編集・削除アイコンのスタイル */
.custom-icon {
    color: #1abc9c;
    cursor: pointer;
}

.custom-icon:hover {
    color: #16a085;
}

/* トグルボタンのスタイル */
.custom-toggle-button {
    background-color: #4a90e2;
    color: white;
    border-radius: 5px;
    padding: 10px 15px;
}
</style>
