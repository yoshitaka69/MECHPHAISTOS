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
import type { Header, Item, SortType } from "vue3-easy-data-table";
import { onMounted, ref } from "vue";
import axios from "axios";
import Modal from '@/components/Safety/Near_miss/Near_miss_form.vue'
import { useUserStore } from '@/stores/userStore'; // Pinia ストアをインポート

const showModal = ref(false)

const searchField = ref('');
const searchValue = ref('');

const sortBy: string[] = ["NearMiss No.", "Name", "Department", "Date", "where?", "Type of accident", "Description/Learning", "Factor", "Injured lv", "Equipment damage lv", "Affect of enviroment", "News coverage", "Affect of quality", "Measures", "Need Action?", "Solved Items?",];
const sortType: SortType[] = ["desc", "asc"];

const NearMiss = ref([]);

const headers: Header[] = [
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
        }
      });

      console.log("Consolidated Near Miss Data:", NearMiss.value);
    } else {
      console.log("No data received or data structure is incorrect");
    }
  } catch (error) {
    console.error("Axios Error:", error); // エラー内容をログ出力
    if (error.response) {
      // サーバーからの応答が存在する場合、その詳細をログ出力
      console.log("Error Response:", error.response);
    }
  }
});



</script>