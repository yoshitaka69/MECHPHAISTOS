<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

		<section class="content-header">
			<div class="container-fluid">
				<div class="row mb-2">
					<div class="col-sm-6">
						<h1>Trend & Demand </h1>
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
				<TabView>
					<TabPanel header="Trend & Demand map">
						<div class="row">
							<div class="flex-child col-12 lg:col-6 xl:col-8">
								<Trend_map />
							</div>
						</div>
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>



<script>

import Trend_map from '@/components/Trend_map/Trend_map.vue'

export default {
	components: {
		Trend_map,
	},
}

</script>

<style>

.row {
    display: flex;
    flex-wrap: wrap;
}

</style>