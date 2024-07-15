<template>
  <div>
    <DataTable
      :value="paginatedCeList"
      class="custom-header striped-rows bordered-table"
      :rows="30"
      :paginator="true"
      :totalRecords="totalRecords"
      :rowClass="rowClass"
      @row-click="onRowClick"
      @page="onPage"
    >
      <Column
        field="ceListNo"
        header="Critical Equipment No"
        sortable
        :headerStyle="{ width: '200px' }"
        :bodyStyle="{ width: '200px' }"
      ></Column>
      <Column
        field="equipment"
        header="Equipment"
        sortable
        :headerStyle="{ width: '300px' }"
        :bodyStyle="{ width: '300px' }"
      ></Column>
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
      paginatedCeList: [],
      selectedRow: null,
      totalRecords: 0,
      currentPage: 1,
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
            companyCode: companyCode,
          },
        });

        console.log(response.data);

        // 応答データの処理
        const companyData = response.data.find(
          (company) => company.companyCode === companyCode
        );
        if (companyData) {
          this.ceList = companyData.ceList;
          this.totalRecords = this.ceList.length;
          this.updatePaginatedCeList();
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
    },
    onPage(event) {
      this.currentPage = event.page + 1;
      this.updatePaginatedCeList();
    },
    updatePaginatedCeList() {
      const start = (this.currentPage - 1) * 30;
      const end = start + 30;
      const pageData = this.ceList.slice(start, end);

      // 30個未満の場合は空行を追加
      while (pageData.length < 30) {
        pageData.push({});
      }

      this.paginatedCeList = pageData;
    },
  },
};
</script>

<style>
.custom-header .p-datatable-thead > tr > th {
  background-color: #2d3a4f;
  color: white;
  white-space: pre-line; /* 改行をサポートするために追加 */
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

/* CSS for bordered table */
.bordered-table {
  border: 1px solid #ddd;
}

.bordered-table .p-datatable-thead > tr > th,
.bordered-table .p-datatable-tbody > tr > td {
  border: 1px solid #ddd;
}
</style>
