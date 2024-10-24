<template>
	<div class="specification-form">
	  <div class="left-side">
		<!-- Form Explanation Page -->
		<div class="explanation-page">
		  <h2>フォームの説明</h2>
		  <p>このフォームは仕様書を作成するためのものです。以下の手順で使用してください。</p>
		  <ol>
			<li>会社名、タイトル、日付、改定日を入力します。</li>
			<li>右側のページで詳細情報を入力します。</li>
			<li>必要に応じて新しいページを追加してください。</li>
			<li>完了後、PDFとして保存できます。</li>
		  </ol>
		  
		  <!-- 新しく追加するボタン -->
		  <div class="explanation-buttons">
			<Button class="example-button">Example Button</Button>
			<Button @click="showWizard" class="wizard-button">入力ウィザードフォーム</Button>
		  </div>
		</div>
	  </div>
  
	  <div class="right-side">
		<div class="pages">
		  <!-- 横並びのレイアウトにするためのコンテナ -->
		  <div class="page-container">
			<!-- Page 1: Cover Page -->
			<div class="page cover-page">
			  <div class="outer-box">
				<div class="inner-box">
				  <div class="form-fields">
					<input v-model="title" type="text" placeholder="タイトル" />
					<input v-model="companyName" type="text" placeholder="会社名" />
					<input v-model="date" type="date" placeholder="日付" />
					<label class="revision-label">改定日</label>
					<input v-model="revisionDate" type="date" placeholder="改定日" />
				  </div>
				</div>
			  </div>
			</div>
  
			<!-- Page 2 and beyond: Content Pages -->
			<div v-for="(page, index) in pages" :key="'page-'+index" class="page content-page">
			  <div class="content-layout">
				<div class="left-side-content">
				  <input v-model="page.leftInput" type="text" placeholder="左側の入力フォーム" />
				</div>
				<div class="right-side-content" @contextmenu.prevent="showContextMenu($event, index)">
				  <input v-model="page.rightInput" type="text" placeholder="右側の入力フォーム" />
				</div>
			  </div>
			</div>
		  </div>
		</div>
  
		<div class="buttons">
		  <Button @click="addPage" class="blue-button">ページを追加</Button>
		  <Button @click="generatePDF" class="blue-button">PDF保存</Button>
		  <Button @click="savePDF" class="blue-button">保存</Button>
		</div>
	  </div>
  
	  <!-- Context Menu -->
	  <ul v-if="isContextMenuVisible" :style="{ top: `${contextMenuY}px`, left: `${contextMenuX}px` }" class="context-menu">
		<li @click="insertImage">画像を入力</li>
		<li @click="addColumn">列の追加</li>
	  </ul>

	  <!-- 入力ウィザード用モーダル -->
	  <div v-if="isWizardVisible" class="modal">
		<div class="modal-content">
		  <h2>入力ウィザードフォーム</h2>
		  <div class="wizard-form-fields">
			<input v-model="wizardTitle" type="text" placeholder="タイトル" />
			<input v-model="wizardCompanyName" type="text" placeholder="会社名" />
			<input v-model="wizardDate" type="date" placeholder="日付" />
			<label class="revision-label">改定日</label>
			<input v-model="wizardRevisionDate" type="date" placeholder="改定日" />
		  </div>
		  <div class="modal-buttons">
			<Button @click="applyWizardData" class="blue-button">適用</Button>
			<Button @click="closeWizard" class="blue-button">キャンセル</Button>
		  </div>
		</div>
	  </div>
	</div>
</template>



  



<script lang="ts" setup>
import { ref, reactive } from 'vue';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';
import Button from 'primevue/button';
import axios from 'axios';

const companyName = ref('');
const title = ref('');
const date = ref('');
const revisionDate = ref('');
const pages = reactive([{ leftInput: '', rightInput: '' }]);
const isContextMenuVisible = ref(false);
const contextMenuX = ref(0);
const contextMenuY = ref(0);
const selectedPageIndex = ref(null);

// 入力ウィザード関連の状態
const isWizardVisible = ref(false);
const wizardCompanyName = ref('');
const wizardTitle = ref('');
const wizardDate = ref('');
const wizardRevisionDate = ref('');

const addPage = () => {
  pages.push({ leftInput: '', rightInput: '' });
};

const generatePDF = async () => {
  const pdf = new jsPDF('p', 'mm', 'a4');
  const pages = document.querySelectorAll('.page');

  for (let i = 0; i < pages.length; i++) {
    if (i > 0) {
      pdf.addPage();
    }
    const canvas = await html2canvas(pages[i]);
    const imgData = canvas.toDataURL('image/png');
    pdf.addImage(imgData, 'PNG', 0, 0, 210, 297);
  }
  pdf.save('specification.pdf');
};

