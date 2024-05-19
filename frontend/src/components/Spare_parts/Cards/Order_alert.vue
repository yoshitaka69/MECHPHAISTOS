<template>
    <div class="card mb-0">
        <div class="flex justify-content-between mb-3" style="height: 100px;">
            <div>
                <span class="block text-500 font-medium mb-3">Order Alert</span>
                <div v-if="latestOrderAlert">
                    <div class="text-900 large-bold-text">Event Date: {{ latestOrderAlert.eventDate }}</div>
                    <div class="text-900 large-bold-text">Location: {{ latestOrderAlert.location }}</div>
                </div>
            </div>
            <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
                 style="width: 2.5rem; height: 2.5rem">
                <i class="pi pi-map-marker text-orange-500 text-xl"></i>
            </div>
        </div>
    </div>
</template>
  
  <script>
  import { defineComponent } from 'vue';
  import axios from "axios";
  import { useUserStore } from '@/stores/userStore';
  
  export default defineComponent({
    data() {
      return {
        latestOrderAlert: null,
      };
    },
    created() {
      this.fetchOrderAlerts();
    },
    methods: {
      fetchOrderAlerts() {
        const userStore = useUserStore();
        const userCompanyCode = userStore.companyCode;
        const url = `http://127.0.0.1:8000/api/agora/alertScheduleByCompany/?format=json&companyCode=${userCompanyCode}`;
  
        axios.get(url)
          .then(response => {
            console.log("API response:", response);
            const userAlerts = response.data.find(company => company.companyCode === userCompanyCode);
            if (userAlerts && userAlerts.AlertScheduleList) {
              this.latestOrderAlert = this.getLatestAlert(userAlerts.AlertScheduleList);
            } else {
              console.error("No matching company code or empty AlertScheduleList");
              this.latestOrderAlert = null;
            }
          })
          .catch(error => {
            console.error("Error fetching order alerts:", error);
          });
      },
      getLatestAlert(alerts) {
        return alerts.sort((a, b) => new Date(b.eventDate) - new Date(a.eventDate))[0];
      }
    }
  });
  </script>
  
  <style scoped>
  .large-bold-text {
    font-size: 1.5rem; /* 更に大きいフォントサイズに調整 */
    font-weight: bold; /* 太字 */
  }
  
  .block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 太字に設定 */
    font-size: 1.5em; /* 現在のフォントサイズの2倍 */
    color: black; /* 文字色を黒に設定 */
  }
  </style>