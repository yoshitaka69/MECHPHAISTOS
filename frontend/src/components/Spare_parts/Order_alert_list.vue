<template>
  <DataTable :value="sortedTasks" tableStyle="min-width: 50rem" class="custom-datatable">
    <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" sortable></Column>
  </DataTable>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

// カラム定義
const columns = [
  { field: 'orderAlertDate', header: 'Order Alert' },
  { field: 'partsName', header: 'Parts Name' },
  { field: 'deliveryTime', header: 'Delivery Time' },
  { field: 'eventDate', header: 'Event Date' },
  { field: 'location', header: 'Location' },
];

// ユーザーストアと会社コードの取得
const userStore = useUserStore();
const companyCode = userStore.companyCode;

// デフォルトタスクの定義
const defaultTask = () => ({
  orderAlertDate: 'ー',
  partsName: 'ー',
  deliveryTime: 'ー',
  eventDate: 'ー',
  location: 'ー',
});

// タスクリストのリアクティブ参照
const orderAlertList = ref(Array(20).fill(defaultTask()));

// コンポーネントのマウント時にデータを取得
onMounted(async () => {
  if (!companyCode) {
    console.error("No company code found.");
    return;
  }

  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/agora/alertScheduleByCompany/?format=json&companyCode=${companyCode}`);
    if (response.data && response.data.length > 0) {
      const companyData = response.data.find(d => d.companyCode === companyCode);
      if (companyData && companyData.AlertScheduleList) {
        orderAlertList.value = companyData.AlertScheduleList.map(item => ({
          orderAlertDate: item.orderAlertDate || 'ー',
          partsName: item.partsName || 'ー',
          deliveryTime: item.deliveryTime || 'ー',
          eventDate: item.eventDate || 'ー',
          location: item.location || 'ー',
        }));
      }
    }
    // 20件に満たない場合はデフォルトタスクで埋める
    const itemsNeeded = 20 - orderAlertList.value.length;
    if (itemsNeeded > 0) {
      orderAlertList.value.push(...Array(itemsNeeded).fill(defaultTask()));
    }
  } catch (error) {
    console.error("Error fetching data:", error);
    orderAlertList.value = Array(20).fill(defaultTask());
  }
});

// タスクのソートと制限
const sortedTasks = computed(() => {
  return orderAlertList.value.slice(0, 20); // 20件に制限
});
</script>

<style>
.custom-datatable .p-datatable-thead > tr > th {
  background-color: #2d3a4f !important;
  color: white !important;
}

.custom-datatable .p-datatable {
  border: 1px solid black;
}

.custom-datatable .p-datatable-tbody > tr:nth-child(odd) {
  background-color: white !important; /* 奇数行は白色 */
}

.custom-datatable .p-datatable-tbody > tr:nth-child(even) {
  background-color: #d3d3d3 !important; /* 偶数行は明るい灰色 */
}

.custom-datatable .p-datatable-tbody > tr > td {
  border-right: 1px solid black;
  font-size: 16px; /* フォントサイズを調整 */
}

.custom-datatable .p-datatable-thead > tr > th {
  border-right: 1px solid black;
  font-size: 16px; /* ヘッダーのフォントサイズを調整 */
}

.custom-datatable .p-datatable-tbody > tr > td:last-child {
  border-right: none;
}

.custom-datatable .p-datatable-thead > tr > th:last-child {
  border-right: none;
}
</style>
