<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->
		<section class="content-header">
			<div class="container-fluid">
				<div class="row mb-2">
					<div class="col-sm-6">
						<h1>Repairing Cost</h1>
					</div>
					<div class="col-sm-6">
						<ol class="breadcrumb float-sm-right">
							<li class="breadcrumb-item"><a href="#">How to use detail</a></li>
							<li class="breadcrumb-item"><a href="#">Task of maintenance</a></li>
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
					<TabPanel header="Repairing cost">
						<div class="col-12 xl:col-12">
							<div class="card" style="background-color: #f2f2f2">
								<total_graph />
								<p>Planned cost</p>
								<Total_cost_table />
								<p>actual summary cost (readOnly)</p>
								<Actual_summary_table/>
								<Message :closable="false">AI recommendation
									<br>
									Now developing
								</Message>
							</div>
						</div>
						<div class="row">
							<!-- これはいったん消す<p class="line-height-3 m-0">-->
							<div class="col-12 xl:col-6">
								<div class="card" style="background-color: #f2f2f2">
									<PM02_actual_graph />
									<PM02_actual_table />
									<Message :closable="false">AI recommendation
										<br>
										Now developing
									</Message>
								</div>
							</div>
							<div class="col-12 xl:col-6">
								<div class="card" style="background-color: #f2f2f2">
									<PM03_actual_graph />
									<PM03_actual_table />
									<Message :closable="false">AI recommendation
										<br>
										Now developing
									</Message>
								</div>
							</div>
							<div class="col-12 xl:col-6">
								<div class="card" style="background-color: #f2f2f2">
									<PM04_actual_graph />
									<PM04_actual_table />
									<Message :closable="false">AI recommendation
										<br>
										Now developing
									</Message>
								</div>
							</div>
							<div class="col-12 xl:col-6">
								<div class="card" style="background-color: #f2f2f2">
									<PM05_actual_graph />
									<PM05_actual_table />
									<Message :closable="false">AI recommendation
										<br>
										Now developing
									</Message>
								</div>
							</div>
						</div>
						<!-- </p>-->
					</TabPanel>
					<TabPanel header="Task list">
						<div class="row">
							<div class="col-12 lg:col-6 xl:col-6">
								<div class="card mb-0">
									<div class="flex justify-content-between mb-3" style="height: 20px;">
										<div>
											<span class="block text-500 font-medium mb-3">Predict years cost</span>
											<div class="text-900 font-medium text-xl">$2.100</div>
										</div>
										<div class="flex align-items-center justify-content-center bg-orange-100 border-round"
											style="width: 2.5rem; height: 2.5rem">
											<i class="pi pi-map-marker text-orange-500 text-xl"></i>
										</div>
									</div>
								</div>
							</div>
							<div class="col-12 lg:col-6 xl:col-6">
								<div class="card mb-0">
									<div class="flex justify-content-between mb-3" style="height: 20px;">
										<div>
											<span class="block text-500 font-medium mb-3">Next month task event</span>
											<div class="text-900 font-medium text-xl">28441</div>
										</div>
										<div class="flex align-items-center justify-content-center bg-cyan-100 border-round"
											style="width: 2.5rem; height: 2.5rem">
											<i class="pi pi-inbox text-cyan-500 text-xl"></i>
										</div>
									</div>
								</div>
							</div>
							<div class="col-12 xl:col-6">
								<div class="card" style="background-color: #f2f2f2;">
										<Planned_vs_actual />
								</div>
							</div>
							<div class="col-12 xl:col-6">
								<div class="card" style="background-color: #f2f2f2;">
									<h2>Forecast for 10 years</h2>
									<PM02_forecast_table />
									<br>
									<h2>Actual cost (contain PM02 PM03 PM04 PM05)</h2>
									<Actual_summary_table_year />
								</div>
								<br>
								<br>
							</div>
							<Task_list />
						</div>
					</TabPanel>
					<TabPanel header="Simulations">
						<p class="line-height-3 m-0">
						</p>
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>


<script>
import Total_graph from '@/components/Repairing_cost/Total_graph.vue'
import Total_cost_table from '@/components/Repairing_cost/Total_cost_table.vue'
import Planned_vs_actual from '@/components/Repairing_cost/Planned_vs_actual_graph.vue'
import Actual_summary_table from '@/components/Repairing_cost/Actual_summary_table.vue'
import Actual_summary_table_year from '@/components/Repairing_cost/Actual_summary_table_year.vue'
import PM02_forecast_table from '@/components/Repairing_cost/PM02_forecast_table.vue'
import PM02_planned_graph from '@/components/Repairing_cost/PM02_planned_graph.vue'
import PM02_planned_table from '@/components/Repairing_cost/PM02_planned_table.vue'
import PM02_actual_graph from '@/components/Repairing_cost/PM02_actual_graph.vue'
import PM02_actual_table from '@/components/Repairing_cost/PM02_actual_table.vue'
import PM03_actual_graph from '@/components/Repairing_cost/PM03_actual_graph.vue'
import PM03_actual_table from '@/components/Repairing_cost/PM03_actual_table.vue'
import PM04_actual_graph from '@/components/Repairing_cost/PM04_actual_graph.vue'
import PM04_actual_table from '@/components/Repairing_cost/PM04_actual_table.vue'
import PM05_actual_graph from '@/components/Repairing_cost/PM05_actual_graph.vue'
import PM05_actual_table from '@/components/Repairing_cost/PM05_actual_table.vue'
import Task_list from '@/components/Repairing_cost/Task_list.vue'

export default {
	components: {
		Total_graph,
		Total_cost_table,
		Planned_vs_actual,
		Actual_summary_table_year,
		Actual_summary_table,
		PM02_forecast_table,
		PM02_planned_graph,
		PM02_planned_table,
		PM02_actual_graph,
		PM02_actual_table,
		PM03_actual_graph,
		PM03_actual_table,
		PM04_actual_graph,
		PM04_actual_table,
		PM05_actual_graph,
		PM05_actual_table,
		Task_list,
	},
}
</script>
