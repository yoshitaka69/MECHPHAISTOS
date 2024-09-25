<template>
    <div class="daily-report-container">
        <Save_Alert v-if="showAlert" :type="alertType" :message="alertMessage" />
        <div class="surface-ground">
            <div class="p-fluid flex flex-column lg:flex-row">
                <ul class="sidebar list-none m-0 p-0 flex flex-row lg:flex-column justify-content-evenly md:justify-content-between lg:justify-content-start mb-5 lg:pr-8 lg:mb-0">
                    <li>
                        <a
                            @click="selectTab('dailyReport')"
                            :class="['flex align-items-center cursor-pointer p-3 border-round custom-rounded', selectedTab === 'dailyReport' ? 'text-primary' : 'text-800', 'hover:surface-hover transition-duration-150 transition-colors']"
                        >
                            <i class="pi pi-book sidebar-icon"></i>
                            <span class="sidebar-text">Daily Report</span>
                        </a>
                    </li>
                </ul>
                <div class="surface-card p-5 shadow-2 border-round flex-auto form-container">
                    <div v-if="selectedTab === 'dailyReport'">
                        <div class="header-container">
                            <h2 class="mb-4 form-title">Daily Report</h2>
                            <div class="field recorder-field">
                                <label for="recorder">Recorder (記録者)</label>
                                <InputText id="recorder" v-model="recorder" :value="userStore.userName" placeholder="Enter recorder name" readonly />
                                <span class="date">{{ formattedDate }}</span>
                            </div>
                        </div>
                        <div class="field">
                            <label for="activity">What did you do today? (今日の活動内容は？)</label>
                            <Textarea id="activity" v-model="activity" rows="3" autoResize placeholder="Describe your activities..." />
                        </div>
                        <div class="field">
                            <label for="workOrder">Is there any work order? (作業指示はありましたか？)</label>
                            <InputText id="workOrder" v-model="workOrder" placeholder="Enter work order number" />
                        </div>
                        <div class="field">
                            <label for="maintenanceType">What is the type of maintenance? (保全の種類は何ですか？)</label>
                            <InputText id="maintenanceType" v-model="maintenanceType" placeholder="Enter maintenance type" />
                        </div>
                        <div class="field">
                            <label for="maintenanceDescription">What kind of maintenance was it? (どのような保全を行いましたか？)</label>
                            <Textarea id="maintenanceDescription" v-model="maintenanceDescription" rows="3" autoResize placeholder="Describe the maintenance..." />
                        </div>
                        <div class="field">
                            <label for="situation">Do you know what the situation was? (状況はどうでしたか？)</label>
                            <Textarea id="situation" v-model="situation" rows="3" autoResize placeholder="Describe the situation..." />
                        </div>
                        <div class="field">
                            <label for="cause">Do you know what the cause was? (原因は何だと思いますか？)</label>
                            <Textarea id="cause" v-model="cause" rows="3" autoResize placeholder="Describe the cause..." />
                        </div>
                        <div class="field">
                            <label for="sparePartsUsed">Did you use any spare parts? (スペアパーツを使用しましたか？)</label>
                            <div class="spare-parts-selection">
                                <Button label="Yes" class="yes-button custom-button-width" @click="sparePartsUsed = true" :class="{ selected: sparePartsUsed }" />
                                <Button label="No" class="no-button custom-button-width" @click="sparePartsUsed = false" :class="{ selected: !sparePartsUsed }" />
                            </div>
                        </div>
                        <!-- スペアパーツの詳細フォームを外部コンポーネントとして動的に表示 -->
                        <SparePartsForm v-if="sparePartsUsed" v-model="spareParts" />
                        <div class="field">
                            <label for="photoUpload">Upload Photo (写真をアップロード)</label>
                            <input type="file" id="photoUpload" @change="handleFileUpload" accept="image/*" />
                            <div v-if="photoPreview" class="photo-preview">
                                <img :src="photoPreview" alt="Photo Preview" class="preview-image" />
                            </div>
                        </div>
                        <div class="field">
                            <label>Handwritten Notes (手書きのメモ)</label>
                            <div class="canvas-toolbar">
                                <Button label="Pen" class="pen-button custom-button-width" @click="setPenMode" />
                                <Button label="Eraser" class="eraser-button custom-button-width" @click="setEraserMode" />
                                <Button label="Clear All" class="clear-button custom-button-width" @click="clearAll" />
                            </div>
                            <canvas ref="signatureCanvas" width="500" height="200" class="signature-pad"></canvas>
                        </div>
                        <div class="field button-container">
                            <Button label="Save" icon="pi pi-save" class="save-button custom-button-width" @click="saveReport" />
                            <Button label="Clear" icon="pi pi-times" class="clear-button custom-button-width" @click="clearAllForms" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import SignaturePad from 'signature_pad';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import Save_Alert from '@/components/Alert/Save_Alert.vue'; // Save_Alertコンポーネントのインポート
