<template>
	<div class="base-content">
	  <section class="content">
		<div class="card card-solid">
		  <p class="line-height-3 m-0"></p>
		  <MaintenanceReportList />
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
  };
  </script>
  
  <style>
  </style>
  