<template>
  <div class="bubble-comment">
    <div class="image-container">
      <img :src="imageSrc" alt="icon" class="icon" />
      <div class="image-caption">MECHPHAISTOS</div>
    </div>
    <div class="comment-bubble" :style="{ top: `${bubbleTop}px` }">
      {{ comment }}
      <div class="comment-arrow"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    imageSrc: String,
    comment: String,
    bubbleTop: {
      type: Number,
      default: 260
    }
  }
};
</script>

<style scoped>
.bubble-comment {
  position: relative;
  display: inline-block;
  margin-left: auto; /* 右寄せにするために追加 */
}
.image-container {
  display: inline-block;
  background-color: white;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
  margin: 10px; /* 画像コンテナのマージンを追加 */
}
.icon {
  width: 220px; /* 一回り大きくする */
  height: 220px;
}
.image-caption {
  margin-top: 10px;
  font-size: 14px;
  font-weight: bold;
}
.comment-bubble {
  position: absolute;
  left: -700px; /* 少し左に移動 */
  background-color: white;
  border: 1px solid #ccc;
  padding: 20px; /* 少し大きくする */
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 730px; /* 幅を広げる */
  height: 200px; /* 高さを調整する */
}
.comment-arrow {
  /* コメントの角を右側面に移動する */
  position: absolute;
  top: 20px; /* 吹き出しの高さを調整 */
  right: -10px; /* 吹き出しの位置を調整 */
  width: 0;
  height: 0;
  border-top: 15px solid transparent; /* 上部の透明な部分 */
  border-bottom: 15px solid transparent; /* 下部の透明な部分 */
  border-left: 15px solid white; /* 左側の白い部分が吹き出しの角になります */
}
</style>
