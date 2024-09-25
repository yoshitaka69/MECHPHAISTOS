<template>
    <div class="spare-parts-form">
        <h3>Spare Parts Details (スペアパーツの詳細)</h3>
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
        <Button label="Add Part" @click="addPart" />
        <div v-if="spareParts.length">
            <h4>Added Spare Parts:</h4>
            <ul>
                <li v-for="(part, index) in spareParts" :key="index">
                    {{ part.partName }} - {{ part.quantity }} ({{ part.reason }})
                    <Button label="Remove" @click="removePart(index)" />
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
.spare-parts-form {
    margin-top: 20px;
}
</style>
