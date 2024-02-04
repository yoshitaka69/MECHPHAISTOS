<template>
    <div class="IdGroup">
        <p>最新のId: {{ lastId }}</p>
    </div>
    <!--日付-->
    <div class="DateGroup">
        <label class="DateGroup_label" for="Date">Date</label>
        <input type="Date" v-model="formState.Date" id="Date" />
    </div>

    <!--名前-->
    <div class="NameGroup">
        <label class="NameGroup__label" for="Name">Name:</label>
        <input :class="[
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
    <div class="DepartmentGroup">
        <label class="DepartmentGroup__label" for="Department">Department:</label>
        <input :class="[
            'DepartmentGroup__input',
            { 'DepartmentGroup__input-error': errorMessagesState.Department.length },
        ]" type="text" id="Department" placeholder="5文字以上で入力" :value="formState.Department"
            @input="onInputForm('Department', $event.target.value)" />
        <ul class="DepartmentGroup__errorMessages">
            <li v-for="message in errorMessagesState.Department" :key="message">
                {{ message }}
            </li>
        </ul>
    </div>

    <!--場所-->
    <div class="WhereGroup">
        <label class="WhereGroup__label" for="Where">Where?:</label>
        <input :class="[
            'WhereGroup__input',
            { 'WhereGroup__input-error': errorMessagesState.Where.length },
        ]" type="text" id="Where" placeholder="5文字以上で入力" :value="formState.Where"
            @input="onInputForm('Where', $event.target.value)" />
        <ul class="WhereGroup__errorMessages">
            <li v-for="message in errorMessagesState.Where" :key="message">
                {{ message }}
            </li>
        </ul>
    </div>

    <!--事故のタイプ-->
    <div class="TypeOfAccIdentGroup">
        <div id="TypeOfAccIdent">
            <label class="TypeOfAccIdentGroup__label" for="TypeOfAccIdent">Type of AccIdent:</label>
            <input type="checkbox" v-model="checkValue" value="fall down">fall down
            <input type="checkbox" v-model="checkValue" value="fall/slip">fall/slip
            <input type="checkbox" v-model="checkValue" value="collision">collision
            <input type="checkbox" v-model="checkValue" value="accIdental fall">accIdental fall
            <input type="checkbox" v-model="checkValue" value="collapse">collapse
            <input type="checkbox" v-model="checkValue" value="hit by something">hit by something
            <input type="checkbox" v-model="checkValue" value="got caught up in">got caught up in
            <input type="checkbox" v-model="checkValue" value="cut/Rubbing">cut/Rubbing
            <input type="checkbox" v-model="checkValue" value="treading on something sharp">treading on something sharp
            <input type="checkbox" v-model="checkValue" value="drown">drown
            <input type="checkbox" v-model="checkValue" value="contact with hot or cold objects">contact with hot or cold
            objects
            <input type="checkbox" v-model="checkValue" value="contact with organic matter">contact with organic matter
            <input type="checkbox" v-model="checkValue" value="electric shock">electric shock
            <input type="checkbox" v-model="checkValue" value="explosion">explosion
            <input type="checkbox" v-model="checkValue" value="rupture">rupture
            <input type="checkbox" v-model="checkValue" value="conflagration">conflagration
            <input type="checkbox" v-model="checkValue" value="traffic accIdent">traffic accIdent
            <input type="checkbox" v-model="checkValue" value="impossible movement">impossible movement
            <input type="checkbox" v-model="checkValue" value="protective equipment violation">protective equipment
            violation
            <input type="checkbox" v-model="checkValue" value="others">others
        </div>
    </div>


    <!--要素-->
    <div class="FactorGroup">
        <div id="Factor">
            <label>Factor</label>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="Factor" value="Person" v-model="val_Factor" tabindex="0">
                    <label>Person</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="Factor" value="Rule" v-model="val_Factor" tabindex="1">
                    <label>Rule</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="Factor" value="Equipment" v-model="val_Factor" tabindex="2">
                    <label>Equipment</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="Factor" value="Methods" v-model="val_Factor" tabindex="3">
                    <label>Methods</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="Factor" value="Others" v-model="val_Factor" tabindex="4">
                    <label>Others</label>
                </div>
            </div>
        </div>
    </div>
    <!--ケガのレベル-->
    <div class="InjuredLvGroup">
        <div id="InjuredLv">
            <label>Injured Lv</label>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="InjuredLv" value="A" v-model="val_InjuredLv" tabindex="0">
                    <label>A</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="InjuredLv" value="B" v-model="val_InjuredLv" tabindex="1">
                    <label>B</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="InjuredLv" value="C" v-model="val_InjuredLv" tabindex="2">
                    <label>C</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="InjuredLv" value="D" v-model="val_InjuredLv" tabindex="3">
                    <label>D</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="InjuredLv" value="E" v-model="val_InjuredLv" tabindex="4">
                    <label>E</label>
                </div>
            </div>
            <h2 class="ui gray header">{{ val_InjuredLv }}</h2>
        </div>
    </div>

    <!--設備損傷のレベル-->
    <div class="EquipmentDamageLvGroup">
        <div id="EquipmentDamageLv">
            <label>Equipment Damage Lv</label>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="EquipmentDamageLv" value="A" v-model="val_EDlv" tabindex="0">
                    <label>A</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="EquipmentDamageLv" value="B" v-model="val_EDlv" tabindex="1">
                    <label>B</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="EquipmentDamageLv" value="C" v-model="val_EDlv" tabindex="2">
                    <label>C</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="EquipmentDamageLv" value="D" v-model="val_EDlv" tabindex="3">
                    <label>D</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="EquipmentDamageLv" value="E" v-model="val_EDlv" tabindex="4">
                    <label>E</label>
                </div>
            </div>
            <h2 class="ui gray header">{{ val_EDlv }}</h2>
        </div>
    </div>

    <!--環境への影響-->
    <div class="AffectOfEnviromentGroup">
        <div id="AffectOfEnviroment">
            <label>Affect Of Enviroment</label>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="AffectOfEnviroment" value="A" v-model="val_AElv" tabindex="0">
                    <label>A</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="AffectOfEnviroment" value="B" v-model="val_AElv" tabindex="1">
                    <label>B</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="AffectOfEnviroment" value="C" v-model="val_AElv" tabindex="2">
                    <label>C</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="AffectOfEnviroment" value="D" v-model="val_AElv" tabindex="3">
                    <label>D</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="AffectOfEnviroment" value="E" v-model="val_AElv" tabindex="4">
                    <label>E</label>
                </div>
            </div>
            <h2 class="ui gray header">{{ val_AElv }}</h2>
        </div>
    </div>

    <!--メディアへの影響-->
    <div class="NewsCoverageGroup">
        <div id="NewsCoverage">
            <label>News Coverage</label>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="NewsCoverage" value="A" v-model="val_NC" tabindex="0">
                    <label>A</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="NewsCoverage" value="B" v-model="val_NC" tabindex="1">
                    <label>B</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="NewsCoverage" value="C" v-model="val_NC" tabindex="2">
                    <label>C</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="NewsCoverage" value="D" v-model="val_NC" tabindex="3">
                    <label>D</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input type="radio" Name="NewsCoverage" value="E" v-model="val_NC" tabindex="4">
                    <label>E</label>
                </div>
            </div>
            <h2 class="ui gray header">{{ val_NC }}</h2>
            <h2 class="ui gray header">{{ calculateCategory() }}</h2>
            <button @click="submitForm">更新</button>
        </div>
    </div>

    <!--詳細記入フォーム-->
    <div class="DiscriptionGroup">
        <label for="Discription-input">Discription</label>
        <textarea v-model="formState.Discription" rows="4" cols="40" id="Discription"></textarea>
    </div>
