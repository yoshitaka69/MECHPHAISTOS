<template>
  <div class="bubble-comment">
    <div class="comment-bubble">
      {{ comment }}
      <div class="comment-arrow"></div>
    </div>
    <div class="image-container">
      <img :src="imageSrc" alt="icon" class="icon" />
      <div class="image-caption">Pandora</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaのストアをインポート

// Viteではimportを使用して画像を読み込む
import imageSrc from '@/assets/pandora.jpg'; // 正しい画像のインポート方法

const comment = ref(''); // 吹き出しのコメント
const userStore = useUserStore(); // Piniaストアからユーザーストアを取得
const companyCode = userStore.companyCode; // PiniaストアからcompanyCodeを取得

// 現在の年を取得
const currentYear = new Date().getFullYear();

// パーセンテージ差を計算する関数
const calculatePercentageDifference = (actual, budget) => {
  if (budget === 0) return '不明'; // 予算が0の場合は計算できない
  return ((actual - budget) / budget * 100).toFixed(2); // 差をパーセンテージで計算
};

// APIからデータを取得する関数
const fetchData = async () => {
  try {
    // 1つ目のAPIからtotalActualCostを取得
    const actualCostResponse = await axios.get(`http://127.0.0.1:8000/api/calculation/summedActualCostByCompany/`, {
      params: {
        companyCode: companyCode,
      },
    });
    
    const companyData = actualCostResponse.data.find(item => item.companyCode === companyCode);
    let totalCosts = [];
    if (companyData && companyData.summedActualCostList.length > 0) {
      const currentYearData = companyData.summedActualCostList.filter(item => item.year === currentYear);
      if (currentYearData.length > 0) {
        totalCosts = currentYearData.map(item => parseFloat(item.totalActualCost));
      }
    }

    const totalActualCostSum = totalCosts.reduce((sum, cost) => sum + cost, 0); // 合計実際コストを計算

    // 2つ目のAPIから各plantのPPM0YearCost（今年の予算）を取得
    const budgetResponse = await axios.get(`http://127.0.0.1:8000/api/junctionTable/eventYearPPMByCompany/`, {
      params: {
        companyCode: companyCode,
      },
    });

    const ppmData = budgetResponse.data.find(item => item.companyCode === companyCode);
    let ppmCosts = [];
    if (ppmData && ppmData.EventYearPPMList.length > 0) {
      ppmCosts = ppmData.EventYearPPMList.map(item => parseFloat(item.PPM0YearCost));
    }

    const totalBudgetSum = ppmCosts.reduce((sum, cost) => sum + cost, 0); // 合計予算を計算

    // 差分をパーセンテージで計算
    const percentageDifference = calculatePercentageDifference(totalActualCostSum, totalBudgetSum);

    // 条件に応じて表示するメッセージを選択
    let message = '';
    const percentageValue = parseFloat(percentageDifference);

    if (percentageValue <= -50) {
      message = 'レビューをお勧めします。このままだと予算とかなり乖離が生じます。';
    } else if (percentageValue <= -25) {
      message = '少し修繕計画の改善が必要です。';
    } else if (percentageValue <= 0) {
      message = 'このままKeepしてください。';
    } else {
      message = 'データに誤りがあります。';
    }

    // コメントを更新
    comment.value = `今年 (${currentYear}) の各プラントの合計実際コストは ${totalCosts.join(', ')} です。予算金額 (PPM0YearCost) は ${ppmCosts.join(', ')} です。\n合計実際コストは予算に対して ${percentageDifference}% です。\n${message}`;
  } catch (error) {
    console.error('APIリクエストエラー:', error);
    comment.value = 'データの取得に失敗しました。';
  }
};

// コンポーネントがマウントされたときにデータを取得
onMounted(fetchData);
</script>

<style scoped>
.bubble-comment {
  position: relative;
  display: flex;
  align-items: stretch; /* 吹き出しと画像の高さを揃える */
  justify-content: flex-start;
  width: 100%; /* 全体の横幅を親要素一杯に広げる */
  height: 100%; /* 親要素の高さを一杯に */
}

.image-container {
  display: inline-block;
  background-color: white;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
  margin: 10px;
  height: 100%; /* 画像コンテナも親要素の高さを一杯に広げる */
}

.icon {
  width: 220px;
  height: 100%; /* 画像の高さも親要素一杯に */
}

.image-caption {
  margin-top: 10px;
  font-size: 14px;
  font-weight: bold;
}

.comment-bubble {
  background-color: white;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-grow: 1; /* 吹き出しを親コンテナ一杯に広げる */
  width: 100%; /* 横幅を親コンテナいっぱいに広げる */
  height: 100%; /* 高さを親コンテナ一杯に */
  position: relative;
  top: 20px; /* 吹き出しを少し下に移動 */
  font-size: 24px; /* 2回り大きくする */
  font-weight: bold; /* 太字に設定 */
  white-space: pre-line; /* 改行を反映 */
}

.comment-arrow {
  position: absolute;
  right: -10px; /* 矢印を吹き出しの右側にさらに寄せる */
  top: 50%;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-left: 15px solid white; /* 左側の白い部分が吹き出しの角になります */
}
</style>
