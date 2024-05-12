<template>
    <!--AdminLTE copy-->
    <div class="base-content">
        <!--AdminLTEのcssがわからなかったから適当に作った-->
        <section class="content">
            <div class="card card-solid">
                <!--Tabはsakai-vue-template-->
                <TabView>
                    <!--Tabの表示-->
                    <TabPanel header="NearMiss List">
                        <div class="row">
                            <div class="col-12 lg:col-6 xl:col-6">
                                <Count_of_nearMiss />
                            </div>
                            <div class="col-12 lg:col-6 xl:col-6">
                                <Action_items />
                            </div>
                        </div>
                        <br />
                        <br />
                        <div>
                            <Near_miss_list />
                        </div>
                    </TabPanel>

                    <TabPanel header="Analyze">
                        <div class="row">
                            <!--このrow classでカードを横並びにしている-->
                            <div class="col-12 lg:col-6 xl:col-3">
                                <div class="card mb-0">
                                    <div class="flex justify-content-between mb-3" style="height: 150px">
                                        <Safety_indicators_alert />
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 lg:col-6 xl:col-3">
                                <div class="card mb-0">
                                    <div class="flex justify-content-between mb-3" style="height: 150px">
                                        <Danger_area />
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 lg:col-6 xl:col-3">
                                <div class="card mb-0">
                                    <div class="flex justify-content-between mb-3" style="height: 150px">
                                        <div style="width: 300px; height: 100px; overflow: hidden">
                                            <Safety_Factor_rate />
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 lg:col-6 xl:col-3">
                                <div class="card mb-0">
                                    <div class="flex justify-content-between mb-3" style="height: 150px">
                                        <div style="width: 300px; height: 100px; overflow: hidden">
                                            <Safety_AccidentType_rate />
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="col-12 lg:col-12 xl:col-12">
                            <div class="card mb-0">
                                <div class="Safety_indicator_trend">
                                    <Safety_indicator_trend />
                                </div>
                                <div class="Safety_Measure_trend">
                                    <Safety_Measure_trend />
                                </div>
                            </div>
                            <Message :closable="false"
                                >AI recommendation
                                <br />
                                Now developing
                            </Message>
                        </div>

                        <div class="card mb-0">
                            <Safety_correlation_diagram />
                            <Message :closable="false"
                                >AI recommendation
                                <br />
                                Now developing
                            </Message>
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
import Safety_AccidentType_rate from '@/components/Safety/Safety_AccidentType_rate.vue';
import Safety_correlation_diagram from '@/components/Safety/Safety_correlation_diagram.vue';
import Safety_Measure_trend from '@/components/Safety/Safety_Measure_trend.vue';
import NearMiss_form from '@/components/Safety/Near_miss/Near_miss_form.vue';
import Safety_indicator_trend from '@/components/Safety/Safety_indicator.vue';

import Safety_indicators_alert from '@/components/Safety/Cards/Safety_indicators';
import Count_of_nearMiss from '@/components/Safety/Cards/Count_of_nearMiss';
import Danger_area from '@/components/Safety/Cards/Danger_area';
import Action_items from '@/components/Safety/Cards/Action_items';

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
        Action_items
    }
};
</script>

<style>
.row {
    display: flex;
    flex-wrap: wrap;
}


.card.mb-0 {
    display: flex; /* Flexboxを有効化 */
    justify-content: space-between; /* 要素間に適切な間隔を設定 */
    align-items: stretch; /* 子要素の高さを揃える */
    width: 100%; /* 親要素の幅に合わせて100% */
}

.Safety_indicator_trend, .Safety_Measure_trend {
    flex: 1; /* 利用可能なスペースを等しく分ける */
    padding: 10px; /* コンテンツ周りの余白 */
    min-width: 0; /* 縮小時の挙動を正常にする */
}

@media (max-width: 768px) {
    .card.mb-0 {
        flex-direction: column; /* 小さい画面では縦並びに切り替え */
    }
}


</style>
