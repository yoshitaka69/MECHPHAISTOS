<template>
  <div class="form-container">
    <Toast /> <!-- Toastコンポーネントを追加 -->
    <div class="content">
      <div class="safety-request-form">
        <h2 class="request-form-title">Safety Request Form</h2>
        <form>
          <div class="form-group">
            <label for="constructionPeriod">Construction Period:</label>
            <br />
            <textarea v-model="safetyRequest.constructionPeriod" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="plant">Plant:</label>
            <br />
            <textarea v-model="safetyRequest.plant" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="equipment">Equipment:</label>
            <br />
            <textarea v-model="safetyRequest.equipment" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="taskName">Task Name:</label>
            <br />
            <textarea v-model="safetyRequest.taskName" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="personInCharge">Person in Charge:</label>
            <br />
            <textarea v-model="safetyRequest.personInCharge" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group contractor-label">
            <label for="contractor">Contractor:</label>
            <br />
            <textarea v-model="safetyRequest.contractor" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="gasDetection">Gas Detection:</label>
            <InputSwitch v-model="safetyRequest.gasDetection" />
          </div>
          <div class="form-group">
            <label for="oxygenDeficiency">Oxygen Deficiency:</label>
            <InputSwitch v-model="safetyRequest.oxygenDeficiency" />
          </div>

          <!-- Valve 1-5 のスイッチを追加 -->
          <div class="grid-two-columns">
            <div class="form-group grid-item-small">
              <label for="valve1_input">Valve 1:</label>
              <InputSwitch v-model="safetyRequest.valve1_input" />
            </div>
            <div class="form-group grid-item-small">
              <label for="valve2_input">Valve 2:</label>
              <InputSwitch v-model="safetyRequest.valve2_input" />
            </div>
            <div class="form-group grid-item-small">
              <label for="valve3_input">Valve 3:</label>
              <InputSwitch v-model="safetyRequest.valve3_input" />
            </div>
            <div class="form-group grid-item-small">
              <label for="valve4_input">Valve 4:</label>
              <InputSwitch v-model="safetyRequest.valve4_input" />
            </div>
            <div class="form-group grid-item-small">
              <label for="valve5_input">Valve 5:</label>
              <InputSwitch v-model="safetyRequest.valve5_input" />
            </div>
          </div>

          <!-- Breaker 1-5 のスイッチを追加 -->
          <div class="grid-two-columns">
            <div class="form-group grid-item-small">
              <label for="breaker1_input">Breaker 1:</label>
              <InputSwitch v-model="safetyRequest.breaker1_input" />
            </div>
            <div class="form-group grid-item-small">
              <label for="breaker2_input">Breaker 2:</label>
              <InputSwitch v-model="safetyRequest.breaker2_input" />
            </div>
            <div class="form-group grid-item-small">
              <label for="breaker3_input">Breaker 3:</label>
              <InputSwitch v-model="safetyRequest.breaker3_input" />
            </div>
            <div class="form-group grid-item-small">
              <label for="breaker4_input">Breaker 4:</label>
              <InputSwitch v-model="safetyRequest.breaker4_input" />
            </div>
            <div class="form-group grid-item-small">
              <label for="breaker5_input">Breaker 5:</label>
              <InputSwitch v-model="safetyRequest.breaker5_input" />
            </div>
          </div>
        </form>
      </div>

      <div class="confirmation-page">
        <h1 class="confirmation-title">Safety Confirmation Certificate</h1>
        <div class="title-space"></div>
        <div class="date-display">{{ currentDate }}</div>

        <div class="form-grid-smaller">
          <div class="form-group grid-item-smaller">
            <label>Construction Period:</label>
            <hr class="separator" />
            <p>{{ safetyRequest.constructionPeriod }}</p>
          </div>
          <div class="form-group grid-item-smaller">
            <label>Plant:</label>
            <hr class="separator" />
            <p>{{ safetyRequest.plant }}</p>
          </div>
          <div class="form-group grid-item-smaller">
            <label>Equipment:</label>
            <hr class="separator" />
            <p>{{ safetyRequest.equipment }}</p>
          </div>
          <div class="form-group grid-item-full">
            <label>Task Name:</label>
            <hr class="separator" />
            <p>{{ safetyRequest.taskName }}</p>
          </div>
          <div class="form-group grid-item">
            <label>Person in Charge:</label>
            <hr class="separator" />
            <p>{{ safetyRequest.personInCharge }}</p>
          </div>
          <div class="form-group grid-item contractor-label">
            <label>Contractor:</label>
            <hr class="separator" />
            <p>{{ safetyRequest.contractor }}</p>
          </div>
        </div>

        <div class="instructions bold-text">
          <p class="instruction-text">At the start of work where there is a risk of fire, explosion, or chemical burns, personnel from relevant departments must be present.</p>
          <p class="instruction-text">Ensure comprehensive communication with contractors regarding site conditions and share information thoroughly through KY, etc.</p>
        </div>

        <div class="form-group question-full important-label question-separator">
          <label>Is on-site safety necessary?</label>
          <hr class="separator" />
          <br />
          <InputSwitch v-model="workerInspection.onSiteSafety" />
          <span v-if="workerInspection.onSiteSafety" class="checkmark">✔</span>
        </div>

        <div class="question-separator"></div>
        <div class="form-group question-full important-label">
          <label>Have the depressurization, liquid removal, and cleaning been completed?</label>
          <hr class="separator" />
        </div>

        <!-- Valve 1-5 のスイッチを表示 -->
        <div class="grid-five-columns">
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.valve1_input && !workerInspection.valve1_approval }"
          >
            <label for="valve1_approval">Valve 1:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.valve1_approval" />
            <span v-if="workerInspection.valve1_approval" class="checkmark">✔</span>
          </div>
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.valve2_input && !workerInspection.valve2_approval }"
          >
            <label for="valve2_approval">Valve 2:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.valve2_approval" />
            <span v-if="workerInspection.valve2_approval" class="checkmark">✔</span>
          </div>
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.valve3_input && !workerInspection.valve3_approval }"
          >
            <label for="valve3_approval">Valve 3:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.valve3_approval" />
            <span v-if="workerInspection.valve3_approval" class="checkmark">✔</span>
          </div>
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.valve4_input && !workerInspection.valve4_approval }"
          >
            <label for="valve4_approval">Valve 4:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.valve4_approval" />
            <span v-if="workerInspection.valve4_approval" class="checkmark">✔</span>
          </div>
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.valve5_input && !workerInspection.valve5_approval }"
          >
            <label for="valve5_approval">Valve 5:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.valve5_approval" />
            <span v-if="workerInspection.valve5_approval" class="checkmark">✔</span>
          </div>
        </div>

        <div class="question-separator"></div>
        <div class="form-group question-full important-label">
          <label>Has power disconnection and LOTO been completed?</label>
          <hr class="separator" />
        </div>

        <!-- Breaker 1-5 のスイッチを表示 -->
        <div class="grid-five-columns">
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.breaker1_input && !workerInspection.breaker1_approval }"
          >
            <label for="breaker1_approval">Breaker 1:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.breaker1_approval" />
            <span v-if="workerInspection.breaker1_approval" class="checkmark">✔</span>
          </div>
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.breaker2_input && !workerInspection.breaker2_approval }"
          >
            <label for="breaker2_approval">Breaker 2:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.breaker2_approval" />
            <span v-if="workerInspection.breaker2_approval" class="checkmark">✔</span>
          </div>
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.breaker3_input && !workerInspection.breaker3_approval }"
          >
            <label for="breaker3_approval">Breaker 3:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.breaker3_approval" />
            <span v-if="workerInspection.breaker3_approval" class="checkmark">✔</span>
          </div>
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.breaker4_input && !workerInspection.breaker4_approval }"
          >
            <label for="breaker4_approval">Breaker 4:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.breaker4_approval" />
            <span v-if="workerInspection.breaker4_approval" class="checkmark">✔</span>
          </div>
          <div 
            class="form-group grid-item-small"
            :class="{ 'highlighted': safetyRequest.breaker5_input && !workerInspection.breaker5_approval }"
          >
            <label for="breaker5_approval">Breaker 5:</label>
            <hr class="separator" />
            <br />
            <InputSwitch v-model="workerInspection.breaker5_approval" />
            <span v-if="workerInspection.breaker5_approval" class="checkmark">✔</span>
          </div>
        </div>
      </div>

      <div class="confirmation-page">
        <!-- 2ページ目 -->
        <h1 class="confirmation-title">Safety Confirmation Certificate</h1>
        <div class="title-space"></div>
        <div class="confirmation-date-display">{{ currentDate }}</div>
        <div class="confirmation-form-group question-tight important-label">
          <label>Is there any flammable gas in the vicinity?</label>
          <hr class="separator-full" />
          <InputSwitch v-model="safetyRequest.gasDetection" />
          <span v-if="safetyRequest.gasDetection" class="checkmark">✔</span>
        </div>
        <div class="question-separator"></div>
        <div class="confirmation-form-group question-tight important-label">
          <label>Is the oxygen concentration in the tank at an appropriate level and maintainable?</label>
          <p class="guideline-text">Generally, an oxygen concentration of 21% is the guideline for work permits.</p>
          <hr class="separator-full" />
          <InputSwitch v-model="safetyRequest.oxygenDeficiency" />
          <span v-if="safetyRequest.oxygenDeficiency" class="checkmark">✔</span>
        </div>
        <div class="confirmation-inspection">
          <p class="inspection-title large-font">Worker Inspection Items</p>
          <div class="confirmation-form-group left-aligned">
            <label>Has LOTO been implemented?</label>
            <hr class="separator-full" />
            <InputSwitch v-model="workerInspection.lotoImplemented" />
            <span v-if="workerInspection.lotoImplemented" class="checkmark">✔</span>
          </div>
          <div class="confirmation-form-group left-aligned">
            <label>Are protective gloves worn?</label>
            <hr class="separator-full" />
            <InputSwitch v-model="workerInspection.protectiveGloves" />
            <span v-if="workerInspection.protectiveGloves" class="checkmark">✔</span>
          </div>
          <div class="confirmation-form-group left-aligned">
            <label>Is there any combustible material in the vicinity?</label>
            <hr class="separator-full" />
            <InputSwitch v-model="workerInspection.noCombustibles" />
            <span v-if="workerInspection.noCombustibles" class="checkmark">✔</span>
          </div>
        </div>
        <div class="ky-input-box">
          <p class="ky-placeholder">KY Content Display Here</p>
        </div>
        <div class="confirmation-approver-box">
          <div class="confirmation-approver confirmation-form-group">
            <label for="approver">Approver:</label>
            <hr class="separator-full" />
            <input type="text" v-model="safetyRequest.approver" placeholder="Enter name" class="approver-input" />
          </div>
        </div>
        <div class="confirmation-page-number">Page 2</div>
        <Button label="Save" icon="pi pi-save" @click="submitForm" />
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue';
import axios from 'axios';
import InputSwitch from 'primevue/inputswitch';
import Button from 'primevue/button';
import Toast from 'primevue/toast'; // Toastコンポーネントを追加
import { useToast } from 'primevue/usetoast'; // Toastフックをインポート
import { useUserStore } from "@/stores/userStore"; // Piniaストアをインポート

