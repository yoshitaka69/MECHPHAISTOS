<template>
  <div class="report-container">
    <div class="header">
      <h1>作業報告書</h1>
    </div>
    <form @submit.prevent="handleSubmit" class="report-form">
      <div>
        <label for="date">日付:</label>
        <input type="date" v-model="form.date" required />
      </div>
      <div>
        <label for="equipment_number">設備番号:</label>
        <input type="text" v-model="form.equipment_number" required />
      </div>
      <div>
        <label for="task_number">タスク番号:</label>
        <input type="text" v-model="form.task_number" required />
      </div>
      <div>
        <label for="image">画像登録:</label>
        <input type="file" @change="handleImageUpload" required />
      </div>
      <div>
        <label for="description">概要説明:</label>
        <textarea v-model="form.description" required></textarea>
      </div>
      <div class="form-actions">
        <button type="submit">保存</button>
        <button type="button" @click="handleCancel">キャンセル</button>
      </div>
    </form>
    <button @click="generatePDF" class="pdf-button">PDF出力</button>
    <div class="footer">
      <p>Footer Content</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        date: '',
        equipment_number: '',
        task_number: '',
        image: null,
        description: ''
      }
    };
  },
  methods: {
    handleImageUpload(event) {
      this.form.image = event.target.files[0];
    },
    handleSubmit() {
      const formData = new FormData();
      formData.append('date', this.form.date);
      formData.append('equipment_number', this.form.equipment_number);
      formData.append('task_number', this.form.task_number);
      formData.append('image', this.form.image);
      formData.append('description', this.form.description);

      axios.post('/api/reports/', formData)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    },
    handleCancel() {
      this.form = {
        date: '',
        equipment_number: '',
        task_number: '',
        image: null,
        description: ''
      };
    },
    generatePDF() {
      // PDF生成のロジックをここに追加
    }
  }
};
</script>


<style scoped>
.report-container {
  width: 210mm; /* A4 width */
  height: 297mm; /* A4 height */
  padding: 20mm;
  background-color: white;
  border: 1px solid #ddd;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.header, .footer {
  text-align: center;
  padding: 10px;
  background-color: #f7f7f7;
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
}

.header {
  border-bottom: none;
}

.footer {
  border-top: none;
}

.report-form {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.report-form > div {
  margin-bottom: 1em;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
}

.pdf-button {
  align-self: flex-end;
  margin-top: 20px;
}
</style>
