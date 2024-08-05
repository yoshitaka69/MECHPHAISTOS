<template>
  <div class="form-container">
    <div class="content">
      <div class="safety-request-form">
        <!-- フォームのタイトルをSafety Request Formに変更 -->
        <h2 class="form-title">Safety Request Form</h2>
        <form>
          <!-- フォームを左側に配置 -->
          <div class="form-group">
            <label for="constructionPeriod">Construction Period:</label>
            <input type="text" v-model="safetyRequest.constructionPeriod" />
          </div>
          <div class="form-group">
            <label for="plant">Plant:</label>
            <input type="text" v-model="safetyRequest.plant" />
          </div>
          <div class="form-group">
            <label for="equipment">Equipment:</label>
            <input type="text" v-model="safetyRequest.equipment" />
          </div>
          <div class="form-group">
            <label for="taskName">Task Name:</label>
            <input type="text" v-model="safetyRequest.taskName" />
          </div>
          <div class="form-group">
            <label for="personInCharge">Person in Charge:</label>
            <input type="text" v-model="safetyRequest.personInCharge" />
          </div>
          <div class="form-group">
            <label for="contractor">Contractor:</label>
            <input type="text" v-model="safetyRequest.contractor" />
          </div>
          <div class="form-group">
            <label for="gasDetection">Gas Detection:</label>
            <InputSwitch v-model="safetyRequest.gasDetection" />
          </div>
          <div class="form-group">
            <label for="oxygenDeficiency">Oxygen Deficiency:</label>
            <InputSwitch v-model="safetyRequest.oxygenDeficiency" />
          </div>
        </form>
      </div>
      <div class="pages">
        <div v-for="(page, index) in pages" :key="index" class="page">
          <form @submit.prevent="submitForm">
            <!-- フォームのタイトルを追加 -->
            <h2 class="form-title">Safety Confirmation Certificate</h2>

            <!-- 左側の入力内容を表示 -->
            <div class="form-grid">
              <div class="form-group grid-item">
                <label>Construction Period:</label>
                <hr class="separator" />
                <p>{{ safetyRequest.constructionPeriod }}</p>
              </div>
              <div class="form-group grid-item">
                <label>Plant:</label>
                <hr class="separator" />
                <p>{{ safetyRequest.plant }}</p>
              </div>
              <div class="form-group grid-item">
                <label>Equipment:</label>
                <hr class="separator" />
                <p>{{ safetyRequest.equipment }}</p>
              </div>
              <div class="form-group grid-item">
                <label>Task Name:</label>
                <hr class="separator" />
                <p>{{ safetyRequest.taskName }}</p>
              </div>
              <div class="form-group grid-item">
                <label>Person in Charge:</label>
                <hr class="separator" />
                <p>{{ safetyRequest.personInCharge }}</p>
              </div>
              <div class="form-group grid-item">
                <label>Contractor:</label>
                <hr class="separator" />
                <p>{{ safetyRequest.contractor }}</p>
              </div>
            </div>

            <!-- 現場での安全化は必要か? の質問 -->
            <div class="form-group question-full">
              <label>Is on-site safety necessary?</label>
              <hr class="separator" />
              <InputSwitch v-model="page.onSiteSafety" />
            </div>

            <!-- 脱圧、液抜き、洗浄は実施済ですか? の質問 -->
            <div class="form-group question-full">
              <label>Have the depressurization, liquid removal, and cleaning been completed?</label>
              <hr class="separator" />
            </div>

            <!-- Valve 1-5 のスイッチを表示 -->
            <div class="grid-multiple">
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve1 && !page.valve1 }]">
                <label for="valve1">Valve 1:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.valve1" />
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve2 && !page.valve2 }]">
                <label for="valve2">Valve 2:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.valve2" />
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve3 && !page.valve3 }]">
                <label for="valve3">Valve 3:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.valve3" />
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve4 && !page.valve4 }]">
                <label for="valve4">Valve 4:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.valve4" />
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve5 && !page.valve5 }]">
                <label for="valve5">Valve 5:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.valve5" />
              </div>
            </div>

            <!-- 動力の遮断を実施し、LOTOを実施済か？ の質問 -->
            <div class="form-group question-full">
              <label>Has power disconnection and LOTO been completed?</label>
              <hr class="separator" />
            </div>

            <!-- Breaker 1-5 のスイッチを表示 -->
            <div class="grid-multiple">
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker1 && !page.breaker1 }]">
                <label for="breaker1">Breaker 1:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.breaker1" />
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker2 && !page.breaker2 }]">
                <label for="breaker2">Breaker 2:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.breaker2" />
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker3 && !page.breaker3 }]">
                <label for="breaker3">Breaker 3:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.breaker3" />
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker4 && !page.breaker4 }]">
                <label for="breaker4">Breaker 4:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.breaker4" />
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker5 && !page.breaker5 }]">
                <label for="breaker5">Breaker 5:</label>
                <hr class="separator" />
                <InputSwitch v-model="page.breaker5" />
              </div>
            </div>
          </form>
          <div class="page-number">Page {{ index + 1 }}</div>
        </div>
        <div class="page">
          <!-- 2ページ目 -->
          <h2 class="form-title">Safety Confirmation Certificate</h2>
          <div class="date-display">{{ currentDate }}</div>
          <div class="form-group question-full">
            <label>Is there any flammable gas in the vicinity?</label>
            <hr class="separator" />
          </div>
          <div class="form-group question-full">
            <label>Gas Detection:</label>
            <hr class="separator" />
            <InputSwitch v-model="safetyRequest.gasDetection" />
          </div>
          <div class="form-group question-full">
            <label>Is the oxygen concentration in the tank at an appropriate level and maintainable?</label>
            <hr class="separator" />
          </div>
          <div class="form-group question-full">
            <label>Oxygen Deficiency:</label>
            <hr class="separator" />
            <InputSwitch v-model="safetyRequest.oxygenDeficiency" />
          </div>
          <div class="page-number">Page 2</div>
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
  valve4: false,
  valve5: false,
  breaker1: false,
  breaker2: false,
  breaker3: false,
  breaker4: false,
  breaker5: false,
  constructionPeriod: '',
  plant: '',
  equipment: '',
  taskName: '',
  personInCharge: '',
  contractor: '',
  gasDetection: false,
  oxygenDeficiency: false,
  onSiteSafety: false,
  isolationCompleted: false,
});

