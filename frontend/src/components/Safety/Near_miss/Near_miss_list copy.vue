<template>
  <div>
    <Button type="button" label="New Entry" @click="openNewEntry"></Button>
    <EasyDataTable
      v-model:server-options="serverOptions"
      :headers="headers"
      :items="items"
      :server-items-length="serverItemsLength"
      :loading="loading"
      buttons-pagination
      table-class-name="customize-table"
      :border-cell="true"
    >
      <template #item-operation="{ item }">
        <div class="operation-wrapper">
          <font-awesome-icon icon="edit" class="operation-icon" @click="editItem(item)" />
          <font-awesome-icon icon="trash" class="operation-icon" @click="deleteItem(item)" />
        </div>
      </template>
    </EasyDataTable>

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



<script lang="ts">
import { defineComponent, ref, reactive, watch } from "vue";
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Pinia storeのインポート
import { Header, ServerOptions, Item } from "vue3-easy-data-table";
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faEdit, faTrash } from '@fortawesome/free-solid-svg-icons';

library.add(faEdit, faTrash);

export default defineComponent({
  components: {
    FontAwesomeIcon,
  },
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
      { text: "Action Items", value: "actionItems" },
      { text: "Solved Action Items", value: "solvedActionItems" },
      { text: "Update Day", value: "updateDay" },
      { text: "Operation", value: "operation" }
    ]);

    const items = ref<Item[]>(Array(5).fill({ // 初期表示の5行を追加
      nearMissNo: "",
      userName: { userName: "" },
      department: "",
      dateOfOccurrence: "",
      placeOfOccurrence: "",
      typeOfAccident: "",
      description: "",
      factor: "",
      injuredLv: "",
      equipmentDamageLv: "",
      affectOfEnviroment: "",
      newsCoverage: "",
      measures: "",
      actionItems: "",
      solvedActionItems: "",
      updateDay: "",
      operation: ""
    }));

    const serverItemsLength = ref(0);
    const serverOptions = ref<ServerOptions>({
      page: 1,
      rowsPerPage: 10, // 初期表示件数を10行に設定
    });
    const loading = ref(false);

    const loadFromServer = async () => {
      loading.value = true;
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?format=json&companyCode=${companyCode}&page=${serverOptions.value.page}&limit=${serverOptions.value.rowsPerPage}`);
        console.log("API response:", response.data);
        if (response.data && Array.isArray(response.data) && response.data.length > 0) {
          const allNearMissLists = response.data.flatMap(data => data.nearMissList);
          items.value = allNearMissLists.concat(items.value.slice(0, 5)); // サーバーデータに5行追加
          serverItemsLength.value = allNearMissLists.length + 5; // 長さを更新
          console.log("Loaded items:", items.value);
        } else {
          items.value = Array(5).fill({
            nearMissNo: "",
            userName: { userName: "" },
            department: "",
            dateOfOccurrence: "",
            placeOfOccurrence: "",
            typeOfAccident: "",
            description: "",
            factor: "",
            injuredLv: "",
            equipmentDamageLv: "",
            affectOfEnviroment: "",
            newsCoverage: "",
            measures: "",
            actionItems: "",
            solvedActionItems: false,
            updateDay: "",
            operation: ""
          });
          serverItemsLength.value = 5;
          console.log("No data found or empty nearMissList");
        }
      } catch (error) {
        console.error("Failed to load data from server:", error);
        items.value = Array(5).fill({
          nearMissNo: "",
          userName: { userName: "" },
          department: "",
          dateOfOccurrence: "",
          placeOfOccurrence: "",
          typeOfAccident: "",
          description: "",
          factor: "",
          injuredLv: "",
          equipmentDamageLv: "",
          affectOfEnviroment: "",
          newsCoverage: "",
          measures: "",
          actionItems: "",
          solvedActionItems: false,
          updateDay: "",
          operation: ""
        });
        serverItemsLength.value = 5;
      } finally {
        loading.value = false;
      }
    };

    const isEditing = ref(false);
    const editingItem = reactive({
      nearMissNo: "",
      userName: { userName: "" },
      department: "",
      dateOfOccurrence: "",
      placeOfOccurrence: "",
      typeOfAccident: "",
      description: "",
      factor: "",
      injuredLv: "",
      equipmentDamageLv: "",
      affectOfEnviroment: "",
      newsCoverage: "",
      measures: "",
      actionItems: "",
      solvedActionItems: false,
      updateDay: "",
      operation: ""
    });

    const deleteItem = async (item: Item) => {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/nearMiss/${item.id}/`);
        items.value = items.value.filter(i => i.id !== item.id);
      } catch (error) {
        console.error("Failed to delete item:", error);
      }
    };

    const editItem = (item: Item) => {
      isEditing.value = true;
      Object.assign(editingItem, item);
    };

    const submitEdit = async () => {
      try {
        await axios.put(`http://127.0.0.1:8000/api/nearMiss/${editingItem.id}/`, editingItem);
        const item = items.value.find(i => i.id === editingItem.id);
        if (item) {
          Object.assign(item, editingItem);
        }
        isEditing.value = false;
      } catch (error) {
        console.error("Failed to update item:", error);
      }
    };

    const cancelEdit = () => {
      isEditing.value = false;
    };

    const openNewEntry = () => {
      window.open('/near_miss_input_form', '_blank'); // 新しいウィンドウまたはタブで開く
    };

    // 初期表示用のモーダル状態
    const showModal = ref(false);

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
      editItem,
      deleteItem,
      isEditing,
      editingItem,
      submitEdit,
      cancelEdit,
      showModal,
      openNewEntry
    };
  },
});
</script>



<style>
.customize-table {
  --easy-table-border: 1px solid #445269;
  --easy-table-row-border: 1px solid #445269;
  --easy-table-header-font-size: 16px; /* ヘッダーの文字の大きさを大きくする */
  --easy-table-header-height: 50px;
  --easy-table-header-font-color: #ffffff; /* ヘッダーの文字色を白に設定 */
  --easy-table-header-background-color: #2d3a4f; /* ヘッダーの背景色を紺色に設定 */
  --easy-table-font-size: 18px; /* テーブル内の文字の大きさを大きくする */
  --easy-table-border-cell: 1px solid #445269; /* セルのボーダーを設定 */
}

.customize-table td {
  font-size: 18px; /* テーブル内の文字のフォントサイズを直接設定 */
}

.operation-wrapper .operation-icon {
  width: 20px;
  cursor: pointer;
  margin-right: 10px;
}

.edit-item {
  margin-top: 20px;
  font-size: 18px; /* 編集フォームの文字の大きさを大きくする */
}
</style>
