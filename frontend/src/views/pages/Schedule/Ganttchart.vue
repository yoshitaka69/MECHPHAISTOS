<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->
		<section class="content">
			<div class="card card-solid">
				
				<Ganttchart />
			</div>
		</section>
	</div>
</template>


<script>
import Ganttchart from '@/components/Ganttchart/Ganttchart.vue'


export default {
	components: {
		Ganttchart
	},
}
</script>