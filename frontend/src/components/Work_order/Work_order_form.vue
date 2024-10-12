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
                    <div class="text-900 font-semibold text-lg mt-3 flex justify-content-end">
                        <div class="flex gap-3 items-center">
                            <!-- Registration Date -->
                            <div class="flex align-items-center">
                                <label for="registrationDate" class="block font-medium text-sm mb-0 mr-2">Registration Date:</label>
                                <InputText id="registrationDate" v-model="localEntry.registrationDate" type="date" class="w-full text-sm" />
                            </div>

                            <!-- Work Order No の表示 -->
                            <div v-if="isNewEntry">
                                <!-- 新規作成の場合の表示 -->
                                <span class="text-sm">Work Order No (New): {{ workOrderNo }}</span>
                            </div>
                            <div v-else>
                                <!-- 編集の場合の表示 -->
                                <span class="text-sm">Work Order No: {{ workOrderNo }}</span>
                            </div>
                        </div>
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
                                    <!-- Plant Dropdown -->
                                    <Dropdown id="plant" v-model="localEntry.plant" :options="plantOptions" optionLabel="label" optionValue="label" placeholder="Select a Plant" />
                                </div>
                                <div class="flex-auto">
                                    <label for="equipment" class="block font-medium text-900 mb-2">Equipment</label>
                                    <Dropdown id="equipment" v-model="localEntry.equipment" :options="equipmentOptions" optionLabel="label" optionValue="label" placeholder="Select Equipment" />
                                </div>
                            </div>

                            <!-- Task List 表示セクション -->
                            <div class="mb-4">
                                <label class="block font-medium text-900 mb-2">Task List</label>
                                <div v-if="taskList.length > 0">
                                    <ul>
                                        <li v-for="task in taskList" :key="task.id">{{ task.name }} - {{ task.description }}</li>
                                    </ul>
                                </div>
                                <div v-else>
                                    <p>該当なし</p>
                                </div>
                            </div>

                            <!-- Request Order と Working Order のセクション -->
                            <div class="flex mb-4 gap-4">
                                <!-- Request Order セクション -->
                                <div class="flex-auto p-3 border-round shadow-1" style="background-color: #e3f2fd">
                                    <h3 class="text-center text-lg mb-3">Request Order</h3>
                                    <div class="mb-4">
                                        <label for="requestType" class="block font-medium text-900 mb-2">Request Type</label>
                                        <Textarea id="requestType" v-model="localEntry.requestType" placeholder="例: メンテナンス依頼の内容を入力してください" autoResize class="w-full" />
                                    </div>

                                    <div class="mb-4">
                                        <label for="failureDate" class="block font-medium text-900 mb-2">Failure Date</label>
                                        <InputText id="failureDate" v-model="localEntry.failureDate" type="date" />
                                    </div>
                                    <div class="mb-4">
                                        <label for="requestedBy" class="block font-medium text-900 mb-2">Requested By</label>
                                        <Textarea id="requestedBy" v-model="localEntry.requestedBy" autoResize class="w-full" />
                                    </div>

                                    <!-- Failure Type をここに移動 -->
                                    <div class="mb-4">
                                        <label class="block font-medium text-900 mb-2">Failure Type</label>
                                        <div class="flex flex-row gap-4">
                                            <!-- Electrical -->
                                            <div class="flex align-items-center">
                                                <Checkbox v-model="localEntry.failureTypes" :value="failureTypes[0].value" class="mr-2" />
                                                <label>{{ failureTypes[0].label }}</label>
                                            </div>
                                            <!-- Mechanical -->
                                            <div class="flex align-items-center">
                                                <Checkbox v-model="localEntry.failureTypes" :value="failureTypes[1].value" class="mr-2" />
                                                <label>{{ failureTypes[1].label }}</label>
                                            </div>
                                            <!-- Software -->
                                            <div class="flex align-items-center">
                                                <Checkbox v-model="localEntry.failureTypes" :value="failureTypes[2].value" class="mr-2" />
                                                <label>{{ failureTypes[2].label }}</label>
                                            </div>
                                            <!-- Building -->
                                            <div class="flex align-items-center">
                                                <Checkbox v-model="localEntry.failureTypes" :value="failureTypes[3].value" class="mr-2" />
                                                <label>{{ failureTypes[3].label }}</label>
                                            </div>
                                            <!-- Utility -->
                                            <div class="flex align-items-center">
                                                <Checkbox v-model="localEntry.failureTypes" :value="failureTypes[4].value" class="mr-2" />
                                                <label>{{ failureTypes[4].label }}</label>
                                            </div>
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

                                    <!-- "Is it urgent?" question and checkbox -->
                                    <!-- "Is it urgent?" question and checkbox -->
                                    <div class="mb-4">
                                        <label class="block font-medium text-900 mb-2">Is it urgent?</label>
                                        <div class="flex align-items-center">
                                            <!-- ここを修正 -->
                                            <Checkbox v-model="localEntry.isUrgent" binary class="mr-2" />
                                            <label>Yes</label>
                                        </div>
                                    </div>
                                </div>

                                <!-- Working Order セクション -->
                                <div class="flex-auto p-3 border-round shadow-1" style="background-color: #fce4ec">
                                    <h3 class="text-center text-lg mb-3">Working Order</h3>
                                    <!-- PM Type を横並びで表示 -->
                                    <div class="mb-4">
                                        <label class="block font-medium text-900 mb-2">PM Type</label>
                                        <div class="flex flex-wrap">
                                            <div v-for="pmType in pmTypes" :key="pmType.value" class="flex align-items-center mr-4">
                                                <Checkbox v-model="localEntry.pmTypes" :value="pmType.value" class="mr-2" />
                                                <label>{{ pmType.label }}</label>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- PM Type と Failure Mode の間に Maintenance Method を追加 -->
                                    <div class="mb-4">
                                        <label class="block font-medium text-900 mb-2">Maintenance Method</label>
                                        <div class="flex flex-wrap">
                                            <div v-for="method in maintenanceMethods" :key="method.value" class="flex align-items-center mr-4">
                                                <Checkbox v-model="localEntry.maintenanceMethods" :value="method.value" class="mr-2" />
                                                <label>{{ method.label }}</label>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Failure Mode -->
                                    <div class="mb-4">
                                        <label class="block font-medium text-900 mb-2">Failure Mode</label>
                                        <div v-for="mode in failureModes" :key="mode.value" class="flex align-items-center">
                                            <Checkbox v-model="localEntry.failureModes" :value="mode.value" class="mr-2" />
                                            <label>{{ mode.label }}</label>
                                        </div>
                                    </div>

                                    <!-- Working Date のStart DateとEnd Dateの追加 -->
                                    <div class="flex flex-row gap-4 mb-4">
                                        <!-- Start Date -->
                                        <div class="flex-auto">
                                            <label for="workingStartDate" class="block font-medium text-900 mb-2">Start Date</label>
                                            <InputText id="workingStartDate" v-model="localEntry.workingStartDate" type="date" class="w-full" />
                                        </div>

                                        <!-- End Date -->
                                        <div class="flex-auto">
                                            <label for="workingEndDate" class="block font-medium text-900 mb-2">End Date</label>
                                            <InputText id="workingEndDate" v-model="localEntry.workingEndDate" type="date" class="w-full" />
                                        </div>
                                    </div>
                                    <!-- Status ラジオボタンに変更 -->
                                    <div class="mb-4">
                                        <label class="block font-medium text-900 mb-2">Status</label>
                                        <div class="flex flex-wrap">
                                            <!-- Statusの選択肢をRadioButtonに変更 -->
                                            <div v-for="statusOption in statuses" :key="statusOption.value" class="flex align-items-center mr-4">
                                                <RadioButton v-model="localEntry.status" :value="statusOption.value" class="mr-2" />
                                                <label>{{ statusOption.label }}</label>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- Status ラジオボタンの後に Repair completion date フィールドを追加 -->
                                    <!-- Repair completion date フィールド -->
                                    <div class="flex flex-wrap mb-4">
                                        <label class="block font-medium text-900 mb-2">Repair completion date</label>
                                        <InputText id="repairCompletionDate" v-model="localEntry.repairCompletionDate" type="date" class="w-full" :disabled="localEntry.status !== 'COMPLETED' && localEntry.status !== 'TEMP_COMPLETED'" />
                                    </div>

                                    <!-- Working By にuserNameをデフォルトで表示 -->
                                    <div class="mb-4">
                                        <label for="workingBy" class="block font-medium text-900 mb-2">Working By</label>
                                        <Textarea id="workingBy" v-model="localEntry.workingBy" :value="userStore.userName" autoResize class="w-full" />
                                    </div>
                                </div>
                            </div>

                            <!-- Failure Description の統合 -->
                            <div class="mb-4">
                                <label class="block font-medium text-900 mb-2">Failure Description</label>
                                <div class="flex flex-wrap">
                                    <div v-for="cause in failureCauses" :key="cause.value" class="flex align-items-center mr-4">
                                        <Checkbox v-model="localEntry.failureCauses" :value="cause.value" class="mr-2" />
                                        <label>{{ cause.label }}</label>
                                    </div>
                                </div>
                                <Textarea id="failureDescription" v-model="localEntry.failureDescription" autoResize type="text" rows="5" class="w-full"></Textarea>
                            </div>

                            <!-- "Spare Parts Used?" question and Yes/No buttons -->
                            <div class="mb-4">
                                <label class="block font-medium text-900 mb-2">Did you use spare parts?</label>
                                <div class="spare-parts-selection">
                                    <!-- Yesボタン -->
                                    <Button label="Yes" class="yes-button custom-button-width mr-2" @click="toggleSparePartsUsage(true)" :class="{ selected: localEntry.sparePartsUsed }" />
                                    <!-- Noボタン -->
                                    <Button label="No" class="no-button custom-button-width" @click="toggleSparePartsUsage(false)" :class="{ selected: !localEntry.sparePartsUsed }" />
                                    <!-- Noが選択された場合にチェックを表示 -->
                                    <span v-if="!localEntry.sparePartsUsed" class="checkmark">✔</span>
                                </div>
                            </div>
                            <!-- SparePartsFormコンポーネントの表示 -->
                            <SparePartsForm v-if="localEntry.sparePartsUsed" v-model="localEntry.spareParts" />

                            <div class="flex flex-row justify-content-start align-items-center mb-4 gap-4">
                                <!-- Picture 1 -->
                                <div class="flex flex-column align-items-center">
                                    <span class="font-medium text-900 mb-2">Picture 1</span>
                                    <img :src="pictureSrc1" class="h-10rem w-10rem border-black mb-4" @click="enlargeImage1" />
                                    <Button type="button" icon="pi pi-pencil" class="p-button-rounded -mt-4"></Button>
                                </div>

                                <!-- Picture 2 -->
                                <div class="flex flex-column align-items-center">
                                    <span class="font-medium text-900 mb-2">Picture 2</span>
                                    <img :src="pictureSrc2" class="h-10rem w-10rem border-black mb-4" @click="enlargeImage2" />
                                    <Button type="button" icon="pi pi-pencil" class="p-button-rounded -mt-4"></Button>
                                </div>
                            </div>

                            <!-- Description を Remark に変更 -->
                            <div class="mb-4">
                                <label for="remark" class="block font-medium text-900 mb-2">Remark</label>
                                <Textarea id="remark" v-model="localEntry.remark" autoResize type="text" rows="5" class="w-full"></Textarea>
                            </div>
                            <div class="flex justify-content-end">
                                <Button label="Save" icon="pi pi-save" class="mr-2 p-button-primary" style="background-color: blue; border-color: blue; color: white" @click="submitEntry" />
                                <Button label="Cancel" icon="pi pi-times" class="p-button-secondary" style="background-color: #ff6347; border-color: #ff6347; color: white" @click="cancelNewEntry" />
                            </div>
                        </div>
                    </div>
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
import SparePartsForm from '@/components/Spare_parts_form/SparePartsForm.vue'; // スペアパーツフォームのインポート