import SparePartsForm from './SparePartsForm.vue'; // スペアパーツフォームのインポート

export default {
    components: {
        InputText,
        Textarea,
        Button,
        Save_Alert, // Save_Alertコンポーネントの登録
        SparePartsForm // スペアパーツフォームの登録
    },
    setup() {
        const userStore = useUserStore(); // Piniaストアのインスタンスを取得
        const selectedTab = ref('dailyReport');
        const recorder = ref(userStore.userName); // Piniaストアからユーザー名を取得
        const companyCode = ref(userStore.companyCode); // PiniaストアからcompanyCodeを取得して定義
        const activity = ref('');
        const workOrder = ref('');
        const maintenanceType = ref('');
        const maintenanceDescription = ref('');
        const situation = ref('');
        const cause = ref('');
        const sparePartsUsed = ref(false); // スペアパーツ使用有無のフラグ
        const spareParts = ref(''); // スペアパーツの詳細データ
        const photoPreview = ref(null); // 写真プレビューのURLを保存する
        const photoFile = ref(null); // ファイルオブジェクトを保存する変数を追加
        const signaturePad = ref(null);

        // Save_Alertに使用するデータ
        const showAlert = ref(false);
        const alertType = ref('success');
        const alertMessage = ref('');

        // 日付をフォーマットする
        const formatDate = (date) => {
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return new Intl.DateTimeFormat('en-US', options).format(date);
        };

        const formattedDate = ref(formatDate(new Date())); // 現在の日付をフォーマット

        const selectTab = (tab) => {
            selectedTab.value = tab;
        };

        // ファイルが選択された時の処理
        const handleFileUpload = (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    photoPreview.value = e.target.result; // プレビュー画像のURLを設定
                };
                reader.readAsDataURL(file);
                photoFile.value = file; // 選択されたファイルを保存
            }
        };

        // ペンモードを設定
        const setPenMode = () => {
            signaturePad.value.penColor = 'black';
            signaturePad.value.minWidth = 1;
            signaturePad.value.maxWidth = 2.5;
        };

        // 消しゴムモードを設定
        const setEraserMode = () => {
            signaturePad.value.penColor = 'white';
            signaturePad.value.minWidth = 10;
            signaturePad.value.max;
        };

        // キャンバス全体をクリア
        const clearAll = () => {
            if (signaturePad.value) {
                signaturePad.value.clear();
            }
        };

        // 全フォームをクリア
        const clearAllForms = () => {
            activity.value = '';
            workOrder.value = '';
            maintenanceType.value = '';
            maintenanceDescription.value = '';
            situation.value = '';
            cause.value = '';
            spareParts.value = '';
            photoPreview.value = null;
            photoFile.value = null;
            clearAll();
        };

        // 手書きキャンバスをクリア
        const clearSignature = () => {
            if (signaturePad.value) {
                signaturePad.value.clear();
            }
        };

        const saveReport = () => {
            // `companyCode` が未定義の場合のエラーチェック
            if (!companyCode.value) {
                alertMessage.value = 'Company code is not defined.';
                alertType.value = 'error';
                showAlert.value = true;
                return;
            }

            const reportData = new FormData();

            // 日付を 'YYYY-MM-DD' 形式に変換
            const formattedDateForAPI = new Date(formattedDate.value).toISOString().split('T')[0];

            reportData.append('companyCode', companyCode.value); // companyCodeを追加
            reportData.append('recorder', recorder.value);
            reportData.append('date', formattedDateForAPI); // 修正された日付形式を使用
            reportData.append('activity', activity.value.trim()); // 空白を削除した値を追加
            reportData.append('workOrder', workOrder.value);
            reportData.append('maintenanceType', maintenanceType.value);
            reportData.append('maintenanceDescription', maintenanceDescription.value);
            reportData.append('situation', situation.value);
            reportData.append('cause', cause.value);
            reportData.append('spareParts', spareParts.value);

            // 写真や手書きメモがある場合、それをFormDataに追加
            if (photoFile.value) {
                const truncatedFileName = photoFile.value.name.slice(-100); // 100文字以内にファイル名を短縮
                const file = new File([photoFile.value], truncatedFileName, { type: photoFile.value.type });
                reportData.append('photo', file); // 短縮されたファイル名でFormDataに追加
            }
            if (signaturePad.value) {
                const dataURL = signaturePad.value.toDataURL(); // サインを画像として取得
                const blob = dataURLToBlob(dataURL); // dataURLをBlobに変換
                reportData.append('handwrittenNotes', blob, 'handwritten_notes.png');
            }

            axios
                .post('http://127.0.0.1:8000/api/workOrder/daily_reports/', reportData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then((response) => {
                    console.log('Report saved successfully:', response.data);
                    alertMessage.value = 'データが正常に保存されました。';
                    alertType.value = 'success';
                    showAlert.value = true;
                    clearFields(); // フィールドをクリア
                })
                .catch((error) => {
                    console.error('Error saving report:', error);
                    console.log('Server error response:', error.response.data); // エラーの詳細をログに出力
                    alertMessage.value = error.response?.data?.detail || 'データの保存に失敗しました。';
                    alertType.value = 'error';
                    showAlert.value = true;
                });
        };

        // dataURLをBlobに変換するヘルパー関数
        const dataURLToBlob = (dataURL) => {
            const byteString = atob(dataURL.split(',')[1]);
            const mimeString = dataURL.split(',')[0].split(':')[1].split(';')[0];
            const ab = new ArrayBuffer(byteString.length);
            const ia = new Uint8Array(ab);
            for (let i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            return new Blob([ab], { type: mimeString });
        };

        onMounted(() => {
            const canvas = document.querySelector('canvas');
            signaturePad.value = new SignaturePad(canvas, {
                penColor: 'black',
                backgroundColor: 'rgba(255, 255, 255, 0)'
            });
        });

        return {
            selectedTab,
            selectTab,
            recorder,
            companyCode, // companyCodeを追加
            activity,
            workOrder,
            maintenanceType,
            maintenanceDescription,
            situation,
            cause,
            spareParts,
            photoPreview,
            photoFile, // photoFileを追加
            handleFileUpload,
            setPenMode, // ペンモード設定
            setEraserMode, // 消しゴムモード設定
            clearSignature, // clearSignature 関数を追加
            clearAll, // キャンバス全体をクリア
            clearAllForms, // 全フォームをクリア
            saveReport,
            formattedDate,
            userStore,
            showAlert,
            alertType,
            alertMessage
        };
    }
};
</script>

