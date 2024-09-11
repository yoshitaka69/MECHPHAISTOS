<template>
    <Dialog :visible="visible" @hide="hideModal" modal :closable="false" style="width: 70vw">
      <template #header>
        <div class="flex justify-content-between align-items-center">
          <span class="text-lg font-bold">Work Order</span>
          <Button icon="pi pi-times" class="p-button-text" @click="hideModal" />
        </div>
      </template>
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
              <span v-if="workOrderNo" class="text-sm">Work Order No: {{ workOrderNo }}</span>
            </div>
            <Divider></Divider>
            <div class="flex gap-5 flex-column-reverse md:flex-row">
              <div class="flex-auto p-fluid">
                <div class="mb-4">
                  <label for="title" class="block font-medium text-900 mb-2">Title</label>
                  <InputText id="title" v-model="localEntry.title" type="text" class="w-full" />
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
                  <Textarea id="failureDescription" v-model="localEntry.failureDescription" type="text" rows="5" :autoResize="true" class="w-full"></Textarea>
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
                <img :src="pictureSrc1" class="h-10rem w-10rem border-black mb-4" @click="enlargeImage1" />
                <Button type="button" icon="pi pi-pencil" class="p-button-rounded -mt-4"></Button>
  
                <span class="font-medium text-900 mb-2">Picture 2</span>
                <img :src="pictureSrc2" class="h-10rem w-10rem border-black mb-4" @click="enlargeImage2" />
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
  import { ref, watch, onMounted, defineEmits, defineProps } from 'vue';
  import axios from 'axios';
  import InputText from 'primevue/inputtext';
  import Textarea from 'primevue/textarea';
  import Button from 'primevue/button';
  import Dropdown from 'primevue/dropdown';
  import Dialog from 'primevue/dialog';
  import Divider from 'primevue/divider';
  import Checkbox from 'primevue/checkbox';
  import noImage from '@/assets/no_image.jpg'; // 画像をimportする
  import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
  
  const props = defineProps(['visible', 'statuses', 'entry']);
  const emit = defineEmits(['update:visible', 'submit', 'cancel']);
  
  const localEntry = ref({ ...props.entry || {} });
  const failureTypes = ref([
    { label: 'Electrical', value: 'electrical' },
    { label: 'Mechanical', value: 'mechanical' },
    { label: 'Software', value: 'software' },
    { label: 'Human Error', value: 'human_error' }
  ]);
  
  const failureModes = ref([
    { label: 'Overload', value: 'overload' },
    { label: 'Wear', value: 'wear' },
    { label: 'Corrosion', value: 'corrosion' },
    { label: 'Fatigue', value: 'fatigue' }
  ]);
  
  const pictureSrc1 = ref(noImage); // 1枚目の画像を初期状態として設定
  const pictureSrc2 = ref(noImage); // 2枚目の画像を初期状態として設定
  const imageDialogVisible1 = ref(false);
  const imageDialogVisible2 = ref(false);
  const currentTab = ref('form');
  const sampleHistory = ref([
    { id: 1, date: '2024-08-01', workOrderNo: 'WO-001', status: 'Completed' },
    { id: 2, date: '2024-07-28', workOrderNo: 'WO-002', status: 'Ongoing' },
    { id: 3, date: '2024-07-20', workOrderNo: 'WO-003', status: 'Delayed' }
  ]);
  
  const plantOptions = ref([]); // プラントの選択肢を格納する状態
  const equipmentOptions = ref([]); // 装置の選択肢を格納する状態
  const workOrderNo = ref(''); // Work Order Noを格納する状態
  
  // PiniaストアからcompanyCodeを取得
  const userStore = useUserStore();
  const companyCode = userStore.companyCode;
  
  // axiosを使用してプラントのリストを取得するメソッド
  const fetchPlantOptions = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/ceList/ceListByCompany/', {
        params: {
          companyCode: companyCode // クエリパラメータとしてcompanyCodeを渡す
        }
      });
  
      const companyData = response.data.find((company) => company.companyCode === companyCode);
      if (companyData) {
        console.log('Company data found:', companyData); // 成功時のコンソールログ
        plantOptions.value = [...new Set(companyData.ceList.map((item) => item.plant))].map((plant) => ({
          label: `Plant ${plant}`, // 表示名
          value: plant // 実際の値
        }));
        console.log('Plant options:', plantOptions.value);
      } else {
        console.log('No data found for companyCode:', companyCode);
      }
    } catch (error) {
      console.error('Failed to fetch plant options:', error); // エラー時のコンソールログ
    }
  };
  
  // axiosを使用して装置のリストを取得するメソッド
  const fetchEquipmentOptions = async (selectedPlant) => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/ceList/ceListByCompany/', {
        params: {
          companyCode: companyCode, // クエリパラメータとしてcompanyCodeを渡す
          plant: selectedPlant // 選択されたplantをクエリパラメータとして渡す
        }
      });
  
      const companyData = response.data.find((company) => company.companyCode === companyCode);
      if (companyData) {
        console.log('Selected plant:', selectedPlant); // 成功時のコンソールログ
        equipmentOptions.value = companyData.ceList
          .filter((item) => item.plant === selectedPlant)
          .map((equipment) => ({
            label: `Equipment ${equipment.equipment}`, // 表示名
            value: equipment.equipment // 実際の値
          }));
        console.log('Equipment options:', equipmentOptions.value);
      } else {
        console.log('No data found for companyCode and selected plant:', companyCode, selectedPlant);
      }
    } catch (error) {
      console.error('Failed to fetch equipment options:', error); // エラー時のコンソールログ
    }
  };
  
  // axiosを使用してWork Order Noを取得し、最大値+1を設定するメソッド
  const fetchAndIncrementWorkOrderNo = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/workOrder/workOrderByCompany/', {
        params: {
          companyCode: companyCode // クエリパラメータとしてcompanyCodeを渡す
        }
      });
  
      const companyData = response.data.find((company) => company.companyCode === companyCode);
      if (companyData && companyData.workOrderList.length > 0) {
        const maxWorkOrderNo = Math.max(...companyData.workOrderList.map((order) => parseInt(order.workOrderNo, 10)));
        workOrderNo.value = (maxWorkOrderNo + 1).toString();
        console.log('Incremented Work Order No:', workOrderNo.value); // 成功時のコンソールログ
      } else {
        workOrderNo.value = '1'; // データがない場合は '1' を初期値とする
        console.log('No work order found, setting Work Order No to 1');
      }
    } catch (error) {
      console.error('Failed to fetch and increment work order no:', error); // エラー時のコンソールログ
    }
  };
  
  // コンポーネントがマウントされたときにプラントのリストとWork Order Noを取得
  onMounted(() => {
    fetchPlantOptions();
    fetchAndIncrementWorkOrderNo();
  });
  
  // plantが選択されたときにequipmentのリストを取得
  watch(
    () => localEntry.value.plant,
    (newPlant) => {
      if (newPlant) {
        fetchEquipmentOptions(newPlant);
      }
    }
  );
  
  // SaveボタンがクリックされたときにPOSTリクエストを送信
  const submitEntry = async () => {
      try {
          const postData = {
              companyCode: companyCode,
              plant: localEntry.value.plant || null,
              equipment: localEntry.value.equipment || null,
              workOrderNo: workOrderNo.value,
              workOrderDesc: localEntry.value.workOrderDesc || null,
              status: localEntry.value.status || null,
              title: localEntry.value.title || null,
              failureTypes: localEntry.value.failureTypes && localEntry.value.failureTypes.length > 0 ? localEntry.value.failureTypes : null,
              failureModes: localEntry.value.failureModes && localEntry.value.failureModes.length > 0 ? localEntry.value.failureModes : null,
              failureDescription: localEntry.value.failureDescription || null,
              failureDate: localEntry.value.failureDate || null,
              description: localEntry.value.description || null,
              registrationDate: localEntry.value.registrationDate || null  // 登録日を追加
          };
  
          const response = await axios.post('http://127.0.0.1:8000/api/workOrder/workOrder/', postData);
          console.log('POST request successful:', response.data);
  
          emit('submit', localEntry.value);
          emit('update:visible', false);
      } catch (error) {
          if (error.response) {
              console.error('Error during submitEntry execution:', error.response.data);
          } else if (error.request) {
              console.error('No response received:', error.request);
          } else {
              console.error('Error during submitEntry execution:', error.message);
          }
      }
  };
  
  
  
  const hideModal = () => {
    try {
      cancelNewEntry();
    } catch (error) {
      console.error('Error during hideModal execution:', error);
    }
  };
  
  const cancelNewEntry = () => {
    try {
      emit('cancel');
      emit('update:visible', false);
    } catch (error) {
      console.error('Error during cancelNewEntry execution:', error);
    }
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
        localEntry.value = { ...props.entry || {} };
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
  