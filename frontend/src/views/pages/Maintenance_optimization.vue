<template>
  <div class="base-content">
    <section class="content">
      <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
          <TabPanel header="Maintenance Optimization">
            <p class="line-height-3 m-0"></p>
            <OptimaizeByBaize />
          </TabPanel>
        </TabView>
      </div>
    </section>
  </div>
</template>

<script>
import OptimaizeByBaize from '@/components/Maintenance_Optimization/OptimaizeByBaize.vue';

export default {
  components: {
    OptimaizeByBaize,
  },
  data() {
    return {
      activeIndex: parseInt(localStorage.getItem('maintenanceOptimizationTabIndex')) || 0 // キー名を変更
    };
  },
  methods: {
    onTabChange(event) {
      this.activeIndex = event.index;
      localStorage.setItem('maintenanceOptimizationTabIndex', this.activeIndex); // キー名を変更
    }
  }
};
</script>

<style>
.row {
  display: flex;
  flex-wrap: wrap;
}

.risk-matrix-container {
  display: flex;
  flex-direction: column;
  gap: 40px;
  /* コンポーネント間の隙間 */
}

.risk-matrix-item {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
