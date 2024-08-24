<template>
  <div class="form-container">
    <div class="content">
      <div class="safety-request-form">
        <!-- フォームのタイトルをSafety Request Formに変更 -->
        <h2 class="request-form-title">Safety Request Form</h2>
        <form>
          <!-- フォームを左側に配置 -->
          <div class="form-group">
            <label for="constructionPeriod">Construction Period:</label>
            <br /> <!-- 改行を追加 -->
            <textarea v-model="safetyRequest.constructionPeriod" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="plant">Plant:</label>
            <br /> <!-- 改行を追加 -->
            <textarea v-model="safetyRequest.plant" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="equipment">Equipment:</label>
            <br /> <!-- 改行を追加 -->
            <textarea v-model="safetyRequest.equipment" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="taskName">Task Name:</label>
            <br /> <!-- 改行を追加 -->
            <textarea v-model="safetyRequest.taskName" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="personInCharge">Person in Charge:</label>
            <br /> <!-- 改行を追加 -->
            <textarea v-model="safetyRequest.personInCharge" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group contractor-label">
            <label for="contractor">Contractor:</label>
            <br /> <!-- 改行を追加 -->
            <textarea v-model="safetyRequest.contractor" class="resizable-textarea"></textarea>
          </div>
          <div class="form-group">
            <label for="gasDetection">Gas Detection:</label>
            <br /> <!-- 改行を追加 -->
            <InputSwitch v-model="safetyRequest.gasDetection" />
            <span v-if="safetyRequest.gasDetection" class="checkmark">✔</span>
          </div>
          <div class="form-group">
            <label for="oxygenDeficiency">Oxygen Deficiency:</label>
            <br /> <!-- 改行を追加 -->
            <InputSwitch v-model="safetyRequest.oxygenDeficiency" />
            <span v-if="safetyRequest.oxygenDeficiency" class="checkmark">✔</span>
          </div>
          <!-- Valve 1-5 のスイッチを追加 -->
          <div class="grid-multiple">
            <div class="form-group grid-item-small">
              <label for="valve1">Valve 1:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.valve1" />
              <span v-if="safetyRequest.valve1" class="checkmark">✔</span>
            </div>
            <div class="form-group grid-item-small">
              <label for="valve2">Valve 2:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.valve2" />
              <span v-if="safetyRequest.valve2" class="checkmark">✔</span>
            </div>
            <div class="form-group grid-item-small">
              <label for="valve3">Valve 3:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.valve3" />
              <span v-if="safetyRequest.valve3" class="checkmark">✔</span>
            </div>
            <div class="form-group grid-item-small">
              <label for="valve4">Valve 4:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.valve4" />
              <span v-if="safetyRequest.valve4" class="checkmark">✔</span>
            </div>
            <div class="form-group grid-item-small">
              <label for="valve5">Valve 5:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.valve5" />
              <span v-if="safetyRequest.valve5" class="checkmark">✔</span>
            </div>
          </div>

          <!-- Breaker 1-5 のスイッチを追加 -->
          <div class="grid-multiple">
            <div class="form-group grid-item-small">
              <label for="breaker1">Breaker 1:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.breaker1" />
              <span v-if="safetyRequest.breaker1" class="checkmark">✔</span>
            </div>
            <div class="form-group grid-item-small">
              <label for="breaker2">Breaker 2:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.breaker2" />
              <span v-if="safetyRequest.breaker2" class="checkmark">✔</span>
            </div>
            <div class="form-group grid-item-small">
              <label for="breaker3">Breaker 3:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.breaker3" />
              <span v-if="safetyRequest.breaker3" class="checkmark">✔</span>
            </div>
            <div class="form-group grid-item-small">
              <label for="breaker4">Breaker 4:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.breaker4" />
              <span v-if="safetyRequest.breaker4" class="checkmark">✔</span>
            </div>
            <div class="form-group grid-item-small">
              <label for="breaker5">Breaker 5:</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="safetyRequest.breaker5" />
              <span v-if="safetyRequest.breaker5" class="checkmark">✔</span>
            </div>
          </div>
        </form>
      </div>
      <div class="pages">
        <div v-for="(page, index) in pages" :key="index" class="page">
          <form @submit.prevent="submitForm">
            <!-- フォームのタイトルを追加 -->
            <h1 class="confirmation-title">Safety Confirmation Certificate</h1>
            <div class="title-space"></div> <!-- 大きなスペースを追加 -->

            <!-- 右上に日付を追加 -->
            <div class="date-display">{{ currentDate }}</div>

            <!-- 左側の入力内容を表示 -->
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

            <!-- 指定された文を追加 -->
            <div class="instructions bold-text">
              <p class="instruction-text">At the start of work where there is a risk of fire, explosion, or chemical burns, personnel from relevant departments must be present.</p>
              <p class="instruction-text">Ensure comprehensive communication with contractors regarding site conditions and share information thoroughly through KY, etc.</p>
            </div>

            <!-- 現場での安全化は必要か? の質問 -->
            <div class="form-group question-full important-label question-separator">
              <!-- スペースを追加 -->
              <label>Is on-site safety necessary?</label>
              <hr class="separator" />
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="page.onSiteSafety" />
              <span v-if="page.onSiteSafety" class="checkmark">✔</span>
            </div>

            <!-- 脱圧、液抜き、洗浄は実施済ですか? の質問 -->
            <div class="question-separator"></div> <!-- 隙間を追加 -->
            <div class="form-group question-full important-label">
              <label>Have the depressurization, liquid removal, and cleaning been completed?</label>
              <hr class="separator" />
            </div>

            <!-- Valve 1-5 のスイッチを表示 -->
            <div class="grid-multiple">
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve1 && !page.valve1 }]" :style="{ backgroundColor: safetyRequest.valve1 && !page.valve1 ? 'white' : '' }">
                <label for="valve1">Valve 1:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.valve1" />
                <span v-if="page.valve1" class="checkmark">✔</span>
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve2 && !page.valve2 }]" :style="{ backgroundColor: safetyRequest.valve2 && !page.valve2 ? 'white' : '' }">
                <label for="valve2">Valve 2:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.valve2" />
                <span v-if="page.valve2" class="checkmark">✔</span>
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve3 && !page.valve3 }]" :style="{ backgroundColor: safetyRequest.valve3 && !page.valve3 ? 'white' : '' }">
                <label for="valve3">Valve 3:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.valve3" />
                <span v-if="page.valve3" class="checkmark">✔</span>
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve4 && !page.valve4 }]" :style="{ backgroundColor: safetyRequest.valve4 && !page.valve4 ? 'white' : '' }">
                <label for="valve4">Valve 4:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.valve4" />
                <span v-if="page.valve4" class="checkmark">✔</span>
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.valve5 && !page.valve5 }]" :style="{ backgroundColor: safetyRequest.valve5 && !page.valve5 ? 'white' : '' }">
                <label for="valve5">Valve 5:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.valve5" />
                <span v-if="page.valve5" class="checkmark">✔</span>
              </div>
            </div>

            <!-- 動力の遮断を実施し、LOTOを実施済か？ の質問 -->
            <div class="question-separator"></div> <!-- 隙間を追加 -->
            <div class="form-group question-full important-label">
              <label>Has power disconnection and LOTO been completed?</label>
              <hr class="separator" />
            </div>

            <!-- Breaker 1-5 のスイッチを表示 -->
            <div class="grid-multiple">
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker1 && !page.breaker1 }]" :style="{ backgroundColor: safetyRequest.breaker1 && !page.breaker1 ? 'white' : '' }">
                <label for="breaker1">Breaker 1:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.breaker1" />
                <span v-if="page.breaker1" class="checkmark">✔</span>
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker2 && !page.breaker2 }]" :style="{ backgroundColor: safetyRequest.breaker2 && !page.breaker2 ? 'white' : '' }">
                <label for="breaker2">Breaker 2:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.breaker2" />
                <span v-if="page.breaker2" class="checkmark">✔</span>
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker3 && !page.breaker3 }]" :style="{ backgroundColor: safetyRequest.breaker3 && !page.breaker3 ? 'white' : '' }">
                <label for="breaker3">Breaker 3:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.breaker3" />
                <span v-if="page.breaker3" class="checkmark">✔</span>
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker4 && !page.breaker4 }]" :style="{ backgroundColor: safetyRequest.breaker4 && !page.breaker4 ? 'white' : '' }">
                <label for="breaker4">Breaker 4:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.breaker4" />
                <span v-if="page.breaker4" class="checkmark">✔</span>
              </div>
              <div :class="['form-group', 'grid-item-small', { 'bordered': safetyRequest.breaker5 && !page.breaker5 }]" :style="{ backgroundColor: safetyRequest.breaker5 && !page.breaker5 ? 'white' : '' }">
                <label for="breaker5">Breaker 5:</label>
                <hr class="separator" />
                <br /> <!-- 改行を追加 -->
                <InputSwitch v-model="page.breaker5" />
                <span v-if="page.breaker5" class="checkmark">✔</span>
              </div>
            </div>
          </form>
          <div class="page-number">Page {{ index + 1 }}</div>
        </div>
        <div class="confirmation-page">
          <!-- 2ページ目 -->
          <h1 class="confirmation-title">Safety Confirmation Certificate</h1>
          <div class="title-space"></div> <!-- 大きなスペースを追加 -->
          <div class="confirmation-date-display">{{ currentDate }}</div>
          <!-- 質問を上詰めに配置 -->
          <div class="confirmation-form-group question-tight important-label">
            <label>Is there any flammable gas in the vicinity?</label>
            <hr class="separator-full" /> <!-- 下線を横一杯に広げる -->
            <br /> <!-- 改行を追加 -->
            <InputSwitch v-model="safetyRequest.gasDetection" />
            <span v-if="safetyRequest.gasDetection" class="checkmark">✔</span>
          </div>
          <div class="question-separator"></div> <!-- 隙間を追加 -->
          <div class="confirmation-form-group question-tight important-label">
            <label>Is the oxygen concentration in the tank at an appropriate level and maintainable?</label>
            <p class="guideline-text">Generally, an oxygen concentration of 21% is the guideline for work permits.</p>
            <hr class="separator-full" /> <!-- 下線を横一杯に広げる -->
            <br /> <!-- 改行を追加 -->
            <InputSwitch v-model="safetyRequest.oxygenDeficiency" />
            <span v-if="safetyRequest.oxygenDeficiency" class="checkmark">✔</span>
          </div>
          <!-- 作業者点検項目 -->
          <div class="confirmation-inspection">
            <p class="inspection-title large-font">Worker Inspection Items</p> <!-- フォントサイズを大きく -->
            <div class="confirmation-form-group left-aligned">
              <label>Has LOTO been implemented?</label>
              <hr class="separator-full" /> <!-- 下線を横一杯に広げる -->
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="workerInspection.lotoImplemented" />
              <span v-if="workerInspection.lotoImplemented" class="checkmark">✔</span>
            </div>
            <div class="confirmation-form-group left-aligned">
              <div class="question-separator"></div> <!-- スイッチボックスとの間にスペース -->
              <label>Are protective gloves worn?</label>
              <hr class="separator-full" /> <!-- 下線を横一杯に広げる -->
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="workerInspection.protectiveGloves" />
              <span v-if="workerInspection.protectiveGloves" class="checkmark">✔</span>
            </div>
            <div class="confirmation-form-group left-aligned">
              <div class="question-separator"></div> <!-- スイッチボックスとの間にスペース -->
              <label>Is there any combustible material in the vicinity?</label>
              <hr class="separator-full" /> <!-- 下線を横一杯に広げる -->
              <br /> <!-- 改行を追加 -->
              <InputSwitch v-model="workerInspection.noCombustibles" />
              <span v-if="workerInspection.noCombustibles" class="checkmark">✔</span>
            </div>
          </div>
          <!-- KYボックス -->
          <div class="ky-input-box">
            <p class="ky-placeholder">KY Content Display Here</p> <!-- プレースホルダーを追加 -->
          </div>
          <!-- 確認者入力フォーム -->
          <div class="confirmation-approver-box">
            <div class="confirmation-approver confirmation-form-group">
              <label for="approver">Approver:</label>
              <hr class="separator-full" /> <!-- 下線を横一杯に広げる -->
              <input type="text" v-model="safetyRequest.approver" placeholder="Enter name" class="approver-input" />
            </div>
          </div>
          <div class="confirmation-page-number">Page 2</div>
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

