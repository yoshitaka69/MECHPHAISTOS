<template>
  <div class="table-container">
    <div class="header-container">
      <div class="flex justify-between items-center">
        <span class="p-input-icon-left">
          <i class="pi pi-search" />
          <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
        </span>
        <Button type="button" label="New Entry" @click="showNewEntryForm" />
        <Button type="button" label="Toggle View" @click="toggleView" />
      </div>
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
        :global-filter-fields="['name', 'uploaded_at', 'uploaded_by']"
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
        <Column field="file" header="ファイル" sortable filter filterMatchMode="contains">
          <template #body="slotProps">
            <a :href="`/api/cad_files/${slotProps.data.file}`" download>{{ slotProps.data.file }}</a>
          </template>
        </Column>
        <Column field="name" header="ファイル名" sortable filter filterMatchMode="contains">
          <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by File Name" />
          </template>
        </Column>
        <Column field="uploaded_at" header="登録日" sortable filter filterMatchMode="contains">
          <template #body="slotProps">
            {{ new Date(slotProps.data.uploaded_at).toLocaleDateString() }}
          </template>
        </Column>
        <Column field="uploaded_by" header="登録者" sortable filter filterMatchMode="contains">
          <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by Uploader" />
          </template>
        </Column>
        <Column header="操作">
          <template #body="slotProps">
            <div>
              <i class="pi pi-pencil" @click="editItem(slotProps.data)" style="margin-right: 10px; cursor: pointer;"></i>
              <i class="pi pi-trash" @click="deleteItem(slotProps.data)" style="cursor: pointer;"></i>
            </div>
          </template>
        </Column>
      </DataTable>
      <div v-else class="card-view">
        <div class="p-grid">
          <div v-for="file in sortedItems" :key="file.id" class="p-col-12 p-md-4">
            <div class="p-card">
              <div class="p-card-header">
                <h4>{{ file.name }}</h4>
              </div>
              <div class="p-card-body">
                <p><strong>ファイル:</strong> <a :href="`/api/cad_files/${file.file}`" download>{{ file.file }}</a></p>
                <p><strong>登録日:</strong> {{ new Date(file.uploaded_at).toLocaleDateString() }}</p>
                <p><strong>登録者:</strong> {{ file.uploaded_by }}</p>
              </div>
              <div class="p-card-footer">
                <Button icon="pi pi-pencil" class="p-button-text" @click="editItem(file)" />
                <Button icon="pi pi-trash" class="p-button-text" @click="deleteItem(file)" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <CADUploadForm
      :visible="isEditing || isAddingNew"
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
import { useUserStore } from '@/stores/userStore';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import CADUploadForm from './CAD_upload_form.vue';  // インポート先を確認

const userStore = useUserStore();

const files = ref([]);
const editingRows = ref([]);
const isAddingNew = ref(false);
const isEditing = ref(false);
const newEntry = ref({
    name: '',
    file: '',
    uploaded_at: '',
    uploaded_by: ''
});
const editingItem = ref({});
const viewMode = ref('list'); // デフォルトの表示モードをリストに設定

const toggleView = () => {
  viewMode.value = viewMode.value === 'list' ? 'card' : 'list';
};

onMounted(async () => {
    const response = await axios.get(`http://127.0.0.1:8000/api/cad_files/?format=json&companyCode=${userStore.companyCode}`);
    files.value = response.data;
    console.log('files', files.value);
});

const serverItemsLength = computed(() => files.value.length);
const serverOptions = ref({
  page: 1,
  rowsPerPage: 10,
});
const loading = ref(false);
const sortField = ref(null);
const sortOrder = ref(null);
const filters = ref({
  global: { value: null, matchMode: 'contains' },
  name: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  uploaded_at: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  uploaded_by: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
});

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
    const item = files.value.find(i => i.id === entry.id);
    if (item) {
      Object.assign(item, entry);
    }
    isEditing.value = false;
  } else {
    files.value.push({ ...entry, id: files.value.length + 1 });
    isAddingNew.value = false;
  }
};

const cancelEntry = () => {
  isEditing.value = false;
  isAddingNew.value = false;
};

const deleteItem = (item) => {
  files.value = files.value.filter(i => i.id !== item.id);
  console.log('Item deleted successfully');
};

const showNewEntryForm = () => {
  isAddingNew.value = true;
  newEntry.value = {
    name: '',
    file: '',
    uploaded_at: '',
    uploaded_by: ''
  };
};

const onPage = (event) => {
  serverOptions.value.page = event.page + 1;
  serverOptions.value.rowsPerPage = event.rows;
};

const clearFilter = () => {
  filters.value = {
    global: { value: null, matchMode: 'contains' },
    name: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    uploaded_at: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
    uploaded_by: { operator: 'and', constraints: [{ value: null, matchMode: 'startsWith' }] },
  };
};

const rowClass = (data, index) => {
  return index % 2 === 0 ? 'even-row' : 'odd-row';
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

.card-view .p-card {
  margin-bottom: 2rem;
}
</style>
