<template>
    <div class="base-content">
        <section class="content">
            <div class="card card-solid">
                <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
                    <TabPanel header="Sustainability">
                        <div class="row">
                            <div class="col-12 xl:col-6">
                                <div class="card" style="background-color: #f2f2f2;">
                                    <Co2_trend />
                                    <Message :closable="false">AI recommendation
                                        <br>
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card" style="background-color: #f2f2f2;">
                                    <STM_trend />
                                    <Message :closable="false">AI recommendation
                                        <br>
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card" style="background-color: #f2f2f2;">
                                    <Elec_trend />
                                    <Message :closable="false">AI recommendation
                                        <br>
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card" style="background-color: #f2f2f2;">
                                    <CompAir_trend />
                                    <Message :closable="false">AI recommendation
                                        <br>
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card" style="background-color: #f2f2f2;">
                                    <PureWater_trend />
                                    <Message :closable="false">AI recommendation
                                        <br>
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card" style="background-color: #f2f2f2;">
                                    <WellWater_trend />
                                    <Message :closable="false">AI recommendation
                                        <br>
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card" style="background-color: #f2f2f2;">
                                    <WWT_trend />
                                    <Message :closable="false">AI recommendation
                                        <br>
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card" style="background-color: #f2f2f2;">
                                    <ExGas_trend />
                                    <Message :closable="false">AI recommendation
                                        <br>
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                        </div>
                    </TabPanel>
                    <TabPanel header="Input Form">
                    </TabPanel>
                    <TabPanel header="Setting">
                    </TabPanel>
                </TabView>
            </div>
        </section>
    </div>
</template>

<script>
import Co2_trend from '@/components/Energy/Co2_trend.vue';
import STM_trend from '@/components/Energy/STM_trend.vue';
import Elec_trend from '@/components/Energy/Elec_trend.vue';
import CompAir_trend from '@/components/Energy/CompAir_trend.vue';
import PureWater_trend from '@/components/Energy/PureWater_trend.vue';
import WellWater_trend from '@/components/Energy/WellWater_trend.vue';
import WWT_trend from '@/components/Energy/WWT_trend.vue';
import ExGas_trend from '@/components/Energy/ExGas_trend.vue';

export default {
    components: {
        Co2_trend,
        STM_trend,
        Elec_trend,
        CompAir_trend,
        PureWater_trend,
        WellWater_trend,
        WWT_trend,
        ExGas_trend
    },
    data() {
        return {
            activeIndex: parseInt(localStorage.getItem('activeTabIndex')) || 0
        };
    },
    methods: {
        onTabChange(event) {
            this.activeIndex = event.index;
            localStorage.setItem('activeTabIndex', this.activeIndex);
        }
    }
};
</script>
