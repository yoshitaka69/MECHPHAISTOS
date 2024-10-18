<template>
    <div v-if="selectedRow">
      <h3>Selected Row Details</h3>
      <p><strong>ID:</strong> {{ selectedRow.id }}</p>
      <p><strong>Name:</strong> {{ selectedRow.name }}</p>
      <p><strong>Age:</strong> {{ selectedRow.age }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      selectedRow: {
        type: Object,
        default: null,
      },
    },
  };
  </script>
  
  <style scoped>
  div {
    margin-top: 20px;
  }
  </style>
  