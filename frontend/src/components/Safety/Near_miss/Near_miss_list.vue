
<template>
    <button id="show-modal" @click="showModal = true">Show Modal</button>
    <Teleport to="body">
        <!-- use the modal component, pass in the prop -->
        <modal :show="showModal" @close="showModal = false">
        </modal>
    </Teleport>
    <div>
        <span>search field:</span>
        <select v-model="searchField">
            <option value="name">Name</option>
            <option value="department">Department</option>
            <option value="Date">Date</option>
            <option value="Where">where</option>
            <option value="typeOfAccident">Factor</option>
            <option value="description">Date</option>
            <option value="factor">Factor</option>
        </select>
        <span>&nbsp;&nbsp;</span> <!-- ここに空白を挿入 -->
        <span>search value:</span>
        <input type="text" v-model="searchValue">

        <br><br>
        <EasyDataTable buttons-pagination :headers="headers" :items="items" alternating :search-field="searchField"
            :search-value="searchValue" :sort-by="sortBy" :sort-type="sortType" multi-sort>
            <template #item-description="item">
                <span>
                    {{ item.description }}
                </span>
            </template>

            <template #item-user.name="item">
                <span>
                    {{ item.user.name }}
                </span>
            </template>
        </EasyDataTable>
    </div>
</template>

<script lang="ts" setup>
import type { Header, Item, SortType } from "vue3-easy-data-table";
import { onMounted, ref } from "vue";
import axios from "axios";
import Modal from '@/components/Safety/Near_miss/Near_miss_form.vue'

const showModal = ref(false)

const searchField = ref('');
const searchValue = ref('');

const sortBy: string[] = ["ID No.", "Name", "Department", "Date", "where?", "Type of accident", "Description/Learning", "Factor", "Injured lv", "Equipment damage lv", "Affect of enviroment", "News coverage", "Affect of quality", "Measures",];
const sortType: SortType[] = ["desc", "asc"];

const NearMiss = ref([]);

const headers: Header[] = [
    { text: "ID No.", value: "nearMissListNo", sortable: true },
    { text: "Name", value: "userName", sortable: true },
    { text: "Department", value: "department", sortable: true },
    { text: "Date", value: "dateOfOccurrence", sortable: true },
    { text: "Where?", value: "placeOfOccurrence", sortable: true },
    { text: "Type of accident", value: "typeOfAccident", sortable: true },
    { text: "Description/Learning", value: "description", sortable: true },
    { text: "Factor", value: "factor", sortable: true },
    { text: "Injured lv.", value: "injuredLv", sortable: true },
    { text: "Equipment damage lv.", value: "equipmentDamageLv", sortable: true },
    { text: "Affect of Enviroment", value: "affectOfEnviroment", sortable: true },
    { text: "News coverage", value: "newsCoverage", sortable: true },
    { text: "Measures", value: "measures", sortable: true },
    { text: "Operation", value: "Operation" },
];

const items: Item[] = NearMiss.value;

onMounted(async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/nearMiss/');
        NearMiss.value.push(...response.data);
        console.log(response.data);
    } catch (error) {
        console.log(error);
    }
});
</script>