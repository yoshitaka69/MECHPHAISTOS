<template>
  <div class="base-content">
    <section class="content">
      <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
          <TabPanel header="Precision and Accuracy">
            <div>
              <PrecisionAndAccuracy />
              <TroubleHistoryTable />
              <PreventMaintenanceTable />
            </div>
          </TabPanel>
          <TabPanel header="FTA Analysis">
            <p class="line-height-3 m-0">FTA Analysis content goes here.</p>
            <Tree />
            <HierarchicalEdgeBundling />
          </TabPanel>
          <TabPanel header="Trouble History">
            <p class="line-height-3 m-0">Trouble History content goes here.</p>
            <TroubleTimeline />
          </TabPanel>
        </TabView>
      </div>
    </section>
  </div>
</template>

<script>
import PrecisionAndAccuracy from '@/components/Badactor_management/PrecisionAndAccuracy.vue';
import TroubleHistoryTable from '@/components/Badactor_management/TroubleHistoryTable.vue';
import PreventMaintenanceTable from '@/components/Badactor_management/PreventMaintenanceTable.vue';
import TroubleTimeline from '@/components/Badactor_management/TroubleTimeline.vue';
import Tree from '@/components/Badactor_management/Tree.vue';
import HierarchicalEdgeBundling from '@/components/Badactor_management/HierarchicalEdgeBundling.vue';

export default {
  components: {
    PrecisionAndAccuracy,
    PreventMaintenanceTable,
    TroubleHistoryTable,
    TroubleTimeline,
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
