<template>
    <div class="card card-mb0 custom-height"> <!-- 高さを設定するためのクラスを追加 -->
        <div class="flex justify-content-between mb-3" style="height: auto;">
            <span class="block text-500 font-medium mb-3 large-title">Next Month Top 3 Tasks</span>
        </div>

        <!-- top-tasks-wrapperをNext Month Top 3 Tasksの下に配置 -->
        <div class="top-tasks-wrapper">
            <div v-for="index in 3" :key="index" class="task-item">
                <div class="task-header">
                    <!-- index に応じて異なるアイコンを表示 -->
                    <i :class="getIconClass(index)" class="task-icon"></i>
                    No.{{ index }}
                </div>
                <div class="task-plant">Plant: {{ topTasks[index - 1]?.plant || 'No plant' }}</div>
                <div class="task-name">Task: {{ topTasks[index - 1]?.taskName || 'No task name' }}</div>
                <div class="task-cost">Cost: {{ topTasks[index - 1]?.totalCost || 0 }} USD</div>
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
        const topTasks = ref([
            { plant: '', taskName: '', totalCost: 0 },
            { plant: '', taskName: '', totalCost: 0 },
            { plant: '', taskName: '', totalCost: 0 }
        ]); // 空のデータで初期化

        const fetchTopTasks = async () => {
            const companyCode = userStore.companyCode; // PiniaからcompanyCodeを取得
            const url = `http://127.0.0.1:8000/api/task/taskListByCompany/?format=json&companyCode=${companyCode}`;
            const currentDate = new Date();
            const nextMonth = currentDate.getMonth() + 1 === 12 ? 0 : currentDate.getMonth() + 1;
            const nextYear = currentDate.getMonth() + 1 === 12 ? currentDate.getFullYear() + 1 : currentDate.getFullYear();

            try {
                const response = await axios.get(url);
                const tasks = response.data.find((item) => item.companyCode === companyCode)?.taskList || [];

                // 翌月のタスクをフィルタリング
                const nextMonthTasks = tasks.filter((task) => {
                    const nextEventDate = new Date(task.nextEventDate);
                    return nextEventDate.getMonth() === nextMonth && nextEventDate.getFullYear() === nextYear;
                });

                // コストが高い順に並び替えて上位3件を取得
                topTasks.value = nextMonthTasks.sort((a, b) => parseFloat(b.totalCost) - parseFloat(a.totalCost)).slice(0, 3);

                // データが足りない場合、空のデータで補う
                while (topTasks.value.length < 3) {
                    topTasks.value.push({ plant: '', taskName: '', totalCost: 0 });
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        // 異なるアイコンを返す関数
        const getIconClass = (index) => {
            if (index === 1) {
                return 'pi pi-crown'; // No.1のアイコン
            } else if (index === 2) {
                return 'pi pi-star'; // No.2のアイコン
            } else {
                return 'pi pi-heart'; // No.3のアイコン
            }
        };

        onMounted(fetchTopTasks);

        return { topTasks, getIconClass };
    }
};
</script>

<style scoped>
/* カードの高さを設定 */
.custom-height {
    height: 300px; /* カスタム高さを指定 */
}

.large-title {
    font-size: 2rem; /* フォントサイズを大きく */
    font-weight: bold; /* 太字 */
}

.top-tasks-wrapper {
    display: flex; /* 横並びに配置 */
    gap: 2rem; /* 各タスクの間にスペースを追加 */
    justify-content: center; /* 横方向に中央寄せ */
}

.task-item {
    background-color: #f4f4f4; /* 背景色を設定 */
    padding: 1rem; /* 内側の余白を追加 */
    border-radius: 0.5rem; /* 角を丸く */
    width: 30%; /* 各タスクの幅を設定 */
    text-align: center; /* テキストを中央揃え */
    margin-bottom: 2rem; /* 各タスクの下にスペースを追加 */
}

.task-header {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
}

.task-icon {
    margin-right: 0.5rem; /* アイコンとテキストの間にスペースを追加 */
    font-size: 1.5rem; /* アイコンのサイズを調整 */
}

.task-plant,
.task-name,
.task-cost {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}
</style>
