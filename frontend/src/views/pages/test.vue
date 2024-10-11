<template>
    <div>
      <h3>Assessment Distribution</h3>
      <div id="AssessmentChart" ref="chartContainer" style="width: 100%; height: 400px;"></div>
    </div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  import axios from 'axios';
  import { useUserStore } from '@/stores/userStore';
  
  export default {
    data() {
      return {
        error: null,
        assessmentCounts: {
          'High+': 0,
          'High': 0,
          'Middle': 0,
          'Low': 0,
          'Review': 0,
        },
      };
    },
  
    mounted() {
      this.fetchDataAndCountAssessments();
    },
  
    methods: {
      fetchDataAndCountAssessments() {
        const userStore = useUserStore();
        const companyCode = userStore.companyCode;
  
        if (!companyCode) {
          this.error = 'No company code found for the user.';
          console.error(this.error);
          return;
        }
  
        const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${companyCode}`;
        console.log('Fetching data from:', url);
  
        axios.get(url)
          .then((response) => {
            console.log('Response data:', response.data);
  
            // データがない場合、ダミーデータを使用
            if (response.data.length === 0) {
              this.assessmentCounts = {
                'High+': 1,
                'High': 1,
                'Middle': 1,
                'Low': 1,
                'Review': 1,
              };
              console.log('No data found. Using dummy data:', this.assessmentCounts);
            } else {
              this.countAssessments(response.data);
            }
  
            this.$nextTick(() => {
              this.plotGraph();
            });
          })
          .catch((error) => {
            console.error('Error fetching data:', error);
            this.error = 'Failed to fetch data. Using dummy data.';
            
            // エラーが発生した場合もダミーデータを使用
            this.assessmentCounts = {
              'High+': 1,
              'High': 1,
              'Middle': 1,
              'Low': 1,
              'Review': 1,
            };
            this.$nextTick(() => {
              this.plotGraph();
            });
          });
      },
  
      countAssessments(data) {
        // カウントの初期化
        this.assessmentCounts = {
          'High+': 0,
          'High': 0,
          'Middle': 0,
          'Low': 0,
          'Review': 0,
        };
  
        // assessmentがnullでない場合のみカウント
        data.forEach(item => {
          const assessment = item.assessment;
          if (assessment && assessment in this.assessmentCounts) {
            this.assessmentCounts[assessment]++;
          }
        });
  
        console.log('Final assessment counts:', this.assessmentCounts);
      },
  
      plotGraph() {
        const chartElement = this.$refs.chartContainer;
        if (!chartElement) {
          console.error('Chart container not found.');
          return;
        }
  
        const width = chartElement.clientWidth;
        const height = chartElement.clientHeight;
        const radius = Math.min(width, height) / 2;
  
        // データを準備
        const data = Object.entries(this.assessmentCounts).map(([label, value]) => ({
          label,
          value
        }));
  
        // D3用の色スケール
        const color = d3.scaleOrdinal()
          .domain(data.map(d => d.label))
          .range(d3.schemeCategory10);
  
        // SVGのクリア
        d3.select(chartElement).select('svg').remove();
  
        // SVGを追加
        const svg = d3.select(chartElement)
          .append('svg')
          .attr('width', width)
          .attr('height', height)
          .append('g')
          .attr('transform', `translate(${width / 2},${height / 2})`);
  
        // パイ生成器
        const pie = d3.pie()
          .value(d => d.value)
          .sort(null);
  
        // 弧生成器
        const arc = d3.arc()
          .innerRadius(0)
          .outerRadius(radius);
  
        // パスを生成し、色とデータをバインド
        svg.selectAll('path')
          .data(pie(data))
          .enter()
          .append('path')
          .attr('d', arc)
          .attr('fill', d => color(d.data.label))
          .attr('stroke', '#ffffff')
          .style('stroke-width', '2px');
  
        // ラベルを追加
        svg.selectAll('text')
          .data(pie(data))
          .enter()
          .append('text')
          .attr('transform', d => `translate(${arc.centroid(d)})`)
          .attr('dy', '0.35em')
          .style('text-anchor', 'middle')
          .style('font-size', '12px')
          .text(d => `${d.data.label} (${d.data.value})`);
  
        // 凡例の追加
        const legend = svg.append('g')
          .attr('transform', `translate(${radius + 20}, -${radius})`);
  
        legend.selectAll('rect')
          .data(data)
          .enter()
          .append('rect')
          .attr('x', 0)
          .attr('y', (d, i) => i * 20)
          .attr('width', 18)
          .attr('height', 18)
          .style('fill', d => color(d.label));
  
        legend.selectAll('text')
          .data(data)
          .enter()
          .append('text')
          .attr('x', 24)
          .attr('y', (d, i) => i * 20 + 9)
          .attr('dy', '0.35em')
          .style('text-anchor', 'start')
          .text(d => `${d.label}: ${d.value}`);
      }
    }
  };
  </script>
  
  <style scoped>
    svg {
      width: 100%;
      height: 100%;
    }
  </style>
  