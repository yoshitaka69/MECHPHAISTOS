<template>
    <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
        <div class="grid">
            <div class="col-12 lg:col-2"></div>
            <div class="col-12 lg:col-10">
                <!-- アラート表示 -->
                <Save_Alert v-if="showAlert" :type="alertType" :message="alertMessage" :errorMessages="errorMessages" />
                <!-- フォーム内容 -->

                <div v-if="showError" class="error-message">*The form is incomplete.</div>
                <div class="grid formgrid p-fluid">
                    <div class="field mb-4 col-12">
                        <label for="nearMissNo" class="form-label">NearMiss No</label>

                        <!-- 編集時には既存の nearMissNo を表示 -->
                        <p v-if="isEditing">{{ formState.NearMissNo }}</p>

                        <!-- 新規作成時には lastNearMissNo を表示 -->
                        <p v-else>{{ lastNearMissNo }}</p>
                    </div>
                    <div class="field mb-4 col-12">
                        <label for="date" class="form-label">Date</label>
                        <Calendar v-model="formState.Date" id="date" class="w-full" />
                    </div>
                    <div class="field mb-4 col-12 md:col-6" :class="{ 'input-error': errorMessagesState.Name.length > 0 }">
                        <label for="name" class="form-label">Name</label>
                        <InputText id="name" type="text" placeholder="write your Name" v-model="formState.Name" class="w-full" />
                        <ul class="errorMessages">
                            <li v-for="message in errorMessagesState.Name" :key="message">
                                {{ message }}
                            </li>
                        </ul>
                    </div>
                    <div class="field mb-4 col-12 md:col-6" :class="{ 'input-error': errorMessagesState.Department.length > 0 }">
                        <label for="department" class="form-label">Department</label>
                        <InputText id="department" type="text" placeholder="write your department" v-model="formState.Department" class="w-full" />
                        <ul class="errorMessages">
                            <li v-for="message in errorMessagesState.Department" :key="message">
                                {{ message }}
                            </li>
                        </ul>
                    </div>
                    <div class="field mb-4 col-12" :class="{ 'input-error': errorMessagesState.Where.length > 0 }">
                        <label for="where" class="form-label">Where</label>
                        <InputText id="where" type="text" placeholder="write the place" v-model="formState.Where" class="w-full" />
                        <ul class="errorMessages">
                            <li v-for="message in errorMessagesState.Where" :key="message">
                                {{ message }}
                            </li>
                        </ul>
                    </div>

                    <!-- Type of Accident -->
                    <div class="field mb-4 col-12" :class="{ 'input-error': errorMessagesState.TypeOfAccIdent.length > 0 }">
                        <label for="typeOfAccIdent" class="form-label">Type of Accident</label>
                        <div class="flex flex-wrap gap-3">
                            <div v-for="(type, index) in accidentTypes" :key="index" class="field">
                                <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                    <RadioButton :name="type" :value="type" v-model="formState.TypeOfAccIdent" :tabindex="index" />
                                    <label>{{ type }}</label>
                                </div>
                            </div>
                        </div>
                        <ul class="errorMessages">
                            <li v-for="message in errorMessagesState.TypeOfAccIdent" :key="message">
                                {{ message }}
                            </li>
                        </ul>
                    </div>

                    <!-- Factor -->
                    <div class="field mb-4 col-12 lg:col-4" :class="{ 'input-error': errorMessagesState.Factor.length > 0 }">
                        <label for="factor" class="form-label">Factor</label>
                        <div class="flex flex-wrap gap-3">
                            <div v-for="(factor, index) in factors" :key="index" class="field">
                                <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                    <RadioButton :name="factor" :value="factor" v-model="formState.Factor" :tabindex="index" />
                                    <label>{{ factor }}</label>
                                </div>
                            </div>
                        </div>
                        <ul class="errorMessages">
                            <li v-for="message in errorMessagesState.Factor" :key="message">
                                {{ message }}
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="grid formgrid p-fluid">
                    <div class="form-container lg:col-4">
                        <div class="field mb-4 col-12">
                            <label for="injuredLv" class="form-label">Injured Lv</label>
                            <div class="flex flex-wrap gap-3">
                                <div v-for="(level, index) in injuredLevels" :key="index" class="field">
                                    <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                        <RadioButton :name="level" :value="level" v-model="formState.InjuredLv" :tabindex="index" />
                                        <label>{{ level }}</label>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="field mb-4 col-12">
                            <label for="equipmentDamageLv" class="form-label">Equipment Damage Lv</label>
                            <div class="flex flex-wrap gap-3">
                                <div v-for="(level, index) in equipmentDamageLevels" :key="index" class="field">
                                    <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                        <RadioButton :name="level" :value="level" v-model="formState.EquipmentDamageLv" :tabindex="index" />
                                        <label>{{ level }}</label>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="field mb-4 col-12">
                            <label for="affectOfEnvironment" class="form-label">Affect Of Environment</label>
                            <div class="flex flex-wrap gap-3">
                                <div v-for="(level, index) in affectOfEnviromentLevels" :key="index" class="field">
                                    <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                        <RadioButton :name="level" :value="level" v-model="formState.AffectOfEnviroment" :tabindex="index" />
                                        <label>{{ level }}</label>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="field mb-4 col-12">
                            <label for="newsCoverage" class="form-label">News Coverage</label>
                            <div class="flex flex-wrap gap-3">
                                <div v-for="(level, index) in newsCoverageLevels" :key="index" class="field">
                                    <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                        <RadioButton :name="level" :value="level" v-model="formState.NewsCoverage" :tabindex="index" />
                                        <label>{{ level }}</label>
                                    </div>
                                </div>
                            </div>
                            <div class="risk-level">
                                <div class="risk-label">Risk Level</div>
                                <div class="risk-arrows">
                                    <div class="arrow-label high">High</div>
                                    <div class="arrow">←---------------------------→</div>
                                    <div class="arrow-label low">Low</div>
                                </div>
                            </div>
                        </div>

                        <!-- ボタンを中央に配置 -->
                        <div class="field mb-4 col-12 lg:col-4 measures-field">
                            <label for="measures" class="form-label">Measures</label>
                            <div class="measures-container">
                                <Button :label="calculateCategory()" :severity="getButtonSeverity(calculateCategory())" raised class="measures-button" />
                            </div>
                        </div>

                        <!-- Action Items -->
                        <div class="field mb-4 col-12" :class="{ 'input-error': errorMessagesState.ActionItems && errorMessagesState.ActionItems.length > 0 }">
                            <label for="actionItems" class="form-label">Action Items</label>
                            <Textarea id="actionItems" placeholder="Enter action items" v-model="formState.ActionItems" class="w-full" rows="4" autoResize />
                            <ul class="errorMessages">
                                <li v-for="message in errorMessagesState.ActionItems" :key="message">
                                    {{ message }}
                                </li>
                            </ul>
                        </div>

                        <!-- Solved Action Items -->
                        <div class="field mb-4 col-12">
                            <div class="flex align-items-center gap-2">
                                <Checkbox v-model="formState.SolvedActionItems" id="solvedActionItems" />
                                <label for="solvedActionItems" class="form-label m-0">Solved Action Items</label>
                            </div>
                            <p>＊ここはまだ入力しなくても問題なし</p>
                        </div>
                    </div>

                    <!-- Level Description -->
                    <div class="field mb-8 col-12 lg:col-8">
                        <LevelDescription />
                        <!-- "Define Safety Measures" のテキストを追加 -->
                        <p class="define-safety-measures">Define Safety Measures</p>
                    </div>

                    <!-- Description -->
                    <div class="field mb-4 col-12" :class="{ 'input-error': errorMessagesState.Description.length > 0 }">
                        <label for="description" class="form-label">Description</label>
                        <Textarea v-model="formState.Description" autoResize rows="6" id="description" class="w-full" />
                        <ul class="errorMessages">
                            <li v-for="message in errorMessagesState.Description" :key="message">
                                {{ message }}
                            </li>
                        </ul>
                    </div>

                    <div class="col-12 text-right">
                        <Button type="button" label="Save" @click="validateForm" class="w-auto mt-3 save-button"></Button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue'; // onMountedをインポート
