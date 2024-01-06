<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

		<section class="content-header">
			<div class="container-fluid">
				<div class="row mb-2">
					<div class="col-sm-6">
						<h1>Critical Equipment List</h1>
					</div>
					<div class="col-sm-6">
						<ol class="breadcrumb float-sm-right">
							<li class="breadcrumb-item"><a href="#">How to use detail</a></li>
							<li class="breadcrumb-item"><a href="#">Spare parts list</a></li>
							<li class="breadcrumb-item active">MECHPHAISTOS</li>
						</ol>
					</div>
				</div>
			</div>
		</section>


		<section class="content">
			<div class="card card-solid">
				<!--Tabはsakai-vue-template-->

				<TabView>
					<TabPanel header="Critical equipment list">
						<p class="line-height-3 m-0">
							<Critical_equipment_list />
						</p>
					</TabPanel>
					<TabPanel header="Priority Tasks">
						<p class="line-height-3 m-0">
							<Task_of_maintenance />
						</p>
					</TabPanel>
					<TabPanel header="Risk-Matrix">
						<p class="line-height-3 m-0">
							<Risk_matrix />
						</p>
							<Description />
							<Description_impact />
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>



<script>
import Critical_equipment_list from '@/components/Critical_equipment_list/Critical_equipment_list.vue'
import Task_of_maintenance from '@/components/Task_of_maintenance/Task_of_maintenance.vue'
import Risk_matrix from '@/components/Risk_Matrix/Risk_matrix.vue'
import Description from '@/components/Risk_Matrix/Description.vue'
import Description_impact from '@/components/Risk_Matrix/Description_impact.vue'


export default {
	components: {
		Critical_equipment_list,
		Task_of_maintenance,
		Risk_matrix,
		Description,
		Description_impact
	},
}
</script>