<template>
  <Dialog :visible="visible" @hide="hideModal" modal :closable="false" style="width: 70vw;">
    <div class="surface-ground px-4 py-8 md:px-6 lg:px-8">
      <div class="p-fluid flex flex-column lg:flex-row">
        <ul class="list-none m-0 p-0 flex flex-row lg:flex-column justify-content-evenly md:justify-content-between lg:justify-content-start mb-5 lg:pr-8 lg:mb-0" style="background-color: #e0f7fa;">
          <li @click="currentTab = 'form'">
            <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
              <i class="pi pi-file md:mr-2"></i>
              <span class="font-medium hidden md:block">Work Order Form</span>
            </a>
          </li>
          <li @click="currentTab = 'history'">
            <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
              <i class="pi pi-clock md:mr-2"></i>
              <span class="font-medium hidden md:block">History</span>
            </a>
          </li>
        </ul>
        <div v-if="currentTab === 'form'" class="surface-card p-5 shadow-2 border-round flex-auto">
          <div class="text-900 font-semibold text-lg mt-3">Work Order Entry</div>
          <Divider></Divider>
          <div class="flex gap-5 flex-column-reverse md:flex-row">
            <div class="flex-auto p-fluid">
              <div class="flex mb-4 gap-4">
                <div class="flex-auto">
                  <label for="plant" class="block font-medium text-900 mb-2">Plant</label>
                  <InputText id="plant" v-model="localEntry.plant" type="text" />
                </div>
                <div class="flex-auto">
                  <label for="equipment" class="block font-medium text-900 mb-2">Equipment</label>
                  <InputText id="equipment" v-model="localEntry.equipment" type="text" />
                </div>
              </div>
              <div class="mb-4">
                <label class="block font-medium text-900 mb-2">Failure Type</label>
                <div v-for="type in failureTypes" :key="type.value" class="flex align-items-center">
                  <Checkbox v-model="localEntry.failureTypes" :value="type.value" class="mr-2" />
                  <label>{{ type.label }}</label>
                </div>
              </div>
              <div class="mb-4">
                <label class="block font-medium text-900 mb-2">Failure Mode</label>
                <div v-for="mode in failureModes" :key="mode.value" class="flex align-items-center">
                  <Checkbox v-model="localEntry.failureModes" :value="mode.value" class="mr-2" />
                  <label>{{ mode.label }}</label>
                </div>
              </div>
              <div class="mb-4">
                <label for="failureDescription" class="block font-medium text-900 mb-2">Failure Description</label>
                <Textarea id="failureDescription" v-model="localEntry.failureDescription" type="text" rows="5" :autoResize="true"></Textarea>
              </div>
              <div class="mb-4">
                <label for="failureDate" class="block font-medium text-900 mb-2">Failure Date</label>
                <InputText id="failureDate" v-model="localEntry.failureDate" type="date" />
              </div>
              <div class="mb-4">
                <label for="description" class="block font-medium text-900 mb-2">Description</label>
                <Textarea id="description" v-model="localEntry.description" type="text" rows="5" :autoResize="true"></Textarea>
              </div>
              <div class="mb-4">
                <label for="status" class="block font-medium text-900 mb-2">Status</label>
                <Dropdown id="status" v-model="localEntry.status" :options="statuses" optionLabel="label" optionValue="value" placeholder="Select a Status" />
              </div>
              <div class="flex justify-content-end">
                <Button label="Save" icon="pi pi-check" @click="submitEntry" class="mr-2" />
                <Button label="Cancel" icon="pi pi-times" @click="cancelNewEntry" class="p-button-secondary" />
              </div>
            </div>
            <div class="flex flex-column align-items-center flex-or">
              <span class="font-medium text-900 mb-2">Picture</span>
              <img :src="pictureSrc" class="h-10rem w-10rem border-black" @click="enlargeImage" />
              <Button type="button" icon="pi pi-pencil" class="p-button-rounded -mt-4"></Button>
            </div>
          </div>
        </div>

        <div v-if="currentTab === 'history'" class="surface-card p-5 shadow-2 border-round flex-auto">
          <div class="text-900 font-semibold text-lg mt-3">Work Order History</div>
          <Divider></Divider>
          <ul>
            <li v-for="history in sampleHistory" :key="history.id" class="mb-2">
              <div class="flex justify-content-between">
                <span>{{ history.date }}</span>
                <span>{{ history.workOrderNo }}</span>
                <span>{{ history.status }}</span>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </Dialog>

  <Dialog v-model:visible="imageDialogVisible" modal :closable="false">
    <img :src="pictureSrc" class="w-full h-auto" />
    <Button label="Close" icon="pi pi-times" @click="imageDialogVisible = false" class="p-button-secondary mt-2" />
  </Dialog>
</template>

<script setup>
import { ref, watch, defineEmits, defineProps } from 'vue';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import Dialog from 'primevue/dialog';
import Divider from 'primevue/divider';
import Checkbox from 'primevue/checkbox';
import noImage from '@/assets/no_image.jpg';  // 画像をimportする

const props = defineProps(['visible', 'statuses', 'entry']);
const emit = defineEmits(['update:visible', 'submit', 'cancel']);

const localEntry = ref({ ...props.entry });
const failureTypes = ref([
  { label: 'Electrical', value: 'electrical' },
  { label: 'Mechanical', value: 'mechanical' },
  { label: 'Software', value: 'software' },
  { label: 'Human Error', value: 'human_error' },
]);

const failureModes = ref([
  { label: 'Overload', value: 'overload' },
  { label: 'Wear', value: 'wear' },
  { label: 'Corrosion', value: 'corrosion' },
  { label: 'Fatigue', value: 'fatigue' },
]);

const pictureSrc = ref(noImage);  // 画像を初期状態として設定
const imageDialogVisible = ref(false);
const currentTab = ref('form');
const sampleHistory = ref([
  { id: 1, date: '2024-08-01', workOrderNo: 'WO-001', status: 'Completed' },
  { id: 2, date: '2024-07-28', workOrderNo: 'WO-002', status: 'Ongoing' },
  { id: 3, date: '2024-07-20', workOrderNo: 'WO-003', status: 'Delayed' },
]);

const hideModal = () => {
  cancelNewEntry();
};

const submitEntry = () => {
  emit('submit', localEntry.value);
  emit('update:visible', false);
};

const cancelNewEntry = () => {
  emit('cancel');
  emit('update:visible', false);
};

const enlargeImage = () => {
  imageDialogVisible.value = true;
};

watch(() => props.visible, (newValue) => {
  if (!newValue) {
    localEntry.value = { ...props.entry };
  }
});
</script>

<style scoped>
.surface-ground {
  padding: 1rem;
}

.flex-or {
  margin-top: 1rem;
}

img {
  cursor: pointer;
  border: 1px solid black; /* 黒い細い枠線を追加 */
}

:deep(.p-dialog) {
  max-width: 70vw;
}

.history-list {
  list-style-type: none;
  padding: 0;
}
</style>