// コンポーネントに渡される props とイベント emit の設定
const props = defineProps(['visible', 'entry']); // entryプロップスで編集するデータを受け取る
const emit = defineEmits(['update:visible', 'submit', 'cancel']);
const isNewEntry = ref(false); // 新規作成かどうかを示すフラグ

const localEntry = ref({
    pmTypes: [], // PMタイプの初期化
    failureTypes: [], // 故障タイプの初期化
    failureModes: [], // 故障モードの初期化
    failureCauses: [], // 故障原因の初期化
    situations: [], // 状況の初期化
    title: '', // タイトル
    plant: '', // プラント
    equipment: '', // 設備
    requestType: '', // 要求タイプ
    requestedBy: '', // 要求者
    workingType: '', // 作業タイプ
    workingDate: '', // 作業日
    workingBy: '', // 作業者
    failureDescription: '', // 故障説明
    failureDate: new Date().toISOString().split('T')[0], // デフォルトで本日の日付を設定
    remark: '', // 説明のフィールドを remark に変更
    status: '', // 状態
    repairCompletionDate: null, // 修理完了日
    registrationDate: new Date().toISOString().split('T')[0], // 登録日
    isUrgent: false, // 緊急フラグ
    sparePartsUsed: false, // スペアパーツ使用フラグ
    spareParts: [] // スペアパーツのデータ
});

