<template>
  <div class="bg-light-gray p-4">
    <div class="text-900 font-semibold text-lg mt-3">
      Critical Equipment
    </div>
    <Divider />
    <div class="flex flex-column-reverse md:flex-row gap-5">
      <div class="flex flex-column align-items-center">
        <span class="font-medium text-900 mb-2">Equipment Picture</span>
        <img :src="imageSrc" class="equipment-image" />
        <Button
          type="button"
          icon="pi pi-pencil"
          class="p-button-rounded -mt-4"
        ></Button>
      </div>
      <div class="flex-1 flex flex-wrap content-start p-fluid text-wrap max-h-60">
        <!-- 画像の右側に配置されるフォーム -->
        <div class="w-full md:w-auto flex-auto mb-4" v-for="(field, index) in rightSideFields" :key="index">
          <label :for="field.id" class="block font-medium text-900 mb-2">{{ field.label }}</label>
          <InputText :id="field.id" v-model="field.model" type="text" />
        </div>
      </div>
    </div>
    <!-- 画像の下に配置されるフォーム -->
    <div class="flex flex-wrap content-start p-fluid text-wrap mt-4">
      <div class="w-full flex-auto mb-4" v-for="(field, index) in belowFields" :key="index + rightSideFields.length">
        <label :for="field.id" class="block font-medium text-900 mb-2">{{ field.label }}</label>
        <InputText :id="field.id" v-model="field.model" type="text" />
      </div>
      <div class="w-full">
        <Button label="Update Details" class="w-auto"></Button>
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
import noImage from "@/assets/no_image.jpg";

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

    const imageSrc = ref(noImage);

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
          (equipment) => equipment?.ceListNo?.toString() === ceListNo
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

          if (equipmentData.imageUrl) {
            imageSrc.value = equipmentData.imageUrl;
          }
        } else {
          console.error("Critical equipment not found.");
        }
      } catch (error) {
        console.error("Error fetching critical equipment details:", error);
      }
    };

    onMounted(fetchCriticalEquipmentDetails);

    const rightSideFields = [
      { id: "plant", label: "Plant", model: plant },
      { id: "equipment", label: "Equipment", model: equipment },
      { id: "machine", label: "Machine", model: machine },
      { id: "levelSetValue", label: "Level Set Value", model: levelSetValue },
      { id: "constructionPeriod", label: "Construction Period", model: constructionPeriod },
      { id: "partsDeliveryDate", label: "Parts Delivery Date", model: partsDeliveryDate },
      { id: "mttr", label: "MTTR", model: mttr },
      { id: "probabilityOfFailure", label: "Probability of Failure", model: probabilityOfFailure },
    ];

    const belowFields = [
      { id: "countOfPM02", label: "Count of PM02", model: countOfPM02 },
      { id: "latestPM02", label: "Latest PM02", model: latestPM02 },
      { id: "countOfPM03", label: "Count of PM03", model: countOfPM03 },
      { id: "latestPM03", label: "Latest PM03", model: latestPM03 },
      { id: "countOfPM04", label: "Count of PM04", model: countOfPM04 },
      { id: "latestPM04", label: "Latest PM04", model: latestPM04 },
      { id: "impactForProduction", label: "Impact for Production", model: impactForProduction },
      { id: "assessment", label: "Assessment", model: assessment },
      { id: "typicalTaskName", label: "Typical Task Name", model: typicalTaskName },
      { id: "typicalTaskCost", label: "Typical Task Cost", model: typicalTaskCost },
      { id: "typicalNextEventDate", label: "Typical Next Event Date", model: typicalNextEventDate },
      { id: "typicalSituation", label: "Typical Situation", model: typicalSituation },
      { id: "bomCode", label: "BOM Code", model: bomCode },
    ];

    return {
      rightSideFields,
      belowFields,
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
      imageSrc,
    };
  },
};
</script>

<style scoped>
.bg-light-gray {
  background-color: #f0f0f0; /* 薄い灰色の背景色 */
}

.text-wrap {
  word-wrap: break-word;
  word-break: break-word;
}

.equipment-image {
  width: 30rem;
  height: 30rem;
  border: 1px solid black; /* 細い黒い枠線を追加 */
}

.max-h-60 {
  max-height: 60rem; /* 画像の右側に配置されるエリアの最大高さを設定 */
}

.flex-wrap {
  display: flex;
  flex-wrap: wrap;
}
</style>
