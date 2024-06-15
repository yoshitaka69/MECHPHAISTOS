<template>
	<div>
	  <h1>Image Recognition</h1>
	  <input type="file" @change="uploadImage" />
	  <div v-if="prediction">
		<h2>Prediction: {{ prediction }}</h2>
	  </div>
	</div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
	data() {
	  return {
		prediction: null,
	  };
	},
	methods: {
	  async uploadImage(event) {
		const file = event.target.files[0];
		const formData = new FormData();
		formData.append('image', file);
  
		const response = await axios.post('http://localhost:8000/api/images/', formData, {
		  headers: {
			'Content-Type': 'multipart/form-data',
		  },
		});
  
		this.prediction = response.data.predicted_label;
	  },
	},
  };
  </script>
  