// PMタイプ、故障タイプ、故障モード、故障原因などのオプション
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
    { label: 'Building', value: 'building' },
    { label: 'Utility', value: 'utility' }
]);

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
    { label: 'Piping Leak (配管漏れ)', value: 'piping_leak' },
    { label: 'Piping Blockage (配管閉塞)', value: 'piping_blockage' },
    { label: 'Building Structural Failure (建物の構造的問題)', value: 'building_structural_failure' },
    { label: 'Utility Failure (ユーティリティ故障)', value: 'utility_failure' },
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
    { label: 'Material Issue (材料の問題)', value: 'material_issue' },
    { label: 'Progressive Damage (進行的な損傷)', value: 'progressive_damage' },
    { label: 'Corrosion (腐食)', value: 'corrosion' },
    { label: 'Control System Failure (制御系の異常)', value: 'control_system_failure' },
    { label: 'Process Defect (工程の欠陥)', value: 'process_defect' },
    { label: 'External Factor (外部要因)', value: 'external_factor' },
    { label: 'Natural Disaster (天変地異)', value: 'natural_disaster' },
    { label: 'Other (その他)', value: 'other' }
]);

const situations = ref([
    { label: 'Normal Operation (正常運転)', value: 'normal_operation' },
    { label: 'Abnormal Operation (異常運転)', value: 'abnormal_operation' },
    { label: 'Stopped (停止)', value: 'stopped' },
    { label: 'Maintenance Ongoing (保全中)', value: 'maintenance_ongoing' },
    { label: 'Under Investigation (調査中)', value: 'under_investigation' }
]);

