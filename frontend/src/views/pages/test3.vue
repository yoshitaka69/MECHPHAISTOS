<template>
    <div id="example1">
      <h>test</h>
      <HotTable ref="hotTableComponent" :settings="hotSettings"></HotTable>
    </div>
  </template>
  

  <script>
  import { HotTable } from "@handsontable/vue3";
  import axios from "axios";
  import 'handsontable/dist/handsontable.full.css';
  
  const URL = "http://localhost:3000";
  


  export default {
    created() {
      this.getDataAxios();
      // UnComment setData() to see data loading work without axios...
      //↑アクシオスを使用しない場合は、セットデータを読み込む
      // this.setData()
    },
  
    methods: {
      setData() {
        this.hotSettings.colHeaders = ["h1", "h2", "h3"];
        this.hotSettings.columns = [
          { type: "text" },
          { type: "text" },
          { type: "text" }
        ];
        this.hotSettings.data = [
          ["no ax", "no ax", "no ax"],
          ["no", "axios", "request"]
        ];
      },
  
      getDataAxios() {
        axios
          .get(URL, {
            method: "GET",
            mode: "no-cors",
            headers: {
              "Access-Control-Allow-Origin": "*",
              "Content-Type": "application/json"
            },
            withCredentials: true,
            credentials: "same-origin"
          })
          .then(response => {
            const data = response.data;
            const id = data.id;
            const mail = data.mail;
            // Handle Axios logic here
            // console.log(response.data)
            // Set data...
            // In practice this will be from response.data
            this.$refs.hotTableComponent.hotInstance.updateSettings({
              data: data,
              colHeaders: [id, mail],
              columns: [{ data: "id" }, { data: "mail" }]
            });
          })
          .catch(error => console.log("error"));
  
        // Data Is oaded properly if outside of axios call...
        // UnComment for success...
        // this.hotSettings.data = [
        //    ["ax", "ax", "ax"],
        //    ["outside", "of", "request"]
        //   ]
      }
    },
  
    data: () => ({
      data: null,
      hotSettings: {
        data: null,
        colHeaders: [
          "Data Uploaded on",
          "Duration in Minutes",
          "Start Time",
          "Shift",
          "Description",
          "Next Day Spill Over",
          "Site Name"
        ],
        columns: [
          { type: "text" },
          { type: "text" },
          { type: "text" },
          { type: "text" },
          { type: "text" },
          { type: "text" },
          { type: "text" }
        ],
        rowHeaders: true,
        manualRowMove: true,
        contextMenu: true,
        licenseKey: 'non-commercial-and-evaluation',
      }
    }),

    components: {
      HotTable
    }
  };
  </script>
  