<template>
  <button id="show-modal" @click="showModal = true">Show Modal</button>
  <Teleport to="body">
    <Modal :show="showModal" @close="showModal = false" />
  </Teleport>
  <div>
    <span>search field:</span>
    <select v-model="searchField">
      <option value="userName.userName">Name</option>
      <option value="department">Department</option>
      <option value="dateOfOccurrence">Date</option>
      <option value="placeOfOccurrence">Where</option>
      <option value="typeOfAccident">Type of Accident</option>
      <option value="description">Description</option>
      <option value="factor">Factor</option>
    </select>
    <span>&nbsp;&nbsp;</span>
    <span>search value:</span>
    <input type="text" v-model="searchValue">
    <br><br>
    <EasyDataTable 
      buttons-pagination 
      :headers="headers" 
      :items="items" 
      alternating 
      :search-field="searchField"
      :search-value="searchValue" 
      multi-sort>
      <template #item-description="{ item }">
        <span>{{ item.description }}</span>
      </template>
      <template #item-userName.userName="{ item }">
        <span>{{ item.userName.userName }}</span>
      </template>
    </EasyDataTable>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import Modal from '@/components/Safety/Near_miss/Near_miss_form.vue';
import { useUserStore } from '@/stores/userStore';

const showModal = ref(false);
const searchField = ref('userName.userName'); // 初期検索フィールド
const searchValue = ref('');

const headers = ref([
  { text: "NearMiss No.", value: "nearMissNo", sortable: true },
  { text: "Name", value: "userName.userName", sortable: true },
  { text: "Department", value: "department", sortable: true },
  { text: "Date", value: "dateOfOccurrence", sortable: true },
  { text: "Where?", value: "placeOfOccurrence", sortable: true },
  { text: "Type of Accident", value: "typeOfAccident", sortable: true },
  { text: "Description", value: "description", sortable: true },
  { text: "Factor", value: "factor", sortable: true },
  { text: "Injured Lv.", value: "injuredLv", sortable: true },
  { text: "Equipment Damage Lv.", value: "equipmentDamageLv", sortable: true },
  { text: "Effect on Environment", value: "affectOfEnviroment", sortable: true },
  { text: "News Coverage", value: "newsCoverage", sortable: true },
  { text: "Measures", value: "measures", sortable: true },
  { text: "Update Day", value: "updateDay", sortable: true }
]);

const items = ref([]);

const fetchData = async () => {
  const userStore = useUserStore();
  const companyCode = userStore.companyCode;

  if (!companyCode) {
    console.error("Error: No company code found for the user.");
    return;
  }

  const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?format=json&companyCode=${companyCode}`;
  try {
    const response = await axios.get(url);
    if (response.data && response.data.length > 0) {
      items.value = response.data.flatMap(item => item.nearMissList);
      console.log("Loaded near miss items:", items.value);
    } else {
      items.value = [];
      console.log("No near miss data found.");
    }
  } catch (error) {
    console.error("Error fetching data:", error);
    if (error.response) {
      console.log("Error response:", error.response);
    }
  }
};

onMounted(fetchData);
</script>
