<template>
    <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
            <TabPanel header="Spare Parts List">
                <div class="line-height-3 m-0">
  
                    The below table is Spare parts List.
                    <br />
                    please input a your spare parts list.
                    <BOM />
                    <div class="text-center">
                        <h3>Table. Spare Parts List</h3>
                    </div>
                </div>
            </TabPanel>
            <TabPanel header="Order Alert List">
                <div class="flex flex-wrap justify-content-between">
                    <div class="col-12 lg:col-4 xl:col-4">
                        <div class="card card-light-blue mb-0">
                            <div class="flex justify-content-between mb-3" style="height: 150px">
                                <Card_Order_list />
                            </div>
                        </div>
                    </div>
                    <div class="col-12 lg:col-4 xl:col-4">
                        <div class="card card-light-blue mb-0">
                            <div class="flex justify-content-between mb-3" style="height: 150px">
                                <Card_Order_alert />
                            </div>
                        </div>
                    </div>
                    <div class="col-12 lg:col-4 xl:col-4">
                        <div class="card card-light-blue mb-0">
                            <div class="flex justify-content-between mb-3" style="height: 150px">
                                <Card_Spare_Parts_Total_Cost />
                            </div>
                        </div>
                    </div>
                </div>
                <div class="spacer"></div>
                <Order_alert_timeline />
                <div class="text-center">
                    <h3>Timeline for spare parts order</h3>
                </div>
                <br />
                <br />
                <Order_alert_list />
                <div class="text-center">
                    <h3>Table. Spare parts order list</h3>
                </div>
            </TabPanel>
        </TabView>
    </div>
</template>

<script>
import BOM from '@/components/Spare_parts/Spare_parts_list.vue';
import Order_alert_list from '@/components/Spare_parts/Order_alert_list.vue';
import Card_Order_alert from '@/components/Spare_parts/Cards/Order_alert.vue';
import Card_Spare_Parts_Total_Cost from '@/components/Spare_parts/Cards/Spare_parts_total_cost.vue';
import Card_Order_list from '@/components/Spare_parts/Cards/Order_list.vue';
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
            activeIndex: parseInt(localStorage.getItem('sparePartsTabIndex')) || 0 // キー名を変更
        };
    },
    methods: {
        onTabChange(event) {
            this.activeIndex = event.index;
            localStorage.setItem('sparePartsTabIndex', this.activeIndex); // キー名を変更
        }
    }
};
</script>

<style scoped>
.card-light-blue {
    background-color: #e0f7fa;
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
    height: 50px; /* Adjust the height as needed */
}
</style>
