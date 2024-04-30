<template>
	<div class="base-content">
		<section class="content">
			<div class="card card-solid">
				<TabView>
					<TabPanel header="Critical equipment list Input Form">
						<p class="line-height-3 m-0">
							Critical Equipment List. This data is sample.
							<br>
							<br>
							<Input_critical_equipment />
						</p>

					</TabPanel>
					<TabPanel header="Repairing Cost Input Form">
						<p class="line-height-3 m-0">
							Critical Equipment List. This data is sample.
							<br>
							<br>
							<Input_repairing_cost />
						</p>

					</TabPanel>

					<TabPanel header="Task Input Form">
						<p class="line-height-3 m-0">
							Critical Equipment List. This data is sample.
							<br>
							<br>
							<Input_task_list />
						</p>

					</TabPanel>
					<TabPanel header="Spare Parts Input Form">
						<p class="line-height-3 m-0">
							Critical Equipment List. This data is sample.
							<br>
							<br>
							<Input_spare_parts />
						</p>

					</TabPanel>
					<TabPanel header="Near Miss Input Form">
						<p class="line-height-3 m-0">
							Critical Equipment List. This data is sample.
							<br>
							<br>
							<Input_NearMiss />
						</p>

					</TabPanel>
					<TabPanel header="Energy Input Form">
						<p class="line-height-3 m-0">
							Critical Equipment List. This data is sample.
							<br>
							<br>
							<Input_Energy />
						</p>
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>


<script>


import Input_critical_equipment from '@/components/Input_form/Input_critical_equipment.vue'
import Input_repairing_cost from '@/components/Input_form/Input_repairing_cost.vue'
import Input_task_list from '@/components/Input_form/Input_task_list.vue'
import Input_spare_parts from '@/components/Input_form/Input_spare_parts.vue'
import Input_Energy from '@/components/Input_form/Input_Energy.vue'
import Input_NearMiss from '@/components/Input_form/Input_NearMiss.vue'


export default {
	components: {
		Input_critical_equipment,
		Input_repairing_cost,
		Input_task_list,
		Input_spare_parts,
		Input_Energy,
		Input_NearMiss

	},
}


</script>
