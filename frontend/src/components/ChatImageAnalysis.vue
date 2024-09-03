<template>
    <div class="main-content">
      <h1>Chatbot and Image Analysis</h1>
  
      <div id="chat">
        <h2>Chat with AI</h2>
        <input type="text" v-model="chatInput" placeholder="Type your question here...">
        <button @click="sendChatMessage">Send</button>
        <div class="chat-container">
          <div v-for="message in chatMessages" :key="message.id" :class="message.type">
            {{ message.text }}
          </div>
        </div>
      </div>
  
      <div id="image">
        <h2>Image Analysis</h2>
        <input type="file" @change="onFileChange">
        <button @click="uploadImage">Upload</button>
        <div>{{ imageOutput }}</div>
      </div>
    </div>
  </template>
  
  <script>
  let messageId = 0;
  
  export default {
    data() {
      return {
        chatInput: '',
        chatMessages: [],
        imageFile: null,
        imageOutput: '',
      };
    },
    methods: {
      async sendChatMessage() {
        const userInput = this.chatInput;
        this.chatMessages.push({ id: messageId++, text: userInput, type: 'user' });
        const response = await fetch('/api/chat/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ input: userInput }),
        });
        const data = await response.json();
        this.chatMessages.push({ id: messageId++, text: data.response, type: 'bot' });
        this.chatInput = '';
      },
      onFileChange(event) {
        this.imageFile = event.target.files[0];
      },
      async uploadImage() {
        if (!this.imageFile) {
          this.imageOutput = 'Please select an image file first.';
          return;
        }
        const formData = new FormData();
        formData.append('image', this.imageFile);
  
        const response = await fetch('/api/image-analysis/', {
          method: 'POST',
          body: formData,
        });
        const data = await response.json();
        if (data.error) {
          this.imageOutput = 'Error: ' + data.error;
        } else {
          this.imageOutput = 'Predicted Label: ' + data.predicted_label;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .main-content {
    margin-left: 220px;
    padding: 20px;
  }
  
  .chat-container {
    margin-top: 20px;
    max-width: 600px;
  }
  
  .user, .bot {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
    width: fit-content;
    max-width: 80%;
  }
  
  .user {
    background-color: #dcf8c6;
    align-self: flex-end;
    margin-left: auto;
  }
  
  .bot {
    background-color: #f1f0f0;
    align-self: flex-start;
  }
  
  button {
    margin-left: 10px;
  }
  </style>
  