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
							Critical Equipment List. This data is sample.
							<br>
							<br>
							<Critical_equipment_list />
						</p>
					</TabPanel>
					<TabPanel header="Priority Tasks">
						<div class="row">
							<div class="col-12 xl:col-8">
								<div class="card" style="background-color: #f2f2f2;">
									priority tasks top 20
									<Top20_priority_task />
								</div>
							</div>
							<div class="col-12 xl:col-4">
								<div class="card" style="background-color: #f2f2f2;">
									<Assessment_rate />
								</div>
							</div>
						</div>
					</TabPanel>
					<TabPanel header="Risk-Matrix">
						<p class="line-height-3 m-0">
							<Risk_matrix />
						</p>
						<Impact_for_production />
						<Probability_of_failure />
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>



<script>
import Critical_equipment_list from '@/components/Critical_equipment_list/Critical_equipment_list.vue'

import Assessment_rate from '@/components/Critical_equipment_list/Assessment_rate.vue'

import Risk_matrix from '@/components/Risk_Matrix/Risk_matrix.vue'
import Impact_for_production from '@/components/Risk_Matrix/Impact_for_production.vue'
import Probability_of_failure from '@/components/Risk_Matrix/Probability_of_failure.vue'
import Top20_priority_task from '@/components/Critical_equipment_list/Top20_priority_task.vue'


export default {
	components: {
		Critical_equipment_list,

		Assessment_rate,

		Risk_matrix,
		Impact_for_production,
		Probability_of_failure,

		Top20_priority_task,

	},
}
</script>


<style>

.row {
    display: flex;
    flex-wrap: wrap;
}

</style>