<template>
  <div class="app-container">
    <div class="chart-container">
      <div class="chart-and-description">
        <h2>Pattern A</h2>
        <JohnMoubrayBathtubCurveChart pattern="A" />
      </div>
      <div class="description">
        <h3>パターンA</h3>
        <p><strong>概要:</strong> 初期故障が多く、時間の経過とともに故障率が低下します。</p>
        <p><strong>特長:</strong> 製品の初期段階での欠陥が原因であることが多い。</p>
        <p><strong>対策:</strong> 初期段階での検査と試運転の強化。</p>
      </div>
    </div>

    <div class="chart-container">
      <div class="chart-and-description">
        <h2>Pattern B</h2>
        <JohnMoubrayBathtubCurveChart pattern="B" />
      </div>
      <div class="description">
        <h3>パターンB</h3>
        <p><strong>概要:</strong> 故障率が一定で、突然上昇する。</p>
        <p><strong>特長:</strong> コンポーネントが摩耗して故障する前兆がある。</p>
        <p><strong>対策:</strong> 定期的な交換や事前のメンテナンス。</p>
      </div>
    </div>

    <div class="chart-container">
      <div class="chart-and-description">
        <h2>Pattern C</h2>
        <JohnMoubrayBathtubCurveChart pattern="C" />
      </div>
      <div class="description">
        <h3>パターンC</h3>
        <p><strong>概要:</strong> 故障率が徐々に増加する。</p>
        <p><strong>特長:</strong> 摩耗が徐々に進行する。</p>
        <p><strong>対策:</strong> 定期的な検査と交換。</p>
      </div>
    </div>

    <div class="chart-container">
      <div class="chart-and-description">
        <h2>Pattern D</h2>
        <JohnMoubrayBathtubCurveChart pattern="D" />
      </div>
      <div class="description">
        <h3>パターンD</h3>
        <p><strong>概要:</strong> 故障率がランダムに発生する。</p>
        <p><strong>特長:</strong> 故障の予測が困難である。</p>
        <p><strong>対策:</strong> 予防保全よりも予測保全の活用。</p>
      </div>
    </div>

    <div class="chart-container">
      <div class="chart-and-description">
        <h2>Pattern E</h2>
        <JohnMoubrayBathtubCurveChart pattern="E" />
      </div>
      <div class="description">
        <h3>パターンE</h3>
        <p><strong>概要:</strong> 故障率が低下する。</p>
        <p><strong>特長:</strong> 初期故障後、安定した性能を示す。</p>
        <p><strong>対策:</strong> 初期検査と継続的なモニタリング。</p>
      </div>
    </div>

    <div class="chart-container">
      <div class="chart-and-description">
        <h2>Pattern F</h2>
        <JohnMoubrayBathtubCurveChart pattern="F" />
      </div>
      <div class="description">
        <h3>パターンF</h3>
        <p><strong>概要:</strong> 故障率が急激に上昇する。</p>
        <p><strong>特長:</strong> 突発的な故障が多発。</p>
        <p><strong>対策:</strong> 故障の早期検知と即時対応。</p>
      </div>
    </div>

    <div class="references">
      <h3>参考文献</h3>
      <p>
        ジョン・ムーブレイ（John Moubray）は、信頼性中心のメンテナンス（RCM: Reliability-Centered Maintenance）に関する研究で有名です。バスタブ曲線のパターンは彼の著作で詳しく説明されています。
      </p>
    </div>
  </div>
</template>

<script>
import JohnMoubrayBathtubCurveChart from '@/components/Critical_equipment_list/CeListDetailPage/JohnMoubrayBathtubCurveChart.vue';

export default {
  components: {
    JohnMoubrayBathtubCurveChart,
  },
};
</script>

<style scoped>
.app-container {
  background-color: white;
  padding: 20px;
}

.chart-container {
  display: flex;
  align-items: flex-start;
  margin-bottom: 20px;
}

.chart-and-description {
  flex: 1;
  min-width: 300px;
}

.description {
  margin-left: 10px;
  max-width: 300px;
}

h3 {
  margin-top: 0;
}

.references {
  margin-top: 20px;
  padding: 10px;
  border-top: 1px solid #ccc;
}

.references h3 {
  margin-top: 0;
}
</style>
