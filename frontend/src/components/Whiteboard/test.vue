<!-- Whiteboard.vue -->
<template>
  <div class="whiteboard">
    <button @click="addPostIt">新しいメモを追加</button>
    <draggable v-model="postIts" @end="onEnd">
      <template #item="{ element }">
        <post-it :postIt="element" @remove="removePostIt" @update="updatePostIt" />
      </template>
    </draggable>
  </div>
</template>

<script>
import draggable from 'vuedraggable';
import PostIt from '../../views/pages/PostIt.vue';

export default {
  components: { draggable, PostIt },
  data() {
    return {
      postIts: []
    };
  },
  methods: {
    addPostIt() {
      const newPostIt = {
        id: Date.now(),
        content: '',
        x: 0,
        y: 0
      };
      this.postIts.push(newPostIt);
    },
    removePostIt(id) {
      this.postIts = this.postIts.filter(postIt => postIt.id !== id);
    },
    updatePostIt(updatedPostIt) {
      const index = this.postIts.findIndex(postIt => postIt.id === updatedPostIt.id);
      this.$set(this.postIts, index, updatedPostIt);
    },
    onEnd(event) {
      // ドラッグ終了時の処理（必要に応じて）
    }
  }
};
</script>

<style>
.whiteboard {
  position: relative;
  width: 100%;
  height: 100vh;
  background-color: #f0f0f0;
}
</style>
