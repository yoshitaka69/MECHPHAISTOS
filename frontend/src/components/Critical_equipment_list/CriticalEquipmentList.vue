<template>
    <div id="CeList">
      <div class="legend">
        <div class="legend-item">
          <div class="color-box" style="background-color: #f0a0a0"></div>
          <span>Form input format is incorrect</span>
        </div>
        <div class="legend-item">
          <div class="color-box" style="background-color: #f0f0f0"></div>
          <span>Input not allowed. Value is automatically filled.</span>
        </div>
      </div>
      <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
      <div class="button-container">
        <input type="number" v-model="rowsToAdd" placeholder="Number of rows" />
        <button @click="addRows">Add Rows</button>
        <button @click="saveData">Save</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import Handsontable from "handsontable";
  import { defineComponent } from "vue";
  import { HotTable } from "@handsontable/vue3";
  import { registerAllModules } from "handsontable/registry";
  import "handsontable/dist/handsontable.full.css";
  import { useUserStore } from "@/stores/userStore"; // Piniaストアをインポート
  
  // register Handsontable's modules
  registerAllModules();
  
  function applyBaseStyle(td) {
    if (td && td.style) {
      td.style.backgroundColor = "#F0F0F0"; // 灰色
      td.style.color = "black";
    }
  }
  
  // カスタムレンダラー関数
  function customRenderer(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
    const impactColIndex = 15;
    if (col === impactColIndex) {
      if (value === "High+") {
        td.style.backgroundColor = "#FF0000";
      } else if (value === "High") {
        td.style.backgroundColor = "#FFC000";
      } else if (value === "Middle") {
        td.style.backgroundColor = "#f9d909";
      } else if (value === "Low") {
        td.style.backgroundColor = "#00B050";
      }
    }
  }
  
  function customRendererForProbability(
    instance,
    td,
    row,
    col,
    prop,
    value,
    cellProperties
  ) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
    const probabilityColIndex = 16;
    if (col === probabilityColIndex) {
      switch (value) {
        case "Caution":
          td.style.backgroundColor = "#f9d909";
          break;
        case "Measures":
          td.style.backgroundColor = "#f99d09";
          break;
        case "Danger":
          td.style.backgroundColor = "#f90909";
          break;
        case "Review":
          td.style.backgroundColor = "#4c7c04";
          break;
        case "Appropriate":
          td.style.backgroundColor = "#a0d070";
          break;
      }
    }
  }
  
  function customRendererForReadOnlyCells(
    instance,
    td,
    row,
    col,
    prop,
    value,
    cellProperties
  ) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
  }
  
  function customRendererForCeListNo(
    instance,
    td,
    row,
    col,
    prop,
    value,
    cellProperties
  ) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
  
    td.style.cursor = "pointer"; // ポインタに変更してクリック可能に見せる
    td.style.color = "blue"; // テキスト色を青に設定
    td.style.textDecoration = "underline"; // テキストに下線を付ける
  
    // クリックイベントを追加
    td.addEventListener("click", () => {
      if (value) {
        window.open(`/celist_detail/${value}`, "_blank"); // 新しいタブで詳細ページを開く
      }
    });
  }
  
  function customRendererForAssessment(
    instance,
    td,
    row,
    col,
    prop,
    value,
    cellProperties
  ) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
  
    const rcaOrReplaceColIndex = 25; // 'RCA or <br>Replace(hard)'列のインデックス
    const rcaOrReplaceValue = instance.getDataAtCell(row, rcaOrReplaceColIndex);
  
    const probabilityOfFailureColIndex = 16; // 'Probability <br>of failure'列のインデックス
    const probabilityOfFailureValue = instance.getDataAtCell(
      row,
      probabilityOfFailureColIndex
    );
  
    const coveredFromTaskColIndex = 27; // 'Covered <br>from task'列のインデックス
    const coveredFromTaskValue = instance.getDataAtCell(row, coveredFromTaskColIndex);
  
    // 'Covered <br>from task'にチェックが入っていた場合、このセルに'PM Task'を表示
    if (coveredFromTaskValue === true) {
      value = "PM Task";
      td.innerText = "PM Task";
    }
  
    // 'RCA or <br>Replace(hard)'にチェックが入っていた場合、このセルに'Dealt'を表示
    if (rcaOrReplaceValue === true) {
      value = "Dealt";
      td.innerText = "Dealt";
    }
  
    if (value === "Dealt") {
      td.style.backgroundColor = "#92D050"; // 緑色
    } else if (probabilityOfFailureValue === "Review") {
      td.style.backgroundColor = "#00B050"; // 濃い緑色
    } else if (value === "PM Task") {
      td.style.backgroundColor = "#FFFF00"; // 黄色
    }
  
    const impactForProductionColIndex = 15;
    const impactForProductionValue = instance.getDataAtCell(
      row,
      impactForProductionColIndex
    );
  
    if (value !== "Dealt" && value !== "Review" && value !== "PM Task") {
      if (
        impactForProductionValue === "High+" ||
        probabilityOfFailureValue === "Danger"
      ) {
        td.style.backgroundColor = "#FF0000"; // 赤色
      } else if (
        impactForProductionValue === "High" ||
        probabilityOfFailureValue === "Measures"
      ) {
        td.style.backgroundColor = "#FFC000"; // オレンジ色
      }
    }
  }
  
  function customRendererForNextEventYear(
    instance,
    td,
    row,
    col,
    prop,
    value,
    cellProperties
  ) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
  
    const latestPM02ColIndex = 10; // LatestPM02列のインデックス
    const periodColIndex = 20; // Period列のインデックス
  
    const latestPM02Value = instance.getDataAtCell(row, latestPM02ColIndex);
    const periodValue = instance.getDataAtCell(row, periodColIndex);
  
    if (latestPM02Value && periodValue) {
      const latestPM02Date = new Date(latestPM02Value);
      const nextEventDate = new Date(latestPM02Date);
      nextEventDate.setDate(latestPM02Date.getDate() + parseInt(periodValue));
  
      const formattedDate = nextEventDate.toISOString().split("T")[0];
      td.innerText = formattedDate;
  
      // セルのメタデータとして次のイベント日付を保存
      cellProperties.nextEventDate = nextEventDate;
    }
  }
  
  function customRendererForSituation(
    instance,
    td,
    row,
    col,
    prop,
    value,
    cellProperties
  ) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
  
    const currentDate = new Date();
  
    // nextEventDate を customRendererForNextEventYear から取得
    const nextEventYearColIndex = 21; // NextEventYear列のインデックス
    const nextEventCellMeta = instance.getCellMeta(row, nextEventYearColIndex);
    const nextEventDate = nextEventCellMeta.nextEventDate;
  
    if (nextEventDate && currentDate > nextEventDate) {
      td.style.backgroundColor = "#FFFF00";
      td.innerText = "Delay";
    } else if (value === "Delay") {
      td.style.backgroundColor = "#FFFF00";
    }
  }
  
  function customRendererForMttr(
    instance,
    td,
    row,
    col,
    prop,
    value,
    cellProperties
  ) {
    if (td) {
      Handsontable.renderers.TextRenderer.apply(this, arguments);
      applyBaseStyle(td);
    }
  
    const constructionPeriodColIndex = 5;
    const partsDeliveryDateColIndex = 6;
    const constructionPeriod = instance.getDataAtCell(row, constructionPeriodColIndex);
    const partsDeliveryDate = instance.getDataAtCell(row, partsDeliveryDateColIndex);
    const mttrValue = Math.max(constructionPeriod, partsDeliveryDate);
  
    if (td) {
      // nullチェックを追加
      td.innerHTML = mttrValue === 0 ? "" : mttrValue;
    }
  
    return mttrValue; // MTTR値を返す
  }
  
  const CriticalEquipmentList = defineComponent({
    props: {
      riskTexts: {
        type: Array,
        required: true,
      },
    },
    data() {
      return {
        hotSettings: {
          data: [
            [
              "",
              "PlantA",
              "モーターA",
              "N401/A plant__",
              "4",
              "10",
              "6",
              "10",
              "4",
              "今年",
              "2022-10-02",
              "3",
              "2019-11-01",
              "0",
              "",
              "High+",
              "",
              "対策済",
              "A plant/変換器室 変換器盤1-3パワーサプライ交換",
              "10000",
              "3",
              "2025",
              "",
              "Standard",
              "",
              "",
              "",
              "",
              "",
            ], //1
            [
              "",
              "PlantA",
              "モーターA",
              "N401/A plant__/OX2_",
              "3",
              "10",
              "6",
              "10",
              "4",
              "",
              "",
              "4",
              "2018-08-10",
              "",
              "",
              "High",
              "対策検討",
              "",
              "",
              "750000",
              "3",
              "",
              "遅延",
              "",
              "",
              "",
              "",
              "",
              "",
            ], //2
            [
              "",
              "PlantB",
              "Attach系機械設備",
              "N401/A plant__/OX2_/A",
              "3",
              "10",
              "6",
              "10",
              "今年",
              "2",
              "2022-05-20",
              "0",
              "",
              "",
              "",
              "",
              "注意",
              "",
              "A plant/Di槽撹拌機交換（A）",
              "5000",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
            ], //3
            [
              "",
              "PlantC",
              "回収温水熱交",
              "N401/A plant__/OX2_/A/5E-09",
              "3",
              "10",
              "60",
              "10",
              "4",
              "",
              "",
              "",
              "",
              "",
              "",
              "Low",
              "見直検討",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
            ], //4
          ],
          nestedHeaders: [
            [
              "",
              "",
              "",
              "",
              { label: "Impact", colspan: 5 },
              { label: "Probability of failure", colspan: 6 },
              { label: "Critical equipment Level", colspan: 3 },
              "",
              "",
              "",
              "",
              "",
              { label: "Spare parts", colspan: 2 },
              { label: "Status of measures", colspan: 4 },
              { label: "Order", colspan: 2 },
            ],
            [
              "CeListNo",
              "Plant",
              "Equipment",
              "Machine",
              "Level set <br>value",
              "Construction <br>period",
              "Parts <br>delivery date",
              "MTTR",
              "PossibilityOf<br>ContinuousProduction",
              "Count <br>of PM02",
              "Latest <br>PM02",
              "Count <br>of PM03",
              "Latest <br>PM03",
              "Count <br>of PM04",
              "Latest <br>PM04",
              "Impact for <br>production",
              "Probability <br>of failure",
              "Assessment",
              "Typical Task",
              "Labor <br>Cost(PM02)",
              "Period",
              "Next <br>event date",
              "situation",
              "BomCode",
              "Stock",
              "RCA or <br>Replace(hard)",
              "Spear parts or <br>Alternative(soft)",
              "Covered <br>from task",
              "Two <br>ways",
            ],
          ],
  
          columns: [
            {
              data: "ceListNo",
              type: "text",
              readOnly: true,
              renderer: customRendererForCeListNo,
            },
            { data: "plant", type: "text" },
            { data: "equipment", type: "text" },
            { data: "machineName", type: "text" },
            {
              data: "levelSetValue",
              type: "dropdown",
              source: ["Low", "Middle", "High"],
            },
            { data: "typicalConstPeriod", type: "numeric" },
            { data: "maxPartsDeliveryTimeInBom", type: "numeric" },
            { data: "mttr", type: "numeric", renderer: customRendererForMttr },
            {
              data: "possibilityOfContinuousProduction",
              type: "dropdown",
              source: [1, 2, 3, 4, 5],
              className: "htRight",
              readOnly: false,
            },
            {
              data: "countOfPM02",
              width: 100,
              className: "htRight",
              type: "numeric",
            },
            {
              data: "latestPM02",
              width: 100,
              className: "htRight",
              type: "date",
              dateFormat: "YYYY-MM-DD",
              correctFormat: false,
            },
            {
              data: "countOfPM03",
              width: 100,
              className: "htRight",
              type: "numeric",
            },
            {
              data: "latestPM03",
              width: 100,
              className: "htRight",
              type: "date",
              dateFormat: "YYYY-MM-DD",
              correctFormat: false,
            },
            {
              data: "countOfPM04",
              width: 100,
              className: "htRight",
              type: "numeric",
            },
            {
              data: "latestPM04",
              width: 100,
              className: "htRight",
              type: "date",
              dateFormat: "YYYY-MM-DD",
              correctFormat: false,
            },
            {
              data: "impactForProduction",
              renderer: customRenderer,
              width: 100,
              className: "htCenter",
              readOnly: true,
            },
            {
              data: "probabilityOfFailure",
              renderer: customRendererForProbability,
              width: 100,
              className: "htCenter",
              readOnly: false,
            },
            {
              data: "assessment",
              renderer: customRendererForAssessment,
              readOnly: true,
              width: 100,
              className: "htCenter",
            },
            {
              data: "typicalTaskName",
              type: "text",
              readOnly: true,
              renderer: customRendererForReadOnlyCells,
            },
            {
              data: "typicalTaskCost",
              type: "numeric",
              readOnly: true,
              renderer: customRendererForReadOnlyCells,
            },
            {
              data: "typicalConstPeriod",
              type: "numeric",
              readOnly: true,
              renderer: customRendererForReadOnlyCells,
            },
            {
              data: "typicalNextEventDate",
              className: "htRight",
              type: "date",
              dateFormat: "YYYY-MM-DD",
              correctFormat: false,
              readOnly: true,
              renderer: customRendererForNextEventYear,
            },
            {
              data: "typicalSituation",
              className: "htCenter",
              renderer: customRendererForSituation,
              readOnly: true,
            },
            {
              data: "bomCode",
              className: "htRight",
              type: "text",
              readOnly: true,
              renderer: customRendererForReadOnlyCells,
            },
            {
              data: "bomStock",
              type: "dropdown",
              source: ["有", "無"],
              className: "htCenter",
              readOnly: true,
              renderer: customRendererForReadOnlyCells,
            },
            { data: "rcaOrReplace", width: 100, className: "htCenter", type: "checkbox" },
            {
              data: "sparePartsOrAlternative",
              width: 100,
              className: "htCenter",
              type: "checkbox",
            },
            { data: "coveredFromTask", width: 100, className: "htCenter", type: "checkbox" },
            { data: "twoways", width: 100, className: "htCenter", type: "checkbox" },
          ],
          rowHeaders: true, // 行ヘッダーを有効化
  
          afterGetColHeader: (col, TH) => {
            if (col === -1) {
              return;
            }
            TH.style.backgroundColor = "#FFCC99";
            TH.style.color = "black";
            TH.style.fontWeight = "bold";
          },
  
          width: "100%",
          height: "auto",
          stretchH: "all",
          contextMenu: true,
          autoWrapRow: true,
          autoWrapCol: true,
          fixedColumnsStart: 2,
          fixedRowsTop: 2,
          manualColumnFreeze: true,
          manualColumnResize: true,
          manualRowResize: true,
          filters: true,
          dropdownMenu: true,
          comments: true,
          fillHandle: {
            autoInsertRow: true,
          },
          licenseKey: "non-commercial-and-evaluation",
          afterChange: (changes, source) => {
            if (source !== "loadData") {
              changes.forEach(([row, prop, oldValue, newValue]) => {
                const relevantColumns = [
                  "levelSetValue",
                  "mttr",
                  "possibilityOfContinuousProduction",
                  "countOfPM02",
                  "countOfPM03",
                  "countOfPM04",
                ];
  
                if (relevantColumns.includes(prop)) {
                  this.emitData();
                }
              });
            }
          },
        },
        rowsToAdd: 1, // 追加する行数のデフォルト値
        dataStore: [], // データストア
      };
    },
  
    created() {
      this.getDataAxios();
    },
  
    methods: {
      // Handsontableの初期化
      initHandsontable() {
        const container = this.$el;
        this.hot = new Handsontable(container, {
          afterChange: (changes, source) => {
            if (source !== "loadData") {
              const data = this.hot.getData();
              this.emitData();
            }
          },
        });
      },
  
      // Axiosを使用してデータを取得
      getDataAxios() {
        const userStore = useUserStore();
        const userCompanyCode = userStore.companyCode;
  
        if (!userCompanyCode) {
          console.error("Error: No company code found for the user.");
          return;
        }
  
        const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${userCompanyCode}`;
  
        axios
          .get(url, {
            headers: {
              "Content-Type": "application/json",
            },
            withCredentials: true,
          })
          .then((response) => {
            console.log("Raw response data:", response.data); // デバッグ用
            const masterDataTable = response.data;
            console.log("Fetched masterDataTable:", masterDataTable);
  
            this.dataStore = masterDataTable; // データストアに保存
  
            const blankRows = Array.from({ length: 10 }, () => ({}));
            const newData = masterDataTable.concat(blankRows);
  
            this.$refs.hotTableComponent.hotInstance.loadData(newData);
          })
          .catch((error) => {
            console.error("Error fetching data:", error);
          });
      },
  
      addRows() {
        const hotInstance = this.$refs.hotTableComponent.hotInstance;
        const blankRows = Array.from({ length: this.rowsToAdd }, () => {
          return {
            ceListNo: "",
            plant: "",
            equipment: "",
            machineName: "",
            levelSetValue: "",
            typicalConstPeriod: 0,
            maxPartsDeliveryTimeInBom: 0,
            mttr: 0,
            possibilityOfContinuousProduction: "",
            countOfPM02: 0,
            latestPM02: "",
            countOfPM03: 0,
            latestPM03: "",
            countOfPM04: 0,
            latestPM04: "",
            impactForProduction: "",
            probabilityOfFailure: "",
            assessment: "",
            typicalTaskName: "",
            typicalTaskCost: 0,
            typicalNextEventDate: "",
            typicalSituation: "",
            bomCode: "",
            bomStock: "",
            rcaOrReplace: false,
            sparePartsOrAlternative: false,
            coveredFromTask: false,
            twoways: false,
          };
        });
  
        this.dataStore = this.dataStore.concat(blankRows);
  
        hotInstance.updateSettings({
          data: this.dataStore,
        });
      },
  
      saveData() {
        const userStore = useUserStore();
        const userCompanyCode = userStore.companyCode;
  
        if (!userCompanyCode) {
          console.error("Error: No company code found for the user.");
          return;
        }
  
        const hotInstance = this.$refs.hotTableComponent.hotInstance;
        const dataToSave = hotInstance.getData();
  
        const formattedData = {
          companyCode: userCompanyCode,
          MasterDataTable: dataToSave.map((row) => {
            return {
              companyCode: userCompanyCode,
              ceListNo: row[0],
              plant: row[1],
              equipment: row[2],
              machineName: row[3],
              levelSetValue: row[4],
              typicalConstPeriod: row[5],
              maxPartsDeliveryTimeInBom: row[6],
              mttr: row[7],
              probabilityOfFailure: row[8],
              countOfPM02: row[9],
              latestPM02: row[10],
              countOfPM03: row[11],
              latestPM03: row[12],
              countOfPM04: row[13],
              latestPM04: row[14],
              impactForProduction: row[15],
              assessment: row[16],
              typicalTaskName: row[17] ? row[17].toString() : null,
              typicalTaskCost: row[18],
              typicalNextEventDate: row[19],
              typicalSituation: row[20],
              bomCode: row[21],
              bomStock: row[22],
              rcaOrReplace: row[23],
              sparePartsOrAlternative: row[24],
              coveredFromTask: row[25],
              twoways: row[26],
              ceDescription: row[27],
            };
          }),
        };
  
        console.log("Data to be sent:", formattedData);
  
        const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/`;
  
        axios
          .post(url, formattedData, {
            headers: {
              "Content-Type": "application/json",
            },
            withCredentials: true,
          })
          .then((response) => {
            console.log("Data saved successfully:", response.data);
          })
          .catch((error) => {
            console.error("Error saving data:", error);
            if (error.response) {
              console.error("Error response data:", error.response.data);
            }
          });
      },
  
      // データをRiskMatrixにemitする
      emitData() {
        const hotInstance = this.$refs.hotTableComponent.hotInstance;
        const rows = hotInstance.countRows();
        const emittedData = [];
  
        for (let row = 0; row < rows; row++) {
          const levelSetValue = hotInstance.getDataAtCell(row, 4); // levelSetValueの値を取得
          const mttr = customRendererForMttr(hotInstance, null, row, 7); // MTTRの値を取得するためにcustomRendererForMttrを呼び出す
          const possibilityOfContinuousProduction = hotInstance.getDataAtCell(
            row,
            8
          ); // possibilityOfContinuousProductionの値を取得
          const countOfPM02 = hotInstance.getDataAtCell(row, 9); // countOfPM02の値を取得
          const countOfPM03 = hotInstance.getDataAtCell(row, 11); // countOfPM03の値を取得
          const countOfPM04 = hotInstance.getDataAtCell(row, 13); // countOfPM04の値を取得
  
          emittedData.push({
            levelSetValue,
            mttr,
            possibilityOfContinuousProduction,
            countOfPM02,
            countOfPM03,
            countOfPM04,
          });
        }
  
        console.log("Emitting Data:", emittedData);
        this.$emit("data-emitted", emittedData);
      },
  
      // Impact for Productionの更新
      updateImpactForProduction({ index, impactForProduction }) {
        console.log(
          `Updating impactForProduction at row ${index} with value ${impactForProduction}`
        );
        this.$refs.hotTableComponent.hotInstance.setDataAtCell(
          index,
          15,
          impactForProduction
        );
      },
  
      // Probability of Failureの更新
      updateProbabilityOfFailure({ index, probabilityOfFailure }) {
        console.log(
          `Updating probabilityOfFailure at row ${index} with value ${probabilityOfFailure}`
        );
  
        if (typeof index === "number" && index >= 0) {
          // indexが正の整数であることを確認
          this.$refs.hotTableComponent.hotInstance.setDataAtCell(
            index,
            16,
            probabilityOfFailure
          );
        } else {
          console.error("Invalid index value:", index);
        }
      },
  
      openDetailPage(ceListNo) {
        // 詳細ページを新しいタブで開く
        window.open(`/#/ce-list-detail/${ceListNo}`, "_blank");
      },
    },
  
    components: {
      HotTable,
    },
  });
  
  export default CriticalEquipmentList;
  </script>
  
  <style scoped>
  .button-container {
    display: flex;
    gap: 10px;
    margin-top: 10px;
  }
  
  .legend {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
  }
  
  .legend-item {
    display: flex;
    align-items: center;
    margin-right: 15px;
  }
  
  .color-box {
    width: 20px;
    height: 20px;
    margin-right: 10px;
    border: 1px solid #000;
  }
  </style>
  