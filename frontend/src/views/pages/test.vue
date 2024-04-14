<template>
    <div class="card mb-0">
        <div class="flex justify-content-between mb-3" style="height: 20px">
            <div>
                <span class="block text-500 font-medium mb-3">Spare Parts Total Cost</span>
                <div class="text-900 font-medium text-xl">152 Unread</div>
            </div>
            <div class="flex align-items-center justify-content-center bg-purple-100 border-round" style="width: 2.5rem; height: 2.5rem">
                <i class="pi pi-comment text-purple-500 text-xl"></i>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

const SparePartsTotalCost = ref(0);
const userStore = useUserStore();

onMounted(async () => {
    const companyCode = userStore.companyCode;
    if (!companyCode) {
        console.error('No company code found.');
        return;
    }

    const url = `http://127.0.0.1:8000/api/junctionTable/badActorByCompany/?format=json&companyCode=${companyCode}`;

});
</script>
