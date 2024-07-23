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
                        <p class="line-height-3 m-0">
                            <Work_order_tree_map />
                        </p>
                    </TabPanel>
                </TabView>
            </div>
        </section>
    </div>
</template>

<script>
import Work_permission from '@/components/Work_order/Work_permission_list.vue';
import Work_order_list from '@/components/Work_order/Work_order_list.vue';
import Work_order_tree_map from '@/components/Work_order/Work_order_tree_map.vue';

export default {
    components: {
        Work_order_list,
        Work_permission,
        Work_order_tree_map
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
