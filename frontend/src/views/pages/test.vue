<template>
  <div class="base-content">
    <section class="content">
      <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
          <TabPanel header="Breakdown Prediction">
            <div class="accordion">
              <div class="accordion-item">
                <button class="accordion-header" @click="toggleAccordion(0)">
                  <span class="accordion-icon">{{ isActive(0) ? '▶' : '▼' }}</span>
                  Bathtub Curve and Explanation
                </button>
                <div class="accordion-content" :class="{ active: isActive(0) }">
                  <div class="content-wrapper">
                    <div class="bathtub-curve-container">
                      <BathtubCurve class="small-bathtub-curve" />
                    </div>
                    <div class="bathtub-curve-description">
                      <p>
                        The Bathtub Curve is used in reliability engineering to
                        describe the life of a product. The curve consists of three
                        parts: the decreasing failure rate (infant mortality),
                        constant failure rate (useful life), and increasing failure
                        rate (wear-out period). This graphical representation helps
                        in understanding and predicting failures over time.
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </TabPanel>
          <TabPanel header="Cost Estimate">
            <p class="line-height-3 m-0"></p>
            <div id="appCost" style="display: flex;">
              <div style="width: 50%;">
                <RepairCostPredictionChart />
              </div>
              <div style="width: 50%;">
                <AnnualCostPredictionChart />
              </div>
            </div>
          </TabPanel>
        </TabView>
      </div>
    </section>
  </div>
</template>

<script>
//first tab
import BathtubCurve from '@/components/Breakdown_prediction/BathtubCurve.vue';

//second tab
import RepairCostPredictionChart from '@/components/Cost_Prediction/RepairCostPredictionChart.vue';
import AnnualCostPredictionChart from '@/components/Cost_Prediction/AnnualCostPredictionChart.vue';

export default {
  components: {
    BathtubCurve,
    RepairCostPredictionChart,
    AnnualCostPredictionChart,
  },
  data() {
    return {
      activeIndex: parseInt(localStorage.getItem('breakdownPredictionTabIndex')) || 0, // キー名を変更
      activeAccordionIndex: null,
    };
  },
  methods: {
    onTabChange(event) {
      this.activeIndex = event.index;
      localStorage.setItem('breakdownPredictionTabIndex', this.activeIndex); // キー名を変更
    },
    toggleAccordion(index) {
      this.activeAccordionIndex = this.activeAccordionIndex === index ? null : index;
    },
    isActive(index) {
      return this.activeAccordionIndex === index;
    }
  }
};
</script>

<style>
.accordion {
  width: 100%;
}

.accordion-item {
  margin-bottom: 1rem;
}

.accordion-header {
  width: 100%;
  padding: 1rem;
  background-color: #f1f1f1;
  border: none;
  text-align: left;
  cursor: pointer;
  outline: none;
  display: flex;
  align-items: center;
}

.accordion-icon {
  margin-right: 10px;
  font-size: 1.2rem;
}

.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s ease-out;
}

.accordion-content.active {
  max-height: 1000px; /* 十分な高さを設定 */
}

.content-wrapper {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 20px;
}

.bathtub-curve-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.small-bathtub-curve {
  transform: scale(0.8); /* サイズを80%に縮小 */
}

.bathtub-curve-description {
  flex: 1;
  margin-left: 20px;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
