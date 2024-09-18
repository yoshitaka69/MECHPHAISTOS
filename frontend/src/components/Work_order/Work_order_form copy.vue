<template>
  <!-- Save_Alert コンポーネントをモーダル外に配置し、アラートが画面の上に表示されるようにする -->
  <Save_Alert v-if="showAlert" :type="alertType" :message="alertMessage" @close="showAlert = false" class="fixed-alert" />

  <Dialog :visible="visible" @hide="hideModal" modal :closable="false" style="width: 80vw; z-index: 1000">
      <!-- モーダルのヘッダー -->
      <template #header>
          <div class="flex justify-content-between align-items-center w-full">
              <span class="text-lg font-bold mr-2 ml-auto">Work Order</span>
              <Button icon="pi pi-times" class="p-button-text ml-2" @click="hideModal" />
          </div>
      </template>

      <!-- モーダルのコンテンツ -->
      <div class="surface-ground px-4 py-8 md:px-6 lg:px-8">
          <div class="p-fluid flex flex-column lg:flex-row">
              <ul class="list-none m-0 p-0 flex flex-row lg:flex-column justify-content-evenly md:justify-content-between lg:justify-content-start mb-5 lg:pr-8 lg:mb-0" style="background-color: #e0f7fa">
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
                  <div class="text-900 font-semibold text-lg mt-3 flex align-items-center justify-content-between">
                      <span>Work Order Entry</span>
                      <span v-if="localEntry.workOrderNo" class="text-sm">Work Order No: {{ localEntry.workOrderNo }}</span>

                  </div>
                  <Divider></Divider>
                  <div class="flex gap-5 flex-column-reverse md:flex-row">
                      <div class="flex-auto p-fluid">
                          <div class="mb-4">
                              <label for="title" class="block font-medium text-900 mb-2">Title</label>
                              <InputText id="title" v-model="localEntry.title" :class="{ 'input-error': validationErrors.title }" type="text" class="w-full" />
                          </div>

                          <div class="mb-4">
                              <label for="description" class="block font-medium text-900 mb-2">Description</label>
                              <Textarea id="description" v-model="localEntry.description" type="text" rows="5" :autoResize="true" class="w-full"></Textarea>
                          </div>

                          <div class="flex mb-4 gap-4">
                              <div class="flex-auto">
                                  <label for="plant" class="block font-medium text-900 mb-2">Plant</label>
                                  <Dropdown id="plant" v-model="localEntry.plant" :options="plantOptions" optionLabel="label" optionValue="value" placeholder="Select a Plant" />
                              </div>
                              <div class="flex-auto">
                                  <label for="equipment" class="block font-medium text-900 mb-2">Equipment</label>
                                  <Dropdown id="equipment" v-model="localEntry.equipment" :options="equipmentOptions" optionLabel="label" optionValue="value" placeholder="Select Equipment" />
                              </div>
                          </div>

                          <div class="mb-4">
                              <label class="block font-medium text-900 mb-2">Failure Type</label>
                              <div v-for="type in failureTypes" :key="type.value" class="flex align-items-center">
                                  <Checkbox v-model="localEntry.failureTypes" :value="type.value" class="mr-2 p-checkbox-box" />
                                  <label class="checkbox-label">{{ type.label }}</label>
                              </div>
                          </div>

                          <div class="mb-4">
                              <label class="block font-medium text-900 mb-2">Failure Mode</label>
                              <div v-for="mode in failureModes" :key="mode.value" class="flex align-items-center">
                                  <Checkbox v-model="localEntry.failureModes" :value="mode.value" class="mr-2 p-checkbox-box" />
                                  <label class="checkbox-label">{{ mode.label }}</label>
                              </div>
                          </div>

                          <div class="mb-4">
                              <label for="failureDescription" class="block font-medium text-900 mb-2">Failure Description</label>
                              <Textarea id="failureDescription" v-model="localEntry.failureDescription" type="text" rows="5" :autoResize="true" class="w-full"></Textarea>
                          </div>

                          <div class="mb-4">
                              <label for="failureDate" class="block font-medium text-900 mb-2">Failure Date</label>
                              <InputText id="failureDate" v-model="localEntry.failureDate" type="date" />
                          </div>

                          <div class="mb-4">
                              <label for="status" class="block font-medium text-900 mb-2">Status</label>
                              <Dropdown id="status" v-model="localEntry.status" :options="statuses" optionLabel="label" optionValue="value" placeholder="Select a Status" />
                          </div>

                          <div class="mb-4">
                              <label for="registrationDate" class="block font-medium text-900 mb-2">Registration Date</label>
                              <InputText id="registrationDate" v-model="localEntry.registrationDate" type="date" />
                          </div>

                          <div class="flex justify-content-end">
                              <Button label="Save" icon="pi pi-check" @click="submitEntry" class="mr-2" />
                              <Button label="Cancel" icon="pi pi-times" @click="cancelNewEntry" class="p-button-secondary" />
                          </div>
                      </div>
                      <div class="flex flex-column align-items-center flex-or">
                          <span class="font-medium text-900 mb-2">Picture 1</span>
                          <img :src="pictureSrc1" class="h-14rem w-14rem border-black mb-4" @click="enlargeImage1" />
                          <Button type="button" icon="pi pi-pencil" class="p-button-rounded -mt-4"></Button>

                          <span class="font-medium text-900 mb-2">Picture 2</span>
                          <img :src="pictureSrc2" class="h-14rem w-14rem border-black mb-4" @click="enlargeImage2" />
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

  <Dialog v-model:visible="imageDialogVisible1" modal :closable="false">
      <img :src="pictureSrc1" class="w-full h-auto" />
      <Button label="Close" icon="pi pi-times" @click="imageDialogVisible1 = false" class="p-button-secondary mt-2" />
  </Dialog>

  <Dialog v-model:visible="imageDialogVisible2" modal :closable="false">
      <img :src="pictureSrc2" class="w-full h-auto" />
      <Button label="Close" icon="pi pi-times" @click="imageDialogVisible2 = false" class="p-button-secondary mt-2" />
  </Dialog>
