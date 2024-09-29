<template>
    <div class="spare-parts-form-container">
        <h3 class="form-title">Spare Parts Details (スペアパーツの詳細)</h3>
        <div class="field">
            <label for="partName">Part Name (パーツ名)</label>
            <InputText id="partName" v-model="partName" placeholder="Enter part name" />
        </div>
        <div class="field">
            <label for="quantity">Quantity (数量)</label>
            <InputText id="quantity" v-model="quantity" placeholder="Enter quantity" type="number" />
        </div>
        <div class="field">
            <label for="reason">Reason for Use (使用理由)</label>
            <InputText id="reason" v-model="reason" placeholder="Enter reason" />
        </div>
        <div class="button-container">
            <Button label="Add Part" @click="addPart" class="save-button" />
        </div>
        <div v-if="spareParts.length" class="added-parts-list">
            <h4 class="sub-title">Added Spare Parts:</h4>
            <ul>
                <li v-for="(part, index) in spareParts" :key="index">
                    {{ part.partName }} - {{ part.quantity }} ({{ part.reason }})
                    <Button label="Remove" @click="removePart(index)" class="cancel-button" />
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import { ref, watch } from 'vue';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';

export default {
    components: {
        InputText,
        Button,
    },
    props: {
        modelValue: {
            type: Object,
            default: () => ({}),
        },
    },
    setup(props, { emit }) {
        const partName = ref('');
        const quantity = ref(1);
        const reason = ref('');
        const spareParts = ref([]);

        const addPart = () => {
            if (partName.value && quantity.value > 0) {
                spareParts.value.push({
                    partName: partName.value,
                    quantity: quantity.value,
                    reason: reason.value,
                });
                clearFields();
                emit('update:modelValue', spareParts.value); // 親コンポーネントに通知
            }
        };

        const removePart = (index) => {
            spareParts.value.splice(index, 1);
            emit('update:modelValue', spareParts.value); // 親コンポーネントに通知
        };

        const clearFields = () => {
            partName.value = '';
            quantity.value = 1;
            reason.value = '';
        };

        watch(spareParts, (newVal) => {
            emit('update:modelValue', newVal); // 親コンポーネントに通知
        });

        return {
            partName,
            quantity,
            reason,
            spareParts,
            addPart,
            removePart,
            clearFields,
        };
    },
};
</script>

<style scoped>
.spare-parts-form-container {
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

.field input {
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

.added-parts-list {
    margin-top: 20px;
}

.sub-title {
    font-size: 18px;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
}

.added-parts-list ul {
    padding: 0;
    list-style-type: none;
}

.added-parts-list li {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
}

.added-parts-list li .cancel-button {
    margin-left: 10px;
}
</style>
