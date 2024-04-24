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

    // ヘッダー名の変換マッピング
    const headerMappings = {
      "PPM10YearCostAgo": "2014",
      "PPM9YearCostAgo": "2015",
      "PPM8YearCostAgo": "2016",
      "PPM7YearCostAgo": "2017",
      "PPM6YearCostAgo": "2018",
      "PPM5YearCostAgo": "2019",
      "PPM4YearCostAgo": "2020",
      "PPM3YearCostAgo": "2021",
      "PPM2YearCostAgo": "2022",
      "PPM1YearCostAgo": "2023",
      "PPM0YearCost": "2024",
      "PPM1YearCost": "2025",
      "PPM2earCost": "2026",
      "PPM3YearCost": "2027",
      "PPM4YearCost": "2028",
      "PPM5YearCost": "2029",
      "PPM6YearCost": "2030",
      "PPM7YearCost": "2031",
      "PPM8YearCost": "2032",
      "PPM9YearCost": "2033",
      "PPM10YearCost": "2034",
    };

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
  const eventData = data[0].EventYearPPMList;
  if (eventData && eventData.length > 0) {
    const originalHeaders = Object.keys(eventData[0]).filter(header => !["companyCode", "companyName", "plant", "equipment", "machine"].includes(header));
    console.log('Original Headers:', originalHeaders);

    // 表示用ヘッダーをマッピング
    const displayHeaders = originalHeaders.map(header => headerMappings[header] || header);
    console.log('Display Headers:', displayHeaders);

    // 逆引きマッピングの作成
    const reverseHeaderMappings = {};
    originalHeaders.forEach(header => {
      reverseHeaderMappings[headerMappings[header] || header] = header;
    });
    console.log('Reverse Header Mappings:', reverseHeaderMappings);

    // 元のデータキーを使用してデータ行を取得
    const dataRows = eventData.map(item => displayHeaders.map(displayHeader => item[reverseHeaderMappings[displayHeader]]));
    console.log('Data Rows:', dataRows);

    tableSettings.value = {
      ...tableSettings.value,
      colHeaders: displayHeaders,
      data: dataRows
    };
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
