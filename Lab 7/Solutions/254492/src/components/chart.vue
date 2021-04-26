<script>
import { defineComponent } from "vue";
import { Bar } from "vue3-chart-v2";

export default defineComponent({
  name: "TempChart",
  props: {
    labels: { type: Array },
    data: { type: Array },
  },
  extends: Bar,
  mounted() {
    // Overwriting base render method with actual data.
    this.renderChart(
      {
        labels: [""].concat(this.labels).concat([""]),
        datasets: [
          {
            label: "Temperatura",
            backgroundColor: "#2fb543",
            data: [0].concat(this.data).concat([0]),
          },
        ],
      },
      {
          responsive: false
      }
      
    );
  },
});
</script>

<style>
</style>