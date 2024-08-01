<template>
    <div>
      <h2>CE List Detail</h2>
      <div v-if="ceData">
        <p><strong>CeListNo:</strong> {{ ceData.ceListNo }}</p>
        <p><strong>Plant:</strong> {{ ceData.plant }}</p>
        <p><strong>Equipment:</strong> {{ ceData.equipment }}</p>
        <p><strong>Machine:</strong> {{ ceData.machineName }}</p>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import { useUserStore } from '@/stores/userStore';
  
  export default {
    name: 'CeListDetail',
    setup() {
      const route = useRoute();
      const ceData = ref(null);
  
      onMounted(async () => {
        const ceListNo = route.params.ceListNo;
        const userStore = useUserStore();
        const companyCode = userStore.companyCode;
  
        console.log('Route parameter ceListNo:', ceListNo);
        console.log('Using companyCode from store:', companyCode);
  
        if (ceListNo && companyCode) {
          try {
            const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?companyCode=${companyCode}`;
            console.log('Fetching CE details from URL:', url);
  
            const response = await axios.get(url);
  
            console.log('API response data:', response.data);
  
            // APIのレスポンスデータから、直接 ceListNo を探す
            const item = response.data.find(item => item.ceListNo === Number(ceListNo));
  
            if (item) {
              ceData.value = item;
              console.log('Found CE data:', ceData.value);
            } else {
              console.error('CE data not found for ceListNo:', ceListNo);
            }
          } catch (error) {
            console.error('Error fetching CE list details:', error);
          }
        } else {
          console.error('Invalid ceListNo or companyCode:', ceListNo, companyCode);
        }
      });
  
      return {
        ceData,
      };
    },
  };
  </script>
  
  <style scoped>
  h2 {
    margin-bottom: 20px;
  }
  
  p {
    margin: 5px 0;
  }
  </style>
  