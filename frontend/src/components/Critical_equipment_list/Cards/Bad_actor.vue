<template>
    <div>
        <div>
            <span class="block text-500 font-medium mb-3">Bad Actor</span>
            <div class="text-900 large-bold-text">{{ badActorCount }} items</div>
        </div>
        <br>
        <div class="flex align-items-center justify-content-center bg-orange-100 border-round" style="width: 2.5rem; height: 2.5rem">
            <i class="pi pi-map-marker text-orange-500 text-xl"></i>
        </div>
        <span class="text-green-500 font-medium">%52+ </span>
        <span class="text-500">since last week</span>
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

const badActorCount = ref(0);
const userStore = useUserStore();

onMounted(async () => {
    const companyCode = userStore.companyCode;
    if (!companyCode) {
        console.error("No company code found.");
        return;
    }

    const url = `http://127.0.0.1:8000/api/junctionTable/badActorByCompany/?format=json&companyCode=${companyCode}`;
    try {
        const response = await axios.get(url);
        console.log("API Response Data:", response.data); // Log the complete API response
        if (response.data && Array.isArray(response.data) && response.data.length > 0) {
            // Access the nested BadActorList and count non-empty badActor entries
            badActorCount.value = response.data
                .flatMap(item => item.BadActorList) // Flatten the array of BadActorList
                .reduce((count, badActorItem) => {
                    return count + (badActorItem.badActor && badActorItem.badActor.trim() !== "" ? 1 : 0);
                }, 0);
        } else {
            console.log("No data or invalid data format received");
            badActorCount.value = 0;
        }
    } catch (error) {
        console.error("Error fetching data:", error);
    }
});
</script>

<style scoped>

.large-bold-text {
    font-size: 4rem; /* 更に大きいフォントサイズに調整 */
    font-weight: bold; /* 太字 */
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 太字に設定 */
    font-size: 1.5em; /* 現在のフォントサイズの2倍 */
    color: black; /* 文字色を黒に設定 */
}
</style>
