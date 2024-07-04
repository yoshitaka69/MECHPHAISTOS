<template>
  <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
    <div class="grid">
      <div class="col-12 lg:col-2">
        <div class="text-900 font-medium text-xl mb-3">Near Miss Report</div>
        <p class="m-0 p-0 text-600 line-height-3 mr-3">Fill in the details of the near miss incident.</p>
      </div>
      <div class="col-12 lg:col-10">
        <div v-if="showError" class="error-message">＊このフォームに記入が必要です</div>
        <div class="grid formgrid p-fluid">
          <div class="field mb-4 col-12">
            <label for="nearMissNo" class="form-label">NearMiss No</label>
            <p>{{ lastNearMissNo }}</p>
          </div>
          <div class="field mb-4 col-12">
            <label for="date" class="form-label">Date</label>
            <Calendar v-model="formState.Date" id="date" class="w-full" />
          </div>
          <div class="field mb-4 col-12 md:col-6" :class="{ 'input-error': errorMessagesState.Name.length > 0 }">
            <label for="name" class="form-label">Name</label>
            <InputText id="name" type="text" placeholder="write your Name" v-model="formState.Name" class="w-full" />
            <ul class="errorMessages">
              <li v-for="message in errorMessagesState.Name" :key="message">
                {{ message }}
              </li>
            </ul>
          </div>
          <div class="field mb-4 col-12 md:col-6" :class="{ 'input-error': errorMessagesState.Department.length > 0 }">
            <label for="department" class="form-label">Department</label>
            <InputText id="department" type="text" placeholder="write your department" v-model="formState.Department" class="w-full" />
            <ul class="errorMessages">
              <li v-for="message in errorMessagesState.Department" :key="message">
                {{ message }}
              </li>
            </ul>
          </div>
          <div class="field mb-4 col-12" :class="{ 'input-error': errorMessagesState.Where.length > 0 }">
            <label for="where" class="form-label">Where</label>
            <InputText id="where" type="text" placeholder="write the place" v-model="formState.Where" class="w-full" />
            <ul class="errorMessages">
              <li v-for="message in errorMessagesState.Where" :key="message">
                {{ message }}
              </li>
            </ul>
          </div>
          
          <div class="form-container">
            <div class="field mb-4 col-12">
              <label for="injuredLv" class="form-label">Injured Lv</label>
              <div class="flex flex-wrap gap-3">
                <div v-for="(level, index) in injuredLevels" :key="index" class="field">
                  <div class="ui radio checkbox d-flex gap-1 align-items-center">
                    <RadioButton :name="level" :value="level" v-model="formState.InjuredLv" :tabindex="index" />
                    <label>{{ level }}</label>
                  </div>
                </div>
              </div>
            </div>

            <div class="field mb-4 col-12">
              <label for="equipmentDamageLv" class="form-label">Equipment Damage Lv</label>
              <div class="flex flex-wrap gap-3">
                <div v-for="(level, index) in equipmentDamageLevels" :key="index" class="field">
                  <div class="ui radio checkbox d-flex gap-1 align-items-center">
                    <RadioButton :name="level" :value="level" v-model="formState.EquipmentDamageLv" :tabindex="index" />
                    <label>{{ level }}</label>
                  </div>
                </div>
              </div>
            </div>

            <div class="field mb-4 col-12">
              <label for="affectOfEnvironment" class="form-label">Affect Of Environment</label>
              <div class="flex flex-wrap gap-3">
                <div v-for="(level, index) in affectOfEnviromentLevels" :key="index" class="field">
                  <div class="ui radio checkbox d-flex gap-1 align-items-center">
                    <RadioButton :name="level" :value="level" v-model="formState.AffectOfEnviroment" :tabindex="index" />
                    <label>{{ level }}</label>
                  </div>
                </div>
              </div>
            </div>

            <div class="field mb-4 col-12">
              <label for="newsCoverage" class="form-label">News Coverage</label>
              <div class="flex flex-wrap gap-3">
                <div v-for="(level, index) in newsCoverageLevels" :key="index" class="field">
                  <div class="ui radio checkbox d-flex gap-1 align-items-center">
                    <RadioButton :name="level" :value="level" v-model="formState.NewsCoverage" :tabindex="index" />
                    <label>{{ level }}</label>
                  </div>
                </div>
              </div>
              <div class="risk-level">
                <div class="risk-label">Risk Level</div>
                <div class="risk-arrows">
                  <div class="arrow-label high">High</div>
                  <div class="arrow">←-----------------------------→</div>
                  <div class="arrow-label low">Low</div>
                </div>
              </div>
            </div>

            <div class="field mb-4 col-12 measures-field">
              <label for="measures" class="form-label">Measures</label>
              <Button :label="calculateCategory()" :severity="getButtonSeverity(calculateCategory())" raised class="measures-button" />
            </div>
          </div>
          
          <LevelDescription />

          <div class="field mb-4 col-12">
            <label for="description" class="form-label">Description</label>
            <Textarea v-model="formState.Description" autoResize rows="6" cols="160" id="description" class="w-full" />
          </div>
          <div class="col-12">
            <Button type="button" label="Cancel" severity="secondary" @click="$emit('close')" class="w-auto mt-3 mr-2"></Button>
            <Button type="button" label="Save" @click="validateForm" class="w-auto mt-3"></Button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Calendar from 'primevue/calendar';
