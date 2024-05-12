<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

		<section class="content">
			<div class="card card-solid">
				<!--Tabはsakai-vue-template-->

				<TabView>
					<TabPanel header="Work Order List">
						<p class="line-height-3 m-0">
							<Work_order_list />
						</p>
					</TabPanel>
					<TabPanel header="Work Order Permission">
						<p class="line-height-3 m-0">
						</p>
					</TabPanel>
					<TabPanel header="Work order management">
						<p class="line-height-3 m-0">
						</p>
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>



<script>
import Work_order_list from '@/components/Work_order/Work_order_list.vue';


export default {
	components: {

		Work_order_list,


	},
}
</script>