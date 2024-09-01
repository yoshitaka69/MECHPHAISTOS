<template>
  <div class="base-content">
    <section class="content">
      <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
          <TabPanel header="Work Order List">
            <p class="line-height-3 m-0">
              <Work_order_list />
            </p>
          </TabPanel>
          <TabPanel header="Work Order Permission">
            <p class="line-height-3 m-0">
              <Work_permission />
            </p>
          </TabPanel>
          <TabPanel header="Work order management">
            <div class="tree-map-grid">
              <Failure_type_tree_map />
              <Failure_mode_tree_map />
              <Equipment_tree_map />
            </div>
          </TabPanel>
        </TabView>
      </div>
    </section>
  </div>
</template>

<script>
import Work_permission from '@/components/Work_permission/Work_permission_list.vue';
import Work_order_list from '@/components/Work_order/Work_order_list.vue';
import Failure_type_tree_map from '@/components/Work_order/Failure_type_tree_map.vue';
import Failure_mode_tree_map from '@/components/Work_order/Failure_mode_tree_map.vue';
import Equipment_tree_map from '@/components/Work_order/Equipment_tree_map.vue';

export default {
  components: {
    Work_order_list,
    Work_permission,
    Failure_type_tree_map,
    Failure_mode_tree_map,
    Equipment_tree_map
  },
  data() {
    return {
      activeIndex: parseInt(localStorage.getItem('workOrderTabIndex')) || 0 // キー名を変更
    };
  },
  methods: {
    onTabChange(event) {
      this.activeIndex = event.index;
      localStorage.setItem('workOrderTabIndex', this.activeIndex); // キー名を変更
    }
  }
};
</script>

<style>
.tree-map-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px; /* グリッド間のスペースを調整 */
}

.tree-map-grid > * {
  /* 各TreeMapコンポーネントに対して幅と高さを設定 */
  width: 100%;
  height: 400px; /* 必要に応じて高さを調整 */
}
</style>
