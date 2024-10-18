<template>
  <div>
    <table class="styled-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Age</th>
        </tr>
      </thead>
      <tbody>
        <tr 
          v-for="row in tableData" 
          :key="row.id" 
          @click="selectRow(row)"
          :class="{ 'selected': selectedRow && selectedRow.id === row.id }">
          <td>{{ row.id }}</td>
          <td>{{ row.name }}</td>
          <td>{{ row.age }}</td>
        </tr>
      </tbody>
    </table>

    <!-- 子コンポーネントにデータを渡す -->
    <SelectedRowDetails :selectedRow="selectedRow" />
  </div>
</template>

<script>
import SelectedRowDetails from '../../components/Badactor_management/SelectedRowDetails.vue';

export default {
  components: {
    SelectedRowDetails,
  },
  data() {
    return {
      tableData: [
        { id: 1, name: "John Doe", age: 28 },
        { id: 2, name: "Jane Smith", age: 34 },
        { id: 3, name: "Sam Johnson", age: 45 },
      ],
      selectedRow: null,
    };
  },
  methods: {
    selectRow(row) {
      this.selectedRow = row;
    },
  },
};
</script>

<style scoped>
.styled-table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 18px;
  font-family: 'Arial', sans-serif;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.styled-table thead tr {
  background-color: #2c3e50;
  color: #ffffff;
  text-align: left;
}

.styled-table th, .styled-table td {
  padding: 12px 15px;
}

.styled-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
  background-color: #ecf0f1;
}

.styled-table tbody tr:nth-of-type(odd) {
  background-color: #bdc3c7;
}

.styled-table tbody tr:hover {
  background-color: #3498db;
  cursor: pointer;
  color: #ffffff;
}

.styled-table tbody tr.selected {
  background-color: #2980b9;
  color: #ffffff;
}

.styled-table tbody tr:last-of-type {
  border-bottom: 2px solid #2c3e50;
}
</style>
