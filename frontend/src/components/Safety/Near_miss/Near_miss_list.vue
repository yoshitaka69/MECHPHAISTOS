<template>
  <button id="show-modal" @click="showModal = true">Show Modal</button>
  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal :show="showModal" @close="showModal = false">
    </modal>
  </Teleport>
  <div>
    <span>search field:</span>
    <select v-model="searchField">
      <option value="name">Name</option>
      <option value="department">Department</option>
      <option value="Date">Date</option>
      <option value="Where">where</option>
      <option value="typeOfAccident">Factor</option>
      <option value="description">Date</option>
      <option value="factor">Factor</option>
    </select>
    <span>&nbsp;&nbsp;</span> <!-- ここに空白を挿入 -->
    <span>search value:</span>
    <input type="text" v-model="searchValue">

    <br><br>
    <EasyDataTable buttons-pagination :headers="headers" :items="items" alternating :search-field="searchField"
      :search-value="searchValue" :sort-by="sortBy" :sort-type="sortType" multi-sort>
      <template #item-description="item">
        <span>
          {{ item.description }}
        </span>
      </template>

      <template #item-user.name="item">
        <span>
          {{ item.user.name }}
        </span>
      </template>
    </EasyDataTable>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import Modal from '@/components/Safety/Near_miss/Near_miss_form.vue'
import { useUserStore } from '@/stores/userStore';

const showModal = ref(false);
const searchField = ref('');
const searchValue = ref('');

const headers = ref([
  { text: "NearMiss No.", value: "nearMissNo", sortable: true },
  { text: "Name", value: "userName.userName", sortable: true },
  { text: "Department", value: "department", sortable: true },
  { text: "Date", value: "dateOfOccurrence", sortable: true },
  { text: "Where?", value: "placeOfOccurrence", sortable: true },
  { text: "Type of accident", value: "typeOfAccident", sortable: true },
  { text: "Description/Learning", value: "description", sortable: true },
  { text: "Factor", value: "factor", sortable: true },
  { text: "Injured lv.", value: "injuredLv", sortable: true },
  { text: "Equipment damage lv.", value: "equipmentDamageLv", sortable: true },
  { text: "Affect of Enviroment", value: "affectOfEnviroment", sortable: true },
  { text: "News coverage", value: "newsCoverage", sortable: true },
  { text: "Measures", value: "measures", sortable: true },
  { text: "Need Action?", value: "actionItems", sortable: true },
  { text: "Solved Items?", value: "solvedItems", sortable: true },
  { text: "updateDay", value: "updateDay", sortable: true },
  { text: "Operation", value: "Operation" },
];

const items = ref([]);

const fetchData = async () => {
  const userStore = useUserStore();
  const companyCode = userStore.companyCode;

  if (!companyCode) {
    console.error("Error: No company code found for the user.");
    return;
  }

  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?companyCode=${companyCode}`);
    if (response.data && response.data.length > 0) {
      // Assuming each item in the response data array is what you want to display
      items.value = response.data.map(item => item.nearMissList).flat();
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

onMounted(fetchData);
</script>