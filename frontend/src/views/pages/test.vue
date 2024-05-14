<template>
    <Button :class="buttonClass" :label="label" />
  </template>
  
  <script setup>
  import { computed } from 'vue';
  import { Button } from 'primevue/button';
  
  const props = defineProps({
    label: String,
  });
  
  const buttonClass = computed(() => {
    let classes = [];
    switch (props.label) {
      case 'Very High':
      case 'High':
        classes.push('p-button-danger', 'blinking'); // 'danger'は赤色, 'blinking'は点滅
        break;
      case 'Middle':
        classes.push('p-button-warning'); // 'warning'は黄色
        break;
      case 'Low':
      case 'Very Low':
        classes.push('p-button-success'); // 'success'は緑色
        break;
      default:
        classes.push('p-button-secondary'); // デフォルトのグレー
    }
    return classes.join(' ');
  });
  </script>
  