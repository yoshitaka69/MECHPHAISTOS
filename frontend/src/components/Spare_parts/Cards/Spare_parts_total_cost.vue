<template>
    <div>
        <div>
            <span class="block text-500 font-medium mb-3">Spare Parts Total Cost</span>
            <!-- 改行が反映されるように style を追加 -->
            <div class="text-900 large-bold-text" style="white-space: pre-line;">{{ displaySpareParts }}</div>
        </div>
        <div class="flex align-items-center justify-content-center bg-purple-100 border-round" style="width: 2.5rem; height: 2.5rem">
            <i class="pi pi-comment text-purple-500 text-xl"></i>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

const sparePartsList = ref([]);
const userStore = useUserStore();

onMounted(async () => {
    const companyCode = userStore.companyCode;
    if (!companyCode) {
        console.error('No company code found.');
        return;
    }

    const url = `http://127.0.0.1:8000/api/spareParts/sparePartsManagementByCompany/?format=json&companyCode=${companyCode}`;
    try {
        const response = await axios.get(url);
        console.log('API Response Data:', response.data); 
        const companyData = response.data.find((item) => item.companyCode === companyCode);
        if (companyData && companyData.SparePartsManagementList) {
            console.log('Filtered Spare Parts Management List:', companyData.SparePartsManagementList);
            sparePartsList.value = companyData.SparePartsManagementList.sort((a, b) => b.totalSparePartsCost - a.totalSparePartsCost).slice(0, 5);
        } else {
            console.log('No Spare Parts data or invalid data format received');
            sparePartsList.value = [];
        }
    } catch (error) {
        console.error('Error fetching spare parts data:', error);
    }
});

const displaySpareParts = computed(() => {
    // 改行を反映させるために '\n' を使用
    return sparePartsList.value.map((part) => `${part.plant}: $${part.totalSparePartsCost}`).join('\n');
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
