<template>
    <div class="container">
        <h1>ベイズ予測による機械故障の予測</h1>
        <svg ref="chart" width="900" height="400"></svg>
        <div class="parameters">
            <p><strong>期間:</strong> {{ parameters.start_date }} から {{ parameters.end_date }} まで</p>
        </div>

        <h2>信頼性パラメータ一覧</h2>
        <table>
            <thead>
                <tr>
                    <th></th>
                    <!-- パラメータ行のヘッダー -->
                    <th>
                        Company <br />Code
                    </th>
                    <th>
                        CE List <br />No
                    </th>
                    <th>
                        MTTR <br />[日数]
                    </th>
                    <th>
                        MTBF <br />[日数]
                    </th>
                    <th>
                        MTTF <br />[日数]
                    </th>
                    <th>
                        Total Operating <br />Time
                    </th>
                    <th>
                        Failure <br />Count
                    </th>
                    <th>
                        Failure <br />Type
                    </th>
                    <th>
                        Failure <br />Mode
                    </th>
                    <th>
                        Maintenance <br />Method
                    </th>
                    <th>
                        Maintenance <br />Frequency
                    </th>
                    <th>
                        Maintenance <br />Impact
                    </th>
                    <th>
                        Failure <br />Cause
                    </th>
                    <th>
                        Environment <br />Condition
                    </th>
                    <th>
                        Operational <br />Condition
                    </th>
                    <th>
                        Component <br />Condition
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="param in allParameters" :key="param.ceListNo">
                    <td>パラメータ</td>
                    <!-- 各パラメータの表示 -->
                    <td>{{ param.companyCode }}</td>
                    <td>{{ param.ceListNo }}</td>
                    <td>{{ param.mttr }}</td>
                    <td>{{ param.mtbf }}</td>
                    <td>{{ param.mttf }}</td>
                    <td>{{ param.totalOperatingTime }}</td>
                    <td>{{ param.failureCount }}</td>
                    <td>{{ param.failureType }}</td>
                    <td>{{ param.failureMode }}</td>
                    <td>{{ param.maintenanceMethod }}</td>
                    <td>{{ param.maintenanceFrequency }}</td>
                    <td>{{ param.maintenanceImpact }}</td>
                    <td>{{ param.failureCause }}</td>
                    <td>{{ param.environmentCondition }}</td>
                    <td>{{ param.operationalCondition }}</td>
                    <td>{{ param.componentCondition }}</td>
                </tr>
                <tr v-for="param in allParameters" :key="param.ceListNo + '-impact'">
                    <td>影響度</td>
                    <!-- 影響度の行 -->
                    <td>{{ param.companyCode }}</td>
                    <td>{{ param.ceListNo }}</td>
                    <td>{{ calculateImpact(param.mttr) }}</td>
                    <td>{{ calculateImpact(param.mtbf) }}</td>
                    <td>{{ calculateImpact(param.mttf) }}</td>
                    <td>{{ calculateImpact(param.totalOperatingTime) }}</td>
                    <td>{{ calculateImpact(param.failureCount) }}</td>
                    <td>{{ calculateImpact(param.failureType) }}</td>
                    <td>{{ calculateImpact(param.failureMode) }}</td>
                    <td>{{ calculateImpact(param.maintenanceMethod) }}</td>
                    <td>{{ calculateImpact(param.maintenanceFrequency) }}</td>
                    <td>{{ calculateImpact(param.maintenanceImpact) }}</td>
                    <td>{{ calculateImpact(param.failureCause) }}</td>
                    <td>{{ calculateImpact(param.environmentCondition) }}</td>
                    <td>{{ calculateImpact(param.operationalCondition) }}</td>
                    <td>{{ calculateImpact(param.componentCondition) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';
import * as d3 from 'd3';
import { useUserStore } from '@/stores/userStore'; // Piniaのストアをインポート

export default {
    setup() {
        const userStore = useUserStore();
        return { userStore };
    },
    data() {
        return {
            x: [],
            posterior_pdf: [],
            parameters: {
                machineName: '',
                mttr: 0,
                mtbf: 0,
                start_date: '',
                end_date: ''
            },
            allParameters: [] // パラメータ一覧を保存
        };
    },
    mounted() {
        this.fetchBayesianData();
        this.fetchParameters();
    },
    methods: {
        async fetchBayesianData() {
            const companyCode = this.userStore.companyCode; // PiniaからcompanyCodeを取得
            if (!companyCode) {
                console.error('Company code is required');
                return;
            }

            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/reliability/reliabilityByCompany/bayesian_prediction/`, {
                    params: { companyCode, windowSize: 365, stepSize: 30 } // クエリパラメータとして設定
                });

                if (!response.data || response.data.length === 0) {
                    console.error('No data found for this company code');
                    return;
                }

                const data = response.data[0];
                if (!data.posterior_pdf) {
                    console.error('No valid posterior_pdf data');
                    return;
                }

                this.x = data.x || [];
                this.posterior_pdf = data.posterior_pdf || [];
                this.parameters = {
                    machineName: data.machineName || '',
                    mttr: data.mttr || 0,
                    mtbf: data.mtbf || 0,
                    start_date: data.start_date || '',
                    end_date: data.end_date || ''
                };

                this.renderChart();
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        async fetchParameters() {
            const companyCode = this.userStore.companyCode; // PiniaからcompanyCodeを取得
            if (!companyCode) {
                console.error('Company code is required');
                return;
            }

            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/reliability/reliabilityByCompany/reliability_parameters/`, {
                    params: { companyCode }
                });

                if (!response.data || response.data.length === 0) {
                    console.error('No parameters found for this company code');
                    return;
                }

                this.allParameters = response.data;
            } catch (error) {
                console.error('Error fetching parameters:', error);
            }
        },

        renderChart() {
  if (!this.posterior_pdf || this.posterior_pdf.length === 0) {
    console.error('No posterior_pdf data to render');
    return;
  }

  const svg = d3.select(this.$refs.chart);
  svg.selectAll('*').remove(); // 以前のチャートをクリア

  const margin = { top: 20, right: 100, bottom: 60, left: 80 };
  const width = +svg.attr('width') - margin.left - margin.right;
  const height = +svg.attr('height') - margin.top - margin.bottom;

  // 現在の日付を取得
  const currentDate = new Date();

  // 1年後の日付を計算
  const oneYearLater = d3.timeDay.offset(currentDate, 365);

  // xScaleを現在の日付から3年後の日付までの範囲に設定
  const xScale = d3.scaleTime()
    .domain([currentDate, d3.timeDay.offset(currentDate, 365 * 3)]) // 3年後の日付
    .range([margin.left, width - margin.right]);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(this.posterior_pdf)])
    .range([height - margin.bottom, margin.top]);

  const line = d3.line()
    .x((d, i) => xScale(d3.timeDay.offset(currentDate, this.x[i])))
    .y((d) => yScale(d));

  // グラフを描画
  svg.append('path')
    .datum(this.posterior_pdf)
    .attr('fill', 'none')
    .attr('stroke', 'steelblue')
    .attr('stroke-width', 2)
    .attr('d', line)
    .attr('class', 'line-bayesian');

  // X軸に垂直な赤い破線を1年後の位置に追加
  svg.append('line')
    .attr('x1', xScale(oneYearLater))
    .attr('y1', margin.top)
    .attr('x2', xScale(oneYearLater))
    .attr('y2', height - margin.bottom)
    .attr('stroke', 'red')
    .attr('stroke-width', 2)
    .attr('stroke-dasharray', '4 4'); // 破線パターン

  // X軸の目盛（1か月ごと）
  svg.append('g')
    .attr('transform', `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(xScale)
      .ticks(d3.timeMonth.every(1)) // 1か月ごとに目盛を追加
      .tickFormat(d3.timeFormat('%Y-%m-%d')))
    .selectAll('text')
    .attr('x', -10)
    .attr('y', 10)
    .attr('transform', 'rotate(-45)')
    .style('text-anchor', 'end');

  // Y軸のラベル
  svg.append('g')
    .attr('transform', `translate(${margin.left},0)`)
    .call(d3.axisLeft(yScale))
    .append('text')
    .attr('transform', 'rotate(-90)')
    .attr('x', -height / 2)
    .attr('y', -50)
    .attr('fill', 'black')
    .attr('text-anchor', 'middle')
    .style('font-size', '14px')
    .text('故障確率');

  // 凡例の追加
  const legend = svg.append('g')
    .attr('transform', `translate(${width + margin.right - 100},${margin.top})`);

  // MTBFの凡例
  legend.append('line')
    .attr('x1', 0)
    .attr('y1', 0)
    .attr('x2', 20)
    .attr('y2', 0)
    .attr('stroke', 'red')
    .attr('stroke-width', 2)
    .attr('stroke-dasharray', '4 4');

  legend.append('text')
    .attr('x', 30)
    .attr('y', 5)
    .text('MTBF');

  // ベイズ予測の凡例
  legend.append('line')
    .attr('x1', 0)
    .attr('y1', 20)
    .attr('x2', 20)
    .attr('y2', 20)
    .attr('stroke', 'steelblue')
    .attr('stroke-width', 2);

  legend.append('text')
    .attr('x', 30)
    .attr('y', 25)
    .text('ベイズ予測');
}

,

        calculateImpact(value) {
            // 影響度の計算ロジック
            if (value === null || value === undefined) {
                return 'N/A';
            }

            // ここでは仮に値を100で割ることで影響度を求めています
            // 必要に応じてビジネスロジックに基づいて計算を変更します
            const impact = value / 100;

            // 影響度をフォーマットして返す
            return impact.toFixed(2);
        }
    }
};
</script>

<style scoped>
.container {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.parameters {
    margin-top: 20px;
    font-size: 14px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th,
td {
    border: 1px solid #ddd;
    padding: 6px; /* 少し縮めるためにpaddingを減らす */
    text-align: center;
    font-size: 12px; /* フォントサイズを少し小さくする */
}

th {
    background-color: #f4f4f4;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

tr:hover {
    background-color: #e0e0e0;
}

svg {
    background-color: #f9f9f9;
    border-radius: 4px;
}

.axis-label {
    font-size: 12px;
    font-weight: bold;
    fill: black;
}
</style>
