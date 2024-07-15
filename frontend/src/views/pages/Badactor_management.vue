<template>
  <div class="base-content">
    <section class="content">
      <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
          <TabPanel header="Precision and Accuracy">
            <div class="col-12 lg:col-12 xl:col-12">
              <PrecisionAndAccuracyInfo />
            </div>
            <div class="component-container">
              <PrecisionAndAccuracy />
              <CeList />
            </div>
            <div class="table-container">
              <TroubleHistoryTable />
              <PreventMaintenanceTable />
            </div>
          </TabPanel>
          <TabPanel header="FTA Analysis">
            <p class="line-height-3 m-0">FTA Analysis content goes here.</p>
            <div class="fta-container">
              <Tree />
              <HierarchicalEdgeBundling />
            </div>
          </TabPanel>
          <TabPanel header="Trouble History">
            <p class="line-height-3 m-0">Trouble History content goes here.</p>
            <TroubleTimeline />
            <Mechphaistos_Ai />
          </TabPanel>
        </TabView>
      </div>
    </section>
  </div>
</template>

<script>
import PrecisionAndAccuracy from '@/components/Badactor_management/Precision_and_Accuracy/PrecisionAndAccuracy.vue';
import TroubleHistoryTable from '@/components/Badactor_management/Precision_and_Accuracy/TroubleHistoryTable.vue';
import PreventMaintenanceTable from '@/components/Badactor_management/Precision_and_Accuracy/PreventMaintenanceTable.vue';
import TroubleTimeline from '@/components/Badactor_management/Trouble_History/TroubleTimeline.vue';
import Tree from '@/components/Badactor_management/Tree.vue';
import HierarchicalEdgeBundling from '@/components/Badactor_management/HierarchicalEdgeBundling.vue';
import Mechphaistos_Ai from '@/components/Mechphaistos_Ai/Mechphaistos_Ai.vue';
import CeList from '@/components/Badactor_management/Precision_and_Accuracy/CeList.vue';
import PrecisionAndAccuracyInfo from '@/components/Badactor_management/Precision_and_Accuracy/Card/PrecisionAndAccuracyInfo.vue';

export default {
  components: {
    PrecisionAndAccuracy,
    PreventMaintenanceTable,
    PrecisionAndAccuracyInfo,
    TroubleHistoryTable,
    TroubleTimeline,
    Mechphaistos_Ai,
    CeList,
    Tree,
    HierarchicalEdgeBundling,
  },
  data() {
    return {
      activeIndex: parseInt(localStorage.getItem('activeTabIndex')) || 0,
      sampleDataX: [],
      sampleDataY: [],
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
  },
};
</script>

<style scoped>
.component-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem; /* 下に少し余白を追加 */
}

.component-container > * {
  flex: 1;
  margin-right: 1rem;
}

.component-container > *:last-child {
  margin-right: 0;
}

.component-container > :first-child {
  margin-right: 1rem;
}

.component-container > :last-child {
  margin-right: 0;
  margin-top: 1rem; /* CeListの上に余白を追加 */
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

.fta-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.fta-container > * {
  margin-bottom: 2rem; /* 間に余白を追加 */
}

.fta-container > *:last-child {
  margin-bottom: 0;
}
</style>
