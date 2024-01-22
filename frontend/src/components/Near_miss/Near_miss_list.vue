<template>
  <EasyDataTable
    :headers="headers"
    :items="items"
  />
</template>


<script lang="ts" setup>
import type { Header, Item } from "vue3-easy-data-table";


const headers: Header[] = [
  { text: "ID No.", value: "id_No" },
  { text: "Name", value: "name"},
  { text: "Department", value: "department"},
  { text: "Date", value: "date"},
  { text: "Where?", value: "area"},
  { text: "Type of accident", value: "type_of_accident", sortable: true},
  { text: "Description/Learning", value: "context", width: 200},
  { text: "Factor", value: "factor"},
  { text: "Injured lv.", value: "injured_lv"},
  { text: "Equipment damage lv.", value: "equipment_damage_level"},
  { text: "Affect of Enviroment", value: "affect_of_enviroment"},
  { text: "News coverage", value: "news_coverage"},
  { text: "Affect of quality", value: "affect_of_quality"},
  { text: "Measures", value: "measures"},
  
];

const items: Item[] = [
  { id_No: "ex.)1", name: "Tarou Yamada", department: "MaintenanceG", date: '2023/11/01', area: "Plant A", type_of_accident: "Cut", context: "When I put my hand into the hopper inspection opening, there was a risk of cutting my hand because the surrounding metal was sharp.",factor: 'Equipment', injured_lv: "D", equipment_damage_level: "E", affect_of_enviroment: "E", news_coverage: "E", affect_of_quality: "E", measures: "E",},

  { id_No: "ex.)2", name: "Tony", department: "ProductionG", date: '2023/12/03', area: "Plant B", type_of_accident: "Hit", context: "When I left the factory, the forklift was moving at such a high speed that I almost got hit from behind.",factor: 'Rule', injured_lv: "C", equipment_damage_level: "C", affect_of_enviroment: "E", news_coverage: "E", affect_of_quality: "E", measures: "D",},

  { id_No: "ex.)3", name: "Lee", department: "LogisticG", date: '2023/12/15', area: "wastewater treatment facility", type_of_accident: "Leakage", context: "Because person forgot to close the valve at the bottom of the tank, the acid inside spilled out and flowed into the river.",factor: 'Person', injured_lv: "E", equipment_damage_level: "C", affect_of_enviroment: "A", news_coverage: "B", affect_of_quality: "E", measures: "B",},

  { id_No: "ex.)4", name: "Jon", department: "OfficeStaff", date: '2023/12/20', area: "Office", type_of_accident: "Cut", context: "When I was cutting cardboard with a utility knife at my office, the blade of the knife was still sticking out, so I cut my finger.",factor: 'Rule', injured_lv: "D", equipment_damage_level: "E", affect_of_enviroment: "E", news_coverage: "E", affect_of_quality: "E", measures: "D",},
];


</script>