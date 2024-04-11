<template>
	<div class="card mb-0">
        <div v-for="(equipment, index) in equipments" :key="index" class="equipment-item">
		    <div class="text-900 font-medium text-xl">{{ equipment }}</div>
        </div>
	</div>
</template>

<script>
import { defineComponent } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

export default defineComponent({
    data() {
        return {
            equipments: []
        };
    },
    async mounted() {
        const userStore = useUserStore();
        const companyCode = userStore.companyCode;
        const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${companyCode}`;
        
        try {
            const response = await axios.get(url);
            const data = response.data;
            
            // データを加工して、ランキング形式の equipment リストを生成
            this.equipments = data
                .sort((a, b) => b.countOfPM04 - a.countOfPM04)
                .slice(0, 20)
                .map(item => item.equipment);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
});
</script>
