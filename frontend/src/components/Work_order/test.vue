<template>
  <div class="form-container">
    <h1 class="title">Safety Form</h1>
    <div class="buttons">
      <Button label="Submit" icon="pi pi-check" @click="handleSubmit" />
    </div>
    <div class="content">
      <div class="safety-request-form">
        <h2>Safety Request Form</h2>
        <form>
          <div class="form-group">
            <label for="valve1">Valve 1:</label>
            <InputSwitch v-model="safetyRequest.valve1" />
          </div>
          <div class="form-group">
            <label for="valve2">Valve 2:</label>
            <InputSwitch v-model="safetyRequest.valve2" />
          </div>
          <div class="form-group">
            <label for="valve3">Valve 3:</label>
            <InputSwitch v-model="safetyRequest.valve3" />
          </div>
          <div class="form-group">
            <label for="breaker1">Breaker 1:</label>
            <InputSwitch v-model="safetyRequest.breaker1" />
          </div>
          <div class="form-group">
            <label for="breaker2">Breaker 2:</label>
            <InputSwitch v-model="safetyRequest.breaker2" />
          </div>
          <div class="form-group">
            <label for="breaker3">Breaker 3:</label>
            <InputSwitch v-model="safetyRequest.breaker3" />
          </div>
        </form>
      </div>
      <div class="pages">
        <div v-for="(page, index) in pages" :key="index" class="page">
          <form @submit.prevent="submitForm">
            <div :class="['form-group', { 'bordered': safetyRequest.valve1 && !page.valve1 }]">
              <label for="valve1">Valve 1:</label>
              <InputSwitch v-model="page.valve1" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.valve2 && !page.valve2 }]">
              <label for="valve2">Valve 2:</label>
              <InputSwitch v-model="page.valve2" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.valve3 && !page.valve3 }]">
              <label for="valve3">Valve 3:</label>
              <InputSwitch v-model="page.valve3" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.breaker1 && !page.breaker1 }]">
              <label for="breaker1">Breaker 1:</label>
              <InputSwitch v-model="page.breaker1" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.breaker2 && !page.breaker2 }]">
              <label for="breaker2">Breaker 2:</label>
              <InputSwitch v-model="page.breaker2" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.breaker3 && !page.breaker3 }]">
              <label for="breaker3">Breaker 3:</label>
              <InputSwitch v-model="page.breaker3" />
            </div>
          </form>
          <div class="page-number">Page {{ index + 1 }}</div>
        </div>
        <div v-for="(page, index) in pages" :key="index + pages.length" class="page">
          <form @submit.prevent="submitForm">
            <div :class="['form-group', { 'bordered': safetyRequest.valve1 && !page.valve1 }]">
              <label for="valve1">Valve 1:</label>
              <InputSwitch v-model="page.valve1" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.valve2 && !page.valve2 }]">
              <label for="valve2">Valve 2:</label>
              <InputSwitch v-model="page.valve2" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.valve3 && !page.valve3 }]">
              <label for="valve3">Valve 3:</label>
              <InputSwitch v-model="page.valve3" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.breaker1 && !page.breaker1 }]">
              <label for="breaker1">Breaker 1:</label>
              <InputSwitch v-model="page.breaker1" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.breaker2 && !page.breaker2 }]">
              <label for="breaker2">Breaker 2:</label>
              <InputSwitch v-model="page.breaker2" />
            </div>
            <div :class="['form-group', { 'bordered': safetyRequest.breaker3 && !page.breaker3 }]">
              <label for="breaker3">Breaker 3:</label>
              <InputSwitch v-model="page.breaker3" />
            </div>
          </form>
          <div class="page-number">Page {{ index + 2 }}</div>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <Dialog header="Confirmation" v-model:visible="showConfirmation" :modal="true" :closable="false">
      <p>未安全な項目がありますが、安全化を承認しますか？</p>
      <div class="p-d-flex p-jc-end">
        <Button label="いいえ" icon="pi pi-times" @click="cancelConfirmation" class="p-button-text" />
        <Button label="はい" icon="pi pi-check" @click="confirmApproval" auto-focus />
      </div>
    </Dialog>
    <Dialog header="Success" v-model:visible="showSuccess" :modal="true" :closable="false" :footer="null">
      <p>安全化を承認しました</p>
      <Button label="OK" icon="pi pi-check" @click="closeSuccess" auto-focus />
    </Dialog>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import InputSwitch from 'primevue/inputswitch';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';

const safetyRequest = ref({
  valve1: false,
  valve2: false,
  valve3: false,
  breaker1: false,
  breaker2: false,
  breaker3: false,
});

const pages = ref([
  { valve1: false, valve2: false, valve3: false, breaker1: false, breaker2: false, breaker3: false },
]);

const showConfirmation = ref(false);
const showSuccess = ref(false);

const handleSubmit = () => {
  if (hasUnsafeItems()) {
    showConfirmation.value = true;
  } else {
    showSuccess.value = true;
  }
};

const hasUnsafeItems = () => {
  return pages.value.some(page => (
    (safetyRequest.value.valve1 && !page.valve1) ||
    (safetyRequest.value.valve2 && !page.valve2) ||
    (safetyRequest.value.valve3 && !page.valve3) ||
    (safetyRequest.value.breaker1 && !page.breaker1) ||
    (safetyRequest.value.breaker2 && !page.breaker2) ||
    (safetyRequest.value.breaker3 && !page.breaker3)
  ));
};

const cancelConfirmation = () => {
  showConfirmation.value = false;
};

const confirmApproval = () => {
  showConfirmation.value = false;
  showSuccess.value = true;
};

const closeSuccess = () => {
  showSuccess.value = false;
  // フォームの送信処理をここに追加
};

const submitForm = () => {
  console.log('Form submitted', pages.value);
  // フォームの送信処理をここに追加
};
</script>

<style>
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 16px;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
}

.buttons {
  display: flex;
  gap: 16px;
  position: absolute;
  top: 16px;
  right: 16px;
}

.content {
  display: flex;
  gap: 16px;
}

.safety-request-form {
  width: 200px;
  padding: 16px;
  background-color: #fff;
  border: 1px solid #000;
}

.pages {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
}

.page {
  width: 210mm; /* A4 width */
  height: 297mm; /* A4 height */
  border: 1px solid #000;
  padding: 10mm; /* Reduce padding to increase usable area */
  box-sizing: border-box;
  background-color: #ff9999; /* Change background color to lighter red */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 16px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* Adjust to evenly space out */
}

.bordered {
  border: 2px solid #000;
  background-color: #fff;
  padding: 16px;
  margin-bottom: 16px;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

body {
  background-color: #f5f5f5;
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
}

.page-number {
  text-align: center;
  font-size: 12px;
  position: absolute;
  bottom: 10px;
  left: 0;
  right: 0;
}

@media print {
  .form-container {
    flex-direction: column;
  }
  .page {
    background-color: #ff9999; /* Ensure print background color is the same */
    box-shadow: none;
    border: none;
    page-break-after: always;
  }
  .buttons {
    display: none;
  }
}
</style>
