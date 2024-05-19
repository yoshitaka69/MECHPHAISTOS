<template>
    <div>
      <input type="file" @change="onFileChange" />
      <button @click="uploadFile">アップロード</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        file: null,
        category: 'SpecificCategory',  // クエリパラメータでフィルタリングするカテゴリ
      };
    },
    methods: {
      onFileChange(e) {
        this.file = e.target.files[0];
      },
      uploadFile() {
        const formData = new FormData();
        formData.append('file', this.file);
        axios.post('http://localhost:8000/upload_excel/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          console.log('ファイルが正常にアップロードされました。');
          console.log(response.data);
        })
        .catch(error => {
          console.error('アップロード中にエラーが発生しました：', error.response.data);
        });
      }
    }
  }
  </script>
  