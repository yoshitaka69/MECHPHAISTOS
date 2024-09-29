<template>
  <Toast />
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
                <Textarea id="title" v-model="localEntry.title" autoResize class="w-full" />
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

              <!-- Request Order と Working Order のセクション -->
              <div class="flex mb-4 gap-4">
                <!-- Request Order セクション -->
                <div class="flex-auto p-3 border-round shadow-1" style="background-color: #e3f2fd;">
                  <h3 class="text-center text-lg mb-3">Request Order</h3>
                  <div class="mb-4">
                    <label for="requestType" class="block font-medium text-900 mb-2">Request Type</label>
                    <Textarea id="requestType" v-model="localEntry.requestType" autoResize class="w-full" />
                  </div>
                  <div class="mb-4">
                    <label for="requestDate" class="block font-medium text-900 mb-2">Request Date</label>
                    <InputText id="requestDate" v-model="localEntry.requestDate" type="date" class="w-full" />
                  </div>
                  <div class="mb-4">
                    <label for="requestedBy" class="block font-medium text-900 mb-2">Requested By</label>
                    <Textarea id="requestedBy" v-model="localEntry.requestedBy" autoResize class="w-full" />
                  </div>

                  <!-- Failure Type をここに移動 -->
                  <div class="mb-4">
                    <label class="block font-medium text-900 mb-2">Failure Type</label>
                    <div v-for="type in failureTypes" :key="type.value" class="flex align-items-center">
                      <Checkbox v-model="localEntry.failureTypes" :value="type.value" class="mr-2" />
                      <label>{{ type.label }}</label>
                    </div>
                  </div>

                  <!-- Situation チェックリスト -->
                  <div class="mb-4">
                    <label class="block font-medium text-900 mb-2">Situation</label>
                    <div v-for="situation in situations" :key="situation.value" class="flex align-items-center">
                      <Checkbox v-model="localEntry.situations" :value="situation.value" class="mr-2" />
                      <label>{{ situation.label }}</label>
                    </div>
                  </div>
                </div>

                <!-- Working Order セクション -->
                <div class="flex-auto p-3 border-round shadow-1" style="background-color: #fce4ec;">
                  <!-- PM Type を Working Order の上に配置 -->
                  <div class="mb-4">
                    <label class="block font-medium text-900 mb-2">PM Type</label>
                    <div v-for="pmType in pmTypes" :key="pmType.value" class="flex align-items-center">
                      <Checkbox v-model="localEntry.pmTypes" :value="pmType.value" class="mr-2" />
                      <label>{{ pmType.label }}</label>
                    </div>
                  </div>

                  <h3 class="text-center text-lg mb-3">Working Order</h3>
                  <div class="mb-4">
                    <label for="workingType" class="block font-medium text-900 mb-2">Working Type</label>
                    <Textarea id="workingType" v-model="localEntry.workingType" autoResize class="w-full" />
                  </div>

                  <!-- Failure Mode を Working Type の下に配置 -->
                  <div class="mb-4">
                    <label class="block font-medium text-900 mb-2">Failure Mode</label>
                    <div v-for="mode in failureModes" :key="mode.value" class="flex align-items-center">
                      <Checkbox v-model="localEntry.failureModes" :value="mode.value" class="mr-2" />
                      <label>{{ mode.label }}</label>
                    </div>
                  </div>

                  <div class="mb-4">
                    <label for="workingDate" class="block font-medium text-900 mb-2">Working Date</label>
                    <InputText id="workingDate" v-model="localEntry.workingDate" type="date" class="w-full" />
                  </div>
                  <div class="mb-4">
                    <label for="workingBy" class="block font-medium text-900 mb-2">Working By</label>
                    <Textarea id="workingBy" v-model="localEntry.workingBy" autoResize class="w-full" />
                  </div>
                </div>
              </div>

              <!-- Failure Checkboxes の追加 -->
              <div class="mb-4">
                <label class="block font-medium text-900 mb-2">Failure Cause</label>
                <div v-for="cause in failureCauses" :key="cause.value" class="flex align-items-center">
                  <Checkbox v-model="localEntry.failureCauses" :value="cause.value" class="mr-2" />
                  <label>{{ cause.label }}</label>
                </div>
              </div>

              <div class="mb-4">
                <label for="failureDescription" class="block font-medium text-900 mb-2">Failure Description</label>
                <Textarea id="failureDescription" v-model="localEntry.failureDescription" autoResize type="text" rows="5" class="w-full"></Textarea>
              </div>
              <div class="mb-4">
                <label for="failureDate" class="block font-medium text-900 mb-2">Failure Date</label>
                <InputText id="failureDate" v-model="localEntry.failureDate" type="date" />
              </div>
              <div class="mb-4">
                <label for="description" class="block font-medium text-900 mb-2">Description</label>
                <Textarea id="description" v-model="localEntry.description" autoResize type="text" rows="5" class="w-full"></Textarea>
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
import noImage from '@/assets/no_image.jpg';
import { useUserStore } from '@/stores/userStore';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast'; // Toast用のフックをインポート