// statuses の選択肢に追加
const statuses = ref([
    { label: 'Completed', value: 'COMPLETED' },
    { label: 'Ongoing', value: 'Ongoing' },
    { label: 'Delayed', value: 'Delayed' },
    { label: 'On Hold', value: 'ON_HOLD' }, // 一旦保留
    { label: 'Temporarily Completed', value: 'TEMP_COMPLETED' }, // 一旦完了
    { label: 'HELP', value: 'HELP' } // HELP
]);

const maintenanceMethods = ref([
    { label: 'Inspection (点検)', value: 'inspection' },
    { label: 'Lubrication (潤滑)', value: 'lubrication' },
    { label: 'Adjustment (調整)', value: 'adjustment' },
    { label: 'Replacement (交換)', value: 'replacement' },
    { label: 'Cleaning (清掃)', value: 'cleaning' },
    { label: 'Repair (修理)', value: 'repair' },
    { label: 'Regular Maintenance (定期保全)', value: 'regular_maintenance' },
    { label: 'Overhaul (オーバーホール)', value: 'overhaul' },
    { label: 'Improvement (改善)', value: 'improvement' },
    { label: 'New Installation (新規設置)', value: 'new_installation' },
    { label: 'Other (その他)', value: 'other' }
]);

// 画像、タブ、装置などの状態
const pictureSrc1 = ref(noImage);
const pictureSrc2 = ref(noImage);
const imageDialogVisible1 = ref(false);
const imageDialogVisible2 = ref(false);
const currentTab = ref('form');
const plantOptions = ref([]);
const equipmentOptions = ref([]);
const taskList = ref([]); // タスクリスト
const workOrderNo = ref('');

// PiniaストアからcompanyCodeを取得
const userStore = useUserStore();
const companyCode = userStore.companyCode;

// Toastインスタンスを作成
const toast = useToast();

// Watcherで編集の際にフォームを更新
watch(
    () => props.entry,
    (newEntry) => {
        if (newEntry) {
            localEntry.value = { ...newEntry };
            workOrderNo.value = newEntry.workOrderNo;
        }
    },
    { immediate: true }
);

