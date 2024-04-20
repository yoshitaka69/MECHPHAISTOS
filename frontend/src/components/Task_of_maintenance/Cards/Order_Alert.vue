<template>
  <div class="col-12 lg:col-6 xl:col-4">
      <Accordion>
          <!-- 1つのAccordionTabで、複数のアラートを表示 -->
          <AccordionTab header="Alerts">
              <div v-for="(alert, index) in orderAlertList.slice(0, 20)" :key="alert.companyCode + index">
                  <div>Event Date: {{ alert.eventDate }}</div>
                  <div>Location: {{ alert.location }}</div>
              </div>
          </AccordionTab>
      </Accordion>
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import axios from "axios";
import { useUserStore } from '@/stores/userStore';

export default defineComponent({
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
                  console.log("API response:", response);
                  const userAlerts = response.data.find(company => company.companyCode === userCompanyCode);
                  if (userAlerts && userAlerts.AlertScheduleList) {
                      this.orderAlertList = this.sortAndSelectAlerts(userAlerts.AlertScheduleList);
                  } else {
                      console.error("No matching company code or empty AlertScheduleList");
                      this.orderAlertList = [];
                  }
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
