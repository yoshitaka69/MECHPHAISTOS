<template>
  <svg width="200" height="200">
    <circle cx="100" cy="100" r="95" fill="none" stroke="black" stroke-width="3" />
    <line :x1="100" :y1="100" :x2="100" :y2="20" :transform="`rotate(${secondsAngle}, 100, 100)`" stroke="red" stroke-width="2"/>
    <line :x1="100" :y1="100" :x2="100" :y2="30" :transform="`rotate(${minutesAngle}, 100, 100)`" stroke="black" stroke-width="3"/>
    <line :x1="100" :y1="100" :x2="100" :y2="40" :transform="`rotate(${hoursAngle}, 100, 100)`" stroke="black" stroke-width="5"/>
  </svg>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const date = ref(new Date());
const secondsAngle = ref(0);
const minutesAngle = ref(0);
const hoursAngle = ref(0);

const updateClock = () => {
    date.value = new Date();
    secondsAngle.value = date.value.getSeconds() * 6;
    minutesAngle.value = date.value.getMinutes() * 6 + date.value.getSeconds() * 0.1;
    hoursAngle.value = (date.value.getHours() % 12) * 30 + date.value.getMinutes() * 0.5;
};

onMounted(() => {
    setInterval(updateClock, 1000);
});
</script>

<style>
svg {
    display: block;
    margin: auto;
    background-color: #fff;
    border-radius: 50%;
    box-shadow: 0 0 10px rgba(0,0,0,0.2);
}
</style>