// 安全要求情報のデータを管理するref
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
  approver: '', // 確認者の入力データ
  ky: '', // KYの入力データ
});

// 作業者点検項目のデータを管理するref
const workerInspection = ref({
  lotoImplemented: false,
  protectiveGloves: false,
  noCombustibles: false,
});

// 各ページごとの情報を管理するref
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

// モーダルの表示状態を管理するref
const showConfirmation = ref(false);
const showSuccess = ref(false);
const currentDate = ref(new Date().toLocaleDateString());

// フォームの送信を処理する関数
const handleSubmit = () => {
  if (hasUnsafeItems()) {
    showConfirmation.value = true;
  } else {
    showSuccess.value = true;
  }
};

// 安全でない項目が存在するかをチェックする関数
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

// 確認モーダルをキャンセルする関数
const cancelConfirmation = () => {
  showConfirmation.value = false;
};

// 承認を確認する関数
const confirmApproval = () => {
  showConfirmation.value = false;
  showSuccess.value = true;
};

// 成功モーダルを閉じる関数
const closeSuccess = () => {
  showSuccess.value = false;
  // フォームの送信処理をここに追加
};

// フォームの送信を処理する関数
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
  max-width: 100%; /* 最大幅を設定 */
}

.safety-request-form {
  flex: 1;
  min-width: 300px;
  max-width: 50%; /* 左側に配置 */
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
  justify-content: flex-start; /* 上詰め配置 */
}