<style scoped>
.daily-report-container {
    background-color: #d3d3d3; /* 濃い灰色 */
    font-family: 'Arial', sans-serif; /* フォント */
    padding: 20px;
    border-radius: 8px;
}

.form-container {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.form-title {
    font-weight: bold;
    font-size: 24px;
    color: #333;
}

.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.recorder-field {
    width: 400px;
    display: flex;
    align-items: center;
}

.field {
    margin-bottom: 1.5rem;
}

.field label {
    display: block;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: #555;
}

.field input,
.field textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}

.field textarea {
    resize: vertical;
}

.date {
    margin-left: 20px;
    font-weight: bold;
    font-size: 16px;
    color: #333;
}

.signature-pad {
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 100%;
    max-width: 500px;
    height: 200px;
}

.button-container {
    display: flex;
    justify-content: flex-end;
    gap: 10px; /* ボタン間のスペース */
}

.save-button {
    background-color: #007bff; /* 青色 */
    color: white;
    font-weight: bold;
    padding: 6px 12px; /* ボタンの横幅を通常サイズに */
    border: none;
    border-radius: 4px;
    font-size: 14px; /* ボタン内のフォントサイズを調整 */
    transition: background-color 0.3s ease;
}

.clear-button {
    background-color: #ff6347; /* トマト色 */
    color: white;
    font-weight: bold;
    padding: 6px 12px; /* ボタンの横幅を通常サイズに */
    border: none;
    border-radius: 4px;
    font-size: 14px; /* ボタン内のフォントサイズを調整 */
    transition: background-color 0.3s ease;
}

.save-button:hover {
    background-color: #0056b3; /* 濃い青色 */
}

.clear-button:hover {
    background-color: #d94e3b; /* 濃いトマト色 */
}

.photo-preview {
    margin-top: 10px;
}

.preview-image {
    max-width: 300px; /* プレビュー画像の最大幅 */
    height: auto;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.canvas-toolbar {
    display: flex;
    gap: 10px; /* ボタン間のスペース */
    margin-bottom: 10px; /* ボタンとキャンバスの間にスペースを追加 */
}

.sidebar {
    background-color: #87ceeb; /* 青空のような青色 */
    padding: 10px;
    border-radius: 8px; /* 角を丸める */
}

.custom-rounded {
    border-top-left-radius: 16px !important; /* aタグの左上角を丸める */
}

.sidebar-text {
    font-weight: bold;
    font-size: 18px;
    color: #ffffff;
}

.sidebar-icon {
    font-size: 24px; /* アイコンのサイズ */
    color: #000000; /* アイコンの色を黒に設定 */
    margin-right: 8px;
}

.custom-button-width {
    width: 100px; /* ボタンの横幅を100pxに設定 */
}
</style>
