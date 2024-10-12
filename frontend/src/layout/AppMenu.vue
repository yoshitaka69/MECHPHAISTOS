<script setup>
import { ref } from 'vue';

import AppMenuItem from './AppMenuItem.vue';

const model = ref([
    {
        label: 'Home',
        items: [
            { label: 'What is MECHPHAISTOS', icon: 'pi pi-fw pi-info-circle', to: '/about' },
            { label: 'NEWS', icon: 'pi pi-fw pi-bell', to: '/news' },
            { label: 'AI', icon: 'pi pi-fw pi-cog', to: '/ai' },
            { label: 'Dashboard', icon: 'pi pi-fw pi-chart-bar', to: '/' },
            { label: 'Maintenance Optimization', icon: 'pi pi-fw pi-wrench', to: '/Maintenance_optimization' },
            { label: 'Input Form', icon: 'pi pi-fw pi-file', to: '/input_form' },
            { label: 'Daily Report', icon: 'pi pi-fw pi-calendar', to: '/daily_report' }
            /*
            { label: 'Hand Over', icon: 'pi pi-fw pi-exchange', to: '/hand_over_document' },
            */
        ]
    },
    {
        label: 'MENU',
        items: [
            { label: 'Critical equipment list', icon: 'pi pi-fw pi-list', to: '/critical_equipment_list' },
            { label: 'Repairing cost', icon: 'pi pi-fw pi-money-bill', to: '/repairing_cost' },
            { label: 'Safety', icon: 'pi pi-fw pi-shield', to: '/Safety' },
            { label: 'Badactor management', icon: 'pi pi-fw pi-exclamation-triangle', to: '/badactor_management' }, // Changed to a warning triangle icon
            { label: 'Spare parts', icon: 'pi pi-fw pi-box', to: '/spare_parts' }, // Changed to a box icon
            /*
            { label: 'Communications',icon: 'pi pi-fw pi-comments', 
              items:[
                {label:'Minutes',icon:'pi pi-fw pi-clock', to: '/communications/minutes'},
                {label:'Whiteboard',icon:'pi pi-fw pi-pencil', to: '/communications/whiteboard'},
              ]
            },
            */
            {
                label: 'Schedule',
                icon: 'pi pi-fw pi-calendar-plus',
                items: [
                    { label: 'Calendar', icon: 'pi pi-fw pi-calendar', to: '/schedule/calendar' },
                    { label: 'Ganttchart', icon: 'pi pi-fw pi-chart-bar', to: '/schedule/ganttchart' }
                ]
            },
            {
                label: 'Working Report',
                icon: 'pi pi-fw pi-book',
                items: [
                    { label: 'Maintenance Report', icon: 'pi pi-fw pi-file', to: '/workingReport/maintenance_Report' },
                    { label: 'Specsheet', icon: 'pi pi-fw pi-file', to: '/workingReport/specsheet' }
                ]
            },
            { label: 'SCADA', icon: 'pi pi-fw pi-desktop', to: '/scada' },
            { label: 'Trend & Demand', icon: 'pi pi-fw pi-chart-line', to: '/trend&demand' },
            { label: 'Work order', icon: 'pi pi-fw pi-file-edit', to: '/work_order' },
            { label: 'Design', icon: 'pi pi-fw pi-pencil', to: '/design' },
            { label: 'Energy', icon: 'pi pi-fw pi-bolt', to: '/energy' },
            { label: 'Benefit', icon: 'pi pi-fw pi-briefcase', to: '/benefit' }
        ]
    },
    {
        label: 'Utilities',
        items: [
            { label: 'How to use', icon: 'pi pi-fw pi-question-circle', to: '/how_to_use' },
            { label: 'Handbook', icon: 'pi pi-fw pi-book', to: '/handbook' },
            { label: 'Settings', icon: 'pi pi-fw pi-cog', to: '/settings' }
        ]
    }
]);
</script>

<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
        <!--
        <li>
            <a href="https://www.primefaces.org/primeblocks-vue/#/" target="_blank">
                <img src="/layout/images/banner-primeblocks.png" alt="Prime Blocks" class="w-full mt-3" />
            </a>
        </li>
        --->
    </ul>
</template>

<style lang="scss" scoped></style>
