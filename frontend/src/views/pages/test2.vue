<template>
    <Dialog v-model:visible="visible" modal header="NearMiss Form" :style="{ width: '100rem' }">
        <div class="IdGroup flex align-items-center gap-3 mb-5">
            <label>NearMiss No: {{ lastId }}</label>
        </div>
        <!--日付-->
        <div class="DateGroup flex align-items-center gap-3 mb-5">
            <label class="DateGroup_label" for="Date">Date :</label>
            <input type="Date" v-model="formState.Date" id="Date" />
        </div>
        <!--名前、部署、場所を横並びにする -->
        <div class="flex gap-3">
            <!--名前-->
            <div class="NameGroup flex align-items-center gap-3 mb-5">
                <label class="NameGroup__label" for="Name">Name :</label>
                <InputText :class="[
                    'NameGroup__input',
                    { 'NameGroup__input-error': errorMessagesState.Name.length },
                ]" type="text" id="Name" placeholder="write your Name" :value="formState.Name"
                    @input="onInputForm('Name', $event.target.value)" />
                <ul class="NameGroup__errorMessages">
                    <li v-for="message in errorMessagesState.Name" :key="message">
                        {{ message }}
                    </li>
                </ul>
            </div>

            <!--部署 -->
            <div class="DepartmentGroup flex align-items-center gap-3 mb-5">
                <label class="DepartmentGroup__label" for="Department">Department :</label>
                <InputText :class="[
                    'DepartmentGroup__input',
                    { 'DepartmentGroup__input-error': errorMessagesState.Department.length },
                ]" type="text" id="Department" placeholder="write your department" :value="formState.Department"
                    @input="onInputForm('Department', $event.target.value)" />
                <ul class="DepartmentGroup__errorMessages">
                    <li v-for="message in errorMessagesState.Department" :key="message">
                        {{ message }}
                    </li>
                </ul>
            </div>
            <!--場所-->
            <div class="WhereGroup flex align-items-center gap-3 mb-5">
                <label class="WhereGroup__label" for="Where">Where? :</label>
                <InputText :class="[
                    'WhereGroup__input',
                    { 'WhereGroup__input-error': errorMessagesState.Where.length },
                ]" type="text" id="Where" placeholder="white place" :value="formState.Where"
                    @input="onInputForm('Where', $event.target.value)" />
                <ul class="WhereGroup__errorMessages">
                    <li v-for="message in errorMessagesState.Where" :key="message">
                        {{ message }}
                    </li>
                </ul>
            </div>
        </div>
        <!--事故のタイプ-->
        <div class="TypeOfAccIdentGroup flex flex-wrap gap-3 align-items-center">
            <label class="TypeOfAccIdentGroup__label" for="TypeOfAccIdent">Type of AccIdent :</label>
            <div id="TypeOfAccIdent" class="flex flex-wrap gap-3 mb-5 align-items-center">
                <div v-for="(type, index) in accidentTypes" :key="index" class="field">
                    <div class="ui radio checkbox d-flex gap-1 align-items-center">
                        <RadioButton :name="type" :value="type" v-model="formState.TypeOfAccIdent" :tabindex="index" />
                        <label>{{ type }}</label>
                    </div>
                </div>
            </div>
        </div>



        <!-- Level_descriptionコンポーネントの挿入 -->
        <table class="level-description-table" style="display: flex; justify-content: space-between;">
            <tr>
                <td><!-- 左側の空白セル -->
                    <!--要素-->
                    <div class="FactorGroup flex flex-wrap gap-3">
                        <label>Factor :</label>
                        <div id="Factor" class="flex flex-wrap gap-3 mb-2">
                            <div v-for="(factor, index) in factors" :key="index" class="field">
                                <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                    <RadioButton :name="factor" :value="factor" v-model="formState.Factor"
                                        :tabindex="index" />
                                    <label>{{ factor }}</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- ケガのレベル -->
                    <div class="InjuredLvGroup flex flex-wrap gap-3">
                        <label>Injured Lv :</label>
                        <div id="InjuredLv" class="flex flex-wrap gap-3">
                            <div v-for="(level, index) in injuredLevels" :key="index" class="field">
                                <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                    <RadioButton :name="level" :value="level" v-model="formState.InjuredLv"
                                        :tabindex="index" />
                                    <label>{{ level }}</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- 設備損傷のレベル -->
                    <div class="EquipmentDamageLvGroup flex flex-wrap gap-3">
                        <label>Equipment Damage Lv :</label>
                        <div id="EquipmentDamageLv" class="flex flex-wrap gap-3 mb-2">
                            <div v-for="(level, index) in equipmentDamageLevels" :key="index" class="field">
                                <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                    <RadioButton :name="level" :value="level" v-model="formState.EquipmentDamageLv"
                                        :tabindex="index" />
                                    <label>{{ level }}</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- 環境への影響 -->
                    <div class="AffectOfEnviromentGroup flex flex-wrap gap-3">
                        <label>Affect Of Enviroment :</label>
                        <div id="AffectOfEnviroment" class="flex flex-wrap gap-3 mb-2">
                            <div v-for="(level, index) in affectOfEnviromentLevels" :key="index" class="field">
                                <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                    <RadioButton :name="level" :value="level" v-model="formState.AffectOfEnviroment"
                                        :tabindex="index" />
                                    <label>{{ level }}</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- メディアへの影響 -->
                    <div class="NewsCoverageGroup flex flex-wrap gap-3">
                        <label>News Coverage :</label>
                        <div id="NewsCoverage" class="flex flex-wrap gap-3 mb-2">
                            <div v-for="(level, index) in newsCoverageLevels" :key="index" class="field">
                                <div class="ui radio checkbox d-flex gap-1 align-items-center">
                                    <RadioButton :name="level" :value="level" v-model="formState.NewsCoverage"
                                        :tabindex="index" />
                                    <label>{{ level }}</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Measuresの影響 -->
                    <div class="Measures flex flex-wrap gap-3 mb-5">
                        <label>Measures : {{ calculateCategory() }}</label>
                    </div>
                </td>
                <td style="margin-left: auto; min-width: 800px;"><!-- 右側の空白セル -->
                    <Level_description />
                </td>
            </tr>
        </table>
        <!-- 詳細記入フォーム -->
        <div class="DiscriptionGroup text-center mb-6">
            <div class="flex align-items-start">
                <label for="Discription-input" class="mr-2">Description :</label>
                <br />
                <Textarea v-model="formState.Description" autoResize rows="6" cols="160" id="Discription" />
            </div>
        </div>

        <div class="flex justify-content-end gap-2">
            <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
            <Button type="button" label="Save" @click="visible = false"></Button>
        </div>
    </Dialog>
