<template>
    <Dialog :visible="visible" @hide="hideModal" modal :closable="false">
      <div class="surface-ground px-4 py-8 md:px-6 lg:px-8">
        <div class="p-fluid flex flex-column lg:flex-row">
          <ul class="list-none m-0 p-0 flex flex-row lg:flex-column justify-content-evenly md:justify-content-between lg:justify-content-start mb-5 lg:pr-8 lg:mb-0">
            <li>
              <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
                <i class="pi pi-user md:mr-2"></i>
                <span class="font-medium hidden md:block">Profile</span>
              </a>
            </li>
            <li>
              <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
                <i class="pi pi-cog md:mr-2"></i>
                <span class="font-medium hidden md:block">Account</span>
              </a>
            </li>
            <li>
              <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
                <i class="pi pi-palette md:mr-2"></i>
                <span class="font-medium hidden md:block">Appearance</span>
              </a>
            </li>
            <li>
              <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
                <i class="pi pi-sun md:mr-2"></i>
                <span class="font-medium hidden md:block">Accessibility</span>
              </a>
            </li>
            <li>
              <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
                <i class="pi pi-bell md:mr-2"></i>
                <span class="font-medium hidden md:block">Notifications</span>
              </a>
            </li>
          </ul>
          <div class="surface-card p-5 shadow-2 border-round flex-auto">
            <div class="text-900 font-semibold text-lg mt-3">CE List Entry</div>
            <Divider></Divider>
            <div class="flex gap-5 flex-column-reverse md:flex-row">
              <div class="flex-auto p-fluid">
                <div class="mb-4">
                  <label for="ceListNo" class="block font-medium text-900 mb-2">CeListNo</label>
                  <InputText id="ceListNo" v-model="localEntry.ceListNo" type="text" />
                </div>
                <div class="mb-4">
                  <label for="plant" class="block font-medium text-900 mb-2">Plant</label>
                  <InputText id="plant" v-model="localEntry.plant" type="text" />
                </div>
                <div class="mb-4">
                  <label for="equipment" class="block font-medium text-900 mb-2">Equipment</label>
                  <InputText id="equipment" v-model="localEntry.equipment" type="text" />
                </div>
                <div class="mb-4">
                  <label for="machineName" class="block font-medium text-900 mb-2">Machine Name</label>
                  <InputText id="machineName" v-model="localEntry.machineName" type="text" />
                </div>
                <div>
                  <Button label="Save" icon="pi pi-check" @click="submitEntry" />
                  <Button label="Cancel" icon="pi pi-times" @click="cancelNewEntry" class="p-button-secondary ml-2" />
                </div>
              </div>
              <div class="flex flex-column align-items-center flex-or">
                <span class="font-medium text-900 mb-2">Profile Picture</span>
                <img src="" class="h-10rem w-10rem" />
                <Button type="button" icon="pi pi-pencil" class="p-button-rounded -mt-4"></Button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Dialog>
  </template>
  
  <script setup>
  import { ref, watch, defineEmits, defineProps } from 'vue';
  import InputText from 'primevue/inputtext';
  import Button from 'primevue/button';
  import Dialog from 'primevue/dialog';
  import Divider from 'primevue/divider';
  
  const props = defineProps(['visible', 'statuses', 'entry']);
  const emit = defineEmits(['update:visible', 'submit', 'cancel']);
  
  // 初期化時のエントリデータを確認するログ
  console.log('Props entry data:', props.entry);
  
  const localEntry = ref({ ...props.entry });
  
  // ローカルエントリが初期化されたことを確認するログ
  console.log('Initial localEntry data:', localEntry.value);
  
  const hideModal = () => {
    cancelNewEntry();
  };
  
  const submitEntry = () => {
    // 送信するデータのログ
    console.log('Submitting entry:', localEntry.value);
    emit('submit', localEntry.value);
    emit('update:visible', false);
  };
  
  const cancelNewEntry = () => {
    // キャンセル時の動作を確認するログ
    console.log('Cancelling entry update, reverting changes');
    emit('cancel');
    emit('update:visible', false);
  };
  
  watch(() => props.visible, (newValue) => {
    if (!newValue) {
      // ダイアログが閉じたときにリセットするログ
      console.log('Dialog closed, resetting localEntry data to:', props.entry);
      localEntry.value = { ...props.entry };
    }
  });
  </script>
  
  <style scoped>
  .surface-ground {
    padding: 1rem;
  }
  </style>
  