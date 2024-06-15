<template>
	<div class="upload-form">
	  <h1>点検表のアップロード</h1>
	  <input type="file" @change="onFileChange">
	  <button @click="uploadFile">アップロード</button>
	  <div v-if="uploadSuccess" class="result-box">
		<h2>アップロード成功！</h2>
		<p>抽出されたテキスト：</p>
		<pre>{{ extractedText }}</pre>
	  </div>
	  <div v-if="uploadError" class="error-box">
		<h2>アップロード失敗</h2>
		<p>{{ uploadError }}</p>
	  </div>
	</div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
	data() {
	  return {
		selectedFile: null,
		uploadSuccess: false,
		uploadError: '',
		extractedText: '',
	  };
	},
	methods: {
	  onFileChange(event) {
		this.selectedFile = event.target.files[0];
		console.log("選択されたファイル:", this.selectedFile.name);
	  },
	  async uploadFile() {
		const formData = new FormData();
		formData.append('file', this.selectedFile);
		formData.append('name', this.selectedFile.name);
  
		try {
		  const response = await axios.post('http://localhost:8000/api/workingReport/inspection_forms/', formData, {
			headers: {
			  'Content-Type': 'multipart/form-data',
			},
		  });
		  console.log('アップロード成功:', response.data);
		  this.uploadSuccess = true;
		  this.extractedText = response.data.extracted_text;
		} catch (error) {
		  console.error('アップロード失敗:', error);
		  this.uploadError = error.response ? error.response.data.error : error.message;
		}
	  },
	},
  };
  </script>
  
  <style scoped>
  .upload-form {
	background-color: white;
	padding: 20px;
	border-radius: 10px;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	width: 50%;
	margin: auto;
  }
  
  .result-box {
	margin-top: 20px;
	padding: 20px;
	border: 1px solid #ddd;
	border-radius: 5px;
	background-color: #f9f9f9;
  }
  
  .error-box {
	margin-top: 20px;
	padding: 20px;
	border: 1px solid #ffdddd;
	border-radius: 5px;
	background-color: #ffefef;
  }
  
  pre {
	white-space: pre-wrap; /* 長いテキストを折り返して表示 */
	word-wrap: break-word; /* 長い単語を折り返して表示 */
  }
  </style>
  