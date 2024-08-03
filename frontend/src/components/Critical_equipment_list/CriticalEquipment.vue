<template>
    <div>
      <div class="text-900 font-semibold text-lg mt-3">
        Critical Equipment
      </div>
      <Divider />
      <div class="flex gap-5 flex-column-reverse md:flex-row">
        <div class="flex flex-column align-items-center flex-or">
          <span class="font-medium text-900 mb-2">Equipment Picture</span>
          <img src="" class="h-10rem w-10rem" />
          <Button
            type="button"
            icon="pi pi-pencil"
            class="p-button-rounded -mt-4"
          ></Button>
        </div>
        <div class="flex-auto p-fluid">
          <div class="mb-4">
            <label for="plant" class="block font-medium text-900 mb-2">Plant</label>
            <InputText id="plant" v-model="plant" type="text" />
          </div>
          <div class="mb-4">
            <label for="equipment" class="block font-medium text-900 mb-2">Equipment</label>
            <InputText id="equipment" v-model="equipment" type="text" />
          </div>
          <div class="mb-4">
            <label for="machine" class="block font-medium text-900 mb-2">Machine</label>
            <InputText id="machine" v-model="machine" type="text" />
          </div>
          <div class="mb-4">
            <label for="levelSetValue" class="block font-medium text-900 mb-2">Level Set Value</label>
            <InputText id="levelSetValue" v-model="levelSetValue" type="text" />
          </div>
          <div class="mb-4">
            <label for="constructionPeriod" class="block font-medium text-900 mb-2">Construction Period</label>
            <InputText id="constructionPeriod" v-model="constructionPeriod" type="text" />
          </div>
          <div class="mb-4">
            <label for="partsDeliveryDate" class="block font-medium text-900 mb-2">Parts Delivery Date</label>
            <InputText id="partsDeliveryDate" v-model="partsDeliveryDate" type="text" />
          </div>
          <div class="mb-4">
            <label for="mttr" class="block font-medium text-900 mb-2">MTTR</label>
            <InputText id="mttr" v-model="mttr" type="text" />
          </div>
          <div class="mb-4">
            <label for="probabilityOfFailure" class="block font-medium text-900 mb-2">Probability of Failure</label>
            <InputText id="probabilityOfFailure" v-model="probabilityOfFailure" type="text" />
          </div>
          <div class="mb-4">
            <label for="countOfPM02" class="block font-medium text-900 mb-2">Count of PM02</label>
            <InputText id="countOfPM02" v-model="countOfPM02" type="text" />
          </div>
          <div class="mb-4">
            <label for="latestPM02" class="block font-medium text-900 mb-2">Latest PM02</label>
            <InputText id="latestPM02" v-model="latestPM02" type="text" />
          </div>
          <div class="mb-4">
            <label for="countOfPM03" class="block font-medium text-900 mb-2">Count of PM03</label>
            <InputText id="countOfPM03" v-model="countOfPM03" type="text" />
          </div>
          <div class="mb-4">
            <label for="latestPM03" class="block font-medium text-900 mb-2">Latest PM03</label>
            <InputText id="latestPM03" v-model="latestPM03" type="text" />
          </div>
          <div class="mb-4">
            <label for="countOfPM04" class="block font-medium text-900 mb-2">Count of PM04</label>
            <InputText id="countOfPM04" v-model="countOfPM04" type="text" />
          </div>
          <div class="mb-4">
            <label for="latestPM04" class="block font-medium text-900 mb-2">Latest PM04</label>
            <InputText id="latestPM04" v-model="latestPM04" type="text" />
          </div>
          <div class="mb-4">
            <label for="impactForProduction" class="block font-medium text-900 mb-2">Impact for Production</label>
            <InputText id="impactForProduction" v-model="impactForProduction" type="text" />
          </div>
          <div class="mb-4">
            <label for="assessment" class="block font-medium text-900 mb-2">Assessment</label>
            <InputText id="assessment" v-model="assessment" type="text" />
          </div>
          <div class="mb-4">
            <label for="typicalTaskName" class="block font-medium text-900 mb-2">Typical Task Name</label>
            <InputText id="typicalTaskName" v-model="typicalTaskName" type="text" />
          </div>
          <div class="mb-4">
            <label for="typicalTaskCost" class="block font-medium text-900 mb-2">Typical Task Cost</label>
            <InputText id="typicalTaskCost" v-model="typicalTaskCost" type="text" />
          </div>
          <div class="mb-4">
            <label for="typicalNextEventDate" class="block font-medium text-900 mb-2">Typical Next Event Date</label>
            <InputText id="typicalNextEventDate" v-model="typicalNextEventDate" type="text" />
          </div>
          <div class="mb-4">
            <label for="typicalSituation" class="block font-medium text-900 mb-2">Typical Situation</label>
            <InputText id="typicalSituation" v-model="typicalSituation" type="text" />
          </div>
          <div class="mb-4">
            <label for="bomCode" class="block font-medium text-900 mb-2">BOM Code</label>
            <InputText id="bomCode" v-model="bomCode" type="text" />
          </div>
          <div>
            <Button label="Update Details" class="w-auto"></Button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from "vue";
  import { useRoute } from "vue-router";
  import InputText from "primevue/inputtext";
  import Button from "primevue/button";
  import Divider from "primevue/divider";
  import axios from "axios";
  import { useUserStore } from "@/stores/userStore";
  
  export default {
    components: {
      Divider,
      InputText,
      Button,
    },
    setup() {
      const plant = ref("no data");
      const equipment = ref("no data");
      const machine = ref("no data");
      const levelSetValue = ref("no data");
      const constructionPeriod = ref("no data");
      const partsDeliveryDate = ref("no data");
      const mttr = ref("no data");
      const probabilityOfFailure = ref("no data");
      const countOfPM02 = ref("no data");
      const latestPM02 = ref("no data");
      const countOfPM03 = ref("no data");
      const latestPM03 = ref("no data");
      const countOfPM04 = ref("no data");
      const latestPM04 = ref("no data");
      const impactForProduction = ref("no data");
      const assessment = ref("no data");
      const typicalTaskName = ref("no data");
      const typicalTaskCost = ref("no data");
      const typicalNextEventDate = ref("no data");
      const typicalSituation = ref("no data");
      const bomCode = ref("no data");
  
      const route = useRoute();
  
      const fetchCriticalEquipmentDetails = async () => {
        try {
          const ceListNo = route.params.ceListNo;
          const userStore = useUserStore();
          const companyCode = userStore.companyCode;
  
          const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?companyCode=${companyCode}`;
          console.log("Fetching critical equipment details from:", url);
  
          const response = await axios.get(url);
          console.log("API response:", response.data);
  
          const equipmentData = response.data.find(
            (equipment) => equipment.ceListNo.toString() === ceListNo
          );
  
          if (equipmentData) {
            plant.value = equipmentData.plant || "no data";
            equipment.value = equipmentData.equipment || "no data";
            machine.value = equipmentData.machineName || "no data";
            levelSetValue.value = equipmentData.levelSetValue || "no data";
            constructionPeriod.value =
              equipmentData.typicalConstPeriod || "no data";
            partsDeliveryDate.value =
              equipmentData.maxPartsDeliveryTimeInBom || "no data";
            mttr.value = equipmentData.mttr || "no data";
            probabilityOfFailure.value =
              equipmentData.probabilityOfFailure || "no data";
            countOfPM02.value = equipmentData.countOfPM02 || "no data";
            latestPM02.value = equipmentData.latestPM02 || "no data";
            countOfPM03.value = equipmentData.countOfPM03 || "no data";
            latestPM03.value = equipmentData.latestPM03 || "no data";
            countOfPM04.value = equipmentData.countOfPM04 || "no data";
            latestPM04.value = equipmentData.latestPM04 || "no data";
            impactForProduction.value =
              equipmentData.impactForProduction || "no data";
            assessment.value = equipmentData.assessment || "no data";
            typicalTaskName.value = equipmentData.typicalTaskName || "no data";
            typicalTaskCost.value = equipmentData.typicalTaskCost || "no data";
            typicalNextEventDate.value =
              equipmentData.typicalNextEventDate || "no data";
            typicalSituation.value =
              equipmentData.typicalSituation || "no data";
            bomCode.value = equipmentData.bomCode || "no data";
          } else {
            console.error("Critical equipment not found.");
          }
        } catch (error) {
          console.error("Error fetching critical equipment details:", error);
        }
      };
  
      onMounted(fetchCriticalEquipmentDetails);
  
      return {
        plant,
        equipment,
        machine,
        levelSetValue,
        constructionPeriod,
        partsDeliveryDate,
        mttr,
        probabilityOfFailure,
        countOfPM02,
        latestPM02,
        countOfPM03,
        latestPM03,
        countOfPM04,
        latestPM04,
        impactForProduction,
        assessment,
        typicalTaskName,
        typicalTaskCost,
        typicalNextEventDate,
        typicalSituation,
        bomCode,
      };
    },
  };
  </script>
  