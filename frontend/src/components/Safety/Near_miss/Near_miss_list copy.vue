<template>
  <div>
  <button id="show-modal" @click="showModal = true">Show Modal</button>
  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal :show="showModal" @close="showModal = false">
    </modal>
  </Teleport>
  <div>
<template>
  <EasyDataTable
    v-model:server-options="serverOptions"
    :headers="headers"
    :items="items"
    :server-items-length="serverItemsLength"
    :loading="loading"
    buttons-pagination
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
      { text: "NearMiss No.", value: "nearMissNo" },
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
</script>


