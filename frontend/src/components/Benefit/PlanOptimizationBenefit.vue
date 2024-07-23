<template>
    <div class="container">
        <div class="header">
            <h2>PlanOptimizationBenefit</h2>
        </div>
        <div class="content">
            <div class="content-container">
                <div class="input-group">
                    <label for="initial-cost">Initial Repair Cost: </label>
                    <input id="initial-cost" v-model="initialCost" type="number" />
                </div>
                <div class="input-group">
                    <label for="updated-cost">Updated Repair Cost: </label>
                    <input id="updated-cost" v-model="updatedCost" type="number" />
                </div>
                <div class="result-group">
                    <p>
                        Initial Repair Cost: <span>{{ initialCost }}</span>
                    </p>
                    <p>
                        Updated Repair Cost: <span>{{ updatedCost }}</span>
                    </p>
                    <p>
                        Benefit: <span>{{ benefit }}</span>
                    </p>
                </div>
                <div>
                    <RatingScale />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, computed, onMounted, watch, onUnmounted } from 'vue';
import RatingScale from './Rating_Scale.vue';

export default {
    name: 'PlanOptimizationBenefit',
    components: {
        RatingScale
    },
    setup() {
        const initialCost = ref(5000); // サンプルデータ
        const updatedCost = ref(3000); // サンプルデータ

        const benefit = computed(() => {
            return initialCost.value - updatedCost.value;
        });

        onMounted(() => {
            console.log('PlanOptimizationBenefit Component Mounted');
            console.log('Initial Cost:', initialCost.value);
            console.log('Updated Cost:', updatedCost.value);
            console.log('Benefit:', benefit.value);
        });

        onUnmounted(() => {
            console.log('PlanOptimizationBenefit Component Unmounted');
        });

        watch([initialCost, updatedCost], ([newInitialCost, newUpdatedCost]) => {
            console.log('Initial Cost changed to:', newInitialCost);
            console.log('Updated Cost changed to:', newUpdatedCost);
            console.log('Benefit changed to:', benefit.value);
        });

        return {
            initialCost,
            updatedCost,
            benefit
        };
    }
};
</script>

<style scoped>
.container {
    width: 100%;
    height: 100%;
    background-color: #f9f9f9;
    border-radius: 8px;
    padding: 16px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

.header {
    margin-bottom: 20px;
    text-align: center;
}

.input-group {
    margin-bottom: 20px;
}

.input-group label {
    font-weight: bold;
    margin-right: 10px;
}

.input-group input {
    width: 120px;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

.result-group p {
    font-size: 1.1em;
    margin: 10px 0;
}

.result-group span {
    font-weight: bold;
    color: #007bff;
}
</style>
