<style scoped>
.large-bold-text {
    font-size: 4rem; /* 更に大きいフォントサイズに調整 */
    font-weight: bold; /* 太字 */
}
</style>

<template>
    <div>
        <div>
            <span class="block text-500 font-medium mb-3">Predict years cost</span>
            <div class="text-900 large-bold-text">${{ ppm0YearCost }}</div>
        </div>
        <div class="flex align-items-center justify-content-center bg-orange-100 border-round" style="width: 2.5rem; height: 2.5rem">
            <i class="pi pi-map-marker text-orange-500 text-xl"></i>
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

export default {
    setup() {
        const userStore = useUserStore(); // PiniaのuserStoreを使用
        const ppm0YearCost = ref('0.00'); // 初期値を設定

        const fetchData = async () => {
            const companyCode = userStore.companyCode; // PiniaからcompanyCodeを取得
            const url = `http://127.0.0.1:8000/api/junctionTable/eventYearPPMByCompany/?format=json&companyCode=${companyCode}`;

            try {
                const response = await axios.get(url);
                const data = response.data.find((item) => item.companyCode === companyCode);
                if (data && data.EventYearPPMList.length > 0) {
                    ppm0YearCost.value = data.EventYearPPMList[0].PPM0YearCost; // PPM0YearCostの値を更新
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        onMounted(fetchData);

        return { ppm0YearCost };
    }
};
</script>
