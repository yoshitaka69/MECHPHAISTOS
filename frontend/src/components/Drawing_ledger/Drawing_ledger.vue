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
            <Column field="project_name" header="プロジェクト名" sortable filter filterMatchMode="contains">
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Search by Project Name" class="custom-input" />
                </template>
            </Column>

            <Column field="file" header="ファイル" sortable filter filterMatchMode="contains">
                <template #body="slotProps">
                    <a :href="`/api/cad_files/${slotProps.data.file}`" download class="file-link">{{ slotProps.data.file }}</a>
                </template>
            </Column>

            <Column field="category" header="カテゴリ" sortable filter filterMatchMode="contains">
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Search by Category" class="custom-input" />
                </template>
            </Column>

            <Column field="name" header="ファイル名" sortable filter filterMatchMode="contains">
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Search by File Name" class="custom-input" />
                </template>
            </Column>

            <Column field="uploaded_at" header="登録日" sortable filter filterMatchMode="contains">
                <template #body="slotProps">
                    {{ new Date(slotProps.data.uploaded_at).toLocaleDateString() }}
                </template>
            </Column>

            <Column field="uploaded_by" header="登録者" sortable filter filterMatchMode="contains">
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Search by Uploader" class="custom-input" />
                </template>
            </Column>

            <Column field="tag" header="タグ" sortable filter filterMatchMode="contains">
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
import { ref, onMounted, computed } from 'vue'; // refとonMounted, computedをインポート
import axios from 'axios'; // axiosをインポートしてAPIリクエストに使用
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
import DataUploadForm from '@/components/Drawing_ledger/Data_upload_form.vue'; // データアップロードフォームコンポーネント
import CardView from '@/components/Drawing_ledger/CardView.vue'; // カードビューコンポーネント

const userStore = useUserStore(); // Piniaストアのインスタンスを作成

// データと状態を管理する変数を定義
const files = ref([]); // ファイルデータのリスト
const editingRows = ref([]); // 編集中の行
const isAddingNew = ref(false); // 新規エントリーモードかどうか
const isEditing = ref(false); // 編集モードかどうか
const newEntry = ref({ // 新規エントリーフォーム用の初期値
    name: '',
    file: '',
    uploaded_at: '',
    uploaded_by: '',
    category: ''
});
const editingItem = ref({ // 編集フォーム用の初期値
    name: '',
    file: '',
    uploaded_at: '',
    uploaded_by: '',
    category: ''
});
const viewMode = ref('list'); // リスト表示かカード表示かを管理するフラグ

// カードビューに関連する状態変数
const selectedBrand_1 = ref([]); // カテゴリ選択
const rangeValues = ref([new Date(2020, 0, 1).getTime(), new Date(2024, 11, 31).getTime()]); // 日付範囲の初期値
const minDate = ref(new Date(2020, 0, 1)); // 日付範囲の最小値
const maxDate = ref(new Date(2024, 11, 31)); // 日付範囲の最大値
const oneDay = ref(24 * 60 * 60 * 1000); // 1日のミリ秒数
const formattedStartDate = ref(''); // フォーマットされた開始日
const formattedEndDate = ref(''); // フォーマットされた終了日
const selectedCategories = ref([]); // 選択されたカテゴリ
const sizes = ref([{ value: '28x28' }, { value: '28x30' }, { value: '28x32' }, { value: '28x34' }, { value: '29x28' }]); // サイズオプション
const selectedSizes1 = ref([]); // 選択されたサイズ

// ビューをトグルする関数
const toggleView = () => {
    viewMode.value = viewMode.value === 'list' ? 'card' : 'list';
};

// サーバーからファイルデータを取得する関数
onMounted(async () => {
    const response = await axios.get(`http://127.0.0.1:8000/api/cad_files/?format=json&companyCode=${userStore.companyCode}`);
    files.value = response.data;
});

// カードビューからのイベントを処理する関数（カテゴリやサイズの選択変更など）
const updateSelectedBrand_1 = (newSelection) => {
    selectedBrand_1.value = newSelection;
};

const updateRangeValues = (newRangeValues) => {
    rangeValues.value = newRangeValues;
    formattedStartDate.value = new Date(newRangeValues[0]).toLocaleDateString();
    formattedEndDate.value = new Date(newRangeValues[1]).toLocaleDateString();
};

const updateSelectedCategories = (newCategories) => {
    selectedCategories.value = newCategories;
};

const updateSelectedSizes1 = (newSizes) => {
    selectedSizes1.value = newSizes;
};

// サーバーデータに関する計算済みプロパティ
const serverItemsLength = computed(() => files.value.length);
const serverOptions = ref({
    page: 1,
    rowsPerPage: 10
});
const loading = ref(false);
const sortField = ref(null);
const sortOrder = ref(null);
const filters = ref({
    global: { value: null, matchMode: 'contains' },
    name: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    uploaded_at: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    uploaded_by: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] }
});

// ファイルのソートロジック
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
            uploaded_by: ''
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
        uploaded_by: ''
    };
};

// ページネーション処理
const onPage = (event) => {
    serverOptions.value.page = event.page + 1;
    serverOptions.value.rowsPerPage = event.rows;
};

// 行のスタイルを設定（奇数行と偶数行で異なる背景色）
const rowClass = (data, index) => {
    return index % 2 === 0 ? 'even-row' : 'odd-row';
};

// フォームの表示状態を更新
const updateVisible = (value) => {
    isAddingNew.value = isEditing.value = value;
};
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
    background-color: #ecf0f1; /* 奇数行は薄い灰色 */
}

.p-datatable-custom .p-datatable-tbody > tr:nth-child(even) > td {
    background-color: #f7f7f7; /* 偶数行はさらに薄い灰色 */
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
