<template>
  <footer>
    <button @click="toggleGrid">グリッド線オン/オフ</button>
  </footer>
</template>

<script>
export default {
  emits: ['toggleGrid']
}
</script>

<style>
footer {
  background-color: #333;
  color: white;
  padding: 1rem;
  display: flex;
  justify-content: center;
}
button {
  background: none;
  border: 1px solid white;
  color: white;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
button:hover {
  background-color: white;
  color: #333;
}
</style>
