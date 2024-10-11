<template>
  <DataTable :value="sortedTasks" tableStyle="min-width: 50rem" class="styled-table">
    <!-- No. 列をスロットで追加し、slotProps.index を使用 -->
    <Column header="No.">
      <template #body="slotProps">
        <span>{{ slotProps.index + 1 }}</span>
      </template>
    </Column>
    <!-- 他の列を表示 -->
    <Column field="plant" header="Plant" sortable></Column>
    <Column field="machine" header="Machine Name" sortable></Column>
    <Column field="taskName" header="Task Name" sortable></Column>
    <Column field="equipment" header="Equipment" sortable></Column>
    <Column field="pmType" header="PM Type" sortable></Column>
    <Column field="cost" header="Cost" sortable></Column>

    <!-- Assessment 列をslotで表示 -->
    <Column field="assessment" header="Assessment">
      <template #body="slotProps">
        <Tag :value="slotProps.data.assessment" :class="getAssessmentClass(slotProps.data.assessment)" />
      </template>
    </Column>
  </DataTable>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import Tag from 'primevue/tag';

// 列の定義
const columns = [
  { field: 'plant', header: 'Plant' },
  { field: 'machine', header: 'Machine Name' },
  { field: 'taskName', header: 'Task Name' },
  { field: 'equipment', header: 'Equipment' },
  { field: 'pmType', header: 'PM Type' },
  { field: 'cost', header: 'Cost' },
  { field: 'assessment', header: 'Assessment' }
];

// ユーザー情報の取得
const userStore = useUserStore();
const companyCode = userStore.companyCode;

// デフォルトのタスクデータ
const defaultTask = () => ({
  plant: 'ー',
  machine: 'ー',
  taskName: 'ー',
  equipment: 'ー',
  pmType: 'ー',
  cost: 'ー',
  assessment: 'ー'
});

const priorityTasks = ref([]);

// データ取得処理
onMounted(async () => {
  console.log('Mounted. Company code:', companyCode);
  if (!companyCode) {
    console.error('No company code found.');
    priorityTasks.value = Array(20).fill(defaultTask());
    return;
  }

  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/junctionTable/ceListAndTaskByCompany/?companyCode=${companyCode}`
    );
    console.log('API response:', response);
    if (response.data && response.data.length > 0) {
      const companyData = response.data.find(d => d.companyCode === companyCode);
      console.log('Filtered companyData:', companyData);
      if (companyData && companyData.CeListAndTaskList.length > 0) {
        const taskList = [];
        for (let i = 1; i <= 20; i++) {
          taskList.push({
            plant: companyData.CeListAndTaskList[0][`no${i}Plant`] || 'ー',
            machine: companyData.CeListAndTaskList[0][`no${i}HighLevelMachine`] || 'ー',
            taskName: companyData.CeListAndTaskList[0][`no${i}HighPriorityTaskName`] || 'ー',
            equipment: companyData.CeListAndTaskList[0][`no${i}Equipment`] || 'ー',
            pmType: companyData.CeListAndTaskList[0][`no${i}PMType`] || 'ー',
            cost: companyData.CeListAndTaskList[0][`no${i}Cost`] || 'ー',
            assessment: companyData.CeListAndTaskList[0][`no${i}Assessment`] || 'ー'
          });
        }
        priorityTasks.value = taskList;
      }
    }
  } catch (error) {
    console.error('Error fetching data:', error);
    priorityTasks.value = Array(20).fill(defaultTask());
  }

  // 常に20行になるように足りない分をデフォルト値で埋める
  const itemsNeeded = 20 - priorityTasks.value.length;
  if (itemsNeeded > 0) {
    priorityTasks.value.push(...Array(itemsNeeded).fill(defaultTask()));
  }
});

// 表示データの計算
const sortedTasks = computed(() => {
  return priorityTasks.value.slice(0, 20); // 常に20行に制限
});

// Assessmentのクラスを取得するメソッド
const getAssessmentClass = (assessment) => {
  switch (assessment) {
    case 'High+':
      return 'assessment-high-plus';
    case 'High':
      return 'assessment-high';
    case 'Middle':
      return 'assessment-middle';
    case 'Low':
      return 'assessment-low';
    case 'Review':
      return 'assessment-review';
    default:
      return '';
  }
};
</script>



<style>
.styled-table .p-datatable-thead > tr > th {
  background-color: #003366;
  color: #ffffff;
  font-weight: bold;
  padding: 10px;
  text-align: center;
  border-bottom: 2px solid #006699;
  font-size: 14px; /* フォントサイズを14pxに */
}

.styled-table .p-datatable-tbody > tr:nth-child(even) {
  background-color: #f0f8ff;
  font-size: 14px; /* フォントサイズを14pxに */
}

.styled-table .p-datatable-tbody > tr:nth-child(odd) {
  background-color: #ffffff;
  font-size: 14px; /* フォントサイズを14pxに */
}

.styled-table .p-datatable-tbody > tr:hover {
  background-color: #cce7ff; /* Hover effect */
}

.styled-table .p-datatable {
  border-collapse: collapse;
  width: 100%;
  font-family: Arial, sans-serif;
  font-size: 14px; /* フォントサイズを14pxに */
  color: #333;
}

.styled-table .p-datatable-tbody > tr > td {
  padding: 12px 8px;
  text-align: left;
  border-bottom: 1px solid #dddddd;
  font-weight: bold; /* 文字を太字に */
  font-size: 14px; /* フォントサイズを14pxに */
}

.styled-table .p-datatable-tbody > tr > td:first-child {
  font-weight: bold;
}

.styled-table .p-datatable {
  border: 1px solid #cccccc;
}

/* High+ の点滅アニメーション */
.assessment-high-plus {
  background-color: red;
  color: white;
  font-size: 14px; /* フォントサイズを14pxに */
  animation: blink 1s step-start 5; /* 1秒周期で8回点滅 */
}

.assessment-high {
  background-color: orange;
  color: white;
  font-size: 14px; /* フォントサイズを14pxに */
}

.assessment-middle {
  background-color: yellow;
  color: black;
  font-size: 14px; /* フォントサイズを14pxに */
}

.assessment-low {
  background-color: green;
  color: white;
  font-size: 14px; /* フォントサイズを14pxに */
}

.assessment-review {
  background-color: #4c7c04;
  color: white;
  font-size: 14px; /* フォントサイズを14pxに */
}

/* 点滅アニメーションの設定 */
@keyframes blink {
  50% {
    opacity: 0;
  }
}
</style>
