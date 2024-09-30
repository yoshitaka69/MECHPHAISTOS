<template>
  <div class="daily-report-container">
      <Save_Alert v-if="showAlert" :type="alertType" :message="alertMessage" />
      <div class="surface-ground">
          <div class="p-fluid flex flex-column lg:flex-row">
              <ul class="sidebar list-none m-0 p-0 flex flex-row lg:flex-column justify-content-evenly md:justify-content-between lg:justify-content-start mb-5 lg:pr-8 lg:mb-0">
                  <li>
                      <a
                          @click="selectTab('dailyReport')"
                          :class="['flex align-items-center cursor-pointer p-3 border-round custom-rounded', selectedTab === 'dailyReport' ? 'text-primary' : 'text-800', 'hover:surface-hover transition-duration-150 transition-colors']"
                      >
                          <i class="pi pi-book sidebar-icon"></i>
                          <span class="sidebar-text">Daily Report</span>
                      </a>
                  </li>
              </ul>
              <div class="surface-card p-5 shadow-2 border-round flex-auto form-container">
                  <div v-if="selectedTab === 'dailyReport'">
                      <div class="header-container">
                          <div class="field recorder-field">
                              <label for="date" class="date-label">日付</label>
                              <InputText id="date" v-model="formattedDate" class="date" placeholder="YYYY-MM-DD" style="width: 150px" />
                              <label for="recorder">Recorder (記録者)</label>
                              <InputText id="recorder" v-model="recorder" :value="userStore.userName" placeholder="Enter recorder name" readonly style="width: 200px" />
                          </div>
                      </div>
                      <div class="field">
                          <label for="activity">What did you do today? (今日の活動内容は？)</label>
                          <Textarea id="activity" v-model="activity" rows="10" autoResize placeholder="Describe your activities..." />
                      </div>
                      <hr class="divider" />

                      <div class="field">
                          <label for="workOrder">Is there any work order? (作業指示はありましたか？)</label>
                          <div class="work-order-selection">
                              <Button label="Yes" class="yes-button custom-button-width" @click="toggleWorkOrder(true)" :class="{ selected: workOrderExists }" />
                              <Button label="No" class="no-button custom-button-width" @click="toggleWorkOrder(false)" :class="{ selected: !workOrderExists }" />
                              <span v-if="!workOrderExists" class="checkmark">✔</span>
                          </div>
                      </div>

                      <WorkOrderForm v-if="workOrderExists" v-model="workOrderDetails" />
                      <div class="field">
                          <label for="equipmentType">What was the target equipment? (対象となる機器はなんでしたか？)</label>
                          <div class="checkbox-group">
                              <span class="checkbox-item" v-for="(option, index) in equipmentOptions" :key="index"> <Checkbox v-model="selectedEquipment" :value="option" /> {{ option }} </span>
                          </div>
                      </div>

                      <div class="field">
                          <label for="maintenanceType">What is the type of maintenance? (保全の種類は何ですか？)</label>
                          <div class="checkbox-group">
                              <span class="checkbox-item" v-for="(option, index) in maintenanceOptions" :key="index"> <Checkbox v-model="selectedMaintenance" :value="option" /> {{ option }} </span>
                          </div>
                          <InputText id="maintenanceType" v-model="maintenanceType" placeholder="Enter maintenance type" />
                      </div>

                      <div class="field">
                          <label for="maintenanceDescription">What kind of maintenance was it? (どのような保全を行いましたか？)</label>
                          <div class="checkbox-group">
                              <span class="checkbox-item" v-for="(option, index) in maintenanceTypeOptions" :key="index"> <Checkbox v-model="selectedMaintenanceTypes" :value="option" /> {{ option }} </span>
                          </div>
                          <Textarea id="maintenanceDescription" v-model="maintenanceDescription" rows="3" autoResize placeholder="Describe the maintenance..." />
                      </div>

                      <div class="field">
                          <label for="situation">Do you know what the situation was? (状況はどうでしたか？)</label>
                          <div class="checkbox-group">
                              <span class="checkbox-item" v-for="(option, index) in situationOptions" :key="index"> <Checkbox v-model="selectedSituations" :value="option" /> {{ option }} </span>
                          </div>
                          <Textarea id="situation" v-model="situation" rows="3" autoResize placeholder="Describe the situation..." />
                      </div>

                      <div class="field">
                          <label for="damageSituation">What was the damage situation? (どのような破損の状況でしたか？)</label>
                          <div class="checkbox-group">
                              <span class="checkbox-item" v-for="(option, index) in damageOptions" :key="index"> <Checkbox v-model="selectedDamage" :value="option" /> {{ option }} </span>
                          </div>
                          <InputText id="damageOther" v-model="damageOther" placeholder="Enter other damage situation (その他の破損状況を入力)" />
                      </div>

                      <div class="field">
                          <label for="cause">Do you know what the cause was? (原因は何だと思いますか？)</label>
                          <div class="checkbox-group">
                              <span class="checkbox-item" v-for="(option, index) in causeOptions" :key="index"> <Checkbox v-model="selectedCauses" :value="option" /> {{ option }} </span>
                          </div>
                          <Textarea id="cause" v-model="cause" rows="3" autoResize placeholder="Describe the cause..." />
                      </div>

                      <div class="field spare-parts-section">
                          <label for="sparePartsUsed">Did you use any spare parts? (スペアパーツを使用しましたか？)</label>
                          <div class="spare-parts-selection">
                              <Button label="Yes" class="yes-button custom-button-width" @click="toggleSparePartsUsage(true)" :class="{ selected: sparePartsUsed }" />
                              <Button label="No" class="no-button custom-button-width" @click="toggleSparePartsUsage(false)" :class="{ selected: !sparePartsUsed }" />
                              <span v-if="!sparePartsUsed" class="checkmark">✔</span>
                          </div>
                      </div>

                      <SparePartsForm v-if="sparePartsUsed" v-model="spareParts" />

                      <div class="field-container">
                          <div class="field photo-upload-section">
                              <label for="photoUpload">Upload Photo (写真をアップロード)</label>
                              <div class="file-upload-container">
                                  <input type="file" id="photoUpload" @change="handleFileUpload" accept="image/*" class="file-input" />
                                  <Button v-if="photoFile" label="Remove File" icon="pi pi-times" class="remove-button custom-button-width" @click="removeFile" />
                              </div>
                              <div v-if="photoPreview" class="photo-preview">
                                  <img :src="photoPreview" alt="Photo Preview" class="preview-image" />
                              </div>
                          </div>

                          <div class="handwritten-notes-container">
                              <div class="field handwritten-notes-section">
                                  <label>Handwritten Notes (手書きのメモ)</label>
                                  <canvas ref="signatureCanvas" width="500" height="200" class="signature-pad"></canvas>
                                  <div class="canvas-toolbar">
                                      <Button label="Pen" class="pen-button custom-button-width" @click="setPenMode" />
                                      <Button label="Eraser" class="eraser-button custom-button-width" @click="setEraserMode" />
                                      <Button label="Clear All" class="clear-button custom-button-width" @click="clearCanvas" />
                                  </div>
                              </div>
                          </div>
                      </div>

                      <div class="field button-container">
                          <Button label="Save" icon="pi pi-save" class="save-button custom-button-width" @click="saveReport" />
                          <Button label="Clear" icon="pi pi-times" class="clear-button custom-button-width" @click="clearAllForms" />
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import SignaturePad from 'signature_pad';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import Save_Alert from '@/components/Alert/Save_Alert.vue';
import SparePartsForm from '@/components/Spare_parts_form/SparePartsForm.vue';
import WorkOrderForm from './WorkOrderForm.vue';
import Checkbox from 'primevue/checkbox'; // チェックボックスのインポート

