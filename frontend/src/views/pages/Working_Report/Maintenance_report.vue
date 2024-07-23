<template>
	<div class="base-content">
	  <section class="content">
		<div class="card card-solid">
		  <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
			<TabPanel header="Maintenance Report">
			  <p class="line-height-3 m-0"></p>
			  <MaintenanceReportList />
			</TabPanel>
		  </TabView>
		</div>
	  </section>
	</div>
  </template>
  
  <script>
  import MaintenanceReportList from '@/components/Maintenance_report/Maintenance_report_list.vue';
  
  export default {
	components: {
	  MaintenanceReportList,
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
  </style>
  