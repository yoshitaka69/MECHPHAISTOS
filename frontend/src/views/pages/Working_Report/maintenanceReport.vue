<template>
	<div class="form-container">
	  <header>
		<h1>Create Equipment Specification</h1>
	  </header>
	  <form @submit.prevent="submitForm">
		<div>
		  <label for="name">Name:</label>
		  <input type="text" v-model="formData.name" id="name">
		</div>
		<div>
		  <label for="manufacturer">Manufacturer:</label>
		  <input type="text" v-model="formData.manufacturer" id="manufacturer">
		</div>
		<div>
		  <label for="model_number">Model Number:</label>
		  <input type="text" v-model="formData.model_number" id="model_number">
		</div>
		<div>
		  <label for="purchase_date">Purchase Date:</label>
		  <input type="date" v-model="formData.purchase_date" id="purchase_date">
		</div>
		<div>
		  <label for="description">Description:</label>
		  <textarea v-model="formData.description" id="description"></textarea>
		</div>
		<div class="image-upload">
		  <label for="image1">Image 1:</label>
		  <div class="image-row">
			<input type="file" @change="onImageChange($event, 'image1')" id="image1" accept="image/*">
			<textarea v-model="formData.image1_description" placeholder="Description for image 1"></textarea>
		  </div>
		</div>
		<div class="image-upload">
		  <label for="image2">Image 2:</label>
		  <div class="image-row">
			<input type="file" @change="onImageChange($event, 'image2')" id="image2" accept="image/*">
			<textarea v-model="formData.image2_description" placeholder="Description for image 2"></textarea>
		  </div>
		</div>
		<div class="image-upload">
		  <label for="image3">Image 3:</label>
		  <div class="image-row">
			<input type="file" @change="onImageChange($event, 'image3')" id="image3" accept="image/*">
			<textarea v-model="formData.image3_description" placeholder="Description for image 3"></textarea>
		  </div>
		</div>
		<div class="form-actions">
		  <button type="button" @click="cancelForm">Cancel</button>
		  <button type="submit">Save</button>
		</div>
	  </form>
	  <footer>
		<p>&copy; 2024 Your Company</p>
	  </footer>
	</div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref } from 'vue';
  
  export default {
	setup() {
	  const formData = ref({
		name: '',
		manufacturer: '',
		model_number: '',
		purchase_date: '',
		description: '',
		image1: null,
		image1_description: '',
		image2: null,
		image2_description: '',
		image3: null,
		image3_description: ''
	  });
  
	  const submitForm = async () => {
		try {
		  console.log("Form data being submitted:", formData.value);
		  const formPayload = new FormData();
		  formPayload.append('name', formData.value.name);
		  formPayload.append('manufacturer', formData.value.manufacturer);
		  formPayload.append('model_number', formData.value.model_number);
		  formPayload.append('purchase_date', formData.value.purchase_date);
		  formPayload.append('description', formData.value.description);
		  if (formData.value.image1) {
			formPayload.append('image1', formData.value.image1);
		  }
		  formPayload.append('image1_description', formData.value.image1_description);
		  if (formData.value.image2) {
			formPayload.append('image2', formData.value.image2);
		  }
		  formPayload.append('image2_description', formData.value.image2_description);
		  if (formData.value.image3) {
			formPayload.append('image3', formData.value.image3);
		  }
		  formPayload.append('image3_description', formData.value.image3_description);
		  
		  console.log("Payload ready for submission:", formPayload);
		  const response = await axios.post('http://localhost:8000/api/workingReport/equipmentspecifications/', formPayload, {
			headers: {
			  'Content-Type': 'multipart/form-data'
			}
		  });
		  console.log("Form submitted successfully:", response.data);
		  alert('Equipment specification created successfully!');
		  formData.value = {
			name: '',
			manufacturer: '',
			model_number: '',
			purchase_date: '',
			description: '',
			image1: null,
			image1_description: '',
			image2: null,
			image2_description: '',
			image3: null,
			image3_description: ''
		  };
		} catch (error) {
		  console.error("Form submission failed:", error);
		  if (error.response) {
			console.error("Response data:", error.response.data);
			console.error("Response status:", error.response.status);
			console.error("Response headers:", error.response.headers);
		  }
		  alert('Failed to create equipment specification.');
		}
	  };
  
	  const onImageChange = (event, imageField) => {
		const file = event.target.files[0];
		formData.value[imageField] = file;
		console.log(`Image selected for ${imageField}:`, file);
	  };
  
	  const cancelForm = () => {
		formData.value = {
		  name: '',
		  manufacturer: '',
		  model_number: '',
		  purchase_date: '',
		  description: '',
		  image1: null,
		  image1_description: '',
		  image2: null,
		  image2_description: '',
		  image3: null,
		  image3_description: ''
		};
		console.log("Form canceled");
	  };
  
	  return {
		formData,
		submitForm,
		onImageChange,
		cancelForm
	  };
	}
  };
  </script>
  
  <style scoped>
  .form-container {
	width: 210mm;
	height: 297mm;
	margin: 0 auto;
	padding: 20mm;
	box-sizing: border-box;
	border: 1px solid #ddd;
	background-color: white;
  }
  
  form {
	display: flex;
	flex-direction: column;
  }
  
  div {
	margin-bottom: 1em;
  }
  
  label {
	margin-bottom: 0.5em;
	font-weight: bold;
  }
  
  input, textarea {
	padding: 0.5em;
	font-size: 1em;
	width: 100%;
  }
  
  .image-upload {
	margin-bottom: 1em;
  }
  
  .image-row {
	display: flex;
	align-items: center;
  }
  
  .image-row input[type="file"] {
	margin-right: 1em;
  }
  
  button {
	padding: 0.5em;
	font-size: 1em;
	background-color: #4CAF50;
	color: white;
	border: none;
	cursor: pointer;
	margin-right: 0.5em;
  }
  
  button:hover {
	background-color: #45a049;
  }
  
  .form-actions {
	display: flex;
	justify-content: flex-end;
  }
  
  header, footer {
	text-align: center;
	margin-bottom: 1em;
  }
  
  footer p {
	margin-top: 2em;
  }
  </style>
  