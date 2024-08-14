<template>
  <div class="background">
    <div class="text-900 font-semibold text-lg mt-3">Task List</div>
    <Divider />
    <div class="timeline-container">
      <div ref="timeline" class="timeline"></div>

      <h2>タスク一覧</h2>
      <table class="task-table">
        <thead>
          <tr>
            <th>タスク名</th>
            <th>開始日</th>
            <th>終了日</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="task in items" :key="task.id">
            <td>{{ task.content }}</td>
            <td>{{ formatDate(task.start) }}</td>
            <td>{{ formatDate(task.end) || "未定" }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { Timeline } from "vis-timeline/standalone";
import "vis-timeline/styles/vis-timeline-graph2d.css";
import Divider from "primevue/divider";

export default {
  components: {
    Divider,
  },
  data() {
    return {
      items: [
        { id: 1, content: "Task A", start: "2024-01-15", end: "2024-01-20" },
        { id: 2, content: "Task B", start: "2024-03-05", end: "2024-03-10" },
        { id: 3, content: "Task C", start: "2024-05-10", end: "2024-05-15" },
        { id: 4, content: "Task D", start: "2024-08-01", end: "2024-08-05" },
        { id: 5, content: "Task E", start: "2024-11-05", end: "2024-11-10" },
      ],
    };
  },
  mounted() {
    this.createTimeline();
    window.addEventListener("resize", this.updateTimelineSize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.updateTimelineSize);
  },
  methods: {
    createTimeline() {
      const container = this.$refs.timeline;
      const options = {
        height: "400px",
        margin: {
          item: 10,
        },
        showCurrentTime: true,
        showMajorLabels: true,
        showMinorLabels: true,
      };

      this.timeline = new Timeline(container, this.items, options);
      this.updateTimelineSize(); // 初回にサイズを設定
    },
    updateTimelineSize() {
      if (this.timeline) {
        this.timeline.setOptions({ width: "100%" });
      }
    },
    formatDate(date) {
      if (!date) return null;
      const options = { year: "numeric", month: "short", day: "numeric" };
      return new Date(date).toLocaleDateString(undefined, options);
    },
  },
};
</script>

<style scoped>
.background {
  background-color: #f5f5f5; /* 背景を薄い灰色に設定 */
  padding: 20px;
}

.timeline-container {
  background-color: #ffffff; /* 背景色を白に設定 */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
  width: 100%; /* 親要素に合わせてリサイズ */
  max-width: 100%; /* 最大幅を親要素に合わせる */
}

.timeline {
  border: 1px solid #ddd;
  background-color: white; /* タイムラインの背景色を白に設定 */
}

.task-table {
  width: 100%; /* 親要素に合わせてリサイズ */
  border-collapse: collapse;
  margin-top: 20px;
}

.task-table th,
.task-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

.task-table th {
  background-color: #f4f4f4;
  font-weight: bold;
}

.task-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.task-table tr:hover {
  background-color: #e0e0e0;
}
</style>
