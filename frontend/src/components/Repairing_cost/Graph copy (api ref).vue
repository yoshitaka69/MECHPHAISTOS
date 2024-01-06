<template>
  <div ref="graph"></div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref, watch, PropType } from "vue";
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

    onMounted(() => {
      if (!graph.value) return;
      Plotly.newPlot(graph.value, props.data);
    });

    watch(props.data, () => {
      if (!graph.value) return;
      Plotly.redraw(graph.value);
    });

    return { graph };
  },
});
</script>