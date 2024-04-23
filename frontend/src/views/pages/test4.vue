<template>
	<div>
    <hot-table :settings="tableSettings"></hot-table>
  </div>
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue';
import { HotTable } from '@handsontable/vue3';
import 'handsontable/dist/handsontable.full.css';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

export default defineComponent({
  components: {
    HotTable
  },
  setup() {
    const tableSettings = ref({
      data: [],
      colHeaders: [],
      rowHeaders: true,
      width: '100%',
      height: 'auto',
      licenseKey: 'non-commercial-and-evaluation'
    });

    const fetchData = async () => {
      const userStore = useUserStore();
      const companyCode = userStore.companyCode;
      if (!companyCode) {
        console.error("No company code available in the user store.");
        return;
      }
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/junctionTable/eventYearPPMByCompany/?format=json&companyCode=${companyCode}`);
        console.log('API Response:', response.data);  // レスポンスデータの構造を確認
        processData(response.data);
      } catch (error) {
        console.error("Failed to fetch event data:", error);
      }
    };

    const processData = (data) => {
  console.log('Received API data:', data);  // APIデータの全体形を出力
  const eventData = data[0].EventYearPPMList;
  console.log('EventYearPPMList:', eventData);  // EventYearPPMListの内容を出力

  if (eventData && eventData.length > 0) {
    const headers = Object.keys(eventData[0]);
    const dataRows = eventData.map(item => headers.map(header => item[header]));
    
    console.log('Headers:', headers);  // ヘッダーの情報を出力
    console.log('Data Rows:', dataRows);  // データ行の情報を出力

    tableSettings.value = {
      ...tableSettings.value,
      colHeaders: headers,
      data: dataRows
    };
    console.log('Updated table settings:', tableSettings.value);  // 更新された設定を出力
  } else {
    tableSettings.value = {
      ...tableSettings.value,
      colHeaders: [],
      data: []
    };
  }
};


    onMounted(fetchData);

    return {
      tableSettings
    };
  }
});
</script>