<template>
  <div class="information-box">
    <p>{{ message }}</p>
    <button @click="likeMessage">いいね ({{ likes }})</button>
    <Accordion>
      <AccordionTab header="コメント">
        <div class="comments-section">
          <input v-model="newComment" placeholder="コメントを追加" />
          <button @click="addComment">送信</button>
          <ul>
            <li v-for="(comment, index) in comments" :key="index">
              <strong>{{ comment.userName }}</strong> <em>{{ comment.timestamp }}</em><br />
              {{ comment.text }}
            </li>
          </ul>
        </div>
      </AccordionTab>
    </Accordion>
  </div>
</template>

<script>
import { useUserStore } from '@/stores/userStore';

export default {
  name: "InformationBox",
  components: {
    Accordion: () => import('primevue/accordion'),
    AccordionTab: () => import('primevue/accordiontab')
  },
  props: {
    message: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      likes: 0,
      newComment: '',
      comments: [],
      userStore: useUserStore(),
    };
  },
  methods: {
    likeMessage() {
      this.likes += 1;
    },
    addComment() {
      if (this.newComment.trim() !== '') {
        const now = new Date();
        const timestamp = now.toLocaleString();
        const userName = this.userStore.userName;
        this.comments.push({ text: this.newComment, userName, timestamp });
        this.newComment = '';
      }
    },
  },
};
</script>

<style scoped>
.information-box {
    width: 100%;
    max-width: 500px;
    height: 200px;
    border: 1px solid #ccc;
    padding: 1rem;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    margin: 20px auto; /* 中央寄せ */
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    text-align: left; /* テキスト左寄せ */
    background: white; /* 白背景 */
    font-size: 1rem; /* 基本のフォントサイズ */
}
.comments-section {
    margin-top: 1rem;
    width: 100%;
}
.comments-section input {
    width: calc(100% - 80px);
    padding: 0.5rem;
    margin-right: 0.5rem;
}
.comments-section button {
    padding: 0.5rem;
}
.comments-section ul {
    list-style-type: none;
    padding: 0;
    margin-top: 0.5rem;
}
.comments-section li {
    background: #f9f9f9;
    border: 1px solid #eee;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
}
</style>
