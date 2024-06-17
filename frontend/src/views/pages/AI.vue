<template>
	<div>
	  <h1>Image Recognition</h1>
	  <input type="file" @change="uploadImage" />
	  <div v-if="prediction">
		<h2>Prediction: {{ prediction }}</h2>
		<img :src="imageUrl" alt="Uploaded Image" />
	  </div>
	  <div v-if="error">
		<h2>Error: {{ error }}</h2>
	  </div>
	</div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
	data() {
	  return {
		prediction: null,
		imageUrl: null,
		error: null,
	  };
	},
	methods: {
	  async uploadImage(event) {
		this.error = null;
		const file = event.target.files[0];
		const formData = new FormData();
		formData.append('image', file);
  
		try {
		  const response = await axios.post('http://localhost:8000/api/images/', formData, {
			headers: {
			  'Content-Type': 'multipart/form-data',
			},
		  });
  
		  this.prediction = response.data.predicted_label;
		  this.imageUrl = 'http://localhost:8000' + response.data.image;
		} catch (err) {
		  this.error = err.response ? err.response.data.error : err.message;
		}
	  },
	},
  };
  </script>
  