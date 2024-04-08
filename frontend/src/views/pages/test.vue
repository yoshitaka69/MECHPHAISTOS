<template>
  <div>
    <EasyDataTable buttons-pagination :headers="headers" :items="items" alternating :search-field="searchField"
      :search-value="searchValue" :sort-by="sortBy" :sort-type="sortType" multi-sort>
      <!-- headers 定義に合わせてカスタムスロットをここに追加 -->
      <!-- 例えば、description フィールドのためのスロット -->
      <template #item-description="{ item }">
        <span>{{ item.description }}</span>
      </template>
      <!-- user.name フィールドのためのスロット -->
      <template #item-user.name="{ item }">
        <span>{{ item.user?.name }}</span> <!-- オプショナルチェーンを使用 -->
      </template>
    </EasyDataTable>
  </div>
</template>

<script lang="ts" setup>
import type { Header, Item, SortType } from "vue3-easy-data-table";
import { onMounted, ref } from "vue";
import axios from "axios";
import { useUserStore } from '@/stores/userStore';

const showModal = ref(false);
const searchField = ref('');
const searchValue = ref('');
const sortBy: string[] = ["Order Alert", "Parts Name", "Event Date"];
const sortType: SortType[] = ["desc", "asc"];

const OrderAlert = ref([]);

const headers: Header[] = [
  { text: "Order Alert", value: "orderAlert", sortable: true },
  { text: "Parts Name", value: "partsName", sortable: true },
  { text: "Event Date", value: "eventDate", sortable: true },
  { text: "Check", value: "check", sortable: false, align: 'center' },
];

const items: Item[] = OrderAlert.value;

onMounted(async () => {
  const userStore = useUserStore();
  const userCompanyCode = userStore.companyCode;

  console.log("User Company Code:", userCompanyCode);

  if (!userCompanyCode) {
    console.error("Error: No company code found for the user.");
    return;
  }

  try {
    const url = `http://127.0.0.1:8000/api/junctionTable/alertScheduleByCompany/?format=json&companyCode=${userCompanyCode}`;
    console.log("Request URL:", url);

    const response = await axios.get(url);
    console.log("Response Data:", response.data);
    if (response.data && response.data.length > 0) {
      response.data.forEach(item => {
        if (item.AlertScheduleList && item.AlertScheduleList.length > 0) {
          item.AlertScheduleList.forEach(alert => {
            OrderAlert.value.push({
              orderAlert: alert.orderAlertDate,
              partsName: alert.partsName,
              eventDate: alert.eventDate,
              check: false
            });
          });
        }
      });
      console.log("Updated OrderAlert Array:", OrderAlert.value);
    } else {
      console.log("No data received or data structure is incorrect");
    }
  } catch (error) {
    console.error("Axios Error:", error);
    if (error.response) {
      console.error("Error Response Data:", error.response.data);
    }
  }
});
</script>