// Toastインスタンスを作成
const toast = useToast();

// 安全要求情報のデータを管理するref
const safetyRequest = ref({
  valve1_input: false,  // Valve 1の入力状態の初期値
  valve2_input: false,  // Valve 2の入力状態の初期値
  valve3_input: false,  // Valve 3の入力状態の初期値
  valve4_input: false,  // Valve 4の入力状態の初期値
  valve5_input: false,  // Valve 5の入力状態の初期値
  breaker1_input: false,  // Breaker 1の入力状態の初期値
  breaker2_input: false,  // Breaker 2の入力状態の初期値
  breaker3_input: false,  // Breaker 3の入力状態の初期値
  breaker4_input: false,  // Breaker 4の入力状態の初期値
  breaker5_input: false,  // Breaker 5の入力状態の初期値
  constructionPeriod: '',  // 工事期間の初期値（空文字）
  plant: '',  // プラントの初期値（空文字）
  equipment: '',  // 設備の初期値（空文字）
  taskName: '',  // 作業名の初期値（空文字）
  personInCharge: '',  // 責任者の初期値（空文字）
  contractor: '',  // 契約者の初期値（空文字）
  gasDetection: false,  // ガス検知の初期値
  oxygenDeficiency: false,  // 酸素欠乏の初期値
  approver: '',  // 承認者の初期値（空文字）
  companyCode: '',  // 会社コードの初期値（空文字）
});

