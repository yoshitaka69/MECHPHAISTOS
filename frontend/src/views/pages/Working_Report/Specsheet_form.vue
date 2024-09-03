<template>
	<div class="base-content">
	  <section class="content">
		<div class="card card-solid">
		  <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
			<TabPanel header="Specsheet">
			  <p class="line-height-3 m-0"></p>
			  <MaintenanceReportList />
			</TabPanel>
		  </TabView>
		</div>
	  </section>
	</div>
  </template>
  
  <script>
  import MaintenanceReportList from '@/components/Specsheet/Specsheet_list.vue';
  
  export default {
	components: {
	  MaintenanceReportList,
	},
	data() {
	  return {
		activeIndex: parseInt(localStorage.getItem('specsheetTabIndex')) || 0 // キー名を変更
	  };
	},
	methods: {
	  onTabChange(event) {
		this.activeIndex = event.index;
		localStorage.setItem('specsheetTabIndex', this.activeIndex); // キー名を変更
	  }
	}
  };
  </script>
  
  <style>
  </style>
  