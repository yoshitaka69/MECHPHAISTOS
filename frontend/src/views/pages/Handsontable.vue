<template>
    <div>
      <HotTable :data="members" :settings="hotSettings"/>
    </div>
</template>

  <script>
  import { HotTable } from "@handsontable/vue3";
  import 'handsontable/dist/handsontable.full.css';

  export default {
    name: "Handsontable",
    components: {
      HotTable
    },
    props: {
      members: {
        type: Array,
        default: []
      },
      department: {
        type: Array,
        default: []
      }
    },
    data: function() {
      return {
        hotSettings: {
          licenseKey: 'non-commercial-and-evaluation',
          colHeaders: true,
          rowHeaders: true,
          columns: [
            { data: "id", type: "text", placeholder: "ID" },
            { data: "name", type: "text", placeholder: "name" },
            { data: "mail", type: "text", placeholder: "mail" },
            { data: "department", type: "text", placeholder: "department" },
            { data: "position", type: "text", placeholder: "position" }
          ]
        }
      };
    },
    created: async function() {
      await this.$emit("getTableContents");
    },
   methods: {
      getTableData: function() {
        this.$refs.hotTable.hotInstance.render();
        console.log(this.$refs.hotTable.hotInstance.getData());
      }
    }
  };
  </script>