// 作業者点検項目のデータを管理するref
const workerInspection = ref({
  valve1_approval: false,  // Valve 1の承認状態の初期値
  valve2_approval: false,  // Valve 2の承認状態の初期値
  valve3_approval: false,  // Valve 3の承認状態の初期値
  valve4_approval: false,  // Valve 4の承認状態の初期値
  valve5_approval: false,  // Valve 5の承認状態の初期値
  breaker1_approval: false,  // Breaker 1の承認状態の初期値
  breaker2_approval: false,  // Breaker 2の承認状態の初期値
  breaker3_approval: false,  // Breaker 3の承認状態の初期値
  breaker4_approval: false,  // Breaker 4の承認状態の初期値
  breaker5_approval: false,  // Breaker 5の承認状態の初期値
  lotoImplemented: false,  // LOTO実施の初期値
  protectiveGloves: false,  // 保護手袋の着用状態の初期値
  noCombustibles: false,  // 可燃物なしの状態の初期値
});

// 日付を取得するための変数
const currentDate = ref(new Date().toLocaleDateString());

// Piniaのストアを使用
const userStore = useUserStore();



// フォームの送信を処理する関数
const submitForm = () => {
  // POSTするデータを整理して、不要なフィールドを排除
  const postData = {
    companyCode: userStore.companyCode, // PiniaからcompanyCodeを取得
    constructionPeriod: safetyRequest.value.constructionPeriod,
    plant: safetyRequest.value.plant,
    equipment: safetyRequest.value.equipment,
    taskName: safetyRequest.value.taskName,
    personInCharge: safetyRequest.value.personInCharge,
    contractor: safetyRequest.value.contractor,
    gasDetection: safetyRequest.value.gasDetection,
    oxygenDeficiency: safetyRequest.value.oxygenDeficiency,
    onSiteSafety: workerInspection.value.onSiteSafety,
    approver: safetyRequest.value.approver,
    valve1_input: safetyRequest.value.valve1_input,
    valve2_input: safetyRequest.value.valve2_input,
    valve3_input: safetyRequest.value.valve3_input,
    valve4_input: safetyRequest.value.valve4_input,
    valve5_input: safetyRequest.value.valve5_input,
    valve1_approval: workerInspection.value.valve1_approval,
    valve2_approval: workerInspection.value.valve2_approval,
    valve3_approval: workerInspection.value.valve3_approval,
    valve4_approval: workerInspection.value.valve4_approval,
    valve5_approval: workerInspection.value.valve5_approval,
    breaker1_input: safetyRequest.value.breaker1_input,
    breaker2_input: safetyRequest.value.breaker2_input,
    breaker3_input: safetyRequest.value.breaker3_input,
    breaker4_input: safetyRequest.value.breaker4_input,
    breaker5_input: safetyRequest.value.breaker5_input,
    breaker1_approval: workerInspection.value.breaker1_approval,
    breaker2_approval: workerInspection.value.breaker2_approval,
    breaker3_approval: workerInspection.value.breaker3_approval,
    breaker4_approval: workerInspection.value.breaker4_approval,
    breaker5_approval: workerInspection.value.breaker5_approval,
  };

  console.log('Posting data:', postData);

  axios.post('http://127.0.0.1:8000/api/workOrder/workPermission/', postData)
    .then(response => {
      toast.add({ severity: 'success', summary: 'Success', detail: 'Form saved successfully!', life: 3000 });
      console.log('Form saved successfully', response.data);
    })
    .catch(error => {
      toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to save form!', life: 3000 });
      console.error('Error saving form', error);
    });
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
  max-width: 100%;
}

