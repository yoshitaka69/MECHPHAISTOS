<template>
    <div class="grid">
        <div class="col-12 lg:col-6">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3" style="height: 450px">
                    <PlanOptimizationBenefit />
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-6">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3" style="height: 450px">
                    <ImprovementBenefit />
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-6">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3" style="height: 450px">
                    <RiskAvoidanceBenefit />
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-6">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3" style="height: 450px">
                    <VendorSelectionBenefit />
                </div>
            </div>
        </div>

        <div class="col-12">
            <div class="card">
                <h5>Advanced</h5>
            </div>
        </div>
    </div>
</template>

<script>
import PlanOptimizationBenefit from '@/components/Benefit/PlanOptimizationBenefit.vue'
import ImprovementBenefit from '@/components/Benefit/ImprovementBenefit.vue'
import RiskAvoidanceBenefit from '@/components/Benefit/RiskAvoidanceBenefit.vue'
import VendorSelectionBenefit from '@/components/Benefit/VendorSelectionBenefit.vue'


export default {
    components: {
        PlanOptimizationBenefit,
		ImprovementBenefit,
		RiskAvoidanceBenefit,
		VendorSelectionBenefit,
    }
};
</script>