</template>
  
<script>
import { ref, reactive, onMounted } from "vue";
import { notBlank, atLeast } from "./validatorOptions";
import axios from 'axios';

export default {
    setup() {
        const lastId = ref(0);

        const getLastId = async () => {
            try {
                const response = await axios.get("http://localhost:3000/NearMiss");
                const data = response.data;

                if (data.length > 0) {
                    // データがある場合、Idの最大値を取得
                    const maxId = Math.max(...data.map(entry => entry.id));
                    return maxId;
                } else {
                    // データがない場合は0を返すか、適切な初期値を考える
                    return 0;
                }
            } catch (error) {
                console.error("Error getting last Id:", error);
                throw error;
            }
        };

        getLastId().then(Id => {
            lastId.value = Id + 1; // 新しいIdを表示するため、+1する
        });


        const val_InjuredLv = ref("");
        const val_EDlv = ref("");
        const val_AElv = ref("");
        const val_NC = ref("");

        const calculateCategory = () => {
            const valueMapping = { A: 1, B: 2, C: 4, D: 5, E: 6 };
            const total =
                valueMapping[val_InjuredLv.value] +
                valueMapping[val_EDlv.value] +
                valueMapping[val_AElv.value] +
                valueMapping[val_NC.value];

            if (total >= 6) {
                return "E";
            } else if (total >= 5) {
                return "D";
            } else if (total >= 4) {
                return "C";
            } else if (total >= 3) {
                return "B";
            } else {
                return "A";
            }
        };

        const checkValue = reactive({});

        const formState = reactive({
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
            } catch (error) {
                console.error("Error submitting form:", error.response ? error.response.data : error.message);
            }
        };

        return {
            val_InjuredLv,
            val_EDlv,
            val_AElv,
            val_NC,
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
