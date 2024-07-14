<template>
  <div>
    <DataTable :value="ceList" class="custom-header striped-rows" :rowClass="rowClass" @row-click="onRowClick">
      <Column field="ceListNo" header="Critical Equipment No" sortable></Column>
      <Column field="equipment" header="Equipment" sortable></Column>
    </DataTable>
  </div>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Pinia storeのインポート

export default {
  data() {
    return {
      ceList: [],
      selectedRow: null,
    };
  },
  mounted() {
    this.fetchCeList();
  },
  methods: {
    async fetchCeList() {
      const userStore = useUserStore();
      const companyCode = userStore.companyCode;

      try {
        const response = await axios.get('http://127.0.0.1:8000/api/ceList/ceListByCompany/', {
          params: {
            companyCode: companyCode
          }
        });

        console.log(response.data);

        // 応答データの処理
        const companyData = response.data.find(company => company.companyCode === companyCode);
        if (companyData) {
          this.ceList = companyData.ceList;
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    rowClass(data) {
      return data === this.selectedRow ? 'selected-row' : '';
    },
    onRowClick(event) {
      this.selectedRow = event.data;
    }
  }
};
</script>

<style>
.custom-header .p-datatable-thead > tr > th {
  background-color: #2d3a4f;
  color: white;
}

.striped-rows .p-datatable-tbody > tr:nth-child(odd) {
  background-color: #f9f9f9;
}

.striped-rows .p-datatable-tbody > tr:nth-child(even) {
  background-color: #e0e0e0;
}

/* Add this CSS to support multiline headers */
.custom-header .p-column-title {
  white-space: pre-line;
}

/* CSS for selected row */
.selected-row {
  color: red;
  font-weight: bold;
}
</style>
