<template>
  <div class="base-content">
    <section class="content">
      <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
          <TabPanel header="Precision and Accuracy">
            <div>
              <PrecisionAndAccuracy />
            </div>
          </TabPanel>
          <TabPanel header="FTA Analysis">
            <p class="line-height-3 m-0">FTA Analysis content goes here.</p>
          </TabPanel>
          <TabPanel header="Trouble History">
            <p class="line-height-3 m-0">Trouble History content goes here.</p>
          </TabPanel>
        </TabView>
      </div>
    </section>
  </div>
</template>

<script>
import PrecisionAndAccuracy from '@/components/Badactor_management/PrecisionAndAccuracy.vue';

export default {
  components: {
    PrecisionAndAccuracy,
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
