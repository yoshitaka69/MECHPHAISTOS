
<template>
    <div class="card p-fluid">
        <DataTable v-model:editingRows="editingRows" :value="products" editMode="row" dataKey="id" @row-edit-save="onRowEditSave"
            :pt="{
                table: { style: 'min-width: 50rem' },
                column: {
                    bodycell: ({ state }) => ({
                        style:  state['d_editing']&&'padding-top: 0.6rem; padding-bottom: 0.6rem'
                    })
                }
            }"
        >
            <Column field="workOrderNo" header="Work order No" style="width: 20%">
                <template #editor="{ data, field }">
                    <InputText v-model="data[field]" />
                </template>
            </Column>
            <Column field="plant" header="Plant" style="width: 20%">
                <template #editor="{ data, field }">
                    <InputText v-model="data[field]" />
                </template>
            </Column>
            <Column field="equipment" header="Equipment" style="width: 20%">
                <template #editor="{ data, field }">
                    <InputText v-model="data[field]" />
                </template>
            </Column>
            <Column field="workOrderDesc" header="Description" style="width: 20%">
                <template #editor="{ data, field }">
                    <InputText v-model="data[field]" />
                </template>
            </Column>
            <Column field="status" header="Status" style="width: 20%">
                <template #editor="{ data, field }">
                    <Dropdown v-model="data[field]" :options="statuses" optionLabel="label" optionValue="value" placeholder="Select a Status">
                        <template #option="slotProps">
                            <Tag :value="slotProps.option.value" :severity="getStatusLabel(slotProps.option.value)" />
                        </template>
                    </Dropdown>
                </template>
                <template #body="slotProps">
                    <Tag :value="slotProps.data.inventoryStatus" :severity="getStatusLabel(slotProps.data.inventoryStatus)" />
                </template>
            </Column>
            <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center"></Column>
        </DataTable>
    </div>
</template>




<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート




const userStore = useUserStore(); // Piniaストアを使用

const products = ref();
const editingRows = ref([]);
const statuses = ref([
    { label: 'In Stock', value: 'COMPLEATED' },
    { label: 'Low Stock', value: 'Ongoing' },
    { label: 'Out of Stock', value: 'Delayed' }
]);

onMounted(async () => {
    // axiosを使用してデータを取得
    const response = await axios.get(`http://127.0.0.1:8000/api/workOrder/workOrderByCompany/?format=json&companyCode=${userStore.companyCode}`);
    // 取得したデータをフラットな配列に変換
    const flattenedData = response.data.flatMap(company => company.workOrderList);
    products.value = flattenedData; // 変換したデータをproductsにセット
    console.log('flattenedData', flattenedData);
});


const onRowEditSave = (event) => {
    let { newData, index } = event;

    products.value[index] = newData;
};


const getStatusLabel = (status) => {
    switch (status) {
        case 'COMPLETED':
            return 'success';

        case 'Ongoing':
            return 'warning';

        case 'Delayed':
            return 'danger';

        default:
            return null;
    }
};

</script>
