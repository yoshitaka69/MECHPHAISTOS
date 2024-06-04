<template>
    <circle :cx="cx" :cy="cy" r="8" fill="red" @mousedown="$emit('start-drag', $event)" />
  </template>
  
  <script>
  export default {
    props: {
      cx: Number,
      cy: Number
    }
  };
  </script>
  