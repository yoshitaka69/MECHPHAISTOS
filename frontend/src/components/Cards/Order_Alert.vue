<template>
  <div class="col-12 lg:col-6 xl:col-4">
    <div class="card mb-0">
      <div class="flex justify-content-between mb-3">
        <div>
          <span class="block text-500 font-medium mb-3">Number of near misses</span>
          <div class="text-900 font-medium text-xl">{{ orderAlertList[0]?.partsName }}</div>
        </div>
        <!-- ... -->
      </div>
      <!-- ... -->
    </div>
  </div>

  <Accordion>
    <AccordionTab v-for="(alert, index) in orderAlertList.slice(1, 20)" :key="alert.companyCode + index" :header="alert.partsName">
      <div>Event Date: {{ alert.eventDate }}</div>
      <div>Location: {{ alert.location }}</div>
      <!-- 他のデータの表示 -->
    </AccordionTab>
  </Accordion>
</template>

<script>
import { defineComponent } from 'vue';
import { Accordion, AccordionTab } from 'primevue/accordion';
import axios from "axios";
import { useUserStore } from '@/stores/userStore';

export default defineComponent({
  components: {
    Accordion,
    AccordionTab,
  },
  data() {
    return {
      orderAlertList: [],
    };
  },
  created() {
    this.fetchOrderAlerts();
  },
  methods: {
    fetchOrderAlerts() {
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;
      const url = `https://example.com/api/alerts?companyCode=${userCompanyCode}`;

      axios.get(url)
        .then(response => {
          // ここで日付に基づいてソートして20件を選択
          this.orderAlertList = this.sortAndSelectAlerts(response.data.AlertScheduleList);
        })
        .catch(error => {
          console.error("Error fetching order alerts:", error);
        });
    },
    sortAndSelectAlerts(alerts) {
      return alerts
        .sort((a, b) => new Date(b.eventDate) - new Date(a.eventDate))
        .slice(0, 20);
    }
  }
});
</script>