export default {
  components: {
      InputText,
      Textarea,
      Button,
      Save_Alert,
      SparePartsForm,
      WorkOrderForm,
      Checkbox // チェックボックスの登録
  },
  setup() {
      // 日付をフォーマットする関数を定義
      const formatDate = (date) => {
          // 'YYYY-MM-DD' 形式で日付を返す
          const year = date.getFullYear();
          const month = ('0' + (date.getMonth() + 1)).slice(-2);
          const day = ('0' + date.getDate()).slice(-2);
          return `${year}-${month}-${day}`;
      };

      const userStore = useUserStore();
      const selectedTab = ref('dailyReport');
      const recorder = ref(userStore.userName);
      const companyCode = ref(userStore.companyCode);
      const activity = ref('');
      const workOrderExists = ref(false);
      const workOrderDetails = ref({});
      const maintenanceType = ref('');
      const selectedEquipment = ref([]);
      const selectedDamage = ref([]);
      const damageOther = ref('');
      const maintenanceDescription = ref('');
      const situation = ref('');
      const cause = ref('');
      const sparePartsUsed = ref(false);
      const spareParts = ref([]);
      const photoPreview = ref(null);
      const photoFile = ref(null);
      const signaturePad = ref(null);

      const showAlert = ref(false);
      const alertType = ref('success');
      const alertMessage = ref('');

      // 編集可能な日付フィールド用の初期値を設定
      const formattedDate = ref(formatDate(new Date()));

      // チェックボックスの選択肢を定義
      const causeOptions = ref([
          'Human Error (人的ミス)',
          'Fatigue Failure (疲労破壊)',
          'Overheating/Overload (過熱 / 過負荷)',
          'Misuse (誤使用)',
          'Operational Error (操作ミス)',
          'Manufacturing Defect (製造欠陥)',
          'Inadequate Maintenance (不適切な保守)',
          'Improper Installation (不適切な設置)',
          'Material Defect (材料欠陥)',
          'Progressive Damage (進行的な損傷)',
          'Corrosion (腐食)',
          'Control System Failure (制御系の異常)',
          'Process Defect (工程の欠陥)',
          'Material Issue (材料の問題)',
          'External Factor (外部要因)'
      ]);

      const maintenanceOptions = ref(['PM01: Inspection (検査)', 'PM02: Preventive Maintenance (予防保全)', 'PM03: Corrective Maintenance (修正保全)', 'PM04: Breakdown Maintenance (緊急保全)', 'PM05: Improvement (改善改造)']);

      const maintenanceTypeOptions = ref([
          'Inspection (点検 / Inspection)',
          'Lubrication (潤滑 / Lubrication)',
          'Adjustment (調整 / Adjustment)',
          'Replacement (交換 / Replacement)',
          'Cleaning (清掃 / Cleaning)',
          'Repair (修理 / Repair)',
          'Regular Maintenance (定期保全 / Regular Maintenance)',
          'Overhaul (オーバーホール / Overhaul)',
          'Other (その他 / Other)'
      ]);

      const situationOptions = ref(['Normal Operation (正常運転)', 'Abnormal Operation (異常運転)', 'Stopped (停止)', 'Maintenance Ongoing (保全中)', 'Under Investigation (調査中)']);

      const equipmentOptions = ref(['Electrical (電気設備)', 'Mechanical (機械設備)', 'Software (ソフトウェア)']);

      const damageOptions = ref([
          'Wear (摩耗)',
          'Fatigue Failure (疲労破壊)',
          'Corrosion (腐食)',
          'Overheating (過熱)',
          'Inadequate Lubrication (潤滑不足)',
          'Seal Failure (シール破損)',
          'Overload (過負荷)',
          'Vibration (振動)',
          'Electrical Insulation Failure (絶縁破壊)',
          'Short Circuit (短絡)',
          'Mechanical Shock (機械的衝撃)',
          'Thermal Fatigue (熱疲労)',
          'Cavitation (キャビテーション)',
          'Frictional Wear (摩擦摩耗)',
          'Stress Corrosion Cracking (応力腐食割れ)',
          'Erosion (浸食)',
          'Oxidation (酸化)',
          'Cable Breakage (ケーブル断線)',
          'Bearing Failure (ベアリング破損)',
          'Electronic Component Failure (電子部品故障)',
          'Other (その他)'
      ]);

      // 選択された原因、保全内容、保全タイプ、状況を管理する変数
      const selectedCauses = ref([]);
      const selectedMaintenance = ref([]);
      const selectedMaintenanceTypes = ref([]);
      const selectedSituations = ref([]);

      const selectTab = (tab) => {
          selectedTab.value = tab;
      };

      // 作業指示の有無を切り替える
      const toggleWorkOrder = (exists) => {
          workOrderExists.value = exists;
      };

      // ファイルが選択された時の処理
      const handleFileUpload = (event) => {
          const file = event.target.files[0];
          if (file) {
              const reader = new FileReader();
              reader.onload = (e) => {
                  photoPreview.value = e.target.result;
              };
              reader.readAsDataURL(file);
              photoFile.value = file;
          }
      };

      // ペンモードを設定
      const setPenMode = () => {
          signaturePad.value.penColor = 'black';
          signaturePad.value.minWidth = 1;
          signaturePad.value.maxWidth = 2.5;
      };

      // 消しゴムモードを設定
      const setEraserMode = () => {
          signaturePad.value.penColor = 'white';
          signaturePad.value.minWidth = 10;
          signaturePad.value.maxWidth = 10;
      };

      // スペアパーツ使用フラグの切り替え
      const toggleSparePartsUsage = (isUsed) => {
          sparePartsUsed.value = isUsed;
      };

      // キャンバスをクリア
      const clearCanvas = () => {
          if (signaturePad.value) {
              signaturePad.value.clear();
          }
      };

      // 全フォームをクリア
      const clearAllForms = () => {
          activity.value = '';
          workOrderExists.value = false;
          workOrderDetails.value = {};
          maintenanceType.value = '';
          selectedMaintenanceTypes.value = [];
          maintenanceDescription.value = '';
          situation.value = '';
          selectedSituations.value = [];
          cause.value = '';
          selectedCauses.value = [];
          selectedMaintenance.value = [];
          spareParts.value = [];
          sparePartsUsed.value = false;
          photoPreview.value = null;
          photoFile.value = null;
          clearCanvas();
      };

      const removeFile = () => {
          photoFile.value = null; // ファイルデータをクリア
          photoPreview.value = null; // プレビュー表示をクリア
          document.getElementById('photoUpload').value = null; // ファイル選択フォームをリセット
      };

      // レポートを保存
      const saveReport = () => {
          if (!companyCode.value) {
              alertMessage.value = 'Company code is not defined.';
              alertType.value = 'error';
              showAlert.value = true;
              return;
          }

          const reportData = new FormData();
          const formattedDateForAPI = formattedDate.value;

          reportData.append('companyCode', companyCode.value);
          reportData.append('recorder', recorder.value);
          reportData.append('date', formattedDateForAPI);
          reportData.append('activity', activity.value.trim());
          reportData.append('workOrderDetails', JSON.stringify(workOrderDetails.value));
          reportData.append('maintenanceType', maintenanceType.value);
          reportData.append('selectedMaintenanceTypes', JSON.stringify(selectedMaintenanceTypes.value));
          reportData.append('maintenanceDescription', maintenanceDescription.value);
          reportData.append('selectedMaintenance', JSON.stringify(selectedMaintenance.value));
          reportData.append('situation', situation.value);
          reportData.append('selectedSituations', JSON.stringify(selectedSituations.value));
          reportData.append('cause', cause.value);
          reportData.append('selectedCauses', JSON.stringify(selectedCauses.value));
          reportData.append('spareParts', JSON.stringify(spareParts.value));

          if (photoFile.value) {
              const truncatedFileName = photoFile.value.name.slice(-100);
              const file = new File([photoFile.value], truncatedFileName, { type: photoFile.value.type });
              reportData.append('photo', file);
          }
          if (signaturePad.value) {
              const dataURL = signaturePad.value.toDataURL();
              const blob = dataURLToBlob(dataURL);
              reportData.append('handwrittenNotes', blob, 'handwritten_notes.png');
          }

          axios
              .post('http://127.0.0.1:8000/api/workOrder/daily_reports/', reportData, {
                  headers: {
                      'Content-Type': 'multipart/form-data'
                  }
              })
              .then((response) => {
                  alertMessage.value = 'データが正常に保存されました。';
                  alertType.value = 'success';
                  showAlert.value = true;
                  clearAllForms();
              })
              .catch((error) => {
                  alertMessage.value = error.response?.data?.detail || 'データの保存に失敗しました。';
                  alertType.value = 'error';
                  showAlert.value = true;
              });
      };

      // dataURLをBlobに変換するヘルパー関数
      const dataURLToBlob = (dataURL) => {
          const byteString = atob(dataURL.split(',')[1]);
          const mimeString = dataURL.split(',')[0].split(':')[1].split(';')[0];
          const ab = new ArrayBuffer(byteString.length);
          const ia = new Uint8Array(ab);
          for (let i = 0; i < byteString.length; i++) {
              ia[i] = byteString.charCodeAt(i);
          }
          return new Blob([ab], { type: mimeString });
      };

      // マウント時にシグネチャパッドを初期化
      onMounted(() => {
          const canvas = document.querySelector('canvas');
          signaturePad.value = new SignaturePad(canvas, {
              penColor: 'black',
              backgroundColor: 'rgba(255, 255, 255, 0)'
          });
      });

      return {
          selectedTab,
          selectTab,
          recorder,
          companyCode,
          activity,
          workOrderExists,
          workOrderDetails,
          maintenanceType,
          selectedMaintenanceTypes,
          maintenanceTypeOptions,
          maintenanceDescription,
          selectedMaintenance,
          maintenanceOptions,
          situation,
          selectedSituations,
          situationOptions,
          cause,
          selectedCauses,
          causeOptions,
          sparePartsUsed,
          spareParts,
          photoPreview,
          photoFile,
          handleFileUpload,
          setPenMode,
          setEraserMode,
          clearCanvas,
          clearAllForms,
          saveReport,
          formattedDate,
          userStore,
          showAlert,
          alertType,
          alertMessage,
          toggleWorkOrder,
          toggleSparePartsUsage,
          equipmentOptions,
          selectedEquipment,
          damageOptions,
          selectedDamage,
          damageOther,
          removeFile
      };
  }
};
</script>