</template>




<script setup>
import { ref, watch, onMounted } from 'vue';
import axios from 'axios';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import Dialog from 'primevue/dialog';
import Divider from 'primevue/divider';
import Checkbox from 'primevue/checkbox';
import noImage from '@/assets/no_image.jpg';
import Save_Alert from '@/components/Alert/Save_Alert.vue'; // Save_Alert コンポーネントをインポート
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

const props = defineProps(['visible', 'statuses', 'entry']);
const emit = defineEmits(['update:visible', 'submit', 'cancel']);

const localEntry = ref({
  title: '',
  plant: null,
  equipment: null,
  failureTypes: [],
  failureModes: [],
  failureDescription: '',
  failureDate: null,
  description: '',
  status: null,
  registrationDate: null
});

const failureTypes = ref([
  { label: 'Electrical', value: 'electrical' },
  { label: 'Mechanical', value: 'mechanical' },
  { label: 'Software', value: 'software' },
  { label: 'Human Error', value: 'human_error' }
]);

const failureModes = ref([
  { label: 'Wear', value: 'wear' },
  { label: 'Fatigue Failure', value: 'fatigue_failure' },
  { label: 'Corrosion', value: 'corrosion' },
  { label: 'Overheating', value: 'overheating' },
  { label: 'Inadequate Lubrication', value: 'inadequate_lubrication' },
  { label: 'Seal Failure', value: 'seal_failure' },
  { label: 'Overload', value: 'overload' },
  { label: 'Vibration', value: 'vibration' },
  { label: 'Electrical Insulation Failure', value: 'electrical_insulation_failure' },
  { label: 'Short Circuit', value: 'short_circuit' },
  { label: 'Mechanical Shock', value: 'mechanical_shock' },
  { label: 'Thermal Fatigue', value: 'thermal_fatigue' },
  { label: 'Cavitation', value: 'cavitation' },
  { label: 'Frictional Wear', value: 'frictional_wear' },
  { label: 'Stress Corrosion Cracking', value: 'stress_corrosion_cracking' },
  { label: 'Erosion', value: 'erosion' },
  { label: 'Oxidation', value: 'oxidation' },
  { label: 'Cable Breakage', value: 'cable_breakage' },
  { label: 'Bearing Failure', value: 'bearing_failure' },
  { label: 'Electronic Component Failure', value: 'electronic_component_failure' }
]);