.safety-request-form {
  flex: 1;
  min-width: 300px;
  max-width: 50%;
  padding: 16px;
  background-color: #fff;
  border: 1px solid #000;
}

.confirmation-page {
  width: 210mm; /* A4 width */
  height: 297mm; /* A4 height */
  border: 1px solid #000;
  padding: 10mm;
  box-sizing: border-box;
  background-color: #ff9999;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 16px;
  position: relative;
  display: flex;
  flex-direction: column;
}

.request-form-title {
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 8px;
}

.confirmation-title {
  text-align: center;
  font-size: 2em;
  font-weight: bold;
  margin-bottom: 8px;
  width: 100%;
}

.title-space {
  height: 50px;
}

.form-grid-smaller {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3列のグリッド */
  gap: 16px;
  margin-bottom: 16px;
}

.grid-two-columns {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 2列のグリッド */
  gap: 16px;
  width: 100%;
}

.grid-five-columns {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* 5列のグリッド */
  gap: 16px;
  width: 100%;
}

.grid-item-small {
  border: 1px solid #000;
  padding: 8px;
  border-radius: 4px;
  text-align: center;
  min-height: 80px;
}

/* highlightedクラスを追加して、背景色を白に変更 */
.highlighted {
  background-color: white;
}

.form-group {
  margin-bottom: 12px;
}

