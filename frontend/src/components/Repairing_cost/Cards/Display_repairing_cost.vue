<template>
    <div class="card mb-0" v-if="filteredCosts.length > 0">
        <div v-for="(cost, index) in filteredCosts" :key="index">
            <div class="flex justify-content-between mb-3">
                <div>
                    <span class="block text-500 font-medium mb-3">Repairing Cost/year</span>
                    <div class="large-bold-text">Plant&nbsp;:&nbsp; {{ cost.plant }}</div>
                    <div class="large-bold-text">Year&nbsp;:&nbsp;{{ cost.year }}</div>
                    <div class="large-bold-text">Total Actual Cost&nbsp;:&nbsp;{{ cost.totalActualCost }}
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="card mb-0" v-else>
        <span>No Data</span>
    </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';

export default {
    setup() {
        const filteredCosts = ref([]);

        const userStore = useUserStore();

        const fetchTotalActualCost = async () => {
            const currentYear = new Date().getFullYear();
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/calculation/summedActualCostByCompany/?format=json', {
                    params: { companyCode: userStore.companyCode }
                });
                const companyData = response.data.find((company) => company.companyCode === userStore.companyCode);
                if (companyData && companyData.summedActualCostList) {
                    const currentYearCosts = companyData.summedActualCostList.filter((item) => item.year === currentYear);
                    if (currentYearCosts.length > 0) {
                        filteredCosts.value = currentYearCosts; // 現在の年に一致するデータをセット
                    } else {
                        filteredCosts.value = []; // "No Data" を表示するために空の配列をセット
                    }
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        onMounted(fetchTotalActualCost);

        return { filteredCosts };
    }
};
</script>

<style scoped>

.large-bold-text {
    font-size: 3rem; /* 更に大きいフォントサイズに調整 */
    font-weight: bold; /* 太字 */
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 太字に設定 */
    font-size: 1.5em; /* 現在のフォントサイズの2倍 */
    color: black; /* 文字色を黒に設定 */
}
</style>