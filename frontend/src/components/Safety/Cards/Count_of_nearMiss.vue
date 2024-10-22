<template>
    <div class="card card-light-yellow custom-height"> <!-- 背景色を黄色に変更 -->
        <div class="flex-column justify-content-between mb-3" style="height: auto;">
            <!-- 縦に並べるため、flex-columnを使用 -->
            <span class="block text-500 font-medium mb-3">Number of near misses</span>
            <div class="flex align-items-center"> <!-- アイコンと件数を横並びに -->
                <i class="pi pi-exclamation-circle text-orange-500 text-3xl mr-2"></i> <!-- 任意のアイコンを左側に追加 -->
                <div class="large-bold-text">{{ nearMissTotal }}件</div>
            </div>
        </div>

        <!-- アイコンとスタイルの調整 -->
        <div class="icon-wrapper flex align-items-center justify-content-center bg-orange-100 border-round">
            <i class="pi pi-map-marker text-orange-500 text-xl"></i>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';

export default {
    setup() {
        const nearMissTotal = ref(0);
        const userStore = useUserStore();

        const fetchNearMissData = async () => {
            try {
                console.log('Fetching data with companyCode:', userStore.companyCode);
                const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/safetyIndicatorsByCompany/`, {
                    params: { companyCode: userStore.companyCode }
                });
                console.log('Response data:', response.data);
                const data = response.data.find((d) => d.companyCode === userStore.companyCode);
                if (data && data.safetyIndicatorsList.length > 0) {
                    nearMissTotal.value = data.safetyIndicatorsList[0].totalOfNearMiss;
                } else {
                    console.log('No matching data found for companyCode:', userStore.companyCode);
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        onMounted(fetchNearMissData);

        return { nearMissTotal };
    }
};
</script>

<style scoped>
/* カードの高さを設定 */
.custom-height {
    height: 250px; /* カスタム高さを指定 */
}

/* 背景色を黄色に設定 */
.card-light-yellow {
    background-color: #fffae6; /* 淡い黄色の背景色 */
}

.large-bold-text {
    font-size: 4rem; /* 件数を大きく強調 */
    font-weight: bold; /* 太字 */
    margin-top: 1rem; /* 上に余白を追加して改行の間隔を調整 */
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 見出しを太字に設定 */
    font-size: 2rem; /* フォントサイズを大きく */
    color: black; /* 文字色を黒に設定 */
}

/* アイコンを中央に配置 */
.icon-wrapper {
    width: 3rem; 
    height: 3rem;
    margin-top: 1rem; /* 余白を追加 */
}

.pi-map-marker {
    font-size: 2rem; /* アイコンサイズ */
    color: orange; /* アイコンの色 */
}

/* アイコンと件数を横並びにするためのスタイル */
.pi-exclamation-circle {
    margin-right: 10px; /* アイコンとテキストの間に余白 */
}
</style>