import { useRoute } from 'vue-router'; // vue-routerを使っている場合にインポート
import axios from 'axios';
import moment from 'moment';
import { useUserStore } from '@/stores/userStore';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Calendar from 'primevue/calendar';
import RadioButton from 'primevue/radiobutton';
import Checkbox from 'primevue/checkbox';
import Button from 'primevue/button';
import LevelDescription from '@/components/Safety/Near_miss/Level_description.vue';
import Save_Alert from '@/components/Alert/Save_Alert.vue'; // Save_Alert コンポーネントをインポート

export default {
    props: {
        isEditing: {
            type: Boolean,
            default: false
        },
        editingItem: {
            type: Object,
            default: () => ({})
        }
    },
    components: {
        InputText,
        Textarea,
        Calendar,
        RadioButton,
        Checkbox,
        Button,
        LevelDescription,
        Save_Alert // Save_Alertをコンポーネントに追加
    },
    setup(props, { emit }) {
        // ここで emit を受け取る
        const userStore = useUserStore();
        const showError = ref(false);
        const showAlert = ref(false); // 追加
        const alertType = ref(''); // 追加
        const alertMessage = ref(''); // 追加
        const errorMessages = ref([]); // 追加
        const isEditing = ref(false); // 編集モードかどうかの状態を保持

        const resetForm = () => {
            Object.assign(formState, {
                NearMissNo: '',
                Date: new Date(),
                Name: '',
                Department: '',
                Where: '',
                TypeOfAccIdent: '',
                Factor: '',
                InjuredLv: '',
                EquipmentDamageLv: '',
                AffectOfEnviroment: '',
                NewsCoverage: '',
                ActionItems: '',
                SolvedActionItems: false,
                Description: ''
            });

            console.log('Form state after reset:', formState); // フォームの状態を確認
        };

        // フォームの初期化
        const initializeForm = async () => {
            if (props.isEditing && props.nearMissNo) {
                // 編集モードの場合、APIからデータを取得してフォームに設定する
                const response = await fetchNearMissData(props.nearMissNo);
                if (response) {
                    // フォームのフィールドごとにデータをマッピング
                    formState.NearMissNo = response.nearMissNo;
                    formState.Date = new Date(response.dateOfOccurrence); // 日付の変換
                    formState.Name = response.userName.userName; // ネストされたデータを展開
                    formState.Department = response.department;
                    formState.Where = response.placeOfOccurrence;
                    formState.TypeOfAccIdent = response.typeOfAccident;
                    formState.Factor = response.factor;
                    formState.InjuredLv = response.injuredLv;
                    formState.EquipmentDamageLv = response.equipmentDamageLv;
                    formState.AffectOfEnviroment = response.affectOfEnviroment;
                    formState.NewsCoverage = response.newsCoverage;
                    formState.ActionItems = response.actionItems;
                    formState.SolvedActionItems = response.solvedActionItems;
                    formState.Description = response.description;
                }
                console.log('Initialized form with nearMissNo:', formState.NearMissNo);
            } else {
                // 新規作成の場合、NearMissNo を +1
                lastNearMissNo.value = await getLastNearMissNo();
                console.log('Initialized form with new nearMissNo:', lastNearMissNo.value);
            }
        };

        // APIから編集対象のデータを取得

        const fetchNearMissData = async (companyCode, nearMissNo) => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/`, {
                    params: { companyCode }
                });

                const companyData = response.data.find((company) => company.companyCode === companyCode);
                if (!companyData) {
                    console.warn(`CompanyCode: ${companyCode} に一致するデータが見つかりませんでした。`);
                    return null;
                }

                const nearMissData = companyData.nearMissList.find((nearMiss) => nearMiss.nearMissNo === nearMissNo);
                if (!nearMissData) {
                    console.warn(`NearMissNo: ${nearMissNo} が見つかりませんでした。`);
                    return null;
                }

                return nearMissData;
            } catch (error) {
                console.error('Error fetching near miss data:', error);
                return null;
            }
        };

        // マウント時にフォームを初期化
        const route = useRoute(); // クエリパラメータを取得するためにルート情報を取得

        onMounted(async () => {
            const queryNearMissNo = route.query.nearMissNo || null;
            const queryIsEditing = route.query.isEditing === 'true';

            const companyCode = userStore.companyCode;

            if (queryIsEditing && queryNearMissNo) {
                isEditing.value = true;

                // データを取得してフォームに反映
                const nearMissData = await fetchNearMissData(companyCode, queryNearMissNo);
                if (nearMissData) {
                    formState.NearMissNo = nearMissData.nearMissNo; // nearMissNo を設定
                    formState.Date = new Date(nearMissData.dateOfOccurrence); // 日付形式の変換
                    formState.Name = nearMissData.userName.userName; // ネストされたデータ
                    formState.Department = nearMissData.department;
                    formState.Where = nearMissData.placeOfOccurrence;
                    formState.TypeOfAccIdent = nearMissData.typeOfAccident;
                    formState.Factor = nearMissData.factor;
                    formState.InjuredLv = nearMissData.injuredLv;
                    formState.EquipmentDamageLv = nearMissData.equipmentDamageLv;
                    formState.AffectOfEnviroment = nearMissData.affectOfEnviroment;
                    formState.NewsCoverage = nearMissData.newsCoverage;
                    formState.ActionItems = nearMissData.actionItems;
                    formState.SolvedActionItems = nearMissData.solvedActionItems;
                    formState.Description = nearMissData.description;
                }
            } else {
                formState.NearMissNo = await getLastNearMissNo(); // 新規作成モードの場合の NearMissNo の設定
            }
        });
        const lastNearMissNo = ref('001-testChemical-000001');
        const formState = reactive({
            NearMissNo: '',
            Date: new Date(), // デフォルトで現在の日付を設定
            Name: '',
            Department: '',
            Where: '',
            TypeOfAccIdent: '',
            Factor: '',
            InjuredLv: '',
            EquipmentDamageLv: '',
            AffectOfEnviroment: '',
            NewsCoverage: '',
            ActionItems: '',
            SolvedActionItems: false,
            Description: ''
        });

        const errorMessagesState = reactive({
            Date: [],
            Name: [],
            Department: [],
            Where: [],
            TypeOfAccIdent: [],
            Factor: [],
            InjuredLv: [],
            EquipmentDamageLv: [],
            AffectOfEnviroment: [],
            NewsCoverage: [],
            ActionItems: [],
            Description: []
        });

        // lastNearMissNo を取得する関数
        const getLastNearMissNo = async () => {
            try {
                const companyCode = userStore.companyCode;
                const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/last-near-miss-no/?companyCode=${companyCode}`);
                let lastNearMissNo = response.data.lastNearMissNo;

                if (lastNearMissNo && !isEditing.value) {
                    // 新規作成の場合にのみ NearMissNo をインクリメント
                    const numberPart = parseInt(lastNearMissNo.split('-').pop(), 10);
                    if (!isNaN(numberPart)) {
                        const newNearMissNo = `NearMissNo-${(numberPart + 1).toString().padStart(5, '0')}`;
                        return newNearMissNo;
                    }
                }
                return lastNearMissNo || 'NearMissNo-00001';
            } catch (error) {
                console.error('Error getting last nearMissNo:', error);
                throw error;
            }
        };

        // 取得した新しい nearMissNo をフォームに反映
        getLastNearMissNo().then((nearMissNo) => (lastNearMissNo.value = nearMissNo));

        const calculateCategory = () => {
            const valueMapping = { A: 10, B: 8, C: 3, D: 2, E: 1 };
            const total = ['InjuredLv', 'EquipmentDamageLv', 'AffectOfEnviroment', 'NewsCoverage'].reduce((acc, key) => {
                const value = formState[key] || 'E';
                return acc + (valueMapping[formState[key]] || 0);
            }, 0);
            return total >= 11 ? 'A' : total >= 10 ? 'B' : total >= 9 ? 'C' : total >= 5 ? 'D' : 'E';
        };

        const getButtonSeverity = (category) => {
            const severityMapping = {
                A: 'danger',
                B: 'help',
                C: 'warn',
                D: 'info',
                E: 'success'
            };
            return severityMapping[category] || 'secondary';
        };

        const validateForm = () => {
            showError.value = false;
            let hasError = false;

            // フォームのすべてのフィールドについてバリデーションを行う
            Object.keys(formState).forEach((key) => {
                if (formState[key] === '' || formState[key] === null) {
                    // 'nearMissNo'をバリデーションの対象から外す
                    if (key !== 'ActionItems' && key !== 'SolvedActionItems' && key !== 'TypeOfAccIdent' && key !== 'NearMissNo') {
                        showError.value = true;
                        errorMessagesState[key] = ['This field is required'];
                        hasError = true;
                        console.log(`Validation error in field: ${key}`); // エラーのあるフィールドをコンソールに出力
                    }
                } else {
                    errorMessagesState[key] = [];
                }
            });

            if (!hasError) {
                submitForm(); // バリデーションが通った場合はフォームを送信
            } else {
                alertType.value = 'error';
                alertMessage.value = 'Form validation failed.';
                errorMessages.value = ['Please fill in the required fields.'];
                showAlert.value = true; // エラー時にアラート表示
                console.log('Validation errors:', errorMessagesState); // すべてのエラーメッセージをコンソールに出力
            }
        };

        const submitForm = async () => {
            try {
                const companyCode = userStore.companyCode;
                const nearMissNo = formState.NearMissNo || null; // nearMissNo が未定義の場合に null を代入

                if (!companyCode) {
                    throw new Error('CompanyCode is missing.');
                }

                const postData = {
                    userName: { userName: formState.Name, email: formState.Email },
                    department: formState.Department,
                    dateOfOccurrence: moment(formState.Date).format('YYYY-MM-DD'),
                    placeOfOccurrence: formState.Where,
                    typeOfAccident: formState.TypeOfAccIdent,
                    factor: formState.Factor,
                    injuredLv: formState.InjuredLv,
                    equipmentDamageLv: formState.EquipmentDamageLv,
                    affectOfEnviroment: formState.AffectOfEnviroment,
                    newsCoverage: formState.NewsCoverage,
                    actionItems: formState.ActionItems,
                    solvedActionItems: formState.SolvedActionItems,
                    measures: calculateCategory(),
                    description: formState.Description,
                    companyCode: companyCode,
                    nearMissNo: nearMissNo // 更新時に nearMissNo を送信
                };

                let response;

                if (nearMissNo) {
                    // nearMissNo が存在する場合は更新 (PUT)
                    response = await axios.put(`http://127.0.0.1:8000/api/nearMiss/nearMissList/${nearMissNo}/`, postData);
                } else {
                    // nearMissNo が存在しない場合は新規作成 (POST)
                    response = await axios.post('http://127.0.0.1:8000/api/nearMiss/nearMissList/', postData);
                }

                // 成功時にアラートを表示
                alertType.value = 'success';
                alertMessage.value = `Near Miss has been ${nearMissNo ? 'updated' : 'saved'} successfully!`;
                showAlert.value = true;

                resetForm(); // フォームをリセット
            } catch (error) {
                alertType.value = 'error';
                alertMessage.value = `Failed to ${nearMissNo ? 'update' : 'save'} the Near Miss entry.`;
                showAlert.value = true;

                console.error('Error during form submission:', error);
            }
        };

        return {
            lastNearMissNo,
            formState,
            errorMessagesState,
            showError,
            validateForm,
            submitForm,
            calculateCategory,
            getButtonSeverity,
            showAlert, // 追加
            alertType, // 追加
            alertMessage, // 追加
            errorMessages, // 追加
            isEditing, // 編集モードの状態を返す
            initializeForm // 初期化関数を返す
        };
    },
    data() {
        return {
            accidentTypes: [
                'fall down',
                'fall/slip',
                'collision',
                'accidental fall',
                'collapse',
                'hit by something',
                'got caught up in',
                'cut/Rubbing',
                'treading on something sharp',
                'drown',
                'contact with hot or cold objects',
                'contact with organic matter',
                'electric shock',
                'explosion',
                'rupture',
                'conflagration',
                'traffic accident',
                'impossible movement',
                'protective equipment violation',
                'others'
            ],
            factors: ['Person', 'Rule', 'Equipment', 'Methods', 'Others'],
            injuredLevels: ['A', 'B', 'C', 'D', 'E'],
            equipmentDamageLevels: ['A', 'B', 'C', 'D', 'E'],
            affectOfEnviromentLevels: ['A', 'B', 'C', 'D', 'E'],
            newsCoverageLevels: ['A', 'B', 'C', 'D', 'E']
        };
    }
};
</script>

