<template>
    <div class="signal-light">
      <div :class="['light', color1]"></div>
      <div :class="['light', color2]"></div>
      <div :class="['light', color3]"></div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      color1: {
        type: String,
        default: 'gray',
      },
      color2: {
        type: String,
        default: 'gray',
      },
      color3: {
        type: String,
        default: 'gray',
      },
    },
  }
  </script>
  
  <style>
  .signal-light {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: absolute;
    bottom: -15px;
    right: -15px;
  }
  .light {
    width: 10px;
    height: 10px;
    margin: 2px;
    border-radius: 50%;
    background-color: gray;
  }
  .red {
    background-color: red;
  }
  .yellow {
    background-color: yellow;
  }
  .green {
    background-color: green;
  }
  </style>
  