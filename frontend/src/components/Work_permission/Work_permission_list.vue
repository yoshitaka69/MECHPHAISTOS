<template>
  <div class="table-container custom-work-order-table-v3">
      <p class="page-description">This is the Work Permission Page.</p>
      <!-- Company Codeの表示 -->
      <div class="company-code-display">Company Code: {{ userStore.companyCode }}</div>

      <DataTable
          v-model:filters="filters"
          :value="formattedItems"
          :loading="loading"
          paginator
          showGridlines
          :rows="serverOptions.rowsPerPage"
          :total-records="serverItemsLength"
          :lazy="true"
          :resizable-columns="true"
          :global-filter-fields="['workPermissionNo', 'workOrderNo', 'taskName', 'constructionPeriod', 'plant', 'equipment', 'personInCharge', 'status']"
          filter-display="menu"
          @page="onPage"
          @sort="onSort"
          @filter="onFilter"
          :rows-per-page-options="[10, 20, 50]"
          class="p-datatable-custom custom-work-order-table-v3"
          :sort-field="sortField"
          :sort-order="sortOrder"
          style="width: 100%"
      >
          <!-- ヘッダー内に検索バーとボタンを配置 -->
          <template #header>
              <div class="header-content-v3">
                  <span class="p-input-icon-left">
                      <i class="pi pi-search" />
                      <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                  </span>
                  <Button type="button" label="Create Work Permission" @click="openNewEntryForm" class="create-work-permission-button" />
              </div>
          </template>

          <!-- workPermissionNoカラムを追加 -->
          <Column field="workPermissionNo" header="Work Permission No" sortable filter filterMatchMode="contains">
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" placeholder="Search by Work Permission No" />
              </template>
          </Column>

          <!-- Work Order Noカラム -->
          <Column field="workOrderNo" header="Work Order No" sortable filter filterMatchMode="contains">
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" placeholder="Search by Work Order No" />
              </template>
          </Column>

          <!-- Task Nameカラム -->
          <Column field="taskName" header="Task Name" sortable filter filterMatchMode="contains">
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" placeholder="Search by Task Name" />
              </template>
          </Column>

          <!-- Construction Periodカラム -->
          <Column field="constructionPeriod" header="Construction Period" sortable filter filterMatchMode="contains">
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" placeholder="Search by Construction Period" />
              </template>
          </Column>

          <!-- Plantカラム -->
          <Column field="plant" header="Plant" sortable filter filterMatchMode="contains">
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" placeholder="Search by Plant" />
              </template>
          </Column>

          <!-- Equipmentカラム -->
          <Column field="equipment" header="Equipment" sortable filter filterMatchMode="contains">
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" placeholder="Search by Equipment" />
              </template>
          </Column>

          <!-- Person In Chargeカラム -->
          <Column field="personInCharge" header="Person In Charge" sortable filter filterMatchMode="contains">
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" placeholder="Search by Person In Charge" />
              </template>
          </Column>

          <!-- Contractorカラム -->
          <Column field="contractor" header="Contractor" sortable filter filterMatchMode="contains">
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" placeholder="Search by Contractor" />
              </template>
          </Column>

          <!-- Gas Detectionカラム -->
          <Column field="gasDetection" header="Gas Detection" sortable filter>
              <template #body="slotProps">
                  <Tag :value="slotProps.data.gasDetection ? 'YES' : 'NO'" :class="slotProps.data.gasDetection ? 'tag-red' : 'tag-blue'" />
              </template>
          </Column>

          <!-- Oxygen Deficiencyカラム -->
          <Column field="oxygenDeficiency" header="Oxygen Deficiency" sortable filter>
              <template #body="slotProps">
                  <Tag :value="slotProps.data.oxygenDeficiency ? 'YES' : 'NO'" :class="slotProps.data.oxygenDeficiency ? 'tag-red' : 'tag-blue'" />
              </template>
          </Column>

          <!-- Valvesカラム -->
          <Column field="valves" header="Valves" sortable filter>
              <template #body="slotProps">
                  <div>
                      Valve1:
                      <Tag :value="slotProps.data.valveInputs && slotProps.data.valveInputs.valve1 ? 'On' : 'Off'" :class="slotProps.data.valveInputs && slotProps.data.valveInputs.valve1 ? 'tag-red' : 'tag-blue'" />
                      Valve2:
                      <Tag :value="slotProps.data.valveInputs && slotProps.data.valveInputs.valve2 ? 'On' : 'Off'" :class="slotProps.data.valveInputs && slotProps.data.valveInputs.valve2 ? 'tag-red' : 'tag-blue'" />
                      Valve3:
                      <Tag :value="slotProps.data.valveInputs && slotProps.data.valveInputs.valve3 ? 'On' : 'Off'" :class="slotProps.data.valveInputs && slotProps.data.valveInputs.valve3 ? 'tag-red' : 'tag-blue'" />
                      Valve4:
                      <Tag :value="slotProps.data.valveInputs && slotProps.data.valveInputs.valve4 ? 'On' : 'Off'" :class="slotProps.data.valveInputs && slotProps.data.valveInputs.valve4 ? 'tag-red' : 'tag-blue'" />
                      Valve5:
                      <Tag :value="slotProps.data.valveInputs && slotProps.data.valveInputs.valve5 ? 'On' : 'Off'" :class="slotProps.data.valveInputs && slotProps.data.valveInputs.valve5 ? 'tag-red' : 'tag-blue'" />
                  </div>
              </template>
          </Column>

          <!-- Breakersカラム -->
          <Column field="breakers" header="Breakers" sortable filter>
              <template #body="slotProps">
                  <div>
                      Breaker1:
                      <Tag :value="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker1 ? 'On' : 'Off'" :class="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker1 ? 'tag-red' : 'tag-blue'" />
                      Breaker2:
                      <Tag :value="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker2 ? 'On' : 'Off'" :class="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker2 ? 'tag-red' : 'tag-blue'" />
                      Breaker3:
                      <Tag :value="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker3 ? 'On' : 'Off'" :class="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker3 ? 'tag-red' : 'tag-blue'" />
                      Breaker4:
                      <Tag :value="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker4 ? 'On' : 'Off'" :class="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker4 ? 'tag-red' : 'tag-blue'" />
                      Breaker5:
                      <Tag :value="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker5 ? 'On' : 'Off'" :class="slotProps.data.breakerInputs && slotProps.data.breakerInputs.breaker5 ? 'tag-red' : 'tag-blue'" />
                  </div>
              </template>
          </Column>

          <!-- On-Site Safetyカラム -->
          <Column field="onSiteSafety" header="On-site Safety" sortable filter>
              <template #body="slotProps">
                  <Tag :value="slotProps.data.onSiteSafety ? 'YES' : 'NO'" :class="slotProps.data.onSiteSafety ? 'tag-red' : 'tag-blue'" />
              </template>
          </Column>

          <!-- Approverカラム -->
          <Column field="approver" header="Approver" sortable filter>
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" placeholder="Search by Approver" />
              </template>
          </Column>

          <!-- Created Atカラム -->
          <Column field="createdAt" header="Created At" sortable filter>
              <template #body="slotProps">
                  <span>{{ new Date(slotProps.data.createdAt).toLocaleString() }}</span>
              </template>
          </Column>

          <!-- Updated Atカラム -->
          <Column field="updatedAt" header="Updated At" sortable filter>
              <template #body="slotProps">
                  <span>{{ new Date(slotProps.data.updatedAt).toLocaleString() }}</span>
              </template>
          </Column>

          <!-- Operationsカラム -->
          <Column field="operations" header="Operations" body-class="text-center">
              <template #body="slotProps">
                  <i class="pi pi-pencil" @click="editEntry(slotProps.data)" style="margin-right: 10px; cursor: pointer"></i>
                  <i class="pi pi-trash" @click="confirmDelete(slotProps.data)" style="cursor: pointer"></i>
              </template>
          </Column>
      </DataTable>
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