<style scoped>
/* 共通スタイル */
.inputfield {
    width: 100%;
}

.errorMessages {
    color: red;
    list-style-type: none;
    padding: 0;
}

textarea {
    resize: vertical;
}

/* ラベルとエラーメッセージ */
.form-label {
    font-size: 1.5em; /* フォントサイズを大きく */
    font-weight: bold;
}

.error-message {
    color: red;
    font-size: 1.2em;
    margin-bottom: 10px;
}

.input-error {
    border: 1px solid red;
}

/* コンテナスタイル */
.form-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 33%;
}

.flex-wrap {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

/* リスクレベルと矢印のスタイル */
.risk-level {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 10px;
    width: 100%;
}

.risk-label {
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 5px;
    text-align: center;
    width: 100%;
}

.risk-arrows {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 0 10px;
}

.arrow-label {
    font-size: 1.2em;
    font-weight: bold;
}

.arrow-label.high {
    color: red;
}

.arrow-label.low {
    color: green;
}

/* HighとLowのフォントサイズを大きくして太字に */
.risk-arrows .arrow-label.high,
.risk-arrows .arrow-label.low {
    font-size: 1.5em; /* フォントサイズを大きく */
    font-weight: bold; /* 太字にする */
}

.arrow {
    font-size: 1.5em;
    font-weight: bold;
}

/* MeasuresとRisk Levelの間にスペースを追加 */
.measures-field {
    margin-bottom: 20px; /* Measuresの下に余白を追加 */
    max-width: 300px;
}

/* Define Safety Measuresスタイル */
.define-safety-measures {
    font-size: 1.2em;
    font-weight: bold;
    margin-top: 10px;
    text-align: center; /* 中央揃え */
}

/* ボタンのスタイル */
.measures-container {
    display: flex;
    justify-content: center; /* 横方向に中央揃え */
    width: 100%; /* コンテナの幅を100%に */
}

.measures-button {
    width: 200px; /* ボタンの幅を調整 */
    max-width: 100%; /* 必要に応じて幅の最大値を制限 */
    padding: 10px 20px; /* ボタン内の余白を調整 */
}

/* PrimeVueコンポーネントのスタイル */
:deep(.p-inputtext),
:deep(.p-inputtextarea) {
    font-size: 1.2em !important; /* フォントサイズを大きく */
    border: 1px solid black !important; /* 枠線を黒色に */
}

/* PrimeVueのCalendarコンポーネント */
:deep(.p-calendar .p-inputtext) {
    border: 1px solid black !important;
}

/* PrimeVueのRadioButtonラベルのフォントスタイル */
:deep(.p-radiobutton .p-radiobutton-label) {
    font-size: 1.2em !important; /* フォントサイズを大きく */
    font-weight: bold; /* 太字にする */
}

/* 事故の種類リストのラベル */
:deep(.ui.radio.checkbox label) {
    font-size: 1.2em !important; /* フォントサイズを大きく */
    font-weight: bold;
}

/* 特定の背景パターン */
#app > div > div > div.col-12.lg\:col-2 {
    background: repeating-linear-gradient(45deg, black 0, black 5%, yellow 5%, yellow 10%);
}

/* SAVEボタンのスタイルを調整して青色に変更 */
.save-button {
    font-size: 1.2em; /* フォントサイズを大きく */
    padding: 12px 24px; /* ボタンの余白を調整 */
    width: auto; /* 必要に応じてボタンの幅を調整 */
    background-color: #007bff; /* 背景色を青に設定 */
    color: white; /* テキストを白色に設定 */
    border: none; /* ボーダーを削除 */
    border-radius: 4px; /* ボタンに角丸を追加 */
    cursor: pointer; /* カーソルをポインタに変更 */
}

/* ボタンホバー時のスタイル */
.save-button:hover {
    background-color: #0056b3; /* ホバー時に濃い青に変更 */
}
</style>
