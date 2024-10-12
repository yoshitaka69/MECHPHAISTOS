<template>
    <div class="card card-mb0 custom-height"> <!-- 高さを設定するためのクラスを追加 -->
        <div class="flex justify-content-between mb-3" style="height: auto;">
            <span class="block text-500 font-medium mb-3 predict-cost-text">Predict years cost</span>
        </div>

        <!-- その他のコンテンツ -->
        <div class="current-cost-wrapper">
            <i class="pi pi-dollar icon-left"></i>
            <div class="text-900 current-cost-text">${{ ppm0YearCost }}</div>
        </div>
        <div class="last-year-wrapper">
            <i class="pi pi-calendar icon-left"></i>
            <div class="text-500 smaller-bold-text right-align-text">Last year: ${{ ppm1YearCostAgo }}</div>
        </div>
        <div v-if="percentageDifference !== null" class="percentage-difference-wrapper">
            <i class="pi pi-chart-line icon-left"></i>
            <div class="percentage-difference">
                Difference:
                <span v-if="percentageDifference > 0" class="text-red-500 bold-text"> ↑ {{ percentageDifference }}% </span>
                <span v-else-if="percentageDifference < 0" class="text-blue-500 bold-text"> ↓ {{ percentageDifference }}% </span>
                <span v-else> {{ percentageDifference }}% </span>
            </div>
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
        const ppm0YearCost = ref('0.00'); // 現在のコスト
        const ppm1YearCostAgo = ref('0.00'); // 一年前のコスト
        const percentageDifference = ref(null); // 差のパーセンテージ

        const fetchData = async () => {
            const companyCode = userStore.companyCode; // PiniaからcompanyCodeを取得
            const url = `http://127.0.0.1:8000/api/junctionTable/eventYearPPMByCompany/?format=json&companyCode=${companyCode}`;

            try {
                const response = await axios.get(url);
                const data = response.data.find((item) => item.companyCode === companyCode);
                if (data && data.EventYearPPMList.length > 0) {
                    const yearData = data.EventYearPPMList[0];
                    ppm0YearCost.value = yearData.PPM0YearCost;
                    ppm1YearCostAgo.value = yearData.PPM1YearCostAgo;

                    // パーセンテージ差を計算
                    if (parseFloat(ppm1YearCostAgo.value) > 0) {
                        const diff = ((ppm0YearCost.value - ppm1YearCostAgo.value) / ppm1YearCostAgo.value) * 100;
                        percentageDifference.value = diff.toFixed(2);
                    } else {
                        percentageDifference.value = 'N/A'; // 一年前のコストがゼロの場合
                    }
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        onMounted(fetchData);

        return { ppm0YearCost, ppm1YearCostAgo, percentageDifference };
    }
};
</script>


<style scoped>
/* カードの高さを設定 */
.custom-height {
    height: 300px; /* カスタム高さを指定 */
}

.predict-cost-text {
    font-size: 2rem; /* Predict years costのフォントサイズ */
    font-weight: bold; /* 太字 */
}

.current-cost-wrapper,
.last-year-wrapper,
.percentage-difference-wrapper {
    display: flex; /* フレックスボックスで横並びに */
    align-items: center; /* アイコンとテキストの垂直位置を揃える */
    margin-bottom: 1rem; /* 行間の設定 */
    margin-left: 30px; /* 右側にインデントを追加 */
}

.icon-left {
    margin-right: 10px; /* アイコンとテキストの間に余白 */
    font-size: 1.5rem; /* アイコンのサイズを調整 */
}

.current-cost-text {
    font-size: 4rem; /* 現在のコスト用の大きいフォントサイズ */
    font-weight: bold; /* 太字 */
}

.smaller-bold-text {
    font-size: 2rem; /* 一年前のコスト用のフォントサイズ */
    font-weight: bold; /* 太字 */
}

.right-align-text {
    text-align: right; /* 右寄せ */
    display: block; /* ブロック表示で右寄せ */
}

.percentage-difference {
    margin-top: 0.5rem;
    font-size: 1.5rem; /* パーセンテージのフォントサイズを一回り大きく */
}

.text-red-500 {
    color: red;
}

.text-blue-500 {
    color: blue;
}

.bold-text {
    font-weight: bold; /* 矢印とパーセンテージを太字に */
}


</style>