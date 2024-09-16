<template>
    <div class="base-content">
      <section class="content">
        <div class="card card-solid">
          <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
            <TabPanel header="NearMiss List">
              <div class="line-height-3 m-0">
                <div class="flex flex-wrap justify-content-between">
                  <div class="col-12 lg:col-4 xl:col-4">
                    <div class="card card-light-yellow mb-0">
                      <div class="flex justify-content-between mb-3" style="height: 150px">
                        <Count_of_nearMiss />
                      </div>
                    </div>
                  </div>
                  <div class="col-12 lg:col-4 xl:col-4">
                    <div class="card card-light-yellow mb-0">
                      <div class="flex justify-content-between mb-3" style="height: 150px">
                        <Action_items />
                      </div>
                    </div>
                  </div>
                  <div class="col-12 lg:col-4 xl:col-4">
                    <div class="card card-light-yellow mb-0">
                      <div class="flex justify-content-between mb-3" style="height: 150px">
                        <Safety_clock />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="spacer"></div>

                <Near_miss_list />
                <div class="text-center">
                  <h3>Table. Near Miss List</h3>
                </div>

            </TabPanel>
  
            <TabPanel header="Analyze">
              <div class="grid">
                <div class="col-12 lg:col-6 xl:col-3">
                  <div class="card card-light-yellow mb-0">
                    <div class="flex justify-content-between mb-3" style="height: 150px">
                      <Safety_indicators_alert />
                    </div>
                  </div>
                </div>
                <div class="col-12 lg:col-6 xl:col-3">
                  <div class="card card-light-yellow mb-0">
                    <div class="flex justify-content-between mb-3" style="height: 150px">
                      <Danger_area />
                    </div>
                  </div>
                </div>
                <div class="col-12 lg:col-6 xl:col-3">
                  <div class="card card-light-yellow mb-0">
                    <div class="flex justify-content-between mb-3" style="height: 150px">
                      <Safety_Factor_rate />
                    </div>
                  </div>
                </div>
                <div class="col-12 lg:col-6 xl:col-3">
                  <div class="card card-light-yellow mb-0">
                    <div class="flex justify-content-between mb-3" style="height: 150px">
                      <Safety_AccidentType_rate />
                    </div>
                  </div>
                </div>
              </div>
  
              <div class="grid">
                <div class="col-12 lg:col-6 xl:col-6">
                  <div class="card-light-yellow-container">
                    <div class="card mb-0" style="height: 500px;">
                      <Safety_indicator_trend />
                    </div>
                  </div>
                </div>
                <div class="col-12 lg:col-6 xl:col-6">
                  <div class="card-light-yellow-container">
                    <div class="card mb-0" style="height: 500px;">
                      <Safety_Measure_trend />
                    </div>
                  </div>
                </div>
              </div>
  
              <div class="card-light-yellow-container">
                <div class="card mb-0">
                  <Safety_correlation_diagram />
                  <Message :closable="false">
                    AI recommendation
                    <br />
                    Now developing
                  </Message>
                </div>
              </div>
            </TabPanel>
            <TabPanel header="Target setting">
              Now developing
              <p class="line-height-3 m-0"></p>
            </TabPanel>
            <TabPanel header="KYT">
              Now developing
              <p class="line-height-3 m-0"></p>
            </TabPanel>
          </TabView>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import Near_miss_list from '@/components/Safety/Near_miss/Near_miss_list.vue';
  import Safety_Factor_rate from '@/components/Safety/Cards/Safety_factor_rate';
  import Safety_AccidentType_rate from '@/components/Safety/Cards/Safety_AccidentType_rate.vue';
  import Safety_correlation_diagram from '@/components/Safety/Safety_correlation_diagram.vue';
  import Safety_Measure_trend from '@/components/Safety/Safety_Measure_trend.vue';
  import NearMiss_form from '@/components/Safety/Near_miss/Near_miss_form.vue';
  import Safety_indicator_trend from '@/components/Safety/Safety_indicator.vue';
  import Safety_indicators_alert from '@/components/Safety/Cards/Safety_indicators';
  import Count_of_nearMiss from '@/components/Safety/Cards/Count_of_nearMiss';
  import Danger_area from '@/components/Safety/Cards/Danger_area';
  import Action_items from '@/components/Safety/Cards/Action_items';
  import Safety_clock from '@/components/Safety/Safety_clock.vue';
  
  export default {
    components: {
      Near_miss_list,
      Safety_Factor_rate,
      Safety_AccidentType_rate,
      Safety_correlation_diagram,
      Safety_Measure_trend,
      NearMiss_form,
      Safety_indicator_trend,
      Safety_indicators_alert,
      Count_of_nearMiss,
      Danger_area,
      Action_items,
      Safety_clock
    },
    data() {
      return {
        activeIndex: parseInt(localStorage.getItem('nearMissTabIndex')) || 0 // キー名を変更
      };
    },
    methods: {
      onTabChange(event) {
        this.activeIndex = event.index;
        localStorage.setItem('nearMissTabIndex', this.activeIndex); // キー名を変更
      }
    }
  };
  </script>
  
  <style scoped>
  .card-light-yellow {
    background-color: #fff9c4; /* 薄い黄色に変更 */
  }
  .card-light-yellow-container {
    background-color: #fff9c4; /* 薄い黄色に変更 */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 薄い影を追加 */
    padding: 20px; /* パディングを追加して内容を囲む */
    border-radius: 8px; /* 角を丸くする */
  }
  .flex-wrap {
    display: flex;
    flex-wrap: wrap;
  }
  .justify-content-between {
    justify-content: space-between;
  }
  
  .text-center {
    text-align: center;
  }
  
  h3 {
    font-size: 1.25rem; /* Adjust the font size as needed */
  }
  
  .spacer {
    height: 10px; /* Adjust the height as needed */
  }
  
  </style>
  