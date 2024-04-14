<template>
    <div class="card mb-0">
        <div class="flex justify-content-between mb-3" style="height: 20px">
            <div>
                <span class="block text-500 font-medium mb-3">Spare Parts Total Cost</span>
                <div class="text-900 font-medium text-xl">{{ displaySpareParts }}</div>
            </div>
            <div class="flex align-items-center justify-content-center bg-purple-100 border-round" style="width: 2.5rem; height: 2.5rem">
                <i class="pi pi-comment text-purple-500 text-xl"></i>
            </div>
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
        console.log("API Response Data:", response.data); // Log the complete API response
        const companyData = response.data.find(item => item.companyCode === companyCode);
        if (companyData && companyData.SparePartsManagementList) {
            console.log("Filtered Spare Parts Management List:", companyData.SparePartsManagementList);
            sparePartsList.value = companyData.SparePartsManagementList
                .sort((a, b) => b.totalSparePartsCost - a.totalSparePartsCost)
                .slice(0, 5);
        } else {
            console.log("No Spare Parts data or invalid data format received");
            sparePartsList.value = [];
        }
    } catch (error) {
        console.error('Error fetching spare parts data:', error);
    }
});

const displaySpareParts = computed(() => {
    return sparePartsList.value.map(part => `${part.plant}: $${part.totalSparePartsCost}`).join(', ');
});
</script>