.confirmation-page {
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
  align-items: flex-start; /* 左詰め */
  justify-content: flex-start; /* 上詰め配置 */
}

.request-form-title {
  text-align: center;
  font-size: 18px; /* Safety Request Formのサイズ */
  font-weight: bold;
  margin-bottom: 8px; /* スペースを小さく */
}

.confirmation-title {
  text-align: center; /* 横方向にセンター */
  font-size: 2em; /* h1サイズ */
  font-weight: bold;
  margin-bottom: 8px;
  width: 100%;
}

.title-space {
  height: 50px; /* Safety Confirmation Certificateの下に大きなスペース */
}

.form-grid-smaller {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3列のグリッド */
  gap: 16px; /* グリッドアイテム間のスペース */
  margin-bottom: 16px; /* ボックスと次の要素の間にスペース */
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 2列のグリッド */
  gap: 16px; /* グリッドアイテム間のスペース */
}

.grid-multiple {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); /* 自動的に列を調整 */
  gap: 16px; /* グリッドアイテム間のスペース */
}

.grid-item {
  border: 1px solid #000; /* 黒の細い線で囲む */
  padding: 8px;
  border-radius: 4px;
  min-height: 120px; /* 高さを拡大 */
}

.grid-item-smaller {
  border: 1px solid #000; /* 黒の細い線で囲む */
  padding: 8px;
  border-radius: 4px;
  text-align: center; /* 中央寄せ */
  min-height: 80px; /* 高さを調整 */
}

