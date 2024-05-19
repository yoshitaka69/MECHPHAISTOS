<template>
  <EasyDataTable
    v-model:server-options="serverOptions"
    :headers="headers"
    :items="items"
    :server-items-length="serverItemsLength"
    :loading="loading"
    buttons-pagination
    table-class-name="customize-table"
  />
</template>

<script lang="ts">
import { defineComponent, ref, watch } from "vue";
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Pinia storeのインポート
import { Header, ServerOptions, Item } from "vue3-easy-data-table";

export default defineComponent({
  setup() {
    const userStore = useUserStore(); // Pinia storeの使用
    const companyCode = userStore.companyCode; // companyCodeの取得

    const headers = ref<Header[]>([
      { text: "NearMiss No.", value: "nearMissNo"},
      { text: "Name", value: "userName.userName" },
      { text: "Department", value: "department" },
      { text: "Date", value: "dateOfOccurrence" },
      { text: "Where?", value: "placeOfOccurrence" },
      { text: "Type of Accident", value: "typeOfAccident" },
      { text: "Description", value: "description" },
      { text: "Factor", value: "factor" },
      { text: "Injured Lv.", value: "injuredLv" },
      { text: "Equipment Damage Lv.", value: "equipmentDamageLv" },
      { text: "Effect on Environment", value: "affectOfEnviroment" },
      { text: "News Coverage", value: "newsCoverage" },
      { text: "Measures", value: "measures" },
      { text: "Update Day", value: "updateDay" }
    ]);
    const items = ref<Item[]>([]);
    const serverItemsLength = ref(0);
    const serverOptions = ref<ServerOptions>({
      page: 1,
      rowsPerPage: 5,
    });
    const loading = ref(false);

<<<<<<< HEAD
const sortBy: string[] = ["NearMiss No.", "Name", "Department", "Date", "where?", "Type of accident", "Description/Learning", "Factor", "Injured lv", "Equipment damage lv", "Affect of enviroment", "News coverage", "Affect of quality", "Measures", "Need Action?", "Solved Items?",];
const sortType: SortType[] = ["desc", "asc"];

const NearMiss = ref([]);

const headers: Header[] = [
<<<<<<< HEAD
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
=======
    { text: "ID No.", value: "nearMissListNo", sortable: true },
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
    { text: "Operation", value: "Operation" },
>>>>>>> 3c1fa7114a4f2ba2fa60465adf06054576761a2c
];

const items: Item[] = NearMiss.value;

onMounted(async () => {
  const userStore = useUserStore();
  const userCompanyCode = userStore.companyCode;

  console.log("User Company Code:", userCompanyCode); // ユーザーの companyCode をログ出力

  if (!userCompanyCode) {
    console.error("Error: No company code found for the user.");
    return; // 処理を中断
  }

  try {
    const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?companyCode=${userCompanyCode}`;
    const response = await axios.get(url);

    console.log("API Response:", response); // API の応答をログ出力
    console.log("Response data structure:", response.data); // 応答データの構造を確認

    if (response.data && response.data.length > 0) {
      // nearMissList の各要素を個別に NearMiss.value に格納
      response.data.forEach(item => {
        if (item.nearMissList && item.nearMissList.length > 0) {
          item.nearMissList.forEach(nearMiss => {
            NearMiss.value.push(nearMiss);
          });
=======
    const loadFromServer = async () => {
      loading.value = true;
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?format=json&companyCode=${companyCode}&page=${serverOptions.value.page}&limit=${serverOptions.value.rowsPerPage}`);
        console.log("API response:", response.data);
        if (response.data && Array.isArray(response.data) && response.data.length > 0) {
          const allNearMissLists = response.data.flatMap(data => data.nearMissList);
          items.value = allNearMissLists;
          serverItemsLength.value = allNearMissLists.length;
          console.log("Loaded items:", items.value);
        } else {
          items.value = [];
          serverItemsLength.value = 0;
          console.log("No data found or empty nearMissList");
>>>>>>> yoshitaka69-20240509
        }
      } catch (error) {
        console.error("Failed to load data from server:", error);
        items.value = [];
        serverItemsLength.value = 0;
      } finally {
        loading.value = false;
      }
    };

    // first load when created
    loadFromServer();

    watch(serverOptions, (value) => {
      console.log("Server options changed, reloading data:", value);
      loadFromServer();
    }, { deep: true });

    return {
      headers,
      items,
      serverOptions,
      serverItemsLength,
      loading,
    };
  },
});
<<<<<<< HEAD
<<<<<<< HEAD



</script>
=======
</script>
>>>>>>> 3c1fa7114a4f2ba2fa60465adf06054576761a2c
=======
</script>

<style>
.customize-table {

  --easy-table-border: 1px solid #445269;
  --easy-table-row-border: 1px solid #445269;

  --easy-table-header-font-size: 14px;
  --easy-table-header-height: 50px;
  --easy-table-header-font-color: #c1cad4;
  --easy-table-header-background-color: #2d3a4f;


}
</style>
>>>>>>> yoshitaka69-20240509
