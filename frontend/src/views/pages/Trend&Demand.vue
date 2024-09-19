<template>
  <div class="base-content">
    <!-- 左サイドバーエリア -->
    <div class="side-area left-side">
      <!-- World Trend Ranking テーブルを挿入 -->
      <WorldTrendRanking />
    </div>

    <!-- メインコンテンツエリア -->
    <div class="main-content">
      <Trend_map />
    </div>

    <!-- サブコンテンツエリア -->
    <div class="sub-content">
      <!-- 横に並んだチャートのコンポーネントを挿入 -->
      <ChartsRow />
    </div>

    <!-- 右サイドバーエリア -->
    <div class="side-area right-side">
      <!-- World Demand Ranking テーブルを挿入 -->
      <WorldDemandRanking />
    </div>
  </div>
</template>

<script>
import Trend_map from '@/components/Trend_map/Trend_map.vue';
import WorldDemandRanking from '@/components/Trend_map/WorldDemandRanking.vue'; // 右サイドバーのコンポーネント
import WorldTrendRanking from '@/components/Trend_map/WorldTrendRanking.vue'; // 左サイドバーのコンポーネント
import ChartsRow from '@/components/Trend_map/ChartsRow.vue'; // サブコンテンツのチャートコンポーネント

export default {
  components: {
    Trend_map,
    WorldDemandRanking, // コンポーネントを登録
    WorldTrendRanking, // コンポーネントを登録
    ChartsRow // コンポーネントを登録
  }
};
</script>

<style scoped>
.base-content {
  display: grid;
  grid-template-columns: 1fr 3fr 1fr; /* 左右のサイドバーと中央のメインコンテンツの割合を設定 */
  grid-template-rows: auto auto; /* 行の設定を追加して、メインとサブコンテンツを縦に並べる */
  gap: 20px; /* 各グリッド間の隙間を設定 */
  padding: 20px;
  background-color: black; /* 背景を黒に設定 */
  color: white; /* テキストを白に設定 */
  min-height: 100vh; /* ビューポート全体の高さに合わせる */
}

.side-area {
  background-color: #444; /* サイドエリアの背景色 */
  padding: 20px;
  border-radius: 8px;
  grid-row: 1 / 3; /* サイドエリアを1行目から2行目までの高さに設定 */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: auto; /* はみ出し防止用 */
}

.main-content {
  background-color: #333; /* メインコンテンツの背景色 */
  padding: 20px;
  border-radius: 8px;
  overflow: hidden; /* はみ出しを防ぐ */
  grid-column: 2 / 3; /* 中央列に配置 */
  grid-row: 1; /* 1行目に配置 */
}

.sub-content {
  background-color: #555; /* サブコンテンツの背景色 */
  padding: 20px;
  border-radius: 8px;
  grid-column: 2 / 3; /* 中央列に配置 */
  grid-row: 2; /* サブコンテンツを2行目に配置 */
}

/* レスポンシブ対応 */
@media screen and (max-width: 768px) {
  .base-content {
    grid-template-columns: 1fr; /* 全体を1列にする */
    grid-template-rows: auto; /* 行の設定を1列に変更 */
  }

  .side-area {
    grid-row: auto; /* サイドバーを独立させる */
    max-width: 100%; /* サイドバーを全幅に */
  }

  .main-content, .sub-content {
    max-width: 100%; /* メインコンテンツとサブコンテンツを全幅に */
  }
}
</style>