<style scoped>
/* 全体のコンテナ */
.daily-report-container {
  background-color: #d3d3d3;
  font-family: 'Arial', sans-serif;
  padding: 20px;
  border-radius: 8px;
}

.form-container {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* フォームタイトル */
.form-title {
  font-weight: bold;
  font-size: 24px;
  color: #000;
}

/* ヘッダーのスタイル */
.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.recorder-field {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 10px;
}

/* 各フィールドのスタイル */
.field {
  margin-bottom: 1.5rem;
}

.field label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: #555;
  font-size: 18px;
}

/* 質問分のセクションに追加のクラスを追加 */
.question-section {
  margin-top: 50px; /* 各質問分の上部に間隔を追加 */
}

.field input,
.field textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.field textarea {
  resize: vertical;
}

/* テキストフォームとラベルのスタイル */
.date-label {
  font-weight: bold;
  margin-right: 10px;
}

.date {
  margin-left: 20px;
  font-weight: bold;
  font-size: 16px;
  color: #333;
}

/* チェックボックスグループのスタイル */
.checkbox-group {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
}

.checkbox-item {
  display: flex;
  align-items: center;
  font-size: 16px;
  line-height: 1.5;
}

/* サインパッドのスタイル */
.signature-pad {
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  max-width: 500px;
  height: 200px;
}

