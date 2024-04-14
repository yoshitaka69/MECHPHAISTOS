<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

		<section class="content-header">
			<div class="container-fluid">
				<div class="row mb-2">
					<div class="col-sm-6">
						<h1>Spare Parts List</h1>
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
					<TabPanel header="Spare Parts List">
						<p class="line-height-3 m-0">
						<div class="row"><!--このrow classでカードを横並びにしている-->
							<div class="col-12 lg:col-6 xl:col-4">
								<Card_Order_list />
							</div>
							<div class="col-12 lg:col-6 xl:col-4">
								<Card_Order_alert />
							</div>
							<div class="col-12 lg:col-6 xl:col-4">
								<Card_Spare_Parts_Total_Cost />

							</div>
							<br>
							<br>
						</div>		
						<BOM />
						</p>
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>



<script>

import BOM from '@/components/Spare_parts/Spare_parts_list.vue';
import Card_Order_alert from '@/components/Spare_parts/Cards/Order_alert.vue'
import Card_Spare_Parts_Total_Cost from '@/components/Spare_parts/Cards/Spare_parts_total_cost.vue'
import Card_Order_list from '@/components/Spare_parts/Cards/Order_list.vue'



export default {
	components: {
		BOM,

		Card_Order_alert,
		Card_Spare_Parts_Total_Cost,
		Card_Order_list,
	},
}

</script>

<style>

.row {
    display: flex;
    flex-wrap: wrap;
}

</style>