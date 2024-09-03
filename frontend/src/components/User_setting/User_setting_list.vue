<template>
	<div>
	  <Button type="button" label="New Entry" @click="openNewEntry"></Button>
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
		:global-filter-fields="['userName.userName', 'description']"
		filter-display="menu"
		@page="onPage"
		@sort="onSort"
		@filter="onFilter"
		:rows-per-page-options="[5, 10, 20, 50]"
		class="p-datatable-custom striped-rows"
		:sort-field="sortField"
		:sort-order="sortOrder"
	  >
		<!-- ヘッダーとカラム定義 -->
		<template #header>
		  <div class="flex justify-between">
			<Button type="button" icon="pi pi-filter-slash" label="Clear" outlined @click="clearFilter()" />
			<span class="p-input-icon-left">
			  <i class="pi pi-search" />
			  <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
			</span>
		  </div>
		</template>
		<!-- カラム定義 -->
		<Column field="userName.userName" header="Name" sortable filter filterMatchMode="contains">
		  <template #body="slotProps">
			{{ slotProps.data.userName.userName }}
		  </template>
		  <template #filter="{ filterModel }">
			<InputText v-model="filterModel.value" type="text" placeholder="Search by Name" />
		  </template>
		</Column>
		<Column header="Super User 1" field="superUser1" sortable filter filterMatchMode="equals">
		  <template #body="slotProps">
			<Checkbox v-model="slotProps.data.superUser1" :binary="true" />
		  </template>
		  <template #filter="{ filterModel }">
			<Dropdown v-model="filterModel.value" :options="[{ label: 'True', value: true }, { label: 'False', value: false }]"></Dropdown>
		  </template>
		</Column>
		<Column header="Super User 2" field="superUser2" sortable filter filterMatchMode="equals">
		  <template #body="slotProps">
			<Checkbox v-model="slotProps.data.superUser2" :binary="true" />
		  </template>
		  <template #filter="{ filterModel }">
			<Dropdown v-model="filterModel.value" :options="[{ label: 'True', value: true }, { label: 'False', value: false }]"></Dropdown>
		  </template>
		</Column>
		<Column header="Super User 3" field="superUser3" sortable filter filterMatchMode="equals">
		  <template #body="slotProps">
			<Checkbox v-model="slotProps.data.superUser3" :binary="true" />
		  </template>
		  <template #filter="{ filterModel }">
			<Dropdown v-model="filterModel.value" :options="[{ label: 'True', value: true }, { label: 'False', value: false }]"></Dropdown>
		  </template>
		</Column>
		<Column header="Super User 4" field="superUser4" sortable filter filterMatchMode="equals">
		  <template #body="slotProps">
			<Checkbox v-model="slotProps.data.superUser4" :binary="true" />
		  </template>
		  <template #filter="{ filterModel }">
			<Dropdown v-model="filterModel.value" :options="[{ label: 'True', value: true }, { label: 'False', value: false }]"></Dropdown>
		  </template>
		</Column>
		<Column header="Super User 5" field="superUser5" sortable filter filterMatchMode="equals">
		  <template #body="slotProps">
			<Checkbox v-model="slotProps.data.superUser5" :binary="true" />
		  </template>
		  <template #filter="{ filterModel }">
			<Dropdown v-model="filterModel.value" :options="[{ label: 'True', value: true }, { label: 'False', value: false }]"></Dropdown>
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
			  <i class="pi pi-pencil" @click="editItem(slotProps.data)" style="margin-right: 10px; cursor: pointer;"></i>
			  <i class="pi pi-trash" @click="deleteItem(slotProps.data)" style="cursor: pointer;"></i>
			</div>
		  </template>
		</Column>
	  </DataTable>
  
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
  import { ref, onMounted, computed } from 'vue';
  import axios from 'axios';
  import { useUserStore } from '@/stores/userStore'; // Pinia storeのインポート
  import { FilterMatchMode, FilterOperator } from 'primevue/api';
  import InputText from 'primevue/inputtext';
  import Button from 'primevue/button';
  import Checkbox from 'primevue/checkbox';
  import Dropdown from 'primevue/dropdown';
  
  const selectedItem = ref([]);
  const itemsFromApi = ref([]);
  const serverItemsLength = ref(0);
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
	global: { value: null, matchMode: FilterMatchMode.CONTAINS },
	'userName.userName': { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
	description: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }] },
	superUser1: { value: null, matchMode: FilterMatchMode.EQUALS },
	superUser2: { value: null, matchMode: FilterMatchMode.EQUALS },
	superUser3: { value: null, matchMode: FilterMatchMode.EQUALS },
	superUser4: { value: null, matchMode: FilterMatchMode.EQUALS },
	superUser5: { value: null, matchMode: FilterMatchMode.EQUALS }
  });
  
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
	  const nearMissList = response.data.flatMap(company => company.nearMissList);
	  console.log('Extracted nearMissList:', nearMissList);
  
	  if (nearMissList.length > 0) {
		itemsFromApi.value = nearMissList.map(item => ({
		  id: item.id,
		  userName: { userName: item.userName.userName },  // userNameを正しく表示
		  description: item.description,
		  superUser1: item.solvedActionItems, // superUserにリネーム
		  superUser2: item.solvedActionItems,
		  superUser3: item.solvedActionItems,
		  superUser4: item.solvedActionItems,
		  superUser5: item.solvedActionItems,
		  operation: item.operation,
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
  
  onMounted(fetchData);
  
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
		userName: { userName: '' },
		description: '',
		superUser1: false,
		superUser2: false,
		superUser3: false,
		superUser4: false,
		superUser5: false,
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
  
  const editItem = (item) => {
	isEditing.value = true;
	Object.assign(editingItem.value, item);
	console.log('Editing item:', editingItem.value);
  };
  
  const submitEdit = async () => {
	console.log('Submitting edit for item:', editingItem.value);
	try {
	  await axios.put('http://127.0.0.1:8000/api/nearMiss/' + editingItem.value.id + '/', editingItem.value);
	  const item = itemsFromApi.value.find(i => i.id === editingItem.value.id);
	  if (item) {
		Object.assign(item, editingItem.value);
	  }
	  isEditing.value = false;
	  console.log('Edit submitted successfully');
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
	  itemsFromApi.value = itemsFromApi.value.filter(i => i.id !== item.id);
	  console.log('Item deleted successfully');
	} catch (error) {
	  console.error('Failed to delete item:', error);
	}
  };
  
  const openNewEntry = () => {
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
	  'userName.userName': { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
	  description: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }] },
	  superUser1: { value: null, matchMode: FilterMatchMode.EQUALS },
	  superUser2: { value: null, matchMode: FilterMatchMode.EQUALS },
	  superUser3: { value: null, matchMode: FilterMatchMode.EQUALS },
	  superUser4: { value: null, matchMode: FilterMatchMode.EQUALS },
	  superUser5: { value: null, matchMode: FilterMatchMode.EQUALS }
	};
  };
  </script>
  
  <style>
  .p-datatable-custom .p-datatable-thead > tr > th {
	background-color: #2d3a4f;
	color: white;
  }
  .p-input-icon-left .pi {
	left: 10px;
  }
  
  .striped-rows .p-datatable-tbody > tr:nth-child(odd) {
	background-color: #f9f9f9;
  }
  
  .striped-rows .p-datatable-tbody > tr:nth-child(even) {
	background-color: #ffffff;
  }
  </style>
  