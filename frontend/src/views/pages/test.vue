<template>
    <div>
      <v-card>
        <v-card-title>Assessment rate</v-card-title>
        <div id="AssessmentRate"></div>
      </v-card>
    </div>
</template>

<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";
import { useUserStore } from '@/stores/userStore'; // Pinia ストアをインポート

export default {
    data() {
        return {
            values: {},
            error: null,
        };
    },

    mounted() {
        const userStore = useUserStore();
        const userCompanyCode = userStore.companyCode;

        if (!userCompanyCode) {
            console.error("Error: No company code found for the user.");
            return; // companyCodeがない場合、処理を中断
        }

        const url = `NEW_URL_HERE/api/assessmentByCompany/?format=json&companyCode=${userCompanyCode}`;

        axios.get(url, {
            headers: {
                "Content-Type": "application/json"
            },
            withCredentials: true
        })
            .then(response => {
                const assessments = response.data;

                // 各Assessmentの頻度を計算
                this.values = assessments.reduce((accumulator, item) => {
                    const assessment = item.Assessment;
                    accumulator[assessment] = (accumulator[assessment] || 0) + 1;
                    return accumulator;
                }, {});

                // グラフのデータ
                let data = {
                    type: "pie",
                    values: Object.values(this.values),
                    labels: Object.keys(this.values),
                    textinfo: "label+percent",
                    insidetextorientation: "radial",
                };

                const layout = {
                    width: 500,
                    height: 500,
                    automargin: true,
                };

                const config = { responsive: true };

                // AssessmentRate 要素が存在することを確認してからグラフを描画
                Plotly.newPlot('AssessmentRate', [data], layout, config);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    },
};
</script>
