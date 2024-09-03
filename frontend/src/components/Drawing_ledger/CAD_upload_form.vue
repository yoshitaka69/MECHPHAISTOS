<template>
  <Dialog
    header="Upload CAD File"
    :visible="visible"
    :modal="true"
    :closable="false"
    :style="{ width: '50vw' }"
    @update:visible="updateVisible"
  >
    <form @submit.prevent="submitForm">
      <div class="p-fluid">
        <div class="p-field">
          <label for="name">File Name</label>
          <InputText v-model="entry.name" id="name" required />
        </div>
        <div class="p-field">
          <label for="file">Select File</label>
          <InputText type="file" @change="onFileChange" id="file" required />
        </div>
        <div class="p-field">
          <label for="uploaded_by">Uploaded By</label>
          <InputText v-model="entry.uploaded_by" id="uploaded_by" required />
        </div>
      </div>
      <div class="p-d-flex p-jc-end">
        <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="cancelForm" />
        <Button label="Upload" icon="pi pi-check" class="p-ml-2" type="submit" />
      </div>
    </form>
  </Dialog>
</template>

<script setup>
import { ref } from 'vue';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';

const props = defineProps({
  visible: Boolean,
  entry: Object,
});

const emit = defineEmits(['update:visible', 'submit', 'cancel']);

const updateVisible = (value) => {
  emit('update:visible', value);
};

const onFileChange = (event) => {
  props.entry.file = event.target.files[0];
};

const submitForm = () => {
  emit('submit', props.entry);
};

const cancelForm = () => {
  emit('update:visible', false);
  emit('cancel');
};
</script>

<style scoped>
.p-field {
  margin-bottom: 1rem;
}

.p-dialog {
  max-width: 50vw;
}

.p-d-flex {
  display: flex;
}

.p-jc-end {
  justify-content: flex-end;
}

.p-ml-2 {
  margin-left: 0.5rem;
}
</style>
