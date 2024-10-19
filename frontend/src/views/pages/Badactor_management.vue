<template>
    <div class="base-content">
      <section class="content">
        <div class="card card-solid">
          <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
            <TabPanel header="Precision and Accuracy">
              <div class="col-12 lg:col-12 xl:col-12">
                <div class="card-header">
                  <h5>Precision and Accuracy</h5>
                  <Castor />
                </div>
              </div>
  
              <!-- 修正箇所: ボタンをPrecisionAndAccuracyの上に配置 -->
              <div class="button-container">
                <button @click="openCeListWindow" class="ce-list-button">Show CeList</button>
              </div>
  
              <div class="component-container">
                <PrecisionAndAccuracy />
              </div>
  
              <div class="table-container">
                <TroubleHistoryTable />
                <PreventMaintenanceTable />
              </div>
            </TabPanel>
  
            <TabPanel header="FTA Analysis">
              <p class="line-height-3 m-0"></p>
              <BadActorList />
              <!-- Tree コンポーネントを中央に配置 -->
              <div class="tree-container">
                <Tree />
              </div>
            </TabPanel>
  
            <TabPanel header="Trouble History">
              <p class="line-height-3 m-0"></p>
              <TroubleTimeline />
              <Pollux />
            </TabPanel>
          </TabView>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import { createApp } from 'vue';
  import PrimeVue from 'primevue/config';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  
  import PrecisionAndAccuracy from '@/components/Badactor_management/Precision_and_Accuracy/PrecisionAndAccuracy.vue';
  import TroubleHistoryTable from '@/components/Badactor_management/Precision_and_Accuracy/TroubleHistoryTable.vue';
  import PreventMaintenanceTable from '@/components/Badactor_management/Precision_and_Accuracy/PreventMaintenanceTable.vue';
  import TroubleTimeline from '@/components/Badactor_management/Trouble_History/TroubleTimeline.vue';
  import Tree from '@/components/Badactor_management/Tree.vue';
  import BadActorList from '@/components/Badactor_management/Bad_actor_list.vue';
  import Pollux from '@/components/Mechphaistos_Ai/Pollux.vue';
  import CeList from '@/components/Badactor_management/Precision_and_Accuracy/CeList.vue';
  import Castor from '@/components/Mechphaistos_Ai/Castor.vue';
  
  export default {
    components: {
      PrecisionAndAccuracy,
      PreventMaintenanceTable,
      Castor,
      TroubleHistoryTable,
      TroubleTimeline,
      Pollux,
      CeList,
      Tree,
      BadActorList
    },
    data() {
      return {
        activeIndex: parseInt(localStorage.getItem('activeTabIndex')) || 0,
        sampleDataX: [],
        sampleDataY: [],
        ceListWindow: null
      };
    },
    mounted() {
      this.generateSampleData();
    },
    methods: {
      onTabChange(event) {
        this.activeIndex = event.index;
        localStorage.setItem('activeTabIndex', this.activeIndex);
      },
      generateSampleData() {
        this.sampleDataX = Array.from({ length: 100 }, () => Math.random() * 2 - 1);
        this.sampleDataY = Array.from({ length: 100 }, () => Math.random() * 2 - 1);
      },
      openCeListWindow() {
        if (!this.ceListWindow || this.ceListWindow.closed) {
          this.ceListWindow = window.open('', 'CeListWindow', 'width=600,height=400,scrollbars=no,resizable=yes');
          this.ceListWindow.document.write('<div id="ceList"></div>');
          this.ceListWindow.document.close();
  
          const stylesheets = Array.from(document.styleSheets);
          stylesheets.forEach((stylesheet) => {
            if (stylesheet.href) {
              const link = document.createElement('link');
              link.rel = 'stylesheet';
              link.href = stylesheet.href;
              this.ceListWindow.document.head.appendChild(link);
            } else {
              const style = document.createElement('style');
              style.textContent = Array.from(stylesheet.cssRules)
                .map((rule) => rule.cssText)
                .join('\n');
              this.ceListWindow.document.head.appendChild(style);
            }
          });
  
          const ceListApp = createApp(CeList);
          ceListApp.use(PrimeVue);
          ceListApp.component('DataTable', DataTable);
          ceListApp.component('Column', Column);
          ceListApp.mount(this.ceListWindow.document.getElementById('ceList'));
        } else {
          this.ceListWindow.focus();
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .card-header {
    background-color: #ffecb3;
    padding: 1rem;
    border-bottom: 1px solid #dee2e6;
  }
  
  .component-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  .button-container {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 1rem;
  }
  
  .ce-list-button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .ce-list-button:hover {
    background-color: #0056b3;
  }
  
  .table-container {
    display: flex;
    justify-content: space-between;
  }
  
  .table-container > * {
    flex: 1;
    margin-right: 1rem;
  }
  
  .table-container > *:last-child {
    margin-right: 0;
  }
  
  /* Tree コンポーネントを中央に配置 */
  .tree-container {
    display: flex;
    justify-content: center;
  }
  </style>
  