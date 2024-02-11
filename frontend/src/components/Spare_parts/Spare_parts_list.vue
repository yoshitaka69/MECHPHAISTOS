<template>
    <div id="Spare_parts_list">
      <h2>Spare Parts List</h2>
      <HotTable ref="hotTableComponent" :settings="hotSettings"></HotTable>
    </div>
  </template>
  
  <script>
  import { HotTable } from "@handsontable/vue3";
  import axios from "axios";
  import 'handsontable/dist/handsontable.full.css';
  
  const URL = "http://localhost:3000/SpareParts";
  
  export default {
    created() {
      this.getDataAxios();
    },
  
    methods: {
      async getDataAxios() {
        try {
          const response = await axios.get(URL);
          const data = response.data;
  
          this.$refs.hotTableComponent.hotInstance.updateSettings({
            data: data,
          });
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      }
    },
  
    data: () => ({
      hotSettings: {
        colHeaders: [
          "Image",
          "Id",
          "Parts Name",
          "Category",
          "Model",
          "Serial Number",
          "Task Name",
          "Price",
          "Number of ~",
          "Unit",
          "Location",
          "Delivery Time",
          "Description",
        ],
        licenseKey: 'non-commercial-and-evaluation',
      }
    }),
  
    components: {
      HotTable
    }
  };
  </script>
  