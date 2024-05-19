<template>
    <div class="base-content">
        <section class="content">
            <div class="card card-solid">
                <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
                    <TabPanel header="Trend & Demand map">
                        <div class="row">
                            <div class="flex-child col-12 lg:col-6 xl:col-8">
                                <Trend_map />
                            </div>
                        </div>
                    </TabPanel>
                </TabView>
            </div>
        </section>
    </div>
</template>

<script>
import Trend_map from '@/components/Trend_map/Trend_map.vue';

export default {
    components: {
        Trend_map
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

<style>
.row {
    display: flex;
    flex-wrap: wrap;
}
</style>
