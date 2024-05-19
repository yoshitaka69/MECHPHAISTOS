<!-- PostIt.vue -->
<template>
    <div class="post-it" :style="{ top: postIt.y + 'px', left: postIt.x + 'px' }" @dblclick="editMode = true">
      <div v-if="editMode">
        <textarea v-model="localContent" @blur="saveContent" @keyup.enter="saveContent"></textarea>
      </div>
      <div v-else>
        <p>{{ postIt.content }}</p>
        <button @click="remove">削除</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['postIt'],
    data() {
      return {
        editMode: false,
        localContent: this.postIt.content
      };
    },
    methods: {
      remove() {
        this.$emit('remove', this.postIt.id);
      },
      saveContent() {
        this.editMode = false;
        this.$emit('update', { ...this.postIt, content: this.localContent });
      }
    }
  };
  </script>
  
  <style>
  .post-it {
    position: absolute;
    width: 200px;
    height: 200px;
    background-color: yellow;
    padding: 10px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    cursor: pointer;
  }
  textarea {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
  }
  </style>
  