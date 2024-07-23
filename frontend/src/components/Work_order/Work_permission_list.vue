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
        :global-filter-fields="['workOrderNo', 'status']"
        filter-display="menu"
        @page="onPage"
        @sort="onSort"
        @filter="onFilter"
        :rows-per-page-options="[5, 10, 20, 50]"
        class="p-datatable-custom"
        :sort-field="sortField"
        :sort-order="sortOrder"
        :row-class="rowClass"
        style="width: 100%;"
      >
        <template #header>
          <div class="flex justify-between items-center">
            <span class="p-input-icon-left">
              <i class="pi pi-search" />
              <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
            </span>
            <Button type="button" label="New Entry" @click="showNewEntryForm" />
          </div>
        </template>
        <Column field="workOrderNo" header="Work Order No" sortable filter filterMatchMode="contains">
          <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by Work Order No" />
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
        <Column header="Operation">
          <template #body="slotProps">
            <div>
              <i class="pi pi-pencil" @click="editItem(slotProps.data)" style="margin-right: 10px; cursor: pointer;"></i>
              <i class="pi pi-trash" @click="deleteItem(slotProps.data)" style="cursor: pointer;"></i>
            </div>
          </template>
        </Column>
      </DataTable>
    </div>

    <WorkPermissionForm
      :visible="isEditing || isAddingNew"
      :statuses="statuses"
      :entry="isEditing ? editingItem : newEntry"
      @update:visible="updateVisible"
      @submit="submitEntry"
      @cancel="cancelEntry"
    />
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
import WorkPermissionForm from '@/components/Work_order/Work_permission_form.vue';

const userStore = useUserStore(); // Piniaストアを使用

const products = ref([]);
const statuses = ref([
    { label: 'Completed', value: 'COMPLETED' },
    { label: 'Ongoing', value: 'Ongoing' },
    { label: 'Delayed', value: 'Delayed' }
]);

const isAddingNew = ref(false);
const isEditing = ref(false);
const newEntry = ref({
    workOrderNo: '',
    status: ''
});
const editingItem = ref({});

onMounted(async () => {
    // axiosを使用してデータを取得
    const response = await axios.get(`http://127.0.0.1:8000/api/workOrder/workOrderByCompany/?format=json&companyCode=${userStore.companyCode}`);
    // 取得したデータをフラットな配列に変換
    const flattenedData = response.data.flatMap(company => company.workOrderList);
    products.value = flattenedData; // 変換したデータをproductsにセット
    console.log('flattenedData', flattenedData);
});

const serverItemsLength = computed(() => products.value.length);
const serverOptions = ref({
  page: 1,
  rowsPerPage: 10,
});
const loading = ref(false);
const sortField = ref(null);
const sortOrder = ref(null);
const filters = ref({
  global: { value: null, matchMode: 'contains' },
  workOrderNo: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  status: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
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
      status: '',
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

const editItem = (item) => {
  isEditing.value = true;
  editingItem.value = { ...item };
  console.log('Editing item:', editingItem.value);
};

const submitEntry = (entry) => {
  if (isEditing.value) {
    const item = products.value.find(i => i.id === entry.id);
    if (item) {
      Object.assign(item, entry);
    }
    isEditing.value = false;
  } else {
    products.value.push({ ...entry, id: products.value.length + 1 });
    isAddingNew.value = false;
  }
};

const cancelEntry = () => {
  isEditing.value = false;
  isAddingNew.value = false;
};

const deleteItem = (item) => {
  products.value = products.value.filter(i => i.id !== item.id);
  console.log('Item deleted successfully');
};

const showNewEntryForm = () => {
  isAddingNew.value = true;
  newEntry.value = {
    workOrderNo: '',
    status: ''
  };
};

const onPage = (event) => {
  serverOptions.value.page = event.page + 1;
  serverOptions.value.rowsPerPage = event.rows;
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

const updateVisible = (value) => {
  isAddingNew.value = isEditing.value = value;
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
  background-color: #2d3a4f;
  color: white;
}

.p-input-icon-left .pi {
  left: 10px;
}

.even-row {
  background-color: #f7f7f7;
}

.odd-row {
  background-color: #ffffff;
}
</style>
