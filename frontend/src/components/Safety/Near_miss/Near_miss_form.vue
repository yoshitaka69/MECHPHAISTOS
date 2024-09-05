<template>
  <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
      <div class="grid">
          <div class="col-12 lg:col-2">
              <div class="text-900 font-medium text-xl mb-3">Near Miss Report</div>
              <p class="m-0 p-0 text-600 line-height-3 mr-3">Fill in the details of the near miss incident.</p>
          </div>
          <div class="col-12 lg:col-10">
              <div v-if="showError" class="error-message">*The form is incomplete.</div>
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

                  <!-- Type of Accident -->
                  <div class="field mb-4 col-12" :class="{ 'input-error': errorMessagesState.TypeOfAccIdent.length > 0 }">
                      <label for="typeOfAccIdent" class="form-label">Type of Accident</label>
                      <div class="flex flex-wrap gap-3">
                          <div v-for="(type, index) in accidentTypes" :key="index" class="field">
                              <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                  <RadioButton :name="type" :value="type" v-model="formState.TypeOfAccIdent" :tabindex="index" />
                                  <label>{{ type }}</label>
                              </div>
                          </div>
                      </div>
                      <ul class="errorMessages">
                          <li v-for="message in errorMessagesState.TypeOfAccIdent" :key="message">
                              {{ message }}
                          </li>
                      </ul>
                  </div>

                  <!-- Factor -->
                  <div class="field mb-4 col-12 lg:col-4" :class="{ 'input-error': errorMessagesState.Factor.length > 0 }">
                      <label for="factor" class="form-label">Factor</label>
                      <div class="flex flex-wrap gap-3">
                          <div v-for="(factor, index) in factors" :key="index" class="field">
                              <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                  <RadioButton :name="factor" :value="factor" v-model="formState.Factor" :tabindex="index" />
                                  <label>{{ factor }}</label>
                              </div>
                          </div>
                      </div>
                      <ul class="errorMessages">
                          <li v-for="message in errorMessagesState.Factor" :key="message">
                              {{ message }}
                          </li>
                      </ul>
                  </div>
              </div>

              <div class="grid formgrid p-fluid">
                  <div class="form-container lg:col-4">
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
                          <div class="flex justify-content-center">
                              <Button :label="calculateCategory()" :severity="getButtonSeverity(calculateCategory())" raised class="measures-button" />
                          </div>
                      </div>

                      <!-- Action Items -->
                      <div class="field mb-4 col-12" :class="{ 'input-error': errorMessagesState.ActionItems && errorMessagesState.ActionItems.length > 0 }">
                          <label for="actionItems" class="form-label">Action Items</label>
                          <Textarea id="actionItems" placeholder="Enter action items" v-model="formState.ActionItems" class="w-full" rows="4" autoResize />
                          <ul class="errorMessages">
                              <li v-for="message in errorMessagesState.ActionItems" :key="message">
                                  {{ message }}
                              </li>
                          </ul>
                      </div>

                      <!-- Solved Action Items -->
                      <div class="field mb-4 col-12">
                          <div class="flex align-items-center gap-2">
                              <Checkbox v-model="formState.SolvedActionItems" id="solvedActionItems" />
                              <label for="solvedActionItems" class="form-label m-0">Solved Action Items</label>
                          </div>
                          <p>＊ここはまだ入力しなくても問題なし</p>
                      </div>
                  </div>

                  <!-- Level Description -->
                  <div class="field mb-8 col-12 lg:col-8">
                      <LevelDescription />
                  </div>
              </div>

              <!-- Description -->
              <div class="field mb-4 col-12" :class="{ 'input-error': errorMessagesState.Description.length > 0 }">
                  <label for="description" class="form-label">Description</label>
                  <Textarea v-model="formState.Description" autoResize rows="6" id="description" class="w-full" />
                  <ul class="errorMessages">
                      <li v-for="message in errorMessagesState.Description" :key="message">
                          {{ message }}
                      </li>
                  </ul>
              </div>

              <div class="col-12 text-right">
                  <Button type="button" label="Save" @click="validateForm" class="w-auto mt-3"></Button>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
