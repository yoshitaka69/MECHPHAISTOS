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
					path: '/daily_report',
					name:'Daily_report',
					component: () => import('../views/pages/Daily_report.vue')
				},
				{
					path: '/hand_over_document',
					name:'Hand_over_document',
					component: () => import('../views/pages/Hand_over_document.vue')
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
					path: '/badactor_management',
					name:'Badactor_management',
					component: () => import('../views/pages/Badactor_management.vue')
				},
				{
					path: '/spare_parts',
					name:'Spare_parts',
					component: () => import('../views/pages/Spare_parts.vue')
				},
				{
					path: '/communications',
					name:'Communications',
					children:[
						{
							path: '/communications/minutes',
							component: () => import('../views/pages/Communications/Minutes.vue')
						},
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
							component: () => import('../views/pages/Working_Report/Maintenance_report.vue')
						},
						{
							path: '/workingReport/specsheet',
							component: () => import('../views/pages/Working_Report/Specsheet_form.vue')
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
				{
					path: '/design',
					name:'Design',
					component: () => import('../views/pages/Design.vue')
				},
				{
					path: '/handbook',
					name:'Handbook',
					component: () => import('../views/pages/Handbook.vue')
				},
				
			]
		},
		{
            path: '/test',
            name: 'error',
            component: () => import('@/views/pages/test.vue')
        },
		{
			path: '/schedule/ganttchart',
			component: () => import('@/components/Ganttchart/Ganttchart.vue')
		},
		{
			path: '/near_miss_input_form',
			name:'Near_Miss_input_form',
			component: () => import('@/components/Safety/Near_miss/Near_miss_form.vue')
		},
		{
			path: '/maintenance_report_form',
			name:'maintenance_report_form',
			component: () => import('@/components/Maintenance_report/Maintenance_report_form.vue')
		},
		{
			path: '/specsheet_form',
			name:'specsheet_form',
			component: () => import('@/components/Specsheet/Specsheet_form.vue')
		},
		{
			path: '/Work_permission_form',
			name:'Work_permission_form',
			component: () => import('@/components/Work_permission/Work_permission_form.vue')
		},
		{
			path: '/celist_detail/:ceListNo',
			name: 'CeListDetail',
			component: () => import('@/components/Critical_equipment_list/CeListDetailPage/CeListDetail.vue')
		},
		{
			path: '/spare_parts_detail/:partsNo',
			name: 'SparePartsDetail',
			component: () => import('@/components/Spare_parts/Spare_parts_detail.vue')
		},
		{
			path: '/repairing_cost_detail/:plantName',
			name: 'RepairingCostDetail',
			component: () => import('@/components/Repairing_cost/Repairing_cost_detail/RepairingCostDetail.vue'), // 動的インポート
		},
		{
			path: '/task_list_detail/:taskListNo',
			name: 'TaskListDetail',
			component: () => import('@/components/Task_of_maintenance/Detail_task_list/TaskListDetailPage.vue')
		},
		{
			path: '/how_to_use/critical_equipment_list',
			name:'how_to_use_critical_equipment_list',
			component: () => import('@/components/How_to_use/How_to_use_critical_equipment_list.vue')
		},
		{
			path: '/how_to_use/risk_matrix',
			name:'how_to_use_risk_matrix',
			component: () => import('@/components/How_to_use/How_to_use_risk_matrix.vue')
		},
		{
			path: '/how_to_use/repairing_cost',
			name:'how_to_use_repairing_cost',
			component: () => import('@/components/How_to_use/How_to_use_repairing_cost.vue')
		},
		{
			path: '/how_to_use/near_miss',
			name:'how_to_use_near_miss',
			component: () => import('@/components/How_to_use/How_to_use_near_miss.vue')
		},
		{
			path: '/how_to_use/communications',
			name:'how_to_use_communications',
			component: () => import('@/components/How_to_use/How_to_use_communications.vue')
		},
		{
			path: '/how_to_use/schedule',
			name:'how_to_use_schedules',
			component: () => import('@/components/How_to_use/How_to_use_schedule.vue')
		},
		{
			path: '/how_to_use/trend&demand',
			name:'how_to_use_trend&demand',
			component: () => import('@/components/How_to_use/How_to_use_trend&demand.vue')
		},
		{
			path: '/how_to_use/work_order',
			name:'how_to_use_work_order',
			component: () => import('@/components/How_to_use/How_to_use_work_order.vue')
		},
		{
			path: '/how_to_use/benefit',
			name:'how_to_use_benefit',
			component: () => import('@/components/How_to_use/How_to_use_benefit.vue')
		},
		{
			path: '/how_to_use/spare_parts',
			name:'how_to_use_spare_parts',
			component: () => import('@/components/How_to_use/How_to_use_spare_parts.vue')
		},
		{
			path: '/how_to_use/task_list',
			name:'how_to_use_task_list',
			component: () => import('@/components/How_to_use/How_to_use_task_list.vue')
		},
		{
			path: '/what_is_pm_type',
			name:'what_is_pm_type',
			component: () => import('@/components/How_to_use/What_is_PM_type.vue')
		},
	],
})

export default router