const pictureSrc1 = ref(noImage); // 1枚目の画像を初期状態として設定
const pictureSrc2 = ref(noImage); // 2枚目の画像を初期状態として設定
const imageDialogVisible1 = ref(false);
const imageDialogVisible2 = ref(false);
const currentTab = ref('form');
const sampleHistory = ref([]);

const plantOptions = ref([]); // プラントの選択肢を格納する状態
const equipmentOptions = ref([]); // 装置の選択肢を格納する状態

// アラートの状態管理
const showAlert = ref(false); // アラートの表示状態
const alertType = ref(''); // アラートの種類 ('success' または 'error')
const alertMessage = ref(''); // アラートのメッセージ

const validationErrors = ref({});
const submitEntry = async () => {
  // バリデーションを初期化
  validationErrors.value = {};

  // 未入力チェック
  if (!localEntry.value.title) validationErrors.value.title = true;

  // 未入力があれば、処理を中断し赤枠を表示
  if (Object.keys(validationErrors.value).length > 0) {
      showAlert.value = true;
      alertType.value = 'error';
      alertMessage.value = 'Please fill out the required fields!';
      return;
  }

  try {
      const postData = {
          title: localEntry.value.title,
          plant: localEntry.value.plant,
          equipment: localEntry.value.equipment,
          failureTypes: localEntry.value.failureTypes,
          failureModes: localEntry.value.failureModes,
          failureDescription: localEntry.value.failureDescription,
          failureDate: localEntry.value.failureDate,
          description: localEntry.value.description,
          status: localEntry.value.status,
          registrationDate: localEntry.value.registrationDate || new Date().toISOString().split('T')[0],
          companyCode: useUserStore().companyCode
      };

      // ポストデータをコンソールに出力
      console.log('Post Data:', postData);

      // POSTリクエストを送信
      const response = await axios.post('http://127.0.0.1:8000/api/workOrder/workOrder/', postData);

      // 受け取ったworkOrderNoを表示するためにlocalEntryに設定
      localEntry.value.workOrderNo = response.data.workOrderNo;

      alertType.value = 'success';
      alertMessage.value = 'Data saved successfully! Work Order No: ' + localEntry.value.workOrderNo;
      showAlert.value = true;

      emit('submit', localEntry.value);
      emit('update:visible', false);
  } catch (error) {
      alertType.value = 'error';
      alertMessage.value = 'Error saving data!';
      showAlert.value = true;

      console.error('Error during submitEntry execution:', error.response ? error.response.data : error.message);
  }
};



const hideModal = () => {
  cancelNewEntry();
};

const cancelNewEntry = () => {
  emit('cancel');
  emit('update:visible', false);
};

const enlargeImage1 = () => {
  imageDialogVisible1.value = true;
};

const enlargeImage2 = () => {
  imageDialogVisible2.value = true;
};

watch(
  () => props.visible,
  (newValue) => {
      if (!newValue) {
          localEntry.value = { ...(props.entry || {}) };
      }
  }
);
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
  border: 1px solid black;
  height: 14rem; /* サイズを2回り大きく */
  width: 14rem; /* サイズを2回り大きく */
}

:deep(.p-dialog) {
  max-width: 80vw;
  width: 100%;
  border: 1px solid black; /* 黒色の枠線を追加 */
}

input,
textarea,
select,
.p-inputtext,
.p-dropdown,
.p-textarea {
  border: 1px solid black; /* 入力フォームの黒色の枠線 */
}

.history-list {
  list-style-type: none;
  padding: 0;
}

.checkbox-label {
  font-size: 1.5rem; /* フォントを2回り大きく */
}

.p-checkbox-box {
  width: 2rem; /* チェックボックスの大きさを2回り大きく */
  height: 2rem; /* チェックボックスの高さを2回り大きく */
}

/* アラートがモーダルの上に表示されるように、上部に固定 */
.save-alert {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 9999; /* モーダルよりも前面に表示するためにz-indexを高く設定 */
}

/* アラートを画面上に固定し、モーダルより前面に表示 */
.fixed-alert {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1100; /* モーダルのz-indexを超える値に設定 */
}

/* モーダルのスタイルを調整 */
.p-dialog {
  z-index: 1000; /* モーダルのz-indexを1000に設定 */
}

.input-error {
  border: 2px solid red !important; /* 赤い枠線 */
}

.p-invalid {
  border: 1px solid red;
}
.p-error {
  color: red;
}

</style>
