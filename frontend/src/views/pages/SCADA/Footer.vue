<template>
    <footer class="footer">
      <p>&copy; 2024 SCADA System</p>
      <button @click="$emit('toggle-grid')">{{ gridVisible ? 'Hide Grid' : 'Show Grid' }}</button>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'Footer',
    props: {
      gridVisible: {
        type: Boolean,
        required: true,
      },
    },
  };
  </script>
  
  <style>
  .footer {
    width: 100%;
    background-color: #007bff;
    color: #fff;
    padding: 10px 0;
    text-align: center;
    flex-shrink: 0;
  }
  </style>
  