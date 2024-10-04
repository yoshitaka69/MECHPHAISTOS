<template>
    <div>
        <div class="block-category-title">Content Sections</div>
        <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
            <div class="py-4 text-center md:text-left border-round bg-cover h-20rem lg:h-30rem flex flex-column justify-content-end mb-5" :style="{ backgroundImage: `url(${Task_List_Explanation})` }">
                <div class="grid">
                    <div class="col lg:col-offset-2 px-5">
                        <div class="text-5xl font-bold text-black">Best practice tool for Task</div>
                        <p class="line-height-3 text-black text-lg text-center md:text-left mt-3">Published May 16, 2024 by Yoshitaka Noto</p>
                    </div>
                </div>
            </div>
            <!--左側のサイドのいいね！など-->
            <div class="grid">
                <div class="col-12 lg:col-2">
                    <div class="flex flex-row lg:flex-column lg:border-right-1 surface-border gap-5 mb-4 lg:px-5">
                        <div class="text-900 flex flex-row align-items-center justify-content-end">
                            <span class="font-semibold mr-3">71</span>
                            <i class="pi pi-bookmark"></i>
                        </div>
                        <div class="text-900 flex flex-row align-items-center justify-content-end">
                            <span class="font-semibold mr-3">298</span>
                            <i class="pi pi-heart"></i>
                        </div>
                        <div class="text-900 flex flex-row align-items-center justify-content-end">
                            <span class="font-semibold mr-3">34</span>
                            <i class="pi pi-comments"></i>
                        </div>
                    </div>
                </div>

                <!--メインページ-->
                <div class="col-12 lg:col lg:px-5">
                    <div class="mttr-page">
                        <h1>MTTR, MTBF, MTTFの説明</h1>

                        <!-- MTTR Section -->
                        <section>
                            <h2>MTTR（Mean Time To Repair）</h2>
                            <p>MTTRは、故障が発生した際に、修理や復旧にかかる平均時間を示します。</p>
                            <p><strong>計算式:</strong></p>
                            <p class="formula">
                                <span class="formula-label">MTTR =</span>
                                <span class="fraction">
                                    <span class="numerator">修理に要した総時間</span>
                                    <span class="divider"></span>
                                    <span class="denominator">修理回数</span>
                                </span>
                            </p>
                        </section>

                        <!-- MTBF Section -->
                        <section>
                            <h2>MTBF（Mean Time Between Failures）</h2>
                            <p>MTBFは、故障と故障の間の平均動作時間を示します。</p>
                            <p><strong>計算式:</strong></p>
                            <p class="formula">
                                <span class="formula-label">MTBF =</span>
                                <span class="fraction">
                                    <span class="numerator">総稼働時間</span>
                                    <span class="divider"></span>
                                    <span class="denominator">故障回数</span>
                                </span>
                            </p>
                        </section>

                        <!-- MTTF Section -->
                        <section>
                            <h2>MTTF（Mean Time To Failure）</h2>
                            <p>MTTFは、修理が不可能な機器や部品が故障するまでの平均時間を示します。MECHPHISTOSでは、壊れた後に修理ができない設備だけでなく、交換した部品も含めた対象にしています。</p>
                            <p>例として、ブロアのモーターが老朽化や型落ちによって交換された場合、そのモーターは修理不可能な設備としてMTTFの対象に含められます。</p>
                            <p><strong>計算式:</strong></p>
                            <p class="formula">
                                <span class="formula-label">MTTF =</span>
                                <span class="fraction">
                                    <span class="numerator">総稼働時間</span>
                                    <span class="divider"></span>
                                    <span class="denominator">故障するまでの時間</span>
                                </span>
                            </p>
                        </section>

                        <!-- Optional: Calculation form -->
                        <section>
                            <h2>MTTR, MTBF, MTTFの計算</h2>
                            <form @submit.prevent="calculateMetrics">
                                <div>
                                    <label for="totalTime">総稼働時間（時間）:</label>
                                    <input v-model="totalTime" type="number" id="totalTime" required />
                                </div>
                                <div>
                                    <label for="repairTime">修理に要した総時間（時間）:</label>
                                    <input v-model="repairTime" type="number" id="repairTime" required />
                                </div>
                                <div>
                                    <label for="failureCount">故障回数:</label>
                                    <input v-model="failureCount" type="number" id="failureCount" required />
                                </div>
                                <button type="submit">計算</button>
                            </form>

                            <div v-if="result">
                                <p>MTTR: {{ result.mttr }} 時間</p>
                                <p>MTBF: {{ result.mtbf }} 時間</p>
                                <p>MTTF: {{ result.mttf }} 時間</p>
                            </div>
                        </section>
                    </div>
                </div>

                <!--右側のポストページ-->
                <div class="col-12 lg:col-3 lg:border-left-1 surface-border">
                    <div class="p-3">
                        <div class="flex border-bottom-1 surface-border pb-4 mb-5">
                            <img :src="authorImage" alt="Author image" class="mr-3 h-5rem w-5rem" />
                            <div class="flex flex-column align-items-start">
                                <span class="text-lg text-900 font-medium mb-1">Jessica Doe</span>
                                <span class="text-600 font-medium mb-2">1.7K Followers</span>
                                <Button label="Follow" class="p-button-rounded p-button-primary"></Button>
                            </div>
                        </div>
                        <span class="text-900 font-medium text-xl block mb-5">Other Posts</span>
                        <div class="flex pb-4">
                            <img src="" alt="Post thumbnail" class="mr-3 h-5rem w-5rem" />
                            <div class="flex flex-column align-items-start">
                                <span class="text-lg text-900 font-medium mb-1">Post Title</span>
                                <span class="text-600 mb-2">Metus aliquam eleifend mi in nulla posuere。</span>
                            </div>
                        </div>
                        <div class="flex pb-4">
                            <img src="" alt="Post thumbnail" class="mr-3 h-5rem w-5rem" />
                            <div class="flex flex-column align-items-start">
                                <span class="text-lg text-900 font-medium mb-1">Post Title</span>
                                <span class="text-600 mb-2">Metus aliquam eleifend mi in nulla posuere。</span>
                            </div>
                        </div>
                        <div class="flex pb-4">
                            <img src="" alt="Post thumbnail" class="mr-3 h-5rem w-5rem" />
                            <div class="flex flex-column align-items-start">
                                <span class="text-lg text-900 font-medium mb-1">Post Title</span>
                                <span class="text-600 mb-2">Metus aliquam eleifend mi in nulla posuere。</span>
                            </div>
                        </div>
                        <div class="flex flex-column gap-3">
                            <div class="w-full h-full p-5 border-round" :style="{ backgroundImage: `linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%, #000000 100%), url('/images/blocks/content/content-8.png')` }">
                                <span class="text-white font-medium mb-3">Post Title</span>
                                <span class="text-white-alpha-70 block line-height-3">Metus aliquam eleifend mi innulla posuere。</span>
                            </div>
                            <div class="w-full h-full p-5 border-round" :style="{ backgroundImage: `linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%, #000000 100%), url('/images/blocks/content/content-9.png')` }">
                                <span class="text-white font-medium mb-3">Post Title</span>
                                <span class="text-white-alpha-70 block line-height-3">Metus aliquam eleifend mi innulla posuere。</span>
                            </div>
                            <div class="w-full h-full p-5 border-round" :style="{ backgroundImage: `linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%, #000000 100%), url('/images/blocks/content/content-10.png')` }">
                                <span class="text-white font-medium mb-3">Post Title</span>
                                <span class="text-white-alpha-70 block line-height-3">Metus aliquam eleifend mi in nulla posuere。</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Task_List_Explanation from '@/assets/Task_List_Explanation.png';
import authorImage from '@/assets/self_photo.png';

// データの定義
const totalTime = ref<number>(0);
const repairTime = ref<number>(0);
const failureCount = ref<number>(0);
const result = ref<{ mttr: number; mtbf: number; mttf: number } | null>(null);

// メソッドの定義
function calculateMetrics() {
    if (failureCount.value > 0) {
        result.value = {
            mttr: repairTime.value / failureCount.value,
            mtbf: totalTime.value / failureCount.value,
            mttf: totalTime.value / failureCount.value,
        };
    }
}
</script>

<style scoped>
.mttr-page {
    font-family: Arial, sans-serif;
    padding: 20px;
}

h1, h2 {
    color: #333;
}

/* 各セクション間の間隔を広げる */
section {
    margin-bottom: 40px; /* 下に40pxのマージンを追加 */
}

/* 数式表示のスタイル */
.formula {
    display: flex;
    align-items: center;
    font-size: 1.5em;
    margin-bottom: 10px;
}

.formula-label {
    margin-right: 10px;
}

.fraction {
    display: inline-block;
    text-align: center;
}

.numerator, .denominator {
    display: block;
    padding: 0 5px;
}

.divider {
    border-top: 2px solid #333;
    display: block;
    width: 100%;
}
</style>
