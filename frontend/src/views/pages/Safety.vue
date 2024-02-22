<template>
	<!--AdminLTE copy-->
	<div class="base-content">
		<!--AdminLTEのcssがわからなかったから適当に作った-->
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
						<p class="line-height-3 m-0" style="background-color: #f0f0f0">
							<Near_miss_list />
						</p>
					</TabPanel>
					<TabPanel header="Analyze">
						<div class="row"><!--このrow classでカードを横並びにしている-->
							<div class="col-12 lg:col-6 xl:col-4">
								<div class="card mb-0">
									<div class="flex justify-content-between mb-3">
										<div>
											<span class="block text-500 font-medium mb-3">Number of near misses</span>
											<div class="text-900 font-medium text-xl">$2.100</div>
										</div>
										<div class="flex align-items-center justify-content-center bg-orange-100 border-round"
											style="width: 2.5rem; height: 2.5rem">
											<i class="pi pi-map-marker text-orange-500 text-xl"></i>
										</div>
									</div>
									<span class="text-green-500 font-medium">%52+ </span>
									<span class="text-500">since last week</span>
								</div>
							</div>
							<div class="col-12 lg:col-6 xl:col-4">
								<div class="card mb-0">
									<div class="flex justify-content-between mb-3">
										<div>
											<span class="block text-500 font-medium mb-3">Assumed risks</span>
											<div class="text-900 font-medium text-xl">28441</div>
										</div>
										<div class="flex align-items-center justify-content-center bg-cyan-100 border-round"
											style="width: 2.5rem; height: 2.5rem">
											<i class="pi pi-inbox text-cyan-500 text-xl"></i>
										</div>
									</div>
									<span class="text-green-500 font-medium">520 </span>
									<span class="text-500">newly registered</span>
								</div>
							</div>
							<div class="col-12 lg:col-6 xl:col-4">
								<div class="card mb-0">
									<div class="flex justify-content-between mb-3">
										<div>
											<span class="block text-500 font-medium mb-3">Measures needed</span>
											<div class="text-900 font-medium text-xl">152 Unread</div>
										</div>
										<div class="flex align-items-center justify-content-center bg-purple-100 border-round"
											style="width: 2.5rem; height: 2.5rem">
											<i class="pi pi-comment text-purple-500 text-xl"></i>
										</div>
									</div>
									<span class="text-green-500 font-medium">85 </span>
									<span class="text-500">responded</span>
								</div>
							</div>
							<div class="col-12 xl:col-12">
								<div class="card" style="background-color: #f2f2f2">
									<Safety_indicator />
									<Message :closable="false">AI recommendation
										<br />
										Now developing
									</Message>
								</div>
							</div>
							<div class="col-12 xl:col-6">
								<div class="card" style="background-color: #f2f2f2">
									<Safety_factor_rate />
									<Message :closable="false">AI recommendation
										<br />
										Now developing
									</Message>
								</div>
							</div>
							<div class="col-12 xl:col-6">
								<div class="card" style="background-color: #f2f2f2">
									<Safety_AccidentType_rate />
									<Message :closable="false">AI recommendation
										<br />
										Now developing
									</Message>
								</div>
							</div>
						</div>
						<div class="col-12 xl:col-12">
							<div class="card" style="background-color: #f2f2f2">
								<Safety_Measure_trend />
								<Message :closable="false">AI recommendation
									<br />
									Now developing
								</Message>
							</div>
						</div>
						<div class="card" style="background-color: #f2f2f2">
							<Safety_correlation_diagram />
							<Message :closable="false">AI recommendation
								<br />
								Now developing
							</Message>
						</div>
					</TabPanel>
					<TabPanel header="Target setting">
						Now developing
						<p class="line-height-3 m-0"></p>
					</TabPanel>
					<TabPanel header="KYT">
						Now developing
						<p class="line-height-3 m-0"></p>
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>

<script>
import Near_miss_list from '@/components/Safety/Near_miss/near_miss_list';
import Safety_factor_rate from '@/components/Safety/Safety_factor_rate';
import Safety_AccidentType_rate from '@/components/Safety/Safety_AccidentType_rate.vue';
import Safety_correlation_diagram from '@/components/Safety/Safety_correlation_diagram.vue';
import Safety_Measure_trend from '@/components/Safety/Safety_Measure_trend.vue';
import NearMiss_form from '@/components/Safety/Near_miss/Near_miss_form.vue';
import Safety_indicator from '@/components/Safety/Safety_indicator.vue'

export default {
	components: {
		Near_miss_list,
		Safety_factor_rate,
		Safety_AccidentType_rate,
		Safety_correlation_diagram,
		Safety_Measure_trend,
		NearMiss_form,
		Safety_indicator
	}
};
</script>
