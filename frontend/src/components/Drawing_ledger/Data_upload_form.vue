<template>
  <Toast /> <!-- Toastを表示するためのコンポーネント -->
  <Dialog
    header="Upload project file"
    :visible="visible"
    :modal="true"
    :closable="false"
    :style="{ width: '60vw' }"
    @update:visible="updateVisible"
  >
    <div class="p-grid">
      <div class="p-col-8">
        <form @submit.prevent="submitForm">
          <div class="p-fluid">
            <!-- プロジェクトネーム -->
            <div class="p-field">
              <label for="project_name">Project Name</label>
              <InputText v-model="formData.project_name" id="project_name" />
            </div>

            <!-- カテゴリをファイルネームの上に配置し、チェックボックスタイプに変更 -->
            <div class="p-field">
              <label for="category">Category</label>
              <div class="p-checkbox-group">
                <Checkbox v-model="formData.categories" inputId="category1" value="Mechanical" />
                <label for="category1">Mechanical</label>
                <Checkbox v-model="formData.categories" inputId="category2" value="Electrical" />
                <label for="category2">Electrical</label>
                <Checkbox v-model="formData.categories" inputId="category3" value="Software" />
                <label for="category3">Software</label>
                <Checkbox v-model="formData.categories" inputId="category4" value="Building" />
                <label for="category4">Building</label>
                <Checkbox v-model="formData.categories" inputId="category5" value="Utilities" />
                <label for="category5">Utilities</label>
                <Checkbox v-model="formData.categories" inputId="category6" value="Other" />
                <label for="category6">Other</label>
              </div>
            </div>

            <!-- ファイルネーム -->
            <div class="p-field">
              <label for="name">File Name</label>
              <InputText v-model="formData.name" id="name" />
            </div>

            <!-- ファイル選択 -->
            <div class="p-field">
              <label for="file">Select File</label>
              <InputText type="file" @change="onFileChange" id="file" />
            </div>

            <!-- 登録者 -->
            <div class="p-field">
              <label for="uploaded_by">Uploaded By</label>
              <InputText v-model="formData.uploaded_by" id="uploaded_by" />
            </div>

            <!-- 登録日 -->
            <div class="p-field">
              <label for="registration_date">Registration Date</label>
              <Calendar v-model="formData.registration_date" id="registration_date" showIcon />
            </div>

            <!-- タグ -->
            <div class="p-field">
              <label for="tag">Tag</label>
              <textarea v-model="formData.tag" id="tag" class="p-inputtextarea" rows="3" style="width: 100%;" />
            </div>

            <!-- ボタン -->
            <div class="p-d-flex p-jc-end">
              <Button label="Cancel" icon="pi pi-times" class="p-button-text p-button-cancel" @click="cancelForm" />
              <Button label="Save" icon="pi pi-check" class="p-ml-2 p-button-success" type="submit" />
            </div>
          </div>
        </form>
      </div>

      <!-- アップロード後のプレビューパネル -->
      <div class="p-col-4" v-if="formData.file">
        <div class="p-card">
          <div class="p-card-header">
            <h4>File Preview</h4>
          </div>
          <div class="p-card-body">
            <p><strong>File Name:</strong> {{ formData.file.name }}</p>
            <p><strong>File Size:</strong> {{ (formData.file.size / 1024).toFixed(2) }} KB</p>
            <p v-if="filePreviewURL"><strong>Preview:</strong></p>
            <iframe v-if="filePreviewURL" :src="filePreviewURL" style="width: 100%; height: 200px;" />
          </div>
        </div>
      </div>
    </div>
  </Dialog>
</template>

<script setup>




import { ref } from 'vue';
import axios from 'axios';  // axiosのインポートを追加
import { useToast } from 'primevue/usetoast'; // Toast用のフックをインポート
import { useUserStore } from '@/stores/userStore';  // Pinia storeのインポート
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import Checkbox from 'primevue/checkbox';

const props = defineProps({
  visible: Boolean,
  entry: Object,
});

const emit = defineEmits(['update:visible', 'submit', 'cancel']);

// Toastインスタンスを作成
const toast = useToast();

// フォームデータの初期化
const formData = ref({
  project_name: props.entry.project_name || '',
  name: props.entry.name || '',
  file: null,
  categories: props.entry.categories || [],
  uploaded_by: props.entry.uploaded_by || '',
  registration_date: props.entry.registration_date || new Date(),
  tag: props.entry.tag || '',
});

// Pinia storeからcompanyCodeを取得
const userStore = useUserStore();
const companyCode = ref(userStore.companyCode);  // companyCodeを取得

// ファイルプレビュー用URL
const filePreviewURL = ref(null);

const updateVisible = (value) => {
  emit('update:visible', value);
};

const onFileChange = (event) => {
  formData.value.file = event.target.files[0];
  filePreviewURL.value = URL.createObjectURL(formData.value.file); // ファイルプレビューURLを作成
};

const submitForm = async () => {
  try {
    // 送信するデータを準備
    const data = {
      project_name: formData.value.project_name,
      name: formData.value.name,
      categories: formData.value.categories,
      uploaded_by: formData.value.uploaded_by,
      registration_date: formData.value.registration_date.toISOString(),
      tag: formData.value.tag,
      companyCode: companyCode.value  // companyCodeを追加
    };

    // データをコンソールに表示
    console.log('Form data to be posted:', data);

    // ポスト処理
    await axios.post('/api/upload-cad-file', data);

    // 成功時のアラート
    toast.add({ severity: 'success', summary: 'Success', detail: 'File uploaded successfully!', life: 3000 });

    emit('submit', formData.value);
  } catch (error) {
    // エラー時のアラート
    toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to upload file!', life: 3000 });
    console.error('Error uploading file:', error);
  }
};

const cancelForm = () => {
  emit('update:visible', false);
  emit('cancel');
};




</script>

<style scoped>
.p-field {
  margin-bottom: 1rem;
}

.p-dialog {
  max-width: 60vw;
}

.p-d-flex {
  display: flex;
}

.p-jc-end {
  justify-content: flex-end;
}

.p-ml-2 {
  margin-left: 0.5rem;
}

.p-button-success {
  background-color: #28a745;
  border: none;
}

.p-button-cancel {
  color: black; /* キャンセルボタンの文字色を黒に */
  border: none;
}

.p-field label {
  font-weight: bold;
  margin-bottom: 0.5rem;
  display: block;
}

.p-field input,
.p-field textarea {
  border-radius: 4px;
}

form {
  padding: 1rem 0;
  background-color: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.p-checkbox-group {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.p-checkbox-group label {
  margin-right: 1rem;
}
</style>