// コンポーネントに渡される props とイベント emit の設定
const props = defineProps(['visible', 'statuses', 'entry']);
const emit = defineEmits(['update:visible', 'submit', 'cancel']);

// 各種データの初期化
// 各種データの初期化
const localEntry = ref({
    pmTypes: [],
    failureTypes: [],
    failureModes: [],
    title: '',
    plant: '',
    equipment: '',
    requestType: '',
    requestDate: '',
    requestedBy: '',
    workingType: '',
    workingDate: '',
    workingBy: '',
    failureDescription: '',
    failureDate: '',
    description: '',
    status: '',
    registrationDate: ''
});

const pmTypes = ref([
    { label: 'PM01', value: 'PM01' },
    { label: 'PM02', value: 'PM02' },
    { label: 'PM03', value: 'PM03' },
    { label: 'PM04', value: 'PM04' },
    { label: 'PM05', value: 'PM05' }
]);

const failureTypes = ref([
    { label: 'Electrical', value: 'electrical' },
    { label: 'Mechanical', value: 'mechanical' },
    { label: 'Software', value: 'software' },
    { label: 'Human Error', value: 'human_error' }
]);

// 更新されたfailureModesリスト
const failureModes = ref([
    { label: 'Wear (摩耗)', value: 'wear' },
    { label: 'Fatigue Failure (疲労破壊)', value: 'fatigue_failure' },
    { label: 'Corrosion (腐食)', value: 'corrosion' },
    { label: 'Overheating (過熱)', value: 'overheating' },
    { label: 'Inadequate Lubrication (潤滑不足)', value: 'inadequate_lubrication' },
    { label: 'Seal Failure (シール破損)', value: 'seal_failure' },
    { label: 'Overload (過負荷)', value: 'overload' },
    { label: 'Vibration (振動)', value: 'vibration' },
    { label: 'Electrical Insulation Failure (絶縁破壊)', value: 'electrical_insulation_failure' },
    { label: 'Short Circuit (短絡)', value: 'short_circuit' },
    { label: 'Mechanical Shock (機械的衝撃)', value: 'mechanical_shock' },
    { label: 'Thermal Fatigue (熱疲労)', value: 'thermal_fatigue' },
    { label: 'Cavitation (キャビテーション)', value: 'cavitation' },
    { label: 'Frictional Wear (摩擦摩耗)', value: 'frictional_wear' },
    { label: 'Stress Corrosion Cracking (応力腐食割れ)', value: 'stress_corrosion_cracking' },
    { label: 'Erosion (浸食)', value: 'erosion' },
    { label: 'Oxidation (酸化)', value: 'oxidation' },
    { label: 'Cable Breakage (ケーブル断線)', value: 'cable_breakage' },
    { label: 'Bearing Failure (ベアリング破損)', value: 'bearing_failure' },
    { label: 'Electronic Component Failure (電子部品故障)', value: 'electronic_component_failure' },
    { label: 'Other (その他)', value: 'other' }
]);