// PiniaストアからcompanyCodeを取得
const userStore = useUserStore();

const products = ref([]); // データ格納用
const loading = ref(true); // ローディング状態管理

// ステータスのオプション
const statuses = ref([
  { label: 'Completed', value: 'COMPLETED' },
  { label: 'Ongoing', value: 'Ongoing' },
  { label: 'Delayed', value: 'Delayed' }
]);

// データ整形のための関数
const formatData = (data) => {
  const companyData = data.find((company) => company.companyCode === userStore.companyCode);
  return companyData ? companyData.workOrderPermissionList : [];
};

// データ取得処理
onMounted(async () => {
  try {
      // APIエンドポイントにクエリパラメータとしてcompanyCodeを渡す
      const response = await axios.get(`http://127.0.0.1:8000/api/workOrder/workPermissionByCompany/?companyCode=${userStore.companyCode}`);

      // 取得したデータを整形してproductsにセット
      products.value = formatData(response.data);
      console.log('取得したデータ:', products.value);
  } catch (error) {
      console.error('データ取得エラー:', error);
  } finally {
      loading.value = false; // データ取得後にローディングを終了
  }
});

// 常に10行表示するようにデータを整形する
const formattedItems = computed(() => {
  let items = [...products.value];

  // 10行未満の場合は空の行を追加
  while (items.length < 10) {
      items.push({
          workOrderNo: '',
          taskName: '',
          constructionPeriod: '',
          plant: '',
          equipment: '',
          personInCharge: '',
          status: '',
          contractor: '',
          valves: {},
          breakers: {},
          gasDetection: false,
          oxygenDeficiency: false,
          onSiteSafety: false,
          approver: '',
          createdAt: '',
          updatedAt: '',
          companyCode: '',
          companyName: ''
      });
  }

  return items;
});

