<template>
    <div class="card">
        <Accordion :activeIndex="0">
            <AccordionTab header="Priority Tasks">
                <p class="m-0">There are a total of {{ highPriorityCount }} items with an assessment of 'Very High' or 'High'.</p>
                <ul>
                    <li v-for="(item, index) in highPriorityTasks.slice(0, 10)" :key="index">Task Name: {{ item.typicalTaskName || 'No data' }} - Cost: {{ item.typicalTaskCost ? `${item.typicalTaskCost} USD` : 'No data' }}</li>
                </ul>
            </AccordionTab>
        </Accordion>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

const highPriorityTasks = ref([]);
const highPriorityCount = ref(0);
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
        console.log('API Response:', response.data); // Log the entire response from the API
        const masterData = response.data.find((d) => d.companyCode === companyCode)?.MasterDataTable || [];
        console.log('Filtered Master Data:', masterData); // Log the data after finding the right companyCode
        const filteredTasks = masterData.filter((item) => item.assessment === 'Very High' || item.assessment === 'High');
        console.log('Filtered Tasks by Assessment:', filteredTasks);
        console.log(
            'Typical Task Names and Costs in Filtered Tasks:',
            filteredTasks.map((task) => ({
                name: task.typicalTaskName,
                cost: task.typicalTaskCost
            }))
        );
        highPriorityTasks.value = filteredTasks.map((task) => ({
            typicalTaskName: task.typicalTaskName || 'No data',
            typicalTaskCost: task.typicalTaskCost !== null ? `${task.typicalTaskCost} USD` : 'No data', // null チェックを強化
            assessment: task.assessment
        }));
        console.log('Mapped High Priority Tasks:', highPriorityTasks.value); // Log the mapped tasks
        highPriorityCount.value = filteredTasks.length;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
});
</script>
