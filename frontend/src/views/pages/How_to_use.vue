<template>
    <div class="base-content">
        <section class="content">
            <div class="card card-solid">
                <h1 class="title">How to Use Pages</h1>
                <ul class="list">
                    <li>
                        <font-awesome-icon :icon="['fas', 'tools']" class="icon"></font-awesome-icon>
                        <a :href="criticalEquipmentLink" target="_blank">Critical Equipment List</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'dollar-sign']" class="icon"></font-awesome-icon>
                        <a :href="repairingCostLink" target="_blank">Repairing Cost</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'exclamation-triangle']" class="icon"></font-awesome-icon>
                        <a :href="nearMissLink" target="_blank">Near Miss</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'comments']" class="icon"></font-awesome-icon>
                        <a :href="communicationsLink" target="_blank">Communications</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'calendar-alt']" class="icon"></font-awesome-icon>
                        <a :href="scheduleLink" target="_blank">Schedule</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'chart-line']" class="icon"></font-awesome-icon>
                        <a :href="trendDemandLink" target="_blank">Trend & Demand</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'clipboard-list']" class="icon"></font-awesome-icon>
                        <a :href="workOrderLink" target="_blank">Work Order</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'hand-holding-usd']" class="icon"></font-awesome-icon>
                        <a :href="benefitLink" target="_blank">Benefit</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'exclamation-circle']" class="icon"></font-awesome-icon>
                        <a :href="riskMatrixLink" target="_blank">Risk Matrix</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'cogs']" class="icon"></font-awesome-icon>
                        <a :href="sparePartsLink" target="_blank">Spare Parts</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'tasks']" class="icon"></font-awesome-icon>
                        <a :href="taskListLink" target="_blank">Task List</a>
                    </li>
                    <li>
                        <font-awesome-icon :icon="['fas', 'question-circle']" class="icon"></font-awesome-icon>
                        <a :href="pmTypeLink" target="_blank">What’s PM type</a>
                    </li>
                </ul>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    computed: {
        base() {
            return window.location.origin;
        },
        criticalEquipmentLink() {
            return `${this.base}/how_to_use/critical_equipment_list`;
        },
        repairingCostLink() {
            return `${this.base}/how_to_use/repairing_cost`;
        },
        nearMissLink() {
            return `${this.base}/how_to_use/near_miss`;
        },
        communicationsLink() {
            return `${this.base}/how_to_use/communications`;
        },
        scheduleLink() {
            return `${this.base}/how_to_use/schedule`;
        },
        trendDemandLink() {
            return `${this.base}/how_to_use/trend&demand`;
        },
        workOrderLink() {
            return `${this.base}/how_to_use/work_order`;
        },
        benefitLink() {
            return `${this.base}/how_to_use/benefit`;
        },
        riskMatrixLink() {
            return `${this.base}/how_to_use/risk_matrix`;
        },
        sparePartsLink() {
            return `${this.base}/how_to_use/spare_parts`;
        },
        taskListLink() {
            return `${this.base}/how_to_use/task_list`;
        },
        pmTypeLink() {
            return `${this.base}/what_is_pm_type`;
        }
    }
}
</script>

<style scoped>
.base-content {
    padding: 20px;
}

.title {
    font-size: 32px;
    margin-bottom: 20px;
    text-align: center;
    color: #333;
}

ul.list {
    font-size: 20px;
    line-height: 1.8;
    padding: 0;
    list-style: none;
}

ul.list li {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    padding: 10px;
    background: #e0e0e0; /* 濃い灰色に変更 */
    border-radius: 5px;
    transition: background 0.3s;
}

ul.list li:hover {
    background: #b3b3b3; /* ホバー時の色を濃く変更 */
}

ul.list .icon {
    margin-right: 10px;
    color: #007bff;
}

ul.list a {
    text-decoration: none;
    color: inherit;
    font-weight: bold;
}

ul.list a:hover {
    color: #0056b3;
}
</style>