.question-separator {
  margin-bottom: 20px;
}

.left-aligned {
  text-align: left;
}

.confirmation-approver-box {
  border: 1px solid #000;
  padding: 8px;
  border-radius: 4px;
  width: 30%;
  position: absolute;
  bottom: 40px;
  right: 10px;
}

.approver-input {
  width: 100%;
}

.ky-input-box {
  border: 1px solid #000;
  height: 150px;
  width: 100%;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.page-number {
  text-align: center;
  font-size: 12px;
  position: absolute;
  bottom: 10px;
  left: 0;
  right: 0;
}

.confirmation-date-display {
  text-align: right;
  font-size: 12px;
  position: absolute;
  top: 10px;
  right: 10px;
}

.separator {
  border: none;
  border-bottom: 1px solid #000;
  margin: 2px 0;
}

.separator-full {
  border: none;
  border-bottom: 1px solid #000;
  width: calc(100% - 20mm); /* 下線をA4の横幅一杯に広げる */
  margin: 2px 0;
}

.checkmark {
  margin-left: 8px;
  color: green;
  font-size: 20px;
}

.resizable-textarea {
  width: 100%;
  min-height: 40px;
  resize: vertical;
}

body {
  background-color: #f5f5f5;
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
}

@media print {
  .form-container {
    flex-direction: column;
  }
  .confirmation-page {
    background-color: #ff9999;
    box-shadow: none;
    border: none;
    page-break-after: always;
  }
  .buttons {
    display: none;
  }
}

@media screen and (max-width: 768px) {
  .grid-two-columns {
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); /* 画面幅が狭くなった場合に折り返し */
  }
}

@media screen and (max-width: 768px) {
  .grid-five-columns {
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); /* 画面幅が狭くなった場合に折り返し */
  }
}

@media screen and (max-width: 480px) {
  .grid-two-columns {
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); /* さらに狭い場合に折り返し */
  }
  .grid-five-columns {
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); /* さらに狭い場合に折り返し */
  }
}
</style>