// ソート・フィルタリング・ページネーション等の設定
const filters = ref({
  global: { value: null, matchMode: 'contains' },
  workOrderNo: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  taskName: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  constructionPeriod: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  plant: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  equipment: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  personInCharge: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  status: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  contractor: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] }
});

const serverItemsLength = computed(() => products.value.length);
const serverOptions = ref({
  page: 1,
  rowsPerPage: 10 // 初期表示の行数を10に設定
});
const sortField = ref(null);
const sortOrder = ref(null);

// ソート処理
const onSort = (event) => {
  sortField.value = event.sortField;
  sortOrder.value = event.sortOrder;
};

// フィルタ処理
const onFilter = (event) => {
  filters.value = event.filters;
};

// 新規作成フォームを開く関数
const openNewEntryForm = () => {
  window.open('/Work_permission_form', '_blank');
};

// 編集の処理
const editEntry = (entry) => {
  console.log('Editing entry:', entry);
  // 編集画面を開く処理を追加
};

// 削除の処理
const deleteEntry = (entry) => {
  console.log('Deleting entry:', entry);
  // 削除の処理を追加
};

// ステータスに応じたクラスを動的に適用
const getStatusClass = (status) => {
  switch (status) {
      case 'COMPLETED':
          return 'tag-success'; // 緑
      case 'Ongoing':
          return 'tag-warning'; // 黄
      case 'Delayed':
          return 'tag-danger'; // 赤
      default:
          return '';
  }
};
</script>

<style>
/* ステータスごとのカスタムクラス */
.tag-success {
  background-color: #28a745;
  color: #fff;
}

.tag-warning {
  background-color: #ffc107;
  color: #212529;
}

.tag-danger {
  background-color: #dc3545;
  color: #fff;
}

/* companyCode表示用のスタイル */
.company-code-display {
  margin-left: 20px;
  font-weight: bold;
  font-size: 16px;
}

/* その他のスタイル */
.page-description {
  font-size: 16px;
  margin-bottom: 15px;
  color: #333;
}

.custom-work-order-table-v3 .header-container-v3 {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.custom-work-order-table-v3 .create-work-permission-button {
  margin-left: auto;
}

.custom-work-order-table-v3 .p-datatable-thead > tr > th {
  background-color: #f2b2b2 !important;
  color: black !important;
}

.custom-work-order-table-v3 .p-datatable {
  border: none;
}

.custom-work-order-table-v3 .p-datatable-tbody > tr:nth-child(odd) > td {
  background-color: #ffffff !important;
}

.custom-work-order-table-v3 .p-datatable-tbody > tr:nth-child(even) > td {
  background-color: #d3d3d3 !important;
}

.tag-red {
  background-color: red;
  color: white;
}

.tag-blue {
  background-color: blue;
  color: white;
}
</style>
