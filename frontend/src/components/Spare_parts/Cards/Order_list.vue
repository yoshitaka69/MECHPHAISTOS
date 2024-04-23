<template>
    <div class="card mb-0">
        <div class="flex justify-content-between mb-3" style="height: 100px;">
            <div>
                <span class="block text-500 font-medium mb-3">Order List</span>
                <div class="text-900 large-bold-text">{{ displayPartsDetails }}</div>
            </div>
            <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
                 style="width: 2.5rem; height: 2.5rem">
                <i class="pi pi-map-marker text-orange-500 text-xl"></i>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

const partsDetails = ref([]);
const userStore = useUserStore();

onMounted(async () => {
    const companyCode = userStore.companyCode;
    if (!companyCode) {
        console.error('No company code found.');
        return;
    }

    const url = `http://127.0.0.1:8000/api/spareParts/sparePartsByCompany/?format=json&companyCode=${companyCode}`;
    try {
        const response = await axios.get(url);
        const companyData = response.data.find(item => item.companyCode === companyCode);
        if (companyData && companyData.sparePartsList) {
            partsDetails.value = companyData.sparePartsList
                .filter(part => part.orderAlert === 'order' && part.orderSituation === false)
                .map(part => ({
                    partsName: part.partsName,
                    partsCost: part.partsCost
                }))
                .slice(0, 20); // Limit to the first 20 items
        }
    } catch (error) {
        console.error('Error fetching order parts data:', error);
    }
});

const displayPartsDetails = computed(() => {
    if (partsDetails.value.length === 0) {
        return 'No order'; // Display "No order" if there are no items
    }
    return partsDetails.value.map(part => `${part.partsName}: $${part.partsCost}`).join(', ');
});
</script>

<style scoped>

.large-bold-text {
    font-size: 1.5rem; /* 更に大きいフォントサイズに調整 */
    font-weight: bold; /* 太字 */
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 太字に設定 */
    font-size: 1.5em; /* 現在のフォントサイズの2倍 */
    color: black; /* 文字色を黒に設定 */
}
</style>