.grid-item-small {
  border: 1px solid #000; /* 黒の細い線で囲む */
  padding: 8px;
  border-radius: 4px;
  text-align: center; /* 中央寄せ */
  min-height: 80px; /* 高さを調整 */
}

.grid-item-full {
  grid-column: span 3; /* 3列にまたがる */
  border: 1px solid #000; /* 黒の細い線で囲む */
  padding: 8px;
  border-radius: 4px;
  text-align: center; /* 中央寄せ */
  min-height: 80px; /* 高さを調整 */
}

.form-group {
  margin-bottom: 12px; /* 各質問間のスペースを増やす */
}

.confirmation-form-group {
  margin-bottom: 12px; /* 各質問間のスペースを増やす */
}

.confirmation-approver-box {
  border: 1px solid #000; /* 確認者の入力を囲む枠線 */
  padding: 8px;
  border-radius: 4px;
  width: 30%; /* 横幅を調整 */
  position: absolute; /* 絶対配置で右下に */
  bottom: 40px; /* 下詰めのためにスペースを追加 */
  right: 10px; /* 右詰め */
}

.approver-input {
  width: 100%; /* 横幅を入力エリアに合わせる */
}

.ky-input-box {
  border: 1px solid #000; /* KYボックスを囲む枠線 */
  height: 150px; /* 高さをさらに大きく設定 */
  width: 100%; /* 横幅をいっぱいに広げる */
  margin-bottom: 16px; /* 下部のスペースを追加 */
  display: flex;
  align-items: center;
  justify-content: center;
}

