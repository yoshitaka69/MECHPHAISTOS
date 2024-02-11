<template>
  <div>
      <span>search field:</span>
      <select v-model="searchField">
          <option value="name">Name</option>
          <option value="Factor">Factor</option>
      </select>
      <span>search value:</span>
      <input type="text" v-model="searchValue">
      <br><br>
      <EasyDataTable 
      :headers="headers" 
      :items="items" 
      alternating
      :search-field="searchField" 
      :search-value="searchValue"
      :sort-by="sortBy"
      :sort-type="sortType"
      multi-sort
    >
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
import type { Header, Item, SortType } from "vue3-easy-data-table";
import { onMounted, ref } from "vue";
import axios from "axios";

const searchField = ref('');
const searchValue = ref('');

const sortBy : string[] = ["ID No.","Name", "Department","Date","where?","Type of accident","Description/Learning","Factor","Injured lv","Equipment damage lv","Affect of enviroment","News coverage","Affect of quality","Measures",];
const sortType : SortType[] = ["desc", "asc"];



const NearMiss = ref([]);

const headers: Header[] = [
  { text: "ID No.", value: "id", sortable: true},
  { text: "Name", value: "name", sortable: true},
  { text: "Department", value: "department", sortable: true },
  { text: "Date", value: "date", sortable: true },
  { text: "Where?", value: "where", sortable: true },
  { text: "Type of accident", value: "typeOfAccident", sortable: true },
  { text: "Description/Learning", value: "description", sortable: true },
  { text: "Factor", value: "factor", sortable: true },
  { text: "Injured lv.", value: "injuredLv", sortable: true },
  { text: "Equipment damage lv.", value: "equipmentDamageLv", sortable: true },
  { text: "Affect of Enviroment", value: "affectOfEnviroment", sortable: true },
  { text: "News coverage", value: "newsCoverage", sortable: true },
  { text: "Measures", value: "measures", sortable: true },
];

const items: Item[] = NearMiss.value;

onMounted(async () => {
  try {
      const response = await axios.get('http://localhost:3000/NearMiss');
      NearMiss.value.push(...response.data);
      console.log(response.data);
  } catch (error) {
      console.log(error);
  }
});


</script>