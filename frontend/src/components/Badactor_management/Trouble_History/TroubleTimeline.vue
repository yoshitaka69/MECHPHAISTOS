<template>
  <div>
    <h2>PM Trouble History and Event History</h2>
    <div class="table-container">
      <EventHistoryTable @update-timeline="updateTimelineFromEventHistory" />
      <i class="pi pi-arrow-right-arrow-left red-icon"></i>
      <PMTroubleHistoryTable @update-timeline="updateTimelineFromPMTrouble" />
    </div>
    <div ref="timeline" class="timeline" style="height: 400px; margin-top: 20px;"></div>
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
    ...eventHistoryData.map(item => ({ ...item, id: `EV-${item.date}`, group: 'eventHistory' })),
    ...pmTroubleData.map(item => ({ ...item, id: `PM-${item.date}`, group: 'pmTrouble' }))
  ];
  console.log("Combined data for timeline:", combinedData);
  if (timelineInstance) {
    const items = combinedData.map(item => ({
      id: item.id,
      start: new Date(item.date),
      content: `${item.pmType || item.plant} - ${item.description || item.event}`,
      group: item.group,
      style: `background-color: ${item.group === 'pmTrouble' ? '#FFA07A' : '#20B2AA'}`
    }));
    const groups = [
      { id: 'eventHistory', content: 'Event History Data' },
      { id: 'pmTrouble', content: 'PM Trouble Data' }
    ];
    timelineInstance.setGroups(groups);
    timelineInstance.setItems(items);
    console.log("Timeline updated with items and groups:", items, groups);
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
      timeAxis: { scale: 'day', step: 1 }, // 日付軸の設定
      orientation: { axis: 'both' } // 日付軸を上下に表示
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
.timeline {
  background-color: #f0f0f0; /* タイムラインの背景色を薄い灰色に設定 */
}


.red-icon {
  color: red;
  font-size: 1.5rem; /* アイコンを二回り大きくする */
  font-weight: bold; /* 太字にする */
  margin: 0 10px;
}
.table-container {
  display: flex;
  align-items: center;
}


</style>