const pages = ref([
  {
    valve1: false,
    valve2: false,
    valve3: false,
    valve4: false,
    valve5: false,
    breaker1: false,
    breaker2: false,
    breaker3: false,
    breaker4: false,
    breaker5: false,
    onSiteSafety: false,
  },
]);

const showConfirmation = ref(false);
const showSuccess = ref(false);
const currentDate = ref(new Date().toLocaleDateString());

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
    (safetyRequest.value.valve4 && !page.valve4) ||
    (safetyRequest.value.valve5 && !page.valve5) ||
    (safetyRequest.value.breaker1 && !page.breaker1) ||
    (safetyRequest.value.breaker2 && !page.breaker2) ||
    (safetyRequest.value.breaker3 && !page.breaker3) ||
    (safetyRequest.value.breaker4 && !page.breaker4) ||
    (safetyRequest.value.breaker5 && !page.breaker5)
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

.content {
  display: flex;
  gap: 16px;
}

.safety-request-form {
  width: 300px;
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

.form-title {
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 8px; /* スペースを小さく */
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 2列のグリッド */
  gap: 16px; /* グリッドアイテム間のスペース */
}

.grid-multiple {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* 5列のグリッド */
  gap: 16px; /* グリッドアイテム間のスペース */
}

.grid-item {
  border: 1px solid #000; /* 黒の細い線で囲む */
  padding: 8px;
  border-radius: 4px;
  min-height: 120px; /* 高さを拡大 */
}

.grid-item-small {
  border: 1px solid #000; /* 黒の細い線で囲む */
  padding: 8px;
  border-radius: 4px;
  text-align: center; /* 中央寄せ */
  min-height: 80px; /* 高さを調整 */
}

.grid-item-full {
  border: 1px solid #000; /* 黒の細い線で囲む */
  padding: 8px;
  border-radius: 4px;
  text-align: center; /* 中央寄せ */
  grid-column: span 5; /* 5列にまたがる */
}

.form-group {
  margin-bottom: 8px; /* 隙間を小さく調整 */
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

.question-full {
  width: 100%; /* A4いっぱいに広げる */
  margin-bottom: 4px; /* 隙間を小さく調整 */
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

.date-display {
  text-align: right;
  font-size: 12px;
  position: absolute;
  top: 10px;
  right: 10px;
}

.separator {
  border: none;
  border-bottom: 1px solid #000;
  margin: 4px 0;
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
