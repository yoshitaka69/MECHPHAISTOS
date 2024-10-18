<template>
  <div class="base-content">
    <!-- メインコンテンツエリア -->
    <div class="main-content">
      <Trend_map />
    </div>

    <!-- 右サイドバーエリア -->
    <div class="side-area right-side">
      <Broken_Analysis_Board />
    </div>

    <!-- 新しい横幅いっぱいの領域を追加 -->
    <div class="full-width-content">
      <DemandBoard />
    </div>
  </div>
</template>

<script>
import Trend_map from '@/components/Trend_map/Trend_map.vue';
import Broken_Analysis_Board from '@/components/Trend_map/Broken_Analysis_Board.vue'; // 右サイドバーのコンポーネント
import DemandBoard from '@/components/Trend_map/World_Trend_Board.vue'; // 新しいコンポーネント

export default {
  components: {
    Trend_map,
    Broken_Analysis_Board, // コンポーネントを登録
    DemandBoard // 新しいDemandBoardコンポーネントを登録
  }
};
</script>

<style scoped>
.base-content {
  display: grid;
  grid-template-columns: 3fr 2fr; /* 左を広く、右を2/3の割合で表示 */
  grid-template-rows: 1fr auto; /* 2行目を自動調整して横幅いっぱいにする */
  gap: 20px; /* 各グリッド間の隙間を設定 */
  padding: 20px;
  background-color: black; /* 背景を黒に設定 */
  color: white; /* テキストを白に設定 */
  min-height: 100vh; /* ベースコンテンツの高さを100vhに設定 */
}

.main-content {
  background-color: #333; /* メインコンテンツの背景色 */
  padding: 20px;
  border-radius: 8px;
  overflow: hidden; /* はみ出しを防ぐ */
  grid-column: 1 / 2; /* 左列に配置 */
  grid-row: 1; /* 1行目に配置 */
  height: 100%; /* 高さを100%に設定して親要素に合わせる */
}

.side-area {
  background-color: #444; /* サイドエリアの背景色 */
  padding: 20px;
  border-radius: 8px;
  grid-column: 2 / 3; /* 右列に配置 */
  grid-row: 1; /* 1行目に配置 */
  height: 100%; /* 高さを100%に設定して親要素に合わせる */
  overflow: auto; /* はみ出し防止用 */
}

.full-width-content {
  background-color: #222; /* 新しい領域の背景色を設定 */
  padding: 20px;
  border-radius: 8px;
  grid-column: 1 / 3; /* 全幅に広げる */
  grid-row: 2; /* 2行目に配置 */
  height: auto; /* 高さはコンテンツに合わせて自動 */
  width: 100%; /* 横幅一杯に広げる */
}

/* レスポンシブ対応 */
@media screen and (max-width: 768px) {
  .base-content {
    grid-template-columns: 1fr; /* 全体を1列にする */
    grid-template-rows: auto; /* 行の設定を1列に変更 */
  }

  .main-content, .side-area, .full-width-content {
    max-width: 100%; /* メインコンテンツとサイドコンテンツ、フルワイドコンテンツを全幅に */
  }
}
</style>