const savePDF = async () => {
  const pdf = new jsPDF('p', 'mm', 'a4');
  const pages = document.querySelectorAll('.page');

  for (let i = 0; i < pages.length; i++) {
    if (i > 0) {
      pdf.addPage();
    }
    const canvas = await html2canvas(pages[i]);
    const imgData = canvas.toDataURL('image/png');
    pdf.addImage(imgData, 'PNG', 0, 0, 210, 297);
  }

  const pdfBlob = pdf.output('blob');

  const formData = new FormData();
  formData.append('pdf_file', pdfBlob, 'specification.pdf');
  formData.append('title', title.value);

  try {
    const response = await axios.post('http://127.0.0.1:8000/api/workingReport/specsheets/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    console.log('PDF保存成功:', response.data);
  } catch (error) {
    console.error('PDF保存失敗:', error);
    if (error.response) {
      console.error('Server responded with:', error.response.status, error.response.data);
    }
  }
};

// コンテキストメニューとウィザード関連の関数
const showContextMenu = (event, index) => {
  contextMenuX.value = event.clientX;
  contextMenuY.value = event.clientY;
  isContextMenuVisible.value = true;
  selectedPageIndex.value = index;
  document.addEventListener('click', hideContextMenu);
};

const hideContextMenu = () => {
  isContextMenuVisible.value = false;
  document.removeEventListener('click', hideContextMenu);
};

const insertImage = () => {
  alert('画像を入力');
  hideContextMenu();
};

const addColumn = () => {
  alert('列の追加');
  hideContextMenu();
};

// 入力ウィザードの関数
const showWizard = () => {
  isWizardVisible.value = true;
};

const closeWizard = () => {
  isWizardVisible.value = false;
};

const applyWizardData = () => {
  companyName.value = wizardCompanyName.value;
  title.value = wizardTitle.value;
  date.value = wizardDate.value;
  revisionDate.value = wizardRevisionDate.value;
  closeWizard();
};
</script>




<style scoped>
.specification-form {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  margin: 20px;
  justify-content: space-between;
  overflow-x: hidden;
}

.left-side {
  width: 15%;
  margin-right: 20px;
  flex-shrink: 0;
}

.right-side {
  width: 85%;
  display: flex;
  flex-direction: column;
}

.pages {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.page-container {
  display: flex;
  gap: 10px;
  max-width: 100%;
  overflow-x: auto; /* 横スクロールを可能にする */
}

.page {
  flex: 0 0 auto;
  width: 210mm;
  height: 297mm;
  border: 1px solid black;
  box-sizing: border-box;
  background-color: white;
}

.cover-page .outer-box {
  width: 90%; /* サイズを縮小 */
  height: 90%; /* サイズを縮小 */
  border: 3px solid black;
  margin: 50px auto 0 auto; /* 上部に50pxのマージンを追加 */
  display: flex;
  align-items: center;
  justify-content: center;
}

.cover-page .inner-box {
  width: 85%; /* サイズを縮小 */
  height: 85%; /* サイズを縮小 */
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center; /* 中央寄せ */
}

.form-fields {
  display: flex;
  flex-direction: column;
  align-items: center; /* 中央寄せ */
  width: 80%; /* フォーム全体の幅を調整 */
}

input {
  margin-top: 10px;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  box-sizing: border-box;
}

input::placeholder {
  color: lightgray;
}

.revision-label {
  margin-top: 20px;
  font-size: 16px;
}

.content-page .content-layout {
  display: flex;
  height: calc(100% - 20px);
  padding-top: 10px;
  box-sizing: border-box;
}

.left-side-content {
  width: 50%;
  padding-left: 10px;
}

.right-side-content {
  width: 50%;
  padding-right: 10px;
}

.left-side-content input,
.right-side-content input {
  width: 100%;
  height: 100%;
}

.buttons {
  margin-top: 20px;
  display: flex;
  gap: 10px;
}

.blue-button {
  background-color: blue;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.blue-button:hover {
  background-color: darkblue;
}

/* Context Menu Styles */
.context-menu {
  position: absolute;
  list-style-type: none;
  margin: 0;
  padding: 5px;
  background-color: white;
  border: 1px solid #ccc;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  z-index: 1000;
}

.context-menu li {
  padding: 8px 12px;
  cursor: pointer;
}

.context-menu li:hover {
  background-color: #eee;
}

.explanation-page {
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid black;
  box-sizing: border-box;
  word-wrap: break-word;
  height: 100%;
  overflow: hidden;
}

.explanation-page h2 {
  margin-top: 0;
}

.explanation-page p {
  margin-bottom: 10px;
}

.explanation-page ol {
  padding-left: 20px;
}

.explanation-buttons {
  margin-top: 20px;
  display: flex;
  gap: 10px;
}

.example-button,
.wizard-button {
  background-color: blue;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.example-button:hover,
.wizard-button:hover {
  background-color: darkblue;
}

/* モーダル用のスタイル */
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  border: 1px solid black;
  z-index: 1001;
}

.modal-content {
  display: flex;
  flex-direction: column;
}

.wizard-form-fields {
  display: flex;
  flex-direction: column;
  align-items: center; /* 中央寄せ */
}

.wizard-form-fields input {
  margin-top: 10px;
  width: 80%; /* フォーム全体の幅を調整 */
  padding: 10px;
  font-size: 16px;
  box-sizing: border-box;
}

.revision-label {
  margin-top: 20px;
  font-size: 16px;
}

.modal-buttons {
  margin-top: 20px;
  display: flex;
  gap: 10px;
}
</style>
