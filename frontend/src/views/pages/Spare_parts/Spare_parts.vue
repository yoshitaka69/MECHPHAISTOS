<template>
    <div class="base-content">
        <section class="content">
            <div class="card card-solid">
                <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
                    <TabPanel header="Spare Parts List">
                        <div class="line-height-3 m-0">
                            <div class="row">
                                <div class="col-12 lg:col-6 xl:col-4">
                                    <Card_Order_list />
                                </div>
                                <div class="col-12 lg:col-6 xl:col-4">
                                    <Card_Order_alert />
                                </div>
                                <div class="col-12 lg:col-6 xl:col-4">
                                    <Card_Spare_Parts_Total_Cost />
                                </div>
                            </div>
                            <BOM />
                        </div>
                    </TabPanel>
                    <TabPanel header="Order Alert List">
                        <Order_alert_timeline />
                        <br>
                        <br>
                        <Order_alert_list />
                    </TabPanel>
                </TabView>
            </div>
        </section>
    </div>
</template>

<script>
import BOM from '@/components/Spare_parts/Spare_parts_list.vue';
import Order_alert_list from '@/components/Spare_parts/Order_alert_list.vue';
import Card_Order_alert from '@/components/Spare_parts/Cards/Order_alert.vue'
import Card_Spare_Parts_Total_Cost from '@/components/Spare_parts/Cards/Spare_parts_total_cost.vue'
import Card_Order_list from '@/components/Spare_parts/Cards/Order_list.vue'
import Order_alert_timeline from '@/components/Spare_parts/Order_alert_timeline.vue';

export default {
    components: {
        BOM,
        Order_alert_list,
        Order_alert_timeline,
        Card_Order_alert,
        Card_Spare_Parts_Total_Cost,
        Card_Order_list
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