const failureCauses = ref([
  { label: 'Human Error (人的ミス)', value: 'human_error' },
  { label: 'Fatigue Failure (疲労破壊)', value: 'fatigue_failure' },
  { label: 'Overheating/Overload (過熱 / 過負荷)', value: 'overheating_overload' },
  { label: 'Misuse (誤使用)', value: 'misuse' },
  { label: 'Operational Error (操作ミス)', value: 'operational_error' },
  { label: 'Manufacturing Defect (製造欠陥)', value: 'manufacturing_defect' },
  { label: 'Inadequate Maintenance (不適切な保守)', value: 'inadequate_maintenance' },
  { label: 'Improper Installation (不適切な設置)', value: 'improper_installation' },
  { label: 'Material Defect (材料欠陥)', value: 'material_defect' },
  { label: 'Progressive Damage (進行的な損傷)', value: 'progressive_damage' },
  { label: 'Corrosion (腐食)', value: 'corrosion' },
  { label: 'Control System Failure (制御系の異常)', value: 'control_system_failure' },
  { label: 'Process Defect (工程の欠陥)', value: 'process_defect' },
  { label: 'Material Issue (材料の問題)', value: 'material_issue' },
  { label: 'External Factor (外部要因)', value: 'external_factor' }
]);

const situations = ref([
  { label: 'Normal Operation (正常運転)', value: 'normal_operation' },
  { label: 'Abnormal Operation (異常運転)', value: 'abnormal_operation' },
  { label: 'Stopped (停止)', value: 'stopped' },
  { label: 'Maintenance Ongoing (保全中)', value: 'maintenance_ongoing' },
  { label: 'Under Investigation (調査中)', value: 'under_investigation' }
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

// Toastインスタンスを作成
const toast = useToast();

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
            plantOptions.value = [...new Set(companyData.ceList.map((item) => item.plant))].map((plant) => ({
                label: `Plant ${plant}`, // 表示名
                value: plant // 実際の値
            }));
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
            equipmentOptions.value = companyData.ceList
                .filter((item) => item.plant === selectedPlant)
                .map((equipment) => ({
                    label: `Equipment ${equipment.equipment}`, // 表示名
                    value: equipment.equipment // 実際の値
                }));
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
        } else {
            workOrderNo.value = '1'; // データがない場合は '1' を初期値とする
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
        // registrationDateがnullなら、本日の日付を設定
        if (!localEntry.value.registrationDate) {
            const today = new Date().toISOString().split('T')[0]; // 本日の日付をYYYY-MM-DD形式で取得
            localEntry.value.registrationDate = today;
        }

        // POSTリクエストに送信するデータ
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
            registrationDate: localEntry.value.registrationDate || null // 登録日を追加
        };

        // POSTリクエストを送信
        const response = await axios.post('http://127.0.0.1:8000/api/workOrder/workOrder/', postData);
        console.log('POST request successful:', response.data);

        toast.add({ severity: 'success', summary: 'Success', detail: 'Work order saved successfully!', life: 3000 }); // 成功メッセージ
        emit('submit', localEntry.value); // 成功したら親コンポーネントにデータを送信
        emit('update:visible', false); // モーダルを閉じる
    } catch (error) {
        if (error.response) {
            console.error('Error during submitEntry execution:', error.response.data);
        } else if (error.request) {
            console.error('No response received:', error.request);
        } else {
            console.error('Error during submitEntry execution:', error.message);
        }
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to save work order!', life: 3000 }); // エラーメッセージ追加
    }
};

// モーダルを閉じる処理
const hideModal = () => {
    emit('update:visible', false); // visibleをfalseにしてモーダルを閉じる
};

// キャンセルボタンを押したときの処理
const cancelNewEntry = () => {
    emit('cancel'); // 親にキャンセルイベントを伝える
    emit('update:visible', false); // visibleをfalseにしてモーダルを閉じる
};

// 画像を拡大表示
const enlargeImage1 = () => {
    imageDialogVisible1.value = true;
};

const enlargeImage2 = () => {
    imageDialogVisible2.value = true;
};

// モーダルのvisibleが変更されたときにlocalEntryをリセット
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
    border: 1px solid black; /* 黒い細い枠線を追加 */
}

:deep(.p-dialog) {
    max-width: 70vw;
}

textarea,
input[type='text'] {
    resize: both; /* リサイズ可能にする */
    overflow: auto; /* オーバーフロー時にスクロールバーを表示 */
}

.history-list {
    list-style-type: none;
    padding: 0;
}
</style>
