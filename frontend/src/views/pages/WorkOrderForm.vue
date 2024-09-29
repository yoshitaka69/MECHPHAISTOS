<template>
    <div class="work-order-form-container">
        <h3 class="form-title">Work Order Details</h3>
        <div class="field">
            <label for="workOrderNo">Work Order No. (作業指示番号)</label>
            <InputText id="workOrderNo" v-model="formData.workOrderNo" placeholder="Enter work order number" />
        </div>
        <div class="field">
            <label for="description">Description (作業の説明)</label>
            <Textarea id="description" v-model="formData.description" rows="3" autoResize placeholder="Describe the work order..." />
        </div>
        <div class="field">
            <label for="workDate">Work Date (作業日付)</label>
            <InputText id="workDate" v-model="formData.workDate" placeholder="YYYY-MM-DD" />
        </div>
        <div class="field">
            <label for="status">Status (作業ステータス)</label>
            <Dropdown id="status" v-model="formData.status" :options="statusOptions" placeholder="Select status" />
        </div>
        <div class="button-container">
            <Button label="Save" icon="pi pi-check" @click="saveForm" class="save-button" />
            <Button label="Cancel" icon="pi pi-times" @click="cancelForm" class="cancel-button" />
        </div>
    </div>
</template>

<script>
import { ref, watch } from 'vue';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';

export default {
    name: 'WorkOrderForm',
    components: {
        InputText,
        Textarea,
        Button,
        Dropdown
    },
    props: {
        modelValue: {
            type: Object,
            default: () => ({
                workOrderNo: '',
                description: '',
                workDate: '',
                status: ''
            })
        }
    },
    setup(props, { emit }) {
        // フォームデータを保持するための変数
        const formData = ref({ ...props.modelValue });

        // ステータスの選択肢を定義
        const statusOptions = [
            { label: 'Pending', value: 'Pending' },
            { label: 'In Progress', value: 'In Progress' },
            { label: 'Completed', value: 'Completed' }
        ];

        // フォームデータが変更されたら親に通知
        watch(
            formData,
            (newValue) => {
                emit('update:modelValue', newValue);
            },
            { deep: true }
        );

        // フォームのデータを保存
        const saveForm = () => {
            // 必要に応じてデータの保存処理をここに追加
            emit('update:modelValue', formData.value);
            alert('Work Order details saved.');
        };

        // フォームのデータをキャンセル（初期化）
        const cancelForm = () => {
            formData.value = { ...props.modelValue };
            alert('Form cancelled.');
        };

        return {
            formData,
            statusOptions,
            saveForm,
            cancelForm
        };
    }
};
</script>

<style scoped>
.work-order-form-container {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
}

.form-title {
    font-weight: bold;
    font-size: 20px;
    margin-bottom: 15px;
    color: #333;
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
.field textarea,
.field .p-dropdown {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}

.button-container {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
}

.save-button {
    background-color: #007bff;
    color: white;
    font-weight: bold;
    padding: 6px 12px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    transition: background-color 0.3s ease;
}

.cancel-button {
    background-color: #ff6347;
    color: white;
    font-weight: bold;
    padding: 6px 12px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    transition: background-color 0.3s ease;
}

.save-button:hover {
    background-color: #0056b3;
}

.cancel-button:hover {
    background-color: #d94e3b;
}
</style>
