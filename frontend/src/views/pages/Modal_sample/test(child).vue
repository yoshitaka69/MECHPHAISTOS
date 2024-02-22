<template>
      <Dialog v-model:visible="dialogVisible" modal header="Edit Profile" :style="{ width: '25rem' }" @onHide="onClose">
        <span class="p-text-secondary block mb-5">Update your information.</span>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="username" class="font-semibold w-6rem">Username</label>
            <InputText id="username" class="flex-auto" autocomplete="off" />
        </div>
        <div class="flex align-items-center gap-3 mb-5">
            <label for="email" class="font-semibold w-6rem">Email</label>
            <InputText id="Email" class="flex-auto" autocomplete="off" />
        </div>
        <div class="flex justify-content-end gap-2">
            <Button type="button" label="Cancel" severity="secondary" @click="onClose"></Button>
            <Button type="button" label="Save" @click="onSave"></Button>
        </div>
    </Dialog>
</template>


<script setup>
import { defineProps, ref, defineEmits } from 'vue';


const props = defineProps(['visible']);
const emits = defineEmits();
const dialogVisible = ref(props.visible);

// Saveボタンがクリックされた時の処理
const onSave = () => {
  // データの保存処理など

  // モーダルを閉じる
  dialogVisible.value = false;

  // 親コンポーネントに通知
  emits('close');
};


// モーダルが閉じられた時の処理
const onClose = () => {
  // 親コンポーネントに通知
  emits('close');
};

</script>