<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

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