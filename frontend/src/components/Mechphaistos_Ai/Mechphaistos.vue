<template>
  <div class="bubble-comment">
    <div class="comment-bubble">
      <p>
        test
      </p>
      <div class="comment-arrow"></div>
    </div>
    <div class="image-container">
      <img src="@/assets/MECHPHISTOS.jpg" alt="icon" class="icon" />
      <div class="image-caption">MECHPHISTOS</div>
    </div>
  </div>
</template>

<style scoped>
.bubble-comment {
  position: relative;
  display: flex;
  align-items: stretch;
  justify-content: flex-start;
  width: 100%;
  height: 100%;
}

.image-container {
  display: inline-block;
  background-color: white;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
  margin: 10px;
  height: 100%;
}

.icon {
  width: 220px;
  height: 100%;
}

.image-caption {
  margin-top: 10px;
  font-size: 14px;
  font-weight: bold;
}

.comment-bubble {
  background-color: white;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
  width: 100%;
  height: 100%;
  position: relative;
  top: 20px;
  font-size: 24px;
  font-weight: bold;
  white-space: pre-line;
}

.comment-arrow {
  position: absolute;
  right: -10px;
  top: 50%;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-left: 15px solid white;
}
</style>
