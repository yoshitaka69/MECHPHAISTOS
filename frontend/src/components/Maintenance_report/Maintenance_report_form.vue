<template>
  <div class="form-container">
    <h1 class="title">Maintenance working report</h1>
    <div class="pages">
      <div v-for="(page, index) in pages" :key="index" class="page">
        <form @submit.prevent="submitForm">
          <template v-if="index === 0">
            <div class="form-group">
              <label for="taskName">Task Name:</label>
              <InputText v-model="page.taskName" required />
            </div>
            <div class="form-group">
              <label for="date">Date:</label>
              <Calendar v-model="page.date" dateFormat="yy-mm-dd" required />
            </div>
            <div class="form-group">
              <label for="equipment">Equipment:</label>
              <InputText v-model="page.equipment" required />
            </div>
            <div class="form-group">
              <label for="reporter">Reporter:</label>
              <InputText v-model="page.reporter" required />
            </div>
            <div class="form-group">
              <label for="pmType">PM Type:</label>
              <InputText v-model="page.pmType" required />
            </div>
            <div class="form-group">
              <label for="tag">Tag:</label>
              <InputText v-model="page.tag" required />
            </div>
            <div class="form-group">
              <label for="background">Background:</label>
              <InputText v-model="page.background" required />
            </div>
            <div class="form-group">
              <label for="cause">Cause:</label>
              <InputText v-model="page.cause" required />
            </div>
            <div class="form-group">
              <label for="maintenanceCategory">Maintenance Category:</label>
              <InputText v-model="page.maintenanceCategory" required />
            </div>
          </template>
          <template v-else>
            <div class="image-notes-container">
              <div v-for="n in 3" :key="n" class="image-notes-group">
                <div class="form-group-inline">
                  <div class="form-group">
                    <label for="imageUpload">Upload Image:</label>
                    <div class="image-box">
                      <div v-if="!page.images[n-1]" class="no-image">no image</div>
                      <img v-if="page.images[n-1]" :src="page.images[n-1]" alt="Uploaded Image" class="image-preview" />
                    </div>
                    <FileUpload mode="basic" @select="(e) => onFileChange(e, index, n)" />
                  </div>
                  <div class="form-group">
                    <label for="additionalNotes">Additional Notes:</label>
                    <Textarea v-model="page.additionalNotes[n-1]" rows="12" cols="50" autoResize />
                  </div>
                </div>
              </div>
            </div>
          </template>
        </form>
        <div class="page-number">Page {{ index + 1 }}</div>
      </div>
    </div>
    <div class="buttons">
      <Button label="Add Page" icon="pi pi-plus" @click="addPage" />
      <Button label="Submit" icon="pi pi-check" @click="submitForm" />
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

const pages = ref([
  { taskName: '', date: '', equipment: '', reporter: '', pmType: '', tag: '', background: '', cause: '', maintenanceCategory: '' },
  { taskName: '', date: '', equipment: '', reporter: '', pmType: '', images: ['', '', ''], additionalNotes: ['', '', ''] },
]);

const addPage = () => {
  pages.value.push({ taskName: '', date: '', equipment: '', reporter: '', pmType: '', images: ['', '', ''], additionalNotes: ['', '', ''] });
};

const submitForm = () => {
  console.log('Form submitted', pages.value);
  // フォームの送信処理をここに追加
};

const onFileChange = (event, index, imageIndex) => {
  const file = event.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      pages.value[index].images[imageIndex-1] = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};
</script>

<style>
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 16px;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
}

.pages {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
}

.page {
  width: 210mm; /* A4 width */
  height: 297mm; /* A4 height */
  border: 1px solid #000;
  padding: 10mm; /* Reduce padding to increase usable area */
  box-sizing: border-box;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 16px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* Adjust to evenly space out */
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
  height: calc((100% - 30px) / 3); /* Adjust height considering padding */
}

.image-box {
  width: 100%;
  height: 250px; /* Increase height */
  border: 1px solid #000;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
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
  object-fit: contain; /* Adjust to contain image within box */
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
