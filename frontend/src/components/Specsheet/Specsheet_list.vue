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
        :global-filter-fields="['fileName', 'date', 'userName']"
        filter-display="menu"
        @page="onPage"
        @sort="onSort"
        @filter="onFilter"
        :rows-per-page-options="[5, 10, 20, 50]"
        class="p-datatable-custom"
        :sort-field="sortField"
        :sort-order="sortOrder"
        style="width: 100%;"
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
        <Column field="fileName" header="File Name" sortable filter filterMatchMode="contains">
          <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by File Name" />
          </template>
        </Column>
        <Column field="date" header="Date" sortable filter filterMatchMode="contains">
          <template #filter="{ filterModel }">
            <Calendar v-model="filterModel.value" dateFormat="yy-mm-dd" placeholder="Select a Date" />
          </template>
        </Column>
        <Column field="userName" header="User Name" sortable filter filterMatchMode="contains">
          <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by User Name" />
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

    <div class="edit-item" v-if="isEditing">
      <h3>Edit Item</h3>
      <label v-for="(value, key) in editingItem" :key="key">
        {{ key }}: <input type="text" v-model="editingItem[key]" />
        <br />
      </label>
      <button @click="submitEdit">Save</button>
      <button @click="cancelEdit">Cancel</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Calendar from 'primevue/calendar';

const router = useRouter();

const selectedItem = ref([]);
const itemsFromApi = ref([
  { id: 1, fileName: 'File A', date: '2023-07-15', userName: 'User 1' },
  { id: 2, fileName: 'File B', date: '2023-07-16', userName: 'User 2' },
  { id: 3, fileName: 'File C', date: '2023-07-17', userName: 'User 3' },
]);
const serverItemsLength = ref(itemsFromApi.value.length);
const serverOptions = ref({
  page: 1,
  rowsPerPage: 10,
});
const loading = ref(false);
const isEditing = ref(false);
const editingItem = ref({});
const sortField = ref(null);
const sortOrder = ref(null);
const filters = ref({
  global: { value: null, matchMode: 'contains' },
  fileName: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  date: { operator: 'and', constraints: [{ value: null, matchMode: 'contains' }] },
  userName: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
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
      fileName: '',
      date: '',
      userName: '',
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
  Object.assign(editingItem.value, item);
  console.log('Editing item:', editingItem.value);
};

const submitEdit = async () => {
  console.log('Submitting edit for item:', editingItem.value);
  const item = itemsFromApi.value.find(i => i.id === editingItem.value.id);
  if (item) {
    Object.assign(item, editingItem.value);
  }
  isEditing.value = false;
  console.log('Edit submitted successfully');
};

const cancelEdit = () => {
  isEditing.value = false;
  console.log('Edit cancelled');
};

const deleteItem = (item) => {
  itemsFromApi.value = itemsFromApi.value.filter(i => i.id !== item.id);
  console.log('Item deleted successfully');
};

const openNewEntry = () => {
  const routeData = router.resolve({
    name: 'specsheet_form'
  });
  window.open(routeData.href, '_blank');
};

const onPage = (event) => {
  serverOptions.value.page = event.page + 1;
  serverOptions.value.rowsPerPage = event.rows;
};

const clearFilter = () => {
  filters.value = {
    global: { value: null, matchMode: 'contains' },
    fileName: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    date: { operator: 'and', constraints: [{ value: null, matchMode: 'contains' }] },
    userName: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
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
  background-color: #2d3a4f;
  color: white;
}

/* CSSで交互に背景色を設定 */
.p-datatable-custom .p-datatable-tbody > tr:nth-child(odd) {
  background-color: #ffffff !important; /* 白色 */
}

.p-datatable-custom .p-datatable-tbody > tr:nth-child(even) {
  background-color: #d3d3d3 !important; /* 薄い灰色 */
}

.p-input-icon-left .pi {
  left: 10px;
}
</style>
