<template>
  <div class="base-content">
    <section class="content">
      <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
          <TabPanel header="Drawing ledger">
            <p class="line-height-3 m-0 description-text">This table displays management information related to CAD design drawings.</p>

            <CAD_Drawing_ledger />

          </TabPanel>
        </TabView>
      </div>
    </section>
  </div>
</template>

<script>
import CAD_Drawing_ledger from '@/components/Drawing_ledger/Drawing_ledger.vue';

export default {
  components: {
    CAD_Drawing_ledger
  },
  data() {
    return {
      activeIndex: parseInt(localStorage.getItem('cadDrawingActiveTabIndex')) || 0 // キー名を変更
    };
  },
  methods: {
    onTabChange(event) {
      this.activeIndex = event.index;
      localStorage.setItem('cadDrawingActiveTabIndex', this.activeIndex); // キー名を変更
    }
  }
};
</script>

<style>
.description-text {
  font-size: 1.2rem; /* フォントサイズを一回り大きく設定 */
}

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
