<template>
    <div class="task-list-detail">
      <h2>Task List Details for Task List No: {{ taskListNo }}</h2>
      <ul>
        <li><strong>Plant:</strong> {{ taskDetails.plant }}</li>
        <li><strong>Equipment:</strong> {{ taskDetails.equipment }}</li>
        <li><strong>Machine Name:</strong> {{ taskDetails.machineName }}</li>
        <li><strong>Latest Date PM:</strong> {{ taskDetails.typicalLatestDate }}</li>
        <li><strong>Task Name:</strong> {{ taskDetails.typicalTaskName }}</li>
        <li><strong>Task Labor Cost:</strong> {{ taskDetails.typicalTaskCost }}</li>
        <li><strong>Task Construction Cost:</strong> {{ taskDetails.typicalConstPeriod }}</li>
        <li><strong>Multi Tasking:</strong> {{ taskDetails.multiTasking ? 'Yes' : 'No' }}</li>
        <li><strong>Bom Code:</strong> {{ taskDetails.bomCode }}</li>
        <li><strong>Bom Cost:</strong> {{ taskDetails.bomCodeCost }}</li>
        <li><strong>Total Cost:</strong> {{ taskDetails.totalCost }}</li>
        <li><strong>Next Event Date:</strong> {{ taskDetails.typicalNextEventDate }}</li>
        <li><strong>Situation:</strong> {{ taskDetails.typicalSituation }}</li>
        <li><strong>This Year:</strong> {{ taskDetails.thisYear ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 1:</strong> {{ taskDetails.thisYear1later ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 2:</strong> {{ taskDetails.thisYear2later ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 3:</strong> {{ taskDetails.thisYear3later ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 4:</strong> {{ taskDetails.thisYear4later ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 5:</strong> {{ taskDetails.thisYear5later ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 6:</strong> {{ taskDetails.thisYear6later ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 7:</strong> {{ taskDetails.thisYear7later ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 8:</strong> {{ taskDetails.thisYear8later ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 9:</strong> {{ taskDetails.thisYear9later ? 'Yes' : 'No' }}</li>
        <li><strong>This Year + 10:</strong> {{ taskDetails.thisYear10later ? 'Yes' : 'No' }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  
  export default {
    name: 'DetailTaskList',
    setup() {
      const route = useRoute();
      const taskListNo = route.params.taskListNo;
      const taskDetails = ref({});
  
      const fetchTaskDetails = async () => {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/task/taskDetail/${taskListNo}`);
          taskDetails.value = response.data;
        } catch (error) {
          console.error('Error fetching task details:', error);
        }
      };
  
      onMounted(() => {
        fetchTaskDetails();
      });
  
      return {
        taskListNo,
        taskDetails,
      };
    },
  };
  </script>
  
  <style scoped>
  .task-list-detail {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .task-list-detail h2 {
    margin-bottom: 20px;
  }
  
  .task-list-detail ul {
    list-style-type: none;
    padding: 0;
  }
  
  .task-list-detail li {
    margin-bottom: 10px;
    font-size: 16px;
  }
  
  .task-list-detail li strong {
    margin-right: 10px;
  }
  </style>
  