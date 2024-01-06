<template>
    <div ref="graph"></div>
</template>
  <script lang="ts">
    import { defineComponent, onMounted, ref, toRef, watch, PropType } from "vue";
  
    import Plotly from "plotly.js-dist-min";
  
    export default defineComponent({
      props: {
        data: {
          type: Array as PropType<Plotly.Data[]>,
          default: () => [],
          required: true,
        },
      },
      setup(props) {
        const graph = ref<HTMLDivElement>();
  
        let data: Plotly.Data[] = [];
  
        const createData = () => {
          // データのコピーを作成
          let d = Object.assign({}, toRef(props.data, 0).value);
          // 棒グラフの形式を指定
          d.type = "bar";
          data.pop();
          data.push(d);
        };
  
        onMounted(() => {
          createData();
          if (!graph.value) return;
          Plotly.newPlot(graph.value, data);
        });
  
        //watch(props.data, () => {
        watch(props.data, () => {
          createData();
          if (!graph.value) return;
          Plotly.redraw(graph.value);
        });
  
        return { graph };
      },
    });
  </script>