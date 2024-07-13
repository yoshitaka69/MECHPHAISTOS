<template>
  <div>
    <h2>PM Trouble History and Event History</h2>
    <div class="table-container">
      <PMTroubleHistoryTable @update-timeline="updateTimelineFromPMTrouble" />
      <EventHistoryTable @update-timeline="updateTimelineFromEventHistory" />
    </div>
    <div ref="timeline" style="height: 400px; background-color: white; margin-top: 20px;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import PMTroubleHistoryTable from './PMTroubleHistoryTable.vue';
import EventHistoryTable from './EventHistoryTable.vue';
import { Timeline } from 'vis-timeline/standalone';
import 'vis-timeline/styles/vis-timeline-graph2d.css';

const timeline = ref(null);
let timelineInstance = null;
let pmTroubleData = [];
let eventHistoryData = [];

const updateTimelineFromPMTrouble = (filteredTroubles) => {
  console.log("Updating timeline with PM trouble data:", filteredTroubles);
  pmTroubleData = filteredTroubles;
  updateTimeline();
};

const updateTimelineFromEventHistory = (filteredEvents) => {
  console.log("Updating timeline with event history data:", filteredEvents);
  eventHistoryData = filteredEvents;
  updateTimeline();
};

const updateTimeline = () => {
  const combinedData = [
    ...pmTroubleData.map(item => ({ ...item, id: `PM-${item.date}` })),
    ...eventHistoryData.map(item => ({ ...item, id: `EV-${item.date}` }))
  ];
  console.log("Combined data for timeline:", combinedData);
  if (timelineInstance) {
    const items = combinedData.map(item => ({
      id: item.id,
      start: new Date(item.date),
      content: `${item.pmType || item.plant} - ${item.description || item.event}`
    }));
    timelineInstance.setItems(items);
    console.log("Timeline updated with items:", items);
  } else {
    console.log("Timeline instance not initialized yet");
  }
};

onMounted(() => {
  try {
    const now = new Date();
    timelineInstance = new Timeline(timeline.value, [], {
      start: new Date(now.getTime() - 1000 * 60 * 60 * 24 * 30), // 30日前から表示
      end: new Date(now.getTime() + 1000 * 60 * 60 * 24 * 30), // 30日後まで表示
      height: '400px',
      editable: true,
      selectable: true,
      zoomable: true, // スクロールによるズームを有効にする
      zoomMax: 1000 * 60 * 60 * 24 * 365, // 最大ズームレベル
      zoomMin: 1000 * 60 * 60 * 24, // 最小ズームレベル
      moveable: true, // 横スクロールを有効にする
    });
    console.log("Timeline initialized");

    // 初期データをタイムラインに設定
    updateTimeline();
  } catch (error) {
    console.error("Error during timeline initialization:", error);
  }
});
</script>

<style scoped>
h2 {
  color: #333;
  text-align: center;
}
.table-container {
  display: flex;
  justify-content: center;
  gap: 20px; /* テーブル間の間隔を設定 */
  margin-top: 20px; /* 上部の余白を設定 */
}
</style>