// プラントの選択肢を取得
const fetchPlantOptions = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/ceList/ceListByCompany/', {
            params: { companyCode: companyCode }
        });
        const companyData = response.data.find((company) => company.companyCode === companyCode);
        if (companyData) {
            plantOptions.value = [...new Set(companyData.ceList.map((item) => item.plant))].map((plant) => ({
                label: `Plant ${plant}`,
                value: plant
            }));
        }
    } catch (error) {
        console.error('Failed to fetch plant options:', error);
    }
};

// 選択されたプラントに対応する装置のリストを取得
// equipmentを取得する関数を修正
const fetchEquipmentOptions = async (selectedPlant) => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/ceList/ceListByCompany/', {
            params: { companyCode: companyCode }
        });
        const companyData = response.data.find((company) => company.companyCode === companyCode);

        if (companyData) {
            if (selectedPlant) {
                // plantが選択されている場合、そのplant内のequipmentをフィルタリング
                equipmentOptions.value = companyData.ceList
                    .filter((item) => item.plant === selectedPlant)
                    .map((equipment) => ({
                        label: `Equipment ${equipment.equipment}`,
                        value: equipment.equipment
                    }));
            } else {
                // plantが未選択の場合、全てのequipmentを取得して表示
                equipmentOptions.value = companyData.ceList.map((equipment) => ({
                    label: `Equipment ${equipment.equipment}`,
                    value: equipment.equipment
                }));
                // デフォルトで全てのequipmentが選択されるように設定
                localEntry.value.equipment = equipmentOptions.value.map((equipment) => equipment.value);
            }
        }
    } catch (error) {
        console.error('Failed to fetch equipment options:', error);
    }
};

// plantが選択されたときにequipmentのリストを取得
watch(
    () => localEntry.value.plant,
    (newPlant) => {
        // plantが未選択の場合は全てのequipmentを取得
        fetchEquipmentOptions(newPlant || null);
    }
);

// 初期ロード時にすべてのequipmentを選択
onMounted(() => {
    fetchPlantOptions(); // plantリストの取得
    fetchEquipmentOptions(null); // equipmentリストの取得（plantが未選択の場合は全て）
});

// 選択された装置に対応するタスクリストを取得
const fetchTaskList = async (selectedEquipment) => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/task/taskListByEquipment/', {
            params: { companyCode: companyCode, equipment: selectedEquipment }
        });
        taskList.value = response.data.length > 0 ? response.data : [];
    } catch (error) {
        console.error('Failed to fetch task list:', error);
        taskList.value = [];
    }
};

// Work Order Noを取得し、最大値+1を設定
const fetchAndIncrementWorkOrderNo = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/workOrder/workOrderByCompany/', {
            params: { companyCode: companyCode }
        });
        const companyData = response.data.find((company) => company.companyCode === companyCode);
        if (companyData && companyData.workOrderList.length > 0) {
            const maxWorkOrderNo = Math.max(...companyData.workOrderList.map((order) => parseInt(order.workOrderNo, 10)));
            workOrderNo.value = (maxWorkOrderNo + 1).toString(); // 最新のWork Order Noを+1して設定
        } else {
            workOrderNo.value = '1'; // デフォルトで'1'を設定
        }
    } catch (error) {
        console.error('Failed to fetch and increment work order no:', error);
    }
};

