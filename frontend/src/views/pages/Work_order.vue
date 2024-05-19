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
                        </p>
                    </TabPanel>
                    <TabPanel header="Work order management">
                        <p class="line-height-3 m-0">
                        </p>
                    </TabPanel>
                </TabView>
            </div>
        </section>
    </div>
</template>

<script>
import Work_order_list from '@/components/Work_order/Work_order_list.vue';

export default {
    components: {
        Work_order_list
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