</template>


<script>
import { ref, reactive, } from "vue";
import { notBlank, atLeast } from "@/plugins/validatorOptions"
import axios from 'axios';
import Level_description from '@/components/Safety/Near_miss/Level_description.vue'


export default {

    components: {
        Level_description,
    },


    data() {
        return {
            accidentTypes: [
                'fall down', 'fall/slip', 'collision', 'accidental fall', 'collapse',
                'hit by something', 'got caught up in', 'cut/Rubbing', 'treading on something sharp',
                'drown', 'contact with hot or cold objects', 'contact with organic matter',
                'electric shock', 'explosion', 'rupture', 'conflagration', 'traffic accident',
                'impossible movement', 'protective equipment violation', 'others'
            ],
            factors: ['Person', 'Rule', 'Equipment', 'Methods', 'Others'],
            injuredLevels: ['A', 'B', 'C', 'D', 'E'],
            equipmentDamageLevels: ['A', 'B', 'C', 'D', 'E'],
            affectOfEnviromentLevels: ['A', 'B', 'C', 'D', 'E'],
            newsCoverageLevels: ['A', 'B', 'C', 'D', 'E'],
            formState: {
                TypeOfAccIdent: '',
                Factor: '',
                InjuredLv: '',
                EquipmentDamageLv: '',
                AffectOfEnviroment: '',
                NewsCoverage: ''
            }
        };
    },

    setup() {
        const lastId = ref(0);

        const getLastId = async () => {
            try {
                const response = await axios.get("http://localhost:3000/NearMiss");
                const data = response.data;

                return data.length > 0 ? Math.max(...data.map(entry => entry.id)) : 0;
            } catch (error) {
                console.error("Error getting last Id:", error);
                throw error;
            }
        };

        getLastId().then(id => lastId.value = id + 1);

        const calculateCategory = () => {
            const valueMapping = { A: 10, B: 8, C: 3, D: 2, E: 1 };
            const total = ['InjuredLv', 'EquipmentDamageLv', 'AffectOfEnviroment', 'NewsCoverage']
                .reduce((acc, key) => acc + valueMapping[formState[key]], 0);

            return total >= 11 ? 'A' : total >= 10 ? 'B' : total >= 9 ? 'C' : total >= 5 ? 'D' : 'E';
        };

        const checkValue = reactive({});
        const initialFormState = reactive({
            Id: 0,
            Date: "",
            Name: "",
            Department: "",
            Where: "",
            TypeOfAccIdent: "",
            Factor: "",
            InjuredLv: "",
            EquipmentDamageLv: "",
            AffectOfEnviroment: "",
            NewsCoverage: "",
            Description: "",
        });

        const formState = reactive({ ...initialFormState });
        const resetForm = () => {
            Object.assign(formState, initialFormState);
        };

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
            Description: [],
        });

        const validatorsState = {
            Date: [],
            Name: [notBlank()],
            Department: [atLeast(5)],
            Where: [],
            TypeOfAccIdent: [],
            Factor: [],
            InjuredLv: [],
            EquipmentDamageLv: [],
            AffectOfEnviroment: [],
            NewsCoverage: [],
            Description: [],
        };

        const onInputForm = (id, value) => {
            formState[id] = value;
            errorMessagesState[id] = validatorsState[id]
                .map((valiDate) => valiDate(value))
                .filter((msg) => msg !== "");
        };

        //axios postの用methods
        const submitForm = async () => {
            try {
                // 最後のIdを取得
                const lastIdValue = lastId.value;


                // 送信するデータの作成
                const postData = {
                    id: lastIdValue,
                    name: formState.Name,
                    department: formState.Department,
                    date: formState.Date,
                    where: formState.Where,
                    typeOfAccIdent: formState.TypeOfAccIdent,
                    description: formState.Description,
                    factor: formState.Factor,
                    injuredLv: formState.InjuredLv,
                    equipmentDamageLv: formState.EquipmentDamageLv,
                    affectOfEnviroment: formState.AffectOfEnviroment,
                    newsCoverage: formState.NewsCoverage,
                    measures: calculateCategory(),
                    // 他のフォームフィールド ...
                };

                console.log("postData:", postData);  // この行を追加
                console.log("postData before axios.post:", postData);
                // Axiosを使用してPOSTリクエストを送信
                const response = await axios.post("http://localhost:3000/NearMiss", postData);

                // レスポンスの処理（成功時の処理）
                console.log(response.data);

                // lastIdを更新
                lastId.value += 1;

                // フォームを初期化
                resetForm();
            } catch (error) {
                console.error("Error submitting form:", error.response ? error.response.data : error.message);
            }
        };

        return {
            calculateCategory,
            checkValue,
            formState,
            errorMessagesState,
            validatorsState,
            onInputForm,
            submitForm,
            lastId,
        };
    },
};


</script>