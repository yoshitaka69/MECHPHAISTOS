<template>
    <div class="col-12 lg:col-6 xl:col-4">
        <div class="card mb-0">
            <div class="flex justify-content-between mb-3">
                <div>
                    <span class="block text-500 font-medium mb-3">Number of near misses</span>
                    <div class="text-900 font-medium text-xl">{{ orderAlertList[0]?.partsName }} </div>
                    <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
                        style="width: 2.5rem; height: 2.5rem">
                        <i class="pi pi-map-marker text-orange-500 text-xl"></i>
                    </div>
                </div>
                <span class="text-green-500 font-medium">%52+ </span>
                <span class="text-500">since last month</span>
            </div>
        </div>
    </div>
        <Accordion>
            <AccordionTab v-for="(alert, index) in orderAlertList.slice(1, 20)" :key="alert.companyCode + index"
                :header="alert.partsName">
                <div>Event Date: {{ alert.eventDate }}</div>
                <div>Location: {{ alert.location }}</div>
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
      const url = `http://127.0.0.1:8000/api/agora/alertScheduleByCompany/?format=json&companyCode=${userCompanyCode}`;

      axios.get(url)
        .then(response => {
          this.orderAlertList = this.sortAndSelectAlerts(response.data.AlertScheduleList);
        })
        .catch(error => {
          console.error("Error fetching order alerts:", error);
        });
    }, // このカッコが重要です！

    sortAndSelectAlerts(alerts) {
      return alerts
        .sort((a, b) => new Date(b.eventDate) - new Date(a.eventDate))
        .slice(0, 20);
    }
  }
});

</script>