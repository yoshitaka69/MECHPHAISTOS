<template>
  <Handsontable :members="members" :department="department" @getTableContents="getTableContents"/>
</template>
<script>
import api from "axios";
import Handsontable from "@/views/pages/Handsontable.vue";

export default {
  name: "TableIndex",
  components: {
    Handsontable
  },
  data: function() {
    return {
      members: [],
      department: []
    };
  },
  computed: {
    getUrl: () => "http://localhost:3000"
  },
 methods: {
    getMembers: function() {
      return api.get(`${this.getUrl}/members`);
    },
    getDepartment: function() {
      return api.get(`${this.getUrl}/department`);
    },
    getTableContents: async function() {
      const getData = await api.all([this.getMembers(), this.getDepartment()]);
      const membersData = getData[0].data;
      const departmentData = getData[1].data;
this.members = membersData;
      this.department = departmentData;
    }
  }
};
</script>
<style></style>