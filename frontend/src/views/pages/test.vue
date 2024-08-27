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
  import BubbleComment from '@/components/Mechphaistos_Ai/BubbleComment.vue';
  
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
    justify-content: flex-end;
    margin-top: 5px;
    width: 100%; /* 親要素に対して幅を100%にする */
  }
  
  #mechphaistos_ai {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    text-align: center;
    width: 100%; /* 親要素に対して幅を100%にする */
  }
  </style>
  