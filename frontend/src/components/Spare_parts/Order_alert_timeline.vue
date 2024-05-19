<template>
  <div class="timeline-wrapper">
      <div ref="timeline" class="timeline-container"></div>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import { Timeline } from 'vis-timeline/standalone';
import { DataSet } from 'vis-data';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

export default {
setup() {
  const timeline = ref(null);
  const userStore = useUserStore();


  onMounted(async () => {
  const response = await axios.get('http://127.0.0.1:8000/api/agora/alertScheduleByCompany/?format=json', {
    params: {
      companyCode: userStore.companyCode
    }
  });

  const items = new DataSet(response.data.flatMap(item => 
    item.AlertScheduleList.map(alert => ({
      content: alert.partsName,
      start: alert.orderAlertDate
    }))
  ));

  console.log(items);

    const now = new Date();
    const threeMonthsAgo = new Date(now.getFullYear(), now.getMonth() - 3, now.getDate());
    const oneYearLater = new Date(now.getFullYear() + 1, now.getMonth(), now.getDate());

    const options = {
        start: threeMonthsAgo,
        end: oneYearLater,
        width: '1500px',
        height: '100%',
        timeAxis: { scale: 'week', step: 1 },
        zoomMin: 1000 * 60 * 60 * 24 * 7, // 最小ズームレベル（1週間）
        zoomMax: 1000 * 60 * 60 * 24 * 31 * 12 * 2 // 最大ズームレベル（2年）
      };
      new Timeline(timeline.value, items, options);
    });

  return {
    timeline
  };
}
};
</script>

<style>
.timeline-wrapper {
width: 100%; 
overflow-x: auto; 
}

.timeline-container {
min-width: 1500px; 
height: 200px;     
background-color: white; 
}
</style>