<template>
    <div class="spare-parts-form-container">
        <h3 class="form-title">Spare Parts Details (スペアパーツの詳細)</h3>
        
        <!-- Grid container for spare part forms -->
        <div class="part-forms-grid">
            <div v-for="(part, index) in partsList" :key="index" class="part-form">
                <div class="field">
                    <label :for="`partName-${index}`">Part Name (パーツ名)</label>
                    <InputText :id="`partName-${index}`" v-model="part.partName" placeholder="Enter part name" />
                </div>
                <div class="field">
                    <label :for="`quantity-${index}`">Quantity (数量)</label>
                    <InputText :id="`quantity-${index}`" v-model="part.quantity" placeholder="Enter quantity" type="number" />
                </div>
                <div class="field">
                    <label :for="`reason-${index}`">Reason for Use (使用理由)</label>
                    <InputText :id="`reason-${index}`" v-model="part.reason" placeholder="Enter reason" />
                </div>
                <div class="button-container">
                    <Button label="Remove Part" @click="removePart(index)" class="cancel-button" />
                </div>
            </div>
        </div>

        <!-- Add Part Button centered -->
        <div class="button-container centered">
            <Button label="Add Part" @click="addPartForm" class="save-button" />
        </div>
        
        <!-- Display added parts summary -->
        <div v-if="partsList.length" class="added-parts-list">
            <h4 class="sub-title">Added Spare Parts:</h4>
            <ul>
                <li v-for="(part, index) in partsList" :key="index">
                    {{ part.partName }} - {{ part.quantity }} ({{ part.reason }})
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';

export default {
    components: {
        InputText,
        Button,
    },
    setup() {
        // Define an array to hold multiple spare part forms
        const partsList = ref([
            { partName: '', quantity: 1, reason: '' }
        ]);

        // Add a new empty form to the partsList
        const addPartForm = () => {
            partsList.value.push({ partName: '', quantity: 1, reason: '' });
        };

        // Remove a specific part form from the list
        const removePart = (index) => {
            partsList.value.splice(index, 1);
        };

        return {
            partsList,
            addPartForm,
            removePart,
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
    max-width: 1200px; /* 拡張されたコンテナの最大幅 */
    margin: 0 auto;
}

.form-title {
    font-weight: bold;
    font-size: 20px;
    margin-bottom: 15px;
    color: #333;
}

/* Grid layout for part forms */
.part-forms-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* 横に4列 */
    gap: 20px; /* 各フォームの間隔 */
}

.part-form {
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #fff;
}

.field {
    margin-bottom: 1rem;
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

/* Center the Add Part Button */
.button-container.centered {
    justify-content: center; /* 横方向中央寄せ */
    margin-top: 20px; /* ボタンの上部にマージン */
}

.save-button {
    background-color: #007bff;
    color: white;
    font-weight: bold;
    padding: 10px 20px; /* ボタンサイズを大きくする */
    border: none;
    border-radius: 4px;
    font-size: 16px; /* フォントサイズを大きくする */
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
</style>
