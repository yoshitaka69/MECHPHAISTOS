<template>
  <div class="document">
    <h3>{{ doc.title }}</h3>
    <p>{{ doc.content }}</p>
  </div>
</template>

<script>
export default {
  props: ['doc']
};
</script>

<style>
.document {
  background-color: #fff;
  padding: 10px;
  margin: 5px 0;
  box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}
</style>
