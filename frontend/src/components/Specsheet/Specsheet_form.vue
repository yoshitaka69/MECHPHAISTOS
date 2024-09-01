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
					<input v-model="companyName" type="text" placeholder="会社名" />
					<input v-model="title" type="text" placeholder="タイトル" />
					<input v-model="date" type="date" placeholder="日付" />
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
		  <Button @click="generatePDF" class="blue-button">PDF作成</Button>
		</div>
	  </div>
  
	  <!-- Context Menu -->
	  <ul v-if="isContextMenuVisible" :style="{ top: `${contextMenuY}px`, left: `${contextMenuX}px` }" class="context-menu">
		<li @click="insertImage">画像を入力</li>
		<li @click="addColumn">列の追加</li>
	  </ul>
	</div>
  </template>
  
  <script lang="ts" setup>
  import { ref, reactive } from 'vue';
  import jsPDF from 'jspdf';
  import html2canvas from 'html2canvas';
  import Button from 'primevue/button';
  
  const companyName = ref('');
  const title = ref('');
  const date = ref('');
  const revisionDate = ref('');
  const pages = reactive([{ leftInput: '', rightInput: '' }]);
  const isContextMenuVisible = ref(false);
  const contextMenuX = ref(0);
  const contextMenuY = ref(0);
  const selectedPageIndex = ref(null);
  
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
  }
  
  .form-fields {
	display: flex;
	flex-direction: column;
	align-items: flex-start;
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
  
  .left-side-content input, .right-side-content input {
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
  </style>
  