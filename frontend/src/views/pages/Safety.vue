<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

		<section class="content-header">
			<div class="container-fluid">
				<div class="row mb-2">
					<div class="col-sm-6">
						<h1>Safety</h1>
					</div>
					<div class="col-sm-6">
						<ol class="breadcrumb float-sm-right">
							<li class="breadcrumb-item"><a href="#">Dashboard</a></li>
							<li class="breadcrumb-item"><a href="#">Home</a></li>
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
					<TabPanel header="NearMiss List">
						<p class="line-height-3 m-0">
							<Near_miss_list />
						</p>
					</TabPanel>
					<TabPanel header="Analyze">
							<Safety_indicator />
							<Safety_rate />
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>



<script>
import Near_miss_list from '@/components/Near_miss/near_miss_list'
import Safety_indicator from '@/components/Safety/Safety_indicator'
import Safety_rate from '@/components/Safety/Safety_rate'


export default {
	components: {
		Near_miss_list,
		Safety_indicator,
		Safety_rate
	},
}

</script>