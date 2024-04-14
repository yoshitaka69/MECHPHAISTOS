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
								<div class="card mb-0">
									<div class="flex justify-content-between mb-3" style="height: 20px;">
										<div>
											<span class="block text-500 font-medium mb-3">Order List</span>
											<div class="text-900 font-medium text-xl">$2.100</div>
										</div>
										<div class="flex align-items-center justify-content-center bg-orange-100 border-round"
											style="width: 2.5rem; height: 2.5rem">
											<i class="pi pi-map-marker text-orange-500 text-xl"></i>
										</div>
									</div>
								</div>
							</div>
							<div class="col-12 lg:col-6 xl:col-4">
								<Card_Order_alert />
							</div>
							<div class="col-12 lg:col-6 xl:col-4">

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




export default {
	components: {
		BOM,

		Card_Order_alert,
	},
}

</script>

<style>

.row {
    display: flex;
    flex-wrap: wrap;
}

</style>