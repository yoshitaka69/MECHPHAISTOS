<script setup>
import { ref } from 'vue';

import AppMenuItem from './AppMenuItem.vue';

const model = ref([
    {
        label: 'Home',
        items: [
            { label: 'What is MECHPHAISTOS', icon: 'pi pi-fw pi-home', to: '/about' },
            { label: 'NEWS', icon: 'pi pi-fw pi-home', to: '/news' },
            { label: 'AI', icon: 'pi pi-fw pi-tablet', to: '/ai' },
            { label: 'Dashboard', icon: 'pi pi-fw pi-home', to: '/' },
            { label: 'Maintenance Optimization', icon: 'pi pi-fw pi-home', to: '/Maintenance_optimization' },
            { label: 'Input Form', icon: 'pi pi-fw pi-home', to: '/input_form' },
            { label: 'Daily Report', icon: 'pi pi-fw pi-home', to: '/daily_report' },
            { label: 'Hand Over', icon: 'pi pi-fw pi-home', to: '/hand_over_document' },
            ],
    },
    {
        label: 'MENU',
        items: [
            { label: 'Critical equipment list', icon: 'pi pi-fw pi-id-card', to: '/critical_equipment_list' },
            { label: 'Repairing cost', icon: 'pi pi-fw pi-check-square', to: '/repairing_cost' },
            { label: 'Safety', icon: 'pi pi-fw pi-bookmark', to: '/Safety' },
            { label: 'Badactor management', icon: 'pi pi-fw pi-bookmark', to: '/badactor_management' },
            { label: 'Spare_parts', icon: 'pi pi-fw pi-exclamation-circle', to: '/spare_parts' },
            /*
            { label: 'Communications',icon: 'pi pi-fw pi-exclamation-circle', 
              items:[
                {label:'Minutes',icon:'pi pi-fw pi-bookmark', to: '/communications/minutes'},
                {label:'Whiteboard',icon:'pi pi-fw pi-bookmark', to: '/communications/whiteboard'},
              ]
            },
            */
            { label: 'Schedule',icon: 'pi pi-fw pi-exclamation-circle', 
              items:[
                {label:'Calendar',icon:'pi pi-fw pi-bookmark', to: '/schedule/calendar'},
                {label:'Ganttchart',icon:'pi pi-fw pi-bookmark', to: '/schedule/ganttchart'},
              ]
            },
            { label: 'Working Report',icon: 'pi pi-fw pi-exclamation-circle', 
              items:[
                {label:'Maintenance Report',icon:'pi pi-fw pi-bookmark', to: '/workingReport/maintenance_Report'},
                {label:'Specsheet',icon:'pi pi-fw pi-bookmark', to: '/workingReport/specsheet'},
              ]
            },
            { label: 'SCADA', icon: 'pi pi-fw pi-list', to: '/scada' },
            { label: 'Trend & Demand', icon: 'pi pi-fw pi-list', to: '/trend&demand' },
            { label: 'Work order', icon: 'pi pi-fw pi-share-alt', to: '/work_order' },
            { label: 'Design', icon: 'pi pi-fw pi-image', to: '/design' },
            { label: 'Energy', icon: 'pi pi-fw pi-clone', to: '/energy' },
            { label: 'Benefit', icon: 'pi pi-fw pi-image', to: '/benefit' },

        ]
    },
    {
        label: 'Utilities',
        items: [
            { label: 'How to use', icon: 'pi pi-fw pi-prime', to: '/how_to_use' },
            { label: 'Handbook', icon: 'pi pi-fw pi-image', to: '/handbook' },
            { label: 'Settings', icon: 'pi pi-fw pi-circle', to: '/settings' }
        ]
    },
]);
</script>

<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
        <li>
            <a href="https://www.primefaces.org/primeblocks-vue/#/" target="_blank">
                <img src="/layout/images/banner-primeblocks.png" alt="Prime Blocks" class="w-full mt-3" />
            </a>
        </li>
    </ul>
</template>

<style lang="scss" scoped></style>


