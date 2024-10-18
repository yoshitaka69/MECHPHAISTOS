<template>
  <div class="unique-ce-list-container-v2">
    <DataTable
      :value="paginatedCeList"
      class="unique-custom-header-v2 unique-striped-rows-v2 unique-bordered-table-v2"
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
/* このスタイルは unique-ce-list-container-v2 にのみ適用されます */
.unique-ce-list-container-v2 {
  margin: 20px; /* リスト全体にマージンを追加 */
}

/* テーブル全体を縮小 */
.unique-ce-list-container-v2 .unique-custom-header-v2 {
  width: 90%; /* テーブルを一回り小さく */
  margin: 0 auto; /* テーブルをモーダルの中央に配置 */
}

/* テーブルヘッダーをユニークにスタイリング */
.unique-custom-header-v2 .p-datatable-thead > tr > th {
  background-color: #2d3a4f;
  color: white;
  white-space: pre-line; /* 改行サポート */
  font-weight: bold; /* ヘッダーのフォントを太字に */
  font-size: 0.9rem; /* フォントサイズを少し小さく */
}

/* 奇数行と偶数行のストライプ効果 */
.unique-striped-rows-v2 .p-datatable-tbody > tr:nth-child(odd) {
  background-color: #f9f9f9;
  font-weight: bold; /* 奇数行のフォントを太字に */
  font-size: 0.9rem; /* ボディのフォントサイズを小さく */
}

.unique-striped-rows-v2 .p-datatable-tbody > tr:nth-child(even) {
  background-color: #e0e0e0;
  font-weight: bold; /* 偶数行のフォントを太字に */
  font-size: 0.9rem; /* ボディのフォントサイズを小さく */
}

/* 選択された行のスタイリング */
.unique-custom-header-v2 .selected-row {
  color: red;
  font-weight: bold;
  font-size: 0.9rem; /* 選択された行のフォントサイズも調整 */
}

/* 境界線付きのテーブルスタイリング */
.unique-bordered-table-v2 {
  border: 1px solid #ddd;
}

.unique-bordered-table-v2 .p-datatable-thead > tr > th,
.unique-bordered-table-v2 .p-datatable-tbody > tr > td {
  border: 1px solid #ddd;
  padding: 10px; /* セルに余白を追加 */
  font-size: 0.9rem; /* 全体のフォントサイズを小さく */
  text-align: center; /* テキストを中央揃え */
}


</style>
