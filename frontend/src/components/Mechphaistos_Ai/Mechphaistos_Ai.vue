<template>
  <div class="mechphaistos-container">
    <div id="mechphaistos_ai">
      <BubbleComment
        imageSrc="/MECHPHAISTOS_AI/MECHPHISTOS_AI.webp"
        comment="This is a sample comment"
        :bubbleTop="20" 
      />
    </div>
  </div>
</template>

<script>
import BubbleComment from './BubbleComment.vue';

export default {
  name: 'Mechphaistos_Ai',
  components: {
    BubbleComment
  }
};
</script>

<style scoped>
.mechphaistos-container {
  display: flex;
  justify-content: flex-end; /* 子要素を右寄せに配置 */
  margin-top: 5px; /* 上のマージンを調整 */
}

#mechphaistos_ai {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
}
</style>
