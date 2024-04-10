<template>
    <div class="card flex justify-content-center">
      <Button label="Show" @click="visible = true" />
      <ModalDialog :visible="visible" @close="onClose" />
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import ModalDialog from '@/views/pages/test(child).vue';
  
  const visible = ref(false);
  
  const onClose = () => {
    visible.value = false;
  };
  
  </script>