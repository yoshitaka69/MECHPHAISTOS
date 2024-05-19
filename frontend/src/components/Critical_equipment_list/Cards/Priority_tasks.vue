<template>
    <div>
        <div>
            <span class="block text-500 font-medium mb-3">Priority Task</span>
            <div class="text-900 large-bold-text">
                <Button label="Very High" class="p-button-danger custom-button-size"></Button>&nbsp;&&nbsp;<Button label="High" class="p-button-danger custom-button-size"></Button>&nbsp;is {{ highPriorityCount }} items
                <br />
                <div v-if="randomHighPriorityTask">
                    <p>Task Name: {{ randomHighPriorityTask.typicalTaskName || 'No data' }} - Cost: {{ randomHighPriorityTask.typicalTaskCost ? `${randomHighPriorityTask.typicalTaskCost} USD` : 'No data' }}</p>
                </div>
            </div>
            <br />
            <div class="flex align-items-center justify-content-center bg-orange-100 border-round" style="width: 2.5rem; height: 2.5rem">
                <i class="pi pi-map-marker text-orange-500 text-xl"></i>
            </div>
            <span class="text-green-500 font-medium">%52+ </span>
            <span class="text-500">since last week</span>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

const highPriorityTasks = ref([]);
const highPriorityCount = ref(0);
const randomHighPriorityTask = ref(null); // 新しいrefを追加
const userStore = useUserStore();

onMounted(async () => {
    const companyCode = userStore.companyCode;
    if (!companyCode) {
        console.error('No company code found.');
        return;
    }

    const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${companyCode}`;
    try {
        const response = await axios.get(url);
        const masterData = response.data.find((d) => d.companyCode === companyCode)?.MasterDataTable || [];
        const filteredTasks = masterData.filter((item) => item.assessment === 'Very High' || item.assessment === 'High');

        highPriorityTasks.value = filteredTasks.map((task) => ({
            typicalTaskName: task.typicalTaskName || 'No data',
            typicalTaskCost: task.typicalTaskCost !== null ? `${task.typicalTaskCost} USD` : 'No data',
            assessment: task.assessment
        }));
        highPriorityCount.value = filteredTasks.length;

        // ランダムなタスクを選択
        const randomIndex = Math.floor(Math.random() * filteredTasks.length);
        randomHighPriorityTask.value = highPriorityTasks.value[randomIndex];
    } catch (error) {
        console.error('Error fetching data:', error);
    }
});
</script>

<style scoped>
.large-bold-text {
    font-size: 1rem; /* 更に大きいフォントサイズに調整 */
    font-weight: bold; /* 太字 */
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 太字に設定 */
    font-size: 1.5em; /* 現在のフォントサイズの2倍 */
    color: black; /* 文字色を黒に設定 */
}

.custom-button-size {
    padding: 6px 14px;  /* 上下のパディング10px、左右のパディング20px */
    font-size: 12px;    /* フォントサイズ */
}
</style>
