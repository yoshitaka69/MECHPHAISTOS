<template>
	<div class="form-container">
	  <h1 class="title">Maintenance working report</h1>
	  <div class="layout-container">
		<div class="instruction">
		  <h2>Instructions</h2>
		  <p>Please fill out all required fields with accurate information. Refer to the following guidelines:</p>
		  <ul>
			<li><strong>Task Name:</strong> Enter the name of the task.</li>
			<li><strong>Description:</strong> Provide a detailed description of the task.</li>
			<li><strong>Start Date/End Date:</strong> Specify the start and end dates.</li>
			<li><strong>Equipment:</strong> Identify the equipment involved.</li>
			<li><strong>Part Name:</strong> Mention the part name if applicable.</li>
			<li><strong>Cause:</strong> Describe the cause of the issue.</li>
			<li><strong>Summary & Remarks:</strong> Summarize the findings and add any additional remarks.</li>
		  </ul>
		</div>
		<div class="pages" ref="formContent">
		  <div v-for="(page, index) in pages" :key="index" class="page">
			<form @submit.prevent="submitForm">
			  <div v-if="index === 0">
				<div class="header-info">
				  <div class="creation-date">Created on: {{ creationDate }}</div>
				  <div class="form-group reporter">
					<label for="reporter">Reporter:</label>
					<InputText v-model="page.reporter" placeholder="Enter reporter name" required />
				  </div>
				</div>
				<div class="form-group">
				  <label for="taskName">Task Name:</label>
				  <InputText v-model="page.taskName" placeholder="Enter task name" required />
				</div>
				<div class="form-group">
				  <label for="description">Description:</label>
				  <Textarea v-model="page.description" rows="6" style="width: 100%;" autoResize placeholder="Enter description" required />
				</div>
				<div class="form-group-inline">
				  <div class="form-group">
					<label for="startDate">Start Date:</label>
					<Calendar v-model="page.startDate" dateFormat="yy-mm-dd" placeholder="Select a start date" required />
				  </div>
				  <div class="form-group" style="margin-left: 16px;">
					<label for="endDate">End Date:</label>
					<Calendar v-model="page.endDate" dateFormat="yy-mm-dd" placeholder="Select an end date" required />
				  </div>
				</div>
				<div class="form-group-inline">
				  <div class="form-group">
					<label for="equipment">Equipment:</label>
					<InputText v-model="page.equipment" placeholder="Enter equipment name" required />
				  </div>
				  <div class="form-group" style="margin-left: 16px;">
					<label for="partName">Part Name:</label>
					<InputText v-model="page.partName" placeholder="Enter part name" required />
				  </div>
				</div>
				<div class="additional-text" style="margin-top: 24px;">
				  <p>Some additional information or instructions can be placed here under the cause section.</p>
				</div>
				<hr class="separator" />
				<div class="cause-section">
				  <div class="form-group">
					<label for="cause">Cause:</label>
					<InputText v-model="page.cause" placeholder="Enter cause" required />
				  </div>
				</div>
				<div class="form-group">
				  <label for="pmType">PM Type:</label>
				  <InputText v-model="page.pmType" placeholder="Enter PM type" required />
				</div>
				<div class="form-group">
				  <label for="tag">Tag:</label>
				  <InputText v-model="page.tag" placeholder="Enter tag" required />
				</div>
				<div class="form-group">
				  <label for="maintenanceCategory">Maintenance Category:</label>
				  <InputText v-model="page.maintenanceCategory" placeholder="Enter maintenance category" required />
				</div>
				<div class="form-group">
				  <label for="summaryRemarks">Summary & Remarks:</label>
				  <Textarea v-model="page.summaryRemarks" rows="6" style="width: 100%;" autoResize placeholder="Enter summary and remarks" />
				</div>
			  </div>
			  <template v-else>
				<div class="image-notes-container">
				  <div v-for="n in 3" :key="n" class="image-notes-group">
					<div class="form-group-inline">
					  <div class="form-group">
						<label for="imageUpload">Upload Image:</label>
						<div class="image-box">
						  <img :src="page.images[n-1] || noImage" alt="Uploaded Image" class="image-preview" />
						</div>
						<FileUpload mode="basic" @select="(e) => onFileChange(e, index, n)" chooseLabel="Choose" :class="['choose-button']"/>
					  </div>
					  <div class="form-group">
						<label for="additionalNotes">Additional Notes:</label>
						<Textarea v-model="page.additionalNotes[n-1]" rows="12" cols="50" autoResize placeholder="Enter additional notes" />
					  </div>
					</div>
					<hr v-if="n < 3" class="separator" />
				  </div>
				</div>
			  </template>
			</form>
			<div class="page-number">Page {{ index + 1 }}</div>
		  </div>
		</div>
	  </div>
	  <div class="buttons">
		<Button label="Add Page" icon="pi pi-plus" @click="addPage" />
		<Button label="Export PDF" icon="pi pi-file-pdf" @click="exportPDF" /> <!-- PDF出力ボタン -->
		<Button label="Upload PDF" icon="pi pi-upload" @click="uploadPDF" /> <!-- PDFアップロードボタン -->
	  </div>
	</div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import InputText from 'primevue/inputtext';
  import Textarea from 'primevue/textarea';
  import Calendar from 'primevue/calendar';
  import FileUpload from 'primevue/fileupload';
  import Button from 'primevue/button';
  import noImage from '@/assets/no_image.jpg'; // no_image.jpgをインポート
  import jsPDF from 'jspdf';
  import html2canvas from 'html2canvas';
  import axios from 'axios'; // axiosをインポート
  import { useUserStore } from '@/stores/userStore'; // useUserStoreをインポート
  
  const userStore = useUserStore(); // Piniaストアを取得
  
  const pages = ref([
	{ taskName: '', description: '', startDate: '', endDate: '', equipment: '', partName: '', reporter: '', pmType: '', tag: '', cause: '', maintenanceCategory: '', summaryRemarks: '' },
	{ taskName: '', description: '', startDate: '', endDate: '', equipment: '', partName: '', reporter: '', pmType: '', images: ['', '', ''], additionalNotes: ['', '', ''], summaryRemarks: '' },
  ]);
  
  const creationDate = ref(new Date().toLocaleDateString());
  
  const addPage = () => {
	pages.value.push({
	  taskName: '',
	  description: '',
	  startDate: '',
	  endDate: '',
	  equipment: '',
	  partName: '',
	  reporter: '',
	  pmType: '',
	  images: ['', '', ''],
	  additionalNotes: ['', '', ''],
	  summaryRemarks: '',
	});
  };
  
  const onFileChange = (event, index, imageIndex) => {
	const file = event.files[0];
	if (file) {
	  const reader = new FileReader();
	  reader.onload = (e) => {
		pages.value[index].images[imageIndex - 1] = e.target.result;
	  };
	  reader.readAsDataURL(file);
	}
  };
  
  // PDF出力のための関数
  const exportPDF = () => {
	const formContent = document.querySelectorAll('.page');
	const pdf = new jsPDF({
	  orientation: 'portrait',
	  unit: 'mm',
	  format: 'a4'
	});
  
	formContent.forEach((content, index) => {
	  html2canvas(content).then((canvas) => {
		const imgData = canvas.toDataURL('image/png');
		if (index > 0) {
		  pdf.addPage();
		}
		pdf.addImage(imgData, 'PNG', 0, 0, 210, 297); // A4サイズに合わせて画像を追加
		if (index === formContent.length - 1) {
		  pdf.save('Maintenance_report.pdf'); // PDFのファイル名を指定して保存
		}
	  });
	});
  };
  
  // PDFをサーバーにアップロードする関数
  const uploadPDF = () => {
	const formContent = document.querySelectorAll('.page');
	const pdf = new jsPDF({
	  orientation: 'portrait',
	  unit: 'mm',
	  format: 'a4'
	});
  
	formContent.forEach((content, index) => {
	  html2canvas(content).then((canvas) => {
		const imgData = canvas.toDataURL('image/png');
		if (index > 0) {
		  pdf.addPage();
		}
		pdf.addImage(imgData, 'PNG', 0, 0, 210, 297); // A4サイズに合わせて画像を追加
		if (index === formContent.length - 1) {
		  // 最後のページが追加された後にPDFをBlobに変換してアップロード
		  const pdfBlob = pdf.output('blob');
  
		  const formData = new FormData();
		  formData.append('file', pdfBlob, 'Maintenance_report.pdf');
		  formData.append('companyCode', userStore.companyCode); // companyCodeを追加
		  formData.append('task_name', pages.value[0].taskName); 
		  formData.append('description', pages.value[0].description);
		  formData.append('start_date', pages.value[0].startDate);
		  formData.append('end_date', pages.value[0].endDate);
		  formData.append('equipment', pages.value[0].equipment);
		  formData.append('part_name', pages.value[0].partName);
		  formData.append('reporter', pages.value[0].reporter);
		  formData.append('pm_type', pages.value[0].pmType);
		  formData.append('summary_remarks', pages.value[0].summaryRemarks);
  
		  // console.logで送信内容を出力する
		  console.log('FormData being sent:', {
			companyCode: userStore.companyCode,
			task_name: pages.value[0].taskName,
			description: pages.value[0].description,
			start_date: pages.value[0].startDate,
			end_date: pages.value[0].endDate,
			equipment: pages.value[0].equipment,
			part_name: pages.value[0].partName,
			reporter: pages.value[0].reporter,
			pm_type: pages.value[0].pmType,
			summary_remarks: pages.value[0].summaryRemarks,
		  });
  
		  axios.post('api/workingReport/maintenanceReports/', formData, {
			headers: {
			  'Content-Type': 'multipart/form-data'
			}
		  }).then(response => {
			console.log('PDF uploaded successfully:', response.data);
		  }).catch(error => {
			console.error('Error uploading PDF:', error);
		  });
		}
	  });
	});
  };
  </script>
  
  
  <style>
  /* 既存のスタイル */
  .form-container {
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 16px;
	padding: 16px;
	position: relative;
  }
  
  .title {
	font-size: 24px;
	font-weight: bold;
	margin-bottom: 16px;
  }
  
  .layout-container {
	display: flex;
  }
  
  .instruction {
	width: 20%; /* 説明フィールドの横幅を狭くしました */
	padding-right: 16px;
	border-right: 1px solid #ccc;
	box-sizing: border-box;
  }
  
  .pages {
	width: 80%;
	display: flex;
	flex-wrap: wrap;
	gap: 16px;
	justify-content: center;
  }
  
  .page {
	width: calc(50% - 8px); /* A4を2枚並べて表示 */
	height: 297mm; /* A4 height */
	border: 1px solid #000;
	padding: 10mm;
	box-sizing: border-box;
	background-color: #fff;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	margin-bottom: 16px;
	position: relative;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
  }
  
  .form-group {
	margin-bottom: 16px;
  }
  
  .form-group-inline {
	display: flex;
	justify-content: space-between;
	align-items: flex-start;
	gap: 16px;
  }
  
  .form-group label {
	display: block;
	margin-bottom: 8px;
	font-weight: bold;
  }
  
  .cause-section {
	margin-top: 16px;
  }
  
  .additional-text {
	margin-top: 24px;
	font-size: 14px;
	color: #555;
	text-align: left;
  }
  
  .image-notes-container {
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	height: 100%;
  }
  
  .image-notes-group {
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	flex-grow: 1;
	height: calc((100% - 60px) / 3);
  }
  
  .image-box {
	width: 100%;
	height: 250px;
	border: 1px solid #000;
	display: flex;
	justify-content: center;
	align-items: center;
	position: relative;
	margin-bottom: 12px;
  }
  
  .no-image {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	color: #000;
  }
  
  .image-preview {
	max-width: 100%;
	max-height: 100%;
	object-fit: contain;
  }
  
  .choose-button {
	background-color: #007bff !important;
	margin-top: 8px;
  }
  
  .separator {
	border: none;
	border-top: 1px solid #ccc;
	margin: 16px 0;
  }
  
  .buttons {
	display: flex;
	gap: 16px;
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
	  box-shadow: none;
	  border: none;
	  page-break-after: always;
	}
	.buttons {
	  display: none;
	}
  }
  </style>
  