.ky-placeholder {
  font-size: 16px;
  text-align: center;
}

.instructions {
  margin-bottom: 24px; /* スペースを追加 */
}

.instruction-text {
  text-decoration: underline; /* 下線を追加 */
  margin-bottom: 8px; /* 各文の間に少しスペースを追加 */
  font-weight: bold; /* 太字 */
}

.question-separator {
  margin-bottom: 20px; /* スイッチボタンと質問の間のスペースを増やす */
}

.left-aligned {
  text-align: left; /* 左詰め */
}

.right-aligned {
  text-align: right; /* 右詰め */
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

.confirmation-form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

.contractor-label label {
  font-size: 16px;
  font-weight: bold;
}

.important-label label {
  font-size: 16px; /* フォントサイズを大きく */
  font-weight: bold; /* 太字 */
}

.large-font {
  font-size: 18px; /* Worker Inspection Itemsのフォントを大きく */
}

.guideline-text {
  font-size: 14px;
  margin-top: 4px;
  margin-bottom: 4px;
  font-style: italic;
}

.inspection-title {
  font-size: 16px;
  font-weight: bold;
  margin-top: 16px;
  margin-bottom: 8px;
  text-align: left; /* 左詰め */
}

.inspection-item {
  margin-bottom: 8px;
}

.confirmation-approver {
  margin-top: 16px;
}

.question-full {
  width: 100%; /* A4いっぱいに広げる */
  margin-bottom: 4px; /* 隙間を小さく調整 */
  font-weight: bold;
}

.question-tight {
  width: 100%;
  margin-bottom: 4px; /* より小さく間隔を調整 */
  font-weight: bold;
}

.checkmark {
  margin-left: 8px;
  color: green;
  font-size: 20px; /* チェックマークを2回り大きく */
}

.resizable-textarea {
  width: 100%;
  min-height: 40px;
  resize: vertical; /* 垂直方向にリサイズ可能に設定 */
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

.confirmation-page-number {
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
  margin: 2px 0; /* 質問間のスペースをさらに減少 */
}

.separator-full {
  border: none;
  border-bottom: 1px solid #000;
  width: calc(100% - 20mm); /* 下線をA4の横幅一杯に広げる（左右のパディング分を除く） */
  margin: 2px 0; /* 質問間のスペースをさらに減少 */
}

@media print {
  .form-container {
    flex-direction: column;
  }
  .page,
  .confirmation-page {
    background-color: #ff9999; /* Ensure print background color is the same */
    box-shadow: none;
    border: none;
    page-break-after: always;
  }
  .buttons {
    display: none;
  }
}

@media screen and (max-width: 768px) {
  .grid-multiple {
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); /* 画面幅が狭くなった場合に折り返し */
  }
}

@media screen and (max-width: 480px) {
  .grid-multiple {
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); /* さらに狭い場合に折り返し */
  }
}

</style>
