<template>
	<div class="container">
	  <h1>音声認識フォーム</h1>
	  <div class="controls">
		<button @click="startRecording">Start Recording</button>
		<button @click="stopRecording">Stop Recording</button>
	  </div>
	  <div class="form">
		<p>{{ transcript }}</p>
	  </div>
	</div>
  </template>
  
  <script>
  export default {
	data() {
	  return {
		transcript: '',
		mediaRecorder: null,
		socket: null,
	  };
	},
	methods: {
	  async startRecording() {
		console.log("Starting recording...");
		try {
		  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
		  this.mediaRecorder = new MediaRecorder(stream);
		  this.mediaRecorder.start();
  
		  this.socket = new WebSocket('ws://localhost:8000/ws/audio/');
		  this.socket.onopen = () => console.log("WebSocket connection opened.");
		  this.socket.onerror = (error) => console.error("WebSocket error:", error);
		  this.socket.onclose = () => console.log("WebSocket connection closed.");
		  
		  this.mediaRecorder.ondataavailable = (event) => {
			if (event.data.size > 0 && this.socket.readyState === WebSocket.OPEN) {
			  console.log("Sending audio data...");
			  this.socket.send(event.data);
			}
		  };
  
		  this.socket.onmessage = (event) => {
			const data = JSON.parse(event.data);
			this.transcript = data.transcript;
			console.log("Received transcript:", data.transcript);
		  };
		} catch (error) {
		  console.error("Error starting recording:", error);
		}
	  },
	  stopRecording() {
		console.log("Stopping recording...");
		if (this.mediaRecorder) {
		  this.mediaRecorder.stop();
		}
		if (this.socket) {
		  this.socket.close();
		}
	  }
	}
  };
  </script>
  
  <style scoped>
  .container {
	width: 210mm;
	height: 297mm;
	padding: 20mm;
	border: 1px solid #ccc;
	background-color: #fff;  /* 背景を白に設定 */
	margin: auto;
  }
  
  h1 {
	text-align: center;
	margin-bottom: 20px;
  }
  
  .controls {
	text-align: center;
	margin-bottom: 20px;
  }
  
  button {
	margin: 0 10px;
	padding: 10px 20px;
	font-size: 16px;
  }
  
  .form {
	border: 1px solid #ccc;
	padding: 10mm;
	height: 200mm;
	overflow-y: auto;
	background-color: #fff;  /* 背景を白に設定 */
  }
  
  p {
	font-size: 16px;
	line-height: 1.5;
	white-space: pre-wrap; /* Preserve whitespace and newlines */
  }
  </style>
  