<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

		<section class="content-header">
			<div class="container-fluid">
				<div class="row mb-2">
					<div class="col-sm-6">
						<h1>Repairing Cost</h1>
					</div>
					<div class="col-sm-6">
						<ol class="breadcrumb float-sm-right">
							<li class="breadcrumb-item"><a href="#">How to use detail</a></li>
							<li class="breadcrumb-item"><a href="#">Task of maintenance</a></li>
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
					<TabPanel header="Repairing cost">
						<p class="line-height-3 m-0">
                            <Graph :data="data" />
                            <PM02_planned/>
                            <PM02_actual/>
                            <PM03/>
                            <PM04/>
                            <PM05/>
						</p>
					</TabPanel>
					<TabPanel header="Simulations">
						<p class="line-height-3 m-0">
                            <BarGraph :data="data" />
                            <Graph :data="data" />
                            <As_is_plan/>
                            <To_be_plan/>
						</p>
					</TabPanel>
					<TabPanel header="Task list">
						<p class="line-height-3 m-0">
							<Task_list />
						</p>
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>





<script lang="ts">
import { defineComponent,reactive, onMounted } from 'vue'
import Graph from "@/components/Repairing_cost/Graph.vue";
import BarGraph from "@/components/Repairing_cost/BarGraph.vue";
import Plotly from "plotly.js-dist-min";

import PM02_planned from '@/components/Repairing_cost/PM02_planned.vue'
import PM02_actual from '@/components/Repairing_cost/PM02_actual.vue'
import PM03 from '@/components/Repairing_cost/PM03.vue'
import PM04 from '@/components/Repairing_cost/PM04.vue'
import PM05 from '@/components/Repairing_cost/PM05.vue'

import Repairing_cost_graph from '@/components/Repairing_cost/Repairing_cost_graph.vue'
import As_is_plan from '@/components/Repairing_cost/As_is_plan.vue'
import To_be_plan from '@/components/Repairing_cost/As_is_plan.vue'

import Task_list from '@/components/Repairing_cost/Task_list.vue'

export default defineComponent({
  components: {
    Repairing_cost_graph,
    As_is_plan,
    To_be_plan,
    PM02_planned,
    PM02_actual,
    PM03,
    PM04,
    PM05,

    Graph,
    BarGraph,

	Task_list,
  },

  setup() {
      // reactive である必要も無いかもしれないが、
      // 子コンポーネントが reactiveの前提の実装になっているのでそのまま
      const data: Plotly.Data[] = reactive([]);

      // onMounted のタイミングでデータを取得してdetaに登録
      onMounted(async () => {
        const result = await (await fetch("/api/data")).json();
        if (!result) return;
        data.push(result);
      });

      return { data };
    },
  });

</script>