/* ボタンコンテナとボタンのスタイル */
.button-container {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.save-button {
  background-color: #007bff;
  color: white;
  font-weight: bold;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.clear-button {
  background-color: #ff6347;
  color: white;
  font-weight: bold;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.save-button:hover {
  background-color: #0056b3;
}

.clear-button:hover {
  background-color: #d94e3b;
}

/* 写真プレビューのスタイル */
.photo-preview {
  margin-top: 10px;
}

.preview-image {
  max-width: 300px;
  height: auto;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* サインパッドツールバーのスタイル */
.canvas-toolbar {
  display: flex;
  justify-content: flex-start;
  gap: 10px;
  margin-top: 10px;
}

/* サイドバーのスタイル */
.sidebar {
  background-color: #87ceeb;
  padding: 10px;
  border-radius: 8px;
}

.sidebar-text {
  font-weight: bold;
  font-size: 18px;
  color: #000000 !important;
}

.sidebar-icon {
  font-size: 24px;
  color: #000000;
  margin-right: 8px;
}

.custom-rounded {
  border-top-left-radius: 16px !important;
}

/* カスタムボタンの幅設定 */
.custom-button-width {
  width: 100px;
}

/* 各ボタンの色とスタイル */
.yes-button {
  background-color: #28a745;
  color: white;
  font-weight: bold;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.no-button {
  background-color: #dc3545;
  color: white;
  font-weight: bold;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.yes-button:hover {
  background-color: #218838;
}

.no-button:hover {
  background-color: #c82333;
}

/* Yes, No ボタンのグループスタイル */
.spare-parts-selection,
.work-order-selection {
  display: flex;
  gap: 20px;
}

/* 横線のスタイル */
.divider {
  width: 100%;
  border: none;
  border-top: 2px solid black;
  margin: 30px 0;
}

.checkmark {
  font-size: 18px;
  color: #dc3545;
  margin-left: 10px;
  font-weight: bold;
  vertical-align: middle;
}

.no-button.selected {
  background-color: #c82333;
  color: white;
}

/* その他の入力フォームのスタイル */
#damageOther {
  margin-top: 10px;
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

/* ファイルアップロードセクションのスタイル */
.photo-upload-section {
  flex: 1;
}

.file-upload-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

.file-input {
  width: 200px; /* フォーム幅の調整 */
  padding: 6px 12px;
}

.remove-button {
  background-color: #ff6347;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 6px 12px;
  transition: background-color 0.3s ease;
}

.remove-button:hover {
  background-color: #d94e3b;
}

/* field-container のスタイル */
.field-container {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}

/* 手書きメモとボタンを含むコンテナのスタイル */
.handwritten-notes-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* 手書きメモセクションのスタイル */
.handwritten-notes-section {
  flex: 1;
  width: 100%;
}

.photo-preview {
  margin-top: 10px;
}

.preview-image {
  max-width: 300px;
  height: auto;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* サインパッドのスタイル */
.signature-pad {
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  height: 200px;
}

/* キャンバスツールバーのスタイル */
.canvas-toolbar {
  display: flex;
  justify-content: flex-start;
  gap: 10px;
  margin-top: 10px;
}

/* ボタンコンテナのスタイル */
.button-container {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style>