import { ref, reactive } from 'vue';
import axios from 'axios';
import moment from 'moment';
import { useUserStore } from '@/stores/userStore';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Calendar from 'primevue/calendar';
import RadioButton from 'primevue/radiobutton';
import Checkbox from 'primevue/checkbox';
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
    Checkbox,
    Button,
    LevelDescription
},
setup() {
    const userStore = useUserStore();
    const showError = ref(false);

    const lastNearMissNo = ref('001-testChemical-000001');
    const formState = reactive({
        NearMissNo: '',
        Date: new Date(), // デフォルトで現在の日付を設定
        Name: '',
        Department: '',
        Where: '',
        TypeOfAccIdent: '',
        Factor: '',
        InjuredLv: '',
        EquipmentDamageLv: '',
        AffectOfEnviroment: '',
        NewsCoverage: '',
        ActionItems: '',
        SolvedActionItems: false,
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
        ActionItems: [],
        Description: []
    });

    const getLastNearMissNo = async () => {
        try {
            const companyCode = userStore.companyCode;
            const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?companyCode=${companyCode}`);
            const allData = response.data;
            const companyData = allData.find((item) => item.companyCode === companyCode);

            if (companyData && companyData.nearMissList && companyData.nearMissList.length > 0) {
                const existingNumbers = companyData.nearMissList
                    .map((entry) => {
                        const match = entry.nearMissNo.match(/(\d+)-(\w+)-(\d+)$/);
                        return match ? parseInt(match[3], 10) : null;
                    })
                    .filter((num) => num !== null)
                    .sort((a, b) => a - b);

                let newNumber = 1;
                for (let i = 0; i < existingNumbers.length; i++) {
                    if (existingNumbers[i] !== newNumber) {
                        break;
                    }
                    newNumber++;
                }

                const lastNo = `${companyCode}-00${newNumber.toString().padStart(3, '0')}`;
                return lastNo;
            }

            return `${companyCode}-001`; // データがない場合は初期値を設定
        } catch (error) {
            console.error('Error getting last nearMissNo:', error.response ? error.response.data : error.message);
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

        Object.keys(formState).forEach((key) => {
            if (formState[key] === '' || formState[key] === null) {
                if (key !== 'ActionItems' && key !== 'SolvedActionItems' && key !== 'TypeOfAccIdent' && key !== 'NearMissNo') {
                    showError.value = true;
                    errorMessagesState[key] = ['This field is required'];
                    hasError = true;
                    console.log(`Validation error in field: ${key}`); // エラーのあるフィールドをコンソールに出力
                }
            } else {
                errorMessagesState[key] = [];
            }
        });

        if (!hasError) {
            submitForm();
        } else {
            console.log('Validation errors:', errorMessagesState); // すべてのエラーメッセージをコンソールに出力
        }
    };

    const getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    const submitForm = async () => {
  try {
      const userStore = useUserStore();  // userStoreを取得
      const postData = {
          nearMissNo: lastNearMissNo.value,
          userName: {
              userName: formState.Name,
              email: formState.Email  // emailがオプションフィールドであることを確認
          },
          department: formState.Department,
          dateOfOccurrence: moment(formState.Date).format('YYYY-MM-DD'),
          placeOfOccurrence: formState.Where,
          typeOfAccident: formState.TypeOfAccIdent,
          factor: formState.Factor,
          injuredLv: formState.InjuredLv,
          equipmentDamageLv: formState.EquipmentDamageLv,
          affectOfEnviroment: formState.AffectOfEnviroment,
          newsCoverage: formState.NewsCoverage,
          actionItems: formState.ActionItems,
          solvedActionItems: formState.SolvedActionItems,
          measures: calculateCategory(),
          description: formState.Description,
          companyCode: userStore.companyCode  // useUserStore内のcompanyCodeを使用
      };

      console.log("Sending data:", postData);

      const response = await axios.post('http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/', postData, {
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCookie('csrftoken')
          }
      });

      console.log(response.data);
      resetForm();
  } catch (error) {
      if (error.response) {
          console.error('Error submitting form:', error.response.data);
      } else if (error.request) {
          console.error('Error submitting form:', error.request);
      } else {
          console.error('Error submitting form:', error.message);
      }
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
            ActionItems: '',
            SolvedActionItems: false,
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
  max-width: 300px;
}

.measures-button {
  width: 100%;
}

textarea {
  resize: vertical;
}
</style>