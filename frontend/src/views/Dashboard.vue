<template>
    <div class="grid">
        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3" style="height: 150px">
                    <Cards_Priority_tasks />
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3" style="height: 150px">
                    <Cards_Bad_actor />
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3" style="height: 150px">
                    <Cards_Danger_area />
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3" style="height: 150px">
                    <Cards_Repairing_cost_per_year />
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-12 xl:col-12">
            <div class="card mb-0">
                <div class="total-graph">
                    <h5>Repairing Cost</h5>
                    <Total_graph />
                </div>
                <div class="repairing-cost">
                    <Display_repairing_cost />
                </div>
            </div>
        </div>

        <div class="col-12 xl:col-12">
            <div class="card">
                <h5>Trend & Demand</h5>
                <Trend_map />
            </div>
        </div>

        <div class="card">
            <div class="flex justify-content-between align-items-center mb-5">
                <h5>Priority Tasks</h5>
                <div>
                    <Button icon="pi pi-ellipsis-v" class="p-button-text p-button-plain p-button-rounded" @click="$refs.menu2.toggle($event)"></Button>
                    <Menu ref="menu2" :popup="true" :model="items"></Menu>
                </div>
            </div>
            <ul class="list-none p-0 m-0">
                <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                    <div>
                        <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Space T-Shirt</span>
                        <div class="mt-1 text-600">Clothing</div>
                    </div>
                    <div class="mt-2 md:mt-0 flex align-items-center">
                        <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                            <div class="bg-orange-500 h-full" style="width: 50%"></div>
                        </div>
                        <span class="text-orange-500 ml-3 font-medium">%50</span>
                    </div>
                </li>
                <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                    <div>
                        <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Portal Sticker</span>
                        <div class="mt-1 text-600">Accessories</div>
                    </div>
                    <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                        <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                            <div class="bg-cyan-500 h-full" style="width: 16%"></div>
                        </div>
                        <span class="text-cyan-500 ml-3 font-medium">%16</span>
                    </div>
                </li>
                <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                    <div>
                        <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Supernova Sticker</span>
                        <div class="mt-1 text-600">Accessories</div>
                    </div>
                    <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                        <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                            <div class="bg-pink-500 h-full" style="width: 67%"></div>
                        </div>
                        <span class="text-pink-500 ml-3 font-medium">%67</span>
                    </div>
                </li>
                <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                    <div>
                        <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Wonders Notebook</span>
                        <div class="mt-1 text-600">Office</div>
                    </div>
                    <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                        <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                            <div class="bg-green-500 h-full" style="width: 35%"></div>
                        </div>
                        <span class="text-green-500 ml-3 font-medium">%35</span>
                    </div>
                </li>
                <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                    <div>
                        <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Mat Black Case</span>
                        <div class="mt-1 text-600">Accessories</div>
                    </div>
                    <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                        <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                            <div class="bg-purple-500 h-full" style="width: 75%"></div>
                        </div>
                        <span class="text-purple-500 ml-3 font-medium">%75</span>
                    </div>
                </li>
                <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                    <div>
                        <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Robots T-Shirt</span>
                        <div class="mt-1 text-600">Clothing</div>
                    </div>
                    <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                        <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                            <div class="bg-teal-500 h-full" style="width: 40%"></div>
                        </div>
                        <span class="text-teal-500 ml-3 font-medium">%40</span>
                    </div>
                </li>
            </ul>
        </div>
        <div class="col-12 xl:col-6">
            <!--Safety indicator-->
            <div class="card">
                <h5>Safety Indicators</h5>
                <Safety_indicator />
            </div>

            <div class="card">
                <h5>NearMiss Rate</h5>
                <Safety_rate />
            </div>

            <div class="card">
                <h5>NearMiss Rate</h5>
                <Safety_correlation_diagram />
            </div>

            <div class="card">
                <h5>Energy</h5>
                <Energy_waterfall />
            </div>

            <div class="card">
                <div class="flex align-items-center justify-content-between mb-4">
                    <h5>Work Order</h5>
                    <div>
                        <Button icon="pi pi-ellipsis-v" class="p-button-text p-button-plain p-button-rounded" @click="$refs.menu1.toggle($event)"></Button>
                        <Menu ref="menu1" :popup="true" :model="items"></Menu>
                    </div>
                </div>

                <span class="block text-600 font-medium mb-3">TODAY</span>
                <ul class="p-0 mx-0 mt-0 mb-4 list-none">
                    <li class="flex align-items-center py-2 border-bottom-1 surface-border">
                        <div class="w-3rem h-3rem flex align-items-center justify-content-center bg-blue-100 border-circle mr-3 flex-shrink-0">
                            <i class="pi pi-dollar text-xl text-blue-500"></i>
                        </div>
                        <span class="text-900 line-height-3"
                            >Richard Jones
                            <span class="text-700">has purchased a blue t-shirt for <span class="text-blue-500">79$</span></span>
                        </span>
                    </li>
                    <li class="flex align-items-center py-2">
                        <div class="w-3rem h-3rem flex align-items-center justify-content-center bg-orange-100 border-circle mr-3 flex-shrink-0">
                            <i class="pi pi-download text-xl text-orange-500"></i>
                        </div>
                        <span class="text-700 line-height-3">Your request for withdrawal of <span class="text-blue-500 font-medium">2500$</span> has been initiated.</span>
                    </li>
                </ul>

                <span class="block text-600 font-medium mb-3">YESTERDAY</span>
                <ul class="p-0 m-0 list-none">
                    <li class="flex align-items-center py-2 border-bottom-1 surface-border">
                        <div class="w-3rem h-3rem flex align-items-center justify-content-center bg-blue-100 border-circle mr-3 flex-shrink-0">
                            <i class="pi pi-dollar text-xl text-blue-500"></i>
                        </div>
                        <span class="text-900 line-height-3"
                            >Keyser Wick
                            <span class="text-700">has purchased a black jacket for <span class="text-blue-500">59$</span></span>
                        </span>
                    </li>
                    <li class="flex align-items-center py-2 border-bottom-1 surface-border">
                        <div class="w-3rem h-3rem flex align-items-center justify-content-center bg-pink-100 border-circle mr-3 flex-shrink-0">
                            <i class="pi pi-question text-xl text-pink-500"></i>
                        </div>
                        <span class="text-900 line-height-3"
                            >Jane Davis
                            <span class="text-700">has posted a new questions about your product.</span>
                        </span>
                    </li>
                </ul>
            </div>
            <div
                class="px-4 py-5 shadow-2 flex flex-column md:flex-row md:align-items-center justify-content-between mb-3"
                style="border-radius: 1rem; background: linear-gradient(0deg, rgba(0, 123, 255, 0.5), rgba(0, 123, 255, 0.5)), linear-gradient(92.54deg, #1c80cf 47.88%, #ffffff 100.01%)"
            >
                <div>
                    <div class="text-blue-100 font-medium text-xl mt-2 mb-3">TAKE THE NEXT STEP</div>
                    <div class="text-white font-medium text-5xl">Try PrimeBlocks</div>
                </div>
                <div class="mt-4 mr-auto md:mt-0 md:mr-0">
                    <a href="https://www.primefaces.org/primeblocks-vue" class="p-button font-bold px-5 py-3 p-button-warning p-button-rounded p-button-raised"> Get Started </a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Trend_map from '@/components/Trend_map/Trend_map.vue';
import Safety_indicator from '@/components/Safety/Safety_indicator.vue';
import Safety_rate from '@/components/Safety/Safety_factor_rate.vue';
import Safety_correlation_diagram from '@/components/Safety/Safety_correlation_diagram.vue';

import Total_graph from '@/components/Repairing_cost/Total_graph.vue';
import Display_repairing_cost from '@/components/Repairing_cost/Cards/Display_repairing_cost.vue';

import Cards_Priority_tasks from '@/components/Critical_equipment_list/Cards/Priority_tasks.vue';
import Cards_Repairing_cost_per_year from '@/components/Repairing_cost/Cards/Repairing_cost_per_year';
import Cards_Danger_area from '@/components/Safety/Cards/Danger_area';
import Cards_Bad_actor from '@/components/Critical_equipment_list/Cards/Bad_actor.vue';

export default {
    components: {
        Trend_map,
        Safety_indicator,
        Safety_rate,
        Safety_correlation_diagram,

        Total_graph,
        Display_repairing_cost,

        Cards_Bad_actor,
        Cards_Priority_tasks,
        Cards_Repairing_cost_per_year,
        Cards_Danger_area
    }
};
</script>

<style>

.card.mb-0 {
    display: flex; /* Flexboxを有効化 */
    justify-content: space-between; /* 要素間に適切な間隔を設定 */
    align-items: stretch; /* 子要素の高さを揃える */
    width: 100%; /* 親要素の幅に合わせて100% */
}

.total-graph, .repairing-cost {
    flex: 1; /* 利用可能なスペースを等しく分ける */
    padding: 10px; /* コンテンツ周りの余白 */
    min-width: 0; /* 縮小時の挙動を正常にする */
}

@media (max-width: 768px) {
    .card.mb-0 {
        flex-direction: column; /* 小さい画面では縦並びに切り替え */
    }
}


</style>