onMounted(() => {
    // プラントのリストを取得
    fetchPlantOptions();

    // フラグに応じて Work Order No を取得
    if (isNewEntry.value) {
        // 新規作成時は最新のWork Order Noを取得して+1する
        fetchAndIncrementWorkOrderNo();
    } else if (props.entry) {
        // 編集モード時は既存のWork Order Noをセット
        workOrderNo.value = props.entry.workOrderNo;
    }
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

// equipmentが選択されたときにタスクリストを取得
watch(
    () => localEntry.value.equipment,
    (newEquipment) => {
        if (newEquipment) {
            fetchTaskList(newEquipment);
        } else {
            taskList.value = [];
        }
    }
);

// SaveボタンがクリックされたときにPOSTリクエストを送信
const submitEntry = async () => {
    try {
        if (!localEntry.value.registrationDate) {
            const today = new Date().toISOString().split('T')[0];
            localEntry.value.registrationDate = today;
        }

        // POSTデータの準備
        const postData = {
            companyCode: companyCode,
            registrationDate: localEntry.value.registrationDate || null,
            workOrderNo: workOrderNo.value,
            title: localEntry.value.title || null,
            plant: localEntry.value.plant || null, // Plantを文字列として登録
            equipment: localEntry.value.equipment || null, // Equipmentを文字列として登録
            requestType: localEntry.value.requestType || null,
            failureDate: localEntry.value.failureDate || null,
            requestedBy: localEntry.value.requestedBy || null,
            failureTypes: Array.isArray(localEntry.value.failureTypes) && localEntry.value.failureTypes.length > 0 ? localEntry.value.failureTypes : null,
            situations: Array.isArray(localEntry.value.situations) && localEntry.value.situations.length > 0 ? localEntry.value.situations : null,
            isUrgent: localEntry.value.isUrgent || false,
            pmTypes: Array.isArray(localEntry.value.pmTypes) && localEntry.value.pmTypes.length > 0 ? localEntry.value.pmTypes : null,
            maintenanceMethods: Array.isArray(localEntry.value.maintenanceMethods) && localEntry.value.maintenanceMethods.length > 0 ? localEntry.value.maintenanceMethods : null, // 追加
            failureModes: Array.isArray(localEntry.value.failureModes) && localEntry.value.failureModes.length > 0 ? localEntry.value.failureModes : null,
            workingStartDate: localEntry.value.workingStartDate || null,
            workingEndDate: localEntry.value.workingEndDate || null,
            status: localEntry.value.status || null,
            repairCompletionDate: localEntry.value.repairCompletionDate || null, // 修理完了日
            workingBy: localEntry.value.workingBy || null,
            failureCauses: Array.isArray(localEntry.value.failureCauses) && localEntry.value.failureCauses.length > 0 ? localEntry.value.failureCauses : null,
            failureDescription: localEntry.value.failureDescription || null,
            remark: localEntry.value.remark || null // Remark を POST データに追加
        };

        console.log('POSTデータ:', postData);

        // POSTリクエスト
        const response = await axios.post('http://127.0.0.1:8000/api/workOrder/workOrder/', postData);
        console.log('POSTリクエスト成功:', response.data);
        toast.add({ severity: 'success', summary: 'Success', detail: 'Work order saved successfully!', life: 3000 });
        emit('submit', localEntry.value);
        emit('update:visible', false);
    } catch (error) {
        console.error('POSTリクエスト失敗:', error.response ? error.response.data : error.message);
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to save work order!', life: 3000 });
    }
};

// モーダルを閉じる処理
const hideModal = () => {
    emit('update:visible', false);
};

// キャンセル処理
const cancelNewEntry = () => {
    emit('cancel');
    emit('update:visible', false);
};

// スペアパーツ使用フラグの切り替え
const toggleSparePartsUsage = (isUsed) => {
    localEntry.value.sparePartsUsed = isUsed;
};

// 画像の拡大表示
const enlargeImage1 = () => {
    imageDialogVisible1.value = true;
};

const enlargeImage2 = () => {
    imageDialogVisible2.value = true;
};
</script>

<style scoped>
/* Dialogのスタイル */
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

/* History listのスタイル */
.history-list {
    list-style-type: none;
    padding: 0;
}

/* Task listのスタイル */
.task-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.task-list li {
    padding: 8px 0;
    border-bottom: 1px solid #ccc;
}

/* Yes/Noボタンのカスタマイズ */
.custom-button-width {
    width: 100px;
}

.yes-button,
.no-button {
    color: white;
    font-weight: bold;
    padding: 6px 12px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    transition: background-color 0.3s ease;
}

.yes-button {
    background-color: #28a745;
}

.yes-button:hover {
    background-color: #218838;
}

.no-button {
    background-color: #dc3545;
}

.no-button:hover {
    background-color: #c82333;
}

/* Yes/Noボタン選択時のスタイル */
.yes-button.selected {
    background-color: #218838;
}

.no-button.selected {
    background-color: #c82333;
}

/* Noボタンが選択されたときのチェックマーク */
.checkmark {
    font-size: 18px;
    color: #dc3545;
    margin-left: 10px;
    font-weight: bold;
    vertical-align: middle;
}

/* Yes/Noボタンの間に隙間を追加 */
.spare-parts-selection .mr-2 {
    margin-right: 1rem; /* ボタン間に1remの隙間を追加 */
}
</style>