import RadioButton from 'primevue/radiobutton';
import Button from 'primevue/button';
import LevelDescription from '@/components/Safety/Near_miss/Level_description.vue';

export default {
  props: {
    show: Boolean
  },
  components: {
    InputText,
    Textarea,
    Calendar,
    RadioButton,
    Button,
    LevelDescription
  },
  setup() {
    const userStore = useUserStore();
    const showError = ref(false);

    const lastNearMissNo = ref('001-testChemical-000001');
    const formState = reactive({
      NearMissNo: '',
      Date: null,
      Name: '',
      Department: '',
      Where: '',
      TypeOfAccIdent: '',
      Factor: '',
      InjuredLv: '',
      EquipmentDamageLv: '',
      AffectOfEnviroment: '',
      NewsCoverage: '',
      Description: ''
    });

    const errorMessagesState = reactive({
      Date: [],
      Name: [],
      Department: [],
      Where: [],
      TypeOfAccIdent: [],
      Factor: [],
      InjuredLv: [],
      EquipmentDamageLv: [],
      AffectOfEnviroment: [],
      NewsCoverage: [],
      Description: []
    });

    const getLastNearMissNo = async () => {
      try {
        const companyCode = userStore.companyCode;
        const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?companyCode=${companyCode}`);
        const allData = response.data;
        const companyData = allData.find((item) => item.companyCode === companyCode);
        if (companyData && companyData.nearMissList && companyData.nearMissList.length > 0) {
          const lastNo = companyData.nearMissList
            .map((entry) => entry.nearMissNo)
            .sort()
            .pop();
          if (lastNo) {
            const match = lastNo.match(/(\d+)-(\w+)-(\d+)$/);
            if (match) {
              const incremented = (parseInt(match[3], 10) + 1).toString().padStart(match[3].length, '0');
              return `${match[1]}-${match[2]}-${incremented}`;
            }
          }
        }
        return lastNearMissNo.value;
      } catch (error) {
        console.error('Error getting last nearMissNo:', error);
        throw error;
      }
    };

    getLastNearMissNo().then((nearMissNo) => (lastNearMissNo.value = nearMissNo));

    const calculateCategory = () => {
      const valueMapping = { A: 10, B: 8, C: 3, D: 2, E: 1 };
      const total = ['InjuredLv', 'EquipmentDamageLv', 'AffectOfEnviroment', 'NewsCoverage'].reduce((acc, key) => {
        const value = formState[key] || 'E';
        return acc + (valueMapping[formState[key]] || 0);
      }, 0);
      return total >= 11 ? 'A' : total >= 10 ? 'B' : total >= 9 ? 'C' : total >= 5 ? 'D' : 'E';
    };

    const getButtonSeverity = (category) => {
      const severityMapping = {
        A: 'danger',
        B: 'help',
        C: 'warn',
        D: 'info',
        E: 'success'
      };
      return severityMapping[category] || 'secondary';
    };

    const validateForm = () => {
      showError.value = false;
      let hasError = false;

      Object.keys(formState).forEach(key => {
        if (formState[key] === '' || formState[key] === null) {
          showError.value = true;
          errorMessagesState[key] = ['This field is required'];
          hasError = true;
        } else {
          errorMessagesState[key] = [];
        }
      });

      if (!hasError) {
        submitForm();
      }
    };

    const submitForm = async () => {
      try {
        const postData = {
          companyCode: userStore.companyCode,
          nearMissList: [
            {
              nearMissNo: lastNearMissNo.value,
              userName: {
                userName: formState.Name
              },
              department: formState.Department,
              dateOfOccurrence: formState.Date,
              placeOfOccurrence: formState.Where,
              typeOfAccident: formState.TypeOfAccIdent,
              factor: formState.Factor,
              injuredLv: formState.InjuredLv,
              equipmentDamageLv: formState.EquipmentDamageLv,
              affectOfEnviroment: formState.AffectOfEnviroment,
              newsCoverage: formState.NewsCoverage,
              measures: calculateCategory(),
              description: formState.Description
            }
          ]
        };

        const response = await axios.post('http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/', postData);

        console.log(response.data);

        resetForm();
      } catch (error) {
        console.error('Error submitting form:', error.response ? error.response.data : error.message);
      }
    };

    const resetForm = () => {
      Object.assign(formState, {
        NearMissNo: '',
        Date: null,
        Name: '',
        Department: '',
        Where: '',
        TypeOfAccIdent: '',
        Factor: '',
        InjuredLv: '',
        EquipmentDamageLv: '',
        AffectOfEnviroment: '',
        NewsCoverage: '',
        Description: ''
      });
    };

    return {
      lastNearMissNo,
      formState,
      errorMessagesState,
      showError,
      validateForm,
      submitForm,
      calculateCategory,
      getButtonSeverity
    };
  },
  data() {
    return {
      accidentTypes: [
        'fall down',
        'fall/slip',
        'collision',
        'accidental fall',
        'collapse',
        'hit by something',
        'got caught up in',
        'cut/Rubbing',
        'treading on something sharp',
        'drown',
        'contact with hot or cold objects',
        'contact with organic matter',
        'electric shock',
        'explosion',
        'rupture',
        'conflagration',
        'traffic accident',
        'impossible movement',
        'protective equipment violation',
        'others'
      ],
      factors: ['Person', 'Rule', 'Equipment', 'Methods', 'Others'],
      injuredLevels: ['A', 'B', 'C', 'D', 'E'],
      equipmentDamageLevels: ['A', 'B', 'C', 'D', 'E'],
      affectOfEnviromentLevels: ['A', 'B', 'C', 'D', 'E'],
      newsCoverageLevels: ['A', 'B', 'C', 'D', 'E']
    };
  }
};
</script>


<style scoped>
.inputfield {
  width: 100%;
}

.errorMessages {
  color: red;
  list-style-type: none;
  padding: 0;
}

.form-label {
  font-size: 1.2em;
  font-weight: bold;
}

.form-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 33%;
}

.flex-wrap {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.risk-level {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10px;
  width: 100%;
}

.risk-label {
  font-size: 1.2em;
  font-weight: bold;
  margin-bottom: 5px;
  text-align: center;
  width: 100%;
}

.risk-arrows {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 0 10px;
}

.arrow-label {
  font-size: 1.2em;
  font-weight: bold;
}

.arrow-label.high {
  color: red;
}

.arrow-label.low {
  color: green;
}

.arrow {
  font-size: 1.5em;
  font-weight: bold;
}

.error-message {
  color: red;
  font-size: 1.2em;
  margin-bottom: 10px;
}

.input-error {
  border: 1px solid red;
}

.measures-field {
  max-width: 300px; /* 適切な幅に調整 */
}

.measures-button {
  width: 100%;
}
</style>
