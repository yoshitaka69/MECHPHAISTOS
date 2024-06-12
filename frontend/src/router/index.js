import { createRouter, createWebHistory } from 'vue-router'
import AppLayout from '@/layout/AppLayout.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: AppLayout,
            children: [
				{
					path: '/about',
					name:'What is a MECHPHAISTOS',
					component: () => import('../views/pages/What_is_mechphaistos.vue')
				},
				{
					path: '/',
					name:'Dashboard',
					component: () => import('../views/Dashboard.vue')
				},
				{
					path: '/Maintenance_optimization',
					name:'Maintenance_optimization',
					component: () => import('../views/pages/Maintenance_optimization.vue')
				},
				{
					path: '/news',
					name:'News',
					component: () => import('../views/pages/News.vue')
				},
		    		{
					path: '/input_form',
					name:'Input_form',
					component: () => import('../views/pages/Input_form.vue')
				},
				{
					path: '/critical_equipment_list',
					name:'Critical_equipment_list',
					component: () => import('../views/pages/Critical_equipment_list.vue')
				},
				{
					path: '/repairing_cost',
					name:'Repairing_cost',
					component: () => import('../views/pages/Repairing_cost.vue')
				},
				{
					path: '/safety',
					name:'Safety',
					component: () => import('../views/pages/Safety.vue')
				},
				{
					path: '/prediction&estimate',
					name:'Prediction&Estimate',
					component: () => import('../views/pages/Prediction&Estimate.vue')
				},
				{
					path: '/spare_parts',
					name:'Spare_parts',
					component: () => import('../views/pages/Spare_parts/Spare_parts.vue')
				},
				{
					path: '/communications',
					name:'Communications',
					children:[
						{
							path: '/communications/whiteboard',
							component: () => import('../views/pages/Communications/Whiteboard.vue')
						},
					]
				},
				{
					path: '/schedule',
					name:'Schedule',
					children:[
						{
							path: '/schedule/calendar',
							component: () => import('../views/pages/Schedule/Calendar.vue')
						},
						{
							path: '/schedule/ganttchart',
							component: () => import('../views/pages/Schedule/Ganttchart.vue')
						},
					]
				},
				{
					path: '/scada',
					name:'SCADA',
					component: () => import('../views/pages/SCADA/Scada.vue')
				},
				{
					path: '/trend&demand',
					name:'Trend&demand',
					component: () => import('../views/pages/Trend&Demand.vue')
				},
				{
					path: '/workingReport',
					name:'Working_Report',
					children:[
						{
							path: '/workingReport/maintenance_report',
							component: () => import('../views/pages/Working_Report/maintenanceReport.vue')
						},
					]
				},
				{
					path: '/settings',
					name:'settings',
					component: () => import('../views/pages/Settings.vue')
				},
				{
					path: '/how_to_use',
					name:'How_to_use',
					component: () => import('../views/pages/How_to_use.vue')
				},
				{
					path: '/work_order',
					name:'Work_order',
					component: () => import('../views/pages/Work_order.vue')
				},
				{
					path: '/ai',
					name:'AI',
					component: () => import('../views/pages/AI.vue')
				},
				{
					path: '/energy',
					name:'Energy',
					component: () => import('../views/pages/Energy.vue')
				},
				{
					path: '/benefit',
					name:'Benefit',
					component: () => import('../views/pages/Benefit.vue')
				},
			]
		},
		{
            path: '/test',
            name: 'error',
            component: () => import('@/views/pages/test.vue')
        },
	],
})

export default router
