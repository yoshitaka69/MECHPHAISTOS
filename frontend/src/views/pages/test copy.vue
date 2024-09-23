<template>
    <div class="daily-report-container">
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
                <h2 class="mb-4 form-title">Daily Report</h2>
                <div class="field recorder-field">
                  <label for="recorder">Recorder</label>
                  <InputText id="recorder" v-model="recorder" :value="userStore.userName" placeholder="Enter recorder name" readonly />
                  <span class="date">{{ formattedDate }}</span>
                </div>
              </div>
              <div class="field">
                <label for="activity">What did you do today?</label>
                <Textarea id="activity" v-model="activity" rows="3" autoResize placeholder="Describe your activities..." />
              </div>
              <div class="field">
                <label for="workOrder">Is there any work order?</label>
                <InputText id="workOrder" v-model="workOrder" placeholder="Enter work order number" />
              </div>
              <div class="field">
                <label for="maintenanceType">What is the type of maintenance?</label>
                <InputText id="maintenanceType" v-model="maintenanceType" placeholder="Enter maintenance type" />
              </div>
              <div class="field">
                <label for="maintenanceDescription">What kind of maintenance was it?</label>
                <Textarea id="maintenanceDescription" v-model="maintenanceDescription" rows="3" autoResize placeholder="Describe the maintenance..." />
              </div>
              <div class="field">
                <label for="situation">Do you know what the situation was?</label>
                <Textarea id="situation" v-model="situation" rows="3" autoResize placeholder="Describe the situation..." />
              </div>
              <div class="field">
                <label for="cause">Do you know what the cause was?</label>
                <Textarea id="cause" v-model="cause" rows="3" autoResize placeholder="Describe the cause..." />
              </div>
              <div class="field">
                <label for="spareParts">Did you use any spare parts?</label>
                <InputText id="spareParts" v-model="spareParts" placeholder="Enter used spare parts" />
              </div>
              <div class="field">
                <label for="photoUpload">Upload Photo</label>
                <input type="file" id="photoUpload" @change="handleFileUpload" accept="image/*" />
                <div v-if="photoPreview" class="photo-preview">
                  <img :src="photoPreview" alt="Photo Preview" class="preview-image" />
                </div>
              </div>
              <div class="field">
                <label>Handwritten Notes</label>
                <canvas ref="signatureCanvas" width="500" height="200" class="signature-pad"></canvas>
              </div>
              <div class="field button-container">
                <Button label="Save" icon="pi pi-save" class="save-button" @click="saveReport" />
                <Button label="Clear" icon="pi pi-times" class="clear-button" @click="clearSignature" />
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
  
  export default {
    components: {
      InputText,
      Textarea,
      Button
    },
    setup() {
      const userStore = useUserStore(); // Piniaストアのインスタンスを取得
      const selectedTab = ref('dailyReport');
      const recorder = ref(userStore.userName); // Piniaストアからユーザー名を取得
      const activity = ref('');
      const workOrder = ref('');
      const maintenanceType = ref('');
      const maintenanceDescription = ref('');
      const situation = ref('');
      const cause = ref('');
      const spareParts = ref('');
      const photoPreview = ref(null); // 写真プレビューのURLを保存する
      const signaturePad = ref(null);
  
      // 日付をフォーマットする
      const formatDate = (date) => {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Intl.DateTimeFormat('en-US', options).format(date);
      };
  
      const formattedDate = ref(formatDate(new Date())); // 現在の日付をフォーマット
  
      const selectTab = (tab) => {
        selectedTab.value = tab;
      };
  
      const handleFileUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = (e) => {
            photoPreview.value = e.target.result;
          };
          reader.readAsDataURL(file);
        }
      };
  
      const clearSignature = () => {
        signaturePad.value.clear();
      };
  
      const saveReport = () => {
        const reportData = {
          recorder: userStore.userName, // Piniaストアからユーザー名を使用
          activity: activity.value,
          workOrder: workOrder.value,
          maintenanceType: maintenanceType.value,
          maintenanceDescription: maintenanceDescription.value,
          situation: situation.value,
          cause: cause.value,
          spareParts: spareParts.value,
          photo: photoPreview.value, // 写真のデータを保存（base64形式）
          handwrittenNotes: signaturePad.value.toDataURL(), // 手書きノートのデータ（base64形式）
          date: formattedDate.value // 日付を保存
        };
  
        // POSTリクエストでデータをサーバーに送信
        axios
          .post('http://127.0.0.1:8000/api/daily_reports/', reportData)
          .then((response) => {
            console.log('Report saved successfully:', response.data);
          })
          .catch((error) => {
            console.error('Error saving report:', error);
          });
      };
  
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
        activity,
        workOrder,
        maintenanceType,
        maintenanceDescription,
        situation,
        cause,
        spareParts,
        photoPreview,
        handleFileUpload,
        clearSignature,
        saveReport,
        formattedDate,
        userStore // Piniaストアを返す
      };
    }
  };
  </script>
  
  <style scoped>
  .daily-report-container {
    background-color: #d3d3d3; /* 濃い灰色 */
    font-family: 'Arial', sans-serif; /* フォント */
    padding: 20px;
    border-radius: 8px;
  }
  
  .form-container {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  .form-title {
    font-weight: bold;
    font-size: 24px;
    color: #333;
  }
  
  .header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .recorder-field {
    width: 400px;
    display: flex;
    align-items: center;
  }
  
  .field {
    margin-bottom: 1.5rem;
  }
  
  .field label {
    display: block;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: #555;
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
  
  .date {
    margin-left: 20px;
    font-weight: bold;
    font-size: 16px;
    color: #333;
  }
  
  .signature-pad {
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 100%;
    max-width: 500px;
    height: 200px;
  }
  
  .button-container {
    display: flex;
    justify-content: flex-end;
    gap: 10px; /* ボタン間のスペース */
  }
  
  .save-button {
    background-color: #007bff; /* 青色 */
    color: white;
    font-weight: bold;
    padding: 8px 16px; /* ボタンの横幅を狭く */
    border: none;
    border-radius: 4px;
    transition: background-color 0.3s ease;
  }
  
  .clear-button {
    background-color: #ff6347; /* トマト色 */
    color: white;
    font-weight: bold;
    padding: 8px 16px; /* ボタンの横幅を狭く */
    border: none;
    border-radius: 4px;
    transition: background-color 0.3s ease;
  }
  
  .save-button:hover {
    background-color: #0056b3; /* 濃い青色 */
  }
  
  .clear-button:hover {
    background-color: #d94e3b; /* 濃いトマト色 */
  }
  
  .photo-preview {
    margin-top: 10px;
  }
  
  .preview-image {
    max-width: 300px; /* プレビュー画像の最大幅 */
    height: auto;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .sidebar {
    background-color: #87ceeb; /* 青空のような青色 */
    padding: 10px;
    border-radius: 8px; /* 角を丸める */
  }
  
  .custom-rounded {
    border-top-left-radius: 16px !important; /* aタグの左上角を丸める */
  }
  
  .sidebar-text {
    font-weight: bold;
    font-size: 18px;
    color: #ffffff;
  }
  
  .sidebar-icon {
    font-size: 24px; /* アイコンのサイズ */
    color: #000000; /* アイコンの色を黒に設定 */
    margin-right: 8px;
  }
  </style>
  