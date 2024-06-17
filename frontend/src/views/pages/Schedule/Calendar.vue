<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->



		<section class="content">
			<div class="card card-solid">
				<!--Tabはsakai-vue-template-->
                <Calendar />

			</div>
		</section>
	</div>
</template>



<script>
import Calendar from '@/components/Calendar/MainCalendar.vue'


export default {
	components: {
		Calendar
	},
}
</script>