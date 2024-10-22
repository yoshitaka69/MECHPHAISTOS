<template>
    <div class="card card-light-yellow mb-0 custom-height"> <!-- 背景色を黄色にし、カスタム高さを指定 -->
        <div class="flex-column justify-content-between mb-3" style="height: auto;">
            <!-- 縦に並べるため、flex-columnを使用 -->
            <span class="block text-500 font-medium mb-3">Action Items</span>
            <!-- countOfActionItemsの表示 -->
            <div class="flex align-items-center mb-3"> <!-- アイコンとテキストを横並びに -->
                <i class="pi pi-exclamation-circle text-orange-500 text-4xl mr-2"></i> <!-- アイコンを大きく -->
                <div class="normal-bold-text"> <!-- フォントサイズを元に戻しました -->
                    Action Items: {{ countOfActionItems }} &nbsp;&nbsp;Solved Action Items: {{ countOfSolvedActionItems }}
                </div>
            </div>
            <!-- rateOfActionItemsの表示 -->
            <div class="flex align-items-center"> <!-- アイコンとテキストを横並びに -->
                <i class="pi pi-check-circle text-green-500 text-4xl mr-2"></i> <!-- アイコンを大きく -->
                <div class="normal-bold-text"> <!-- フォントサイズを元に戻しました -->
                    Rate of Action Items: {{ rateOfActionItems }}%
                </div>
            </div>
        </div>

        <div class="icon-container mt-4">
            <!-- アイコンコンテナ -->
            <div class="flex align-items-center justify-content-center bg-orange-100 border-round" style="width: 4rem; height: 4rem">
                <i class="pi pi-map-marker text-orange-500 text-2xl"></i> <!-- サイズアップ -->
            </div>
            <i class="pi pi-thumbs-up swing" style="font-size: 4rem; margin-left: 1rem"></i> <!-- アイコンを大きく -->
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';

export default {
    mounted() {
        this.updateFontSize();
        window.addEventListener('resize', this.updateFontSize);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.updateFontSize);
    },
    methods: {
        updateFontSize() {
            const card = this.$el.querySelector('.card');
            const textElements = this.$el.querySelectorAll('.large-bold-text');
            const maxFontSize = 24; // 最大のフォントサイズを大きく設定します。

            if (card && textElements.length > 0) {
                let fontSize = card.offsetHeight * 0.06; // 調整
                fontSize = fontSize > maxFontSize ? maxFontSize : fontSize; // フォントサイズの上限を調整します。

                textElements.forEach((element) => {
                    element.style.fontSize = `${fontSize}px`;
                });
            }
        }
    },
    setup() {
        const countOfActionItems = ref(0);
        const countOfSolvedActionItems = ref(0);
        const rateOfActionItems = ref('');

        const userStore = useUserStore();

        const fetchData = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/nearMiss/safetyIndicatorsByCompany/', {
                    params: { companyCode: userStore.companyCode }
                });
                const dataList = response.data;

                const targetData = dataList.find((data) => data.companyCode === userStore.companyCode);

                if (targetData && targetData.safetyIndicatorsList && targetData.safetyIndicatorsList.length > 0) {
                    const firstItem = targetData.safetyIndicatorsList[0];
                    countOfActionItems.value = firstItem.countOfActionItems;
                    countOfSolvedActionItems.value = firstItem.countOfSolvedActionItems;
                    rateOfActionItems.value = firstItem.rateOfActionItems;
                } else {
                    console.log('No safety indicators data available for the specified companyCode');
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        onMounted(fetchData);

        return { countOfActionItems, countOfSolvedActionItems, rateOfActionItems };
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
    font-size: 2rem; /* タイトルのフォントサイズ */
    font-weight: bold; /* 太字 */
}

.normal-bold-text {
    font-size: 1.5rem; /* Action Items部分のフォントサイズを元に戻す */
    font-weight: bold; /* 太字 */
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 見出しを太字に設定 */
    font-size: 2.5rem; /* フォントサイズをさらに大きく */
    color: black; /* 文字色を黒に設定 */
}

.icon-container {
    display: flex;
    align-items: center;
    margin-top: 1rem; /* 余白を追加 */
}

/* アイコンのアニメーション */
.swing {
    display: inline-block;
    animation: swing ease-in-out 1s infinite alternate;
}

@keyframes swing {
    0% {
        transform: rotate(-10deg);
    }
    100% {
        transform: rotate(10deg);
    }
}

/* アイコンとテキストを横並びにするためのスタイル */
.pi-exclamation-circle,
.pi-check-circle {
    margin-right: 10px; /* アイコンとテキストの間に余白 */
}
</style>
