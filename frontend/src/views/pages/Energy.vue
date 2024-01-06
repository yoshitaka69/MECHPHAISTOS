<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

		<section class="content-header">
			<div class="container-fluid">
				<div class="row mb-2">
					<div class="col-sm-6">
						<h1>Energy</h1>
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
                            <Energy_graph />
							<Energy_list />
						</p>
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>



<script>

import Energy_list from '@/components/Energy/Energy_list';
import Energy_graph from '@/components/Energy/Energy_graph.vue'


export default {
    components: {
        Energy_list,
        Energy_graph,
    },
}

</script>