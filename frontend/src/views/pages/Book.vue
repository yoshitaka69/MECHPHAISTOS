<template>
  <div class="book-container" @click="toggleBook">
    <div class="book" :class="{ 'is-open': isOpen, 'is-centered': isCentered }">
      <div class="book-spine">{{ book.title }}</div>
      <div class="book-pages">
        <div class="book-content" v-if="isOpen">
          <ul>
            <li v-for="doc in book.documents" :key="doc.id">
              <Document :doc="doc" />
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Document from './Document.vue';

export default {
  props: ['book'],
  data() {
    return {
      isOpen: false,  // 本が開いているかどうか
      isCentered: false // 本が中央に来たかどうかを管理
    };
  },
  methods: {
    toggleBook() {
      if (!this.isCentered) {
        // 本を中央に移動させ、少し待ってから開く
        this.isCentered = true;
        setTimeout(() => {
          this.isOpen = true;
        }, 800); // 800ms後に本を開く
      } else {
        // 本を閉じて元に戻す
        this.isOpen = false;
        setTimeout(() => {
          this.isCentered = false;
        }, 500); // 500ms後に元の位置に戻す
      }
    }
  },
  components: { Document }
};
</script>

<style>
.book-container {
  perspective: 1000px;
}

.book {
  width: 150px;
  height: 250px;
  position: relative;
  transform-style: preserve-3d;
  transform-origin: left;
  transition: transform 0.8s ease, width 0.8s ease, height 0.8s ease;
  cursor: pointer;
}

.book.is-centered {
  /* 本がさらに画面中央に近い位置に移動し、サイズも大きくなる */
  position: fixed;
  top: 40%; /* より中央に近い位置 */
  left: 50%;
  transform: translate(-50%, -40%) translateZ(50px); /* より中央へ */
  width: 500px; /* 本のサイズをさらに大きくする */
  height: 700px;
}

.book.is-open {
  /* 本が中央で開くアニメーション */
  transform: translate(-50%, -40%) translateZ(50px) rotateY(-140deg);
}

.book-spine {
  background-color: #8b4513;
  color: white;
  text-align: center;
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.2rem;
  backface-visibility: hidden; /* 裏側を非表示 */
}

.book-pages {
  position: absolute;
  top: 0;
  left: 100%;
  width: 100%;
  height: 100%;
  background-color: #f5f5f5;
  transform: rotateY(0deg);
  backface-visibility: hidden; /* 裏側を非表示 */
}

.book-content {
  padding: 20px;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1);
  opacity: 0;
  transition: opacity 0.5s ease;
}

.book.is-open .book-content {
  opacity: 1; /* 本が開いたときにコンテンツが表示される */
}
</style>
