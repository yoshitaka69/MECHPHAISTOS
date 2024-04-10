<template>
    <Transition name="modal">
        <div v-if="show" class="modal-mask">
            <div class="modal-container">
                <span class="p-text-secondary block mb-5">Registration Form</span>
                <div class="flex gap-6"><!--firstとfamilyを横並びにする-->
                    <!-- FirstName -->
                    <div class="flex align-items-center gap-3 mb-3">
                        <label for="firstName" class="font-semibold w-6rem">First Name</label>
                        <InputText id="firstName" v-model="firstName" class="flex-auto" autocomplete="off" />
                    </div>

                    <!-- FamilyName -->
                    <div class="flex align-items-center gap-3 mb-3">
                        <label for="familyName" class="font-semibold w-6rem">Family Name</label>
                        <InputText id="familyName" v-model="familyName" class="flex-auto" autocomplete="off" />
                    </div>
                </div>
                <div class="flex gap-6"><!--firstとfamilyを横並びにする-->
                    <div class="flex align-items-center gap-3 mb-3">
                        <label for="username" class="font-semibold w-6rem">Username</label>
                        <InputText id="username" v-model="userName" class="flex-auto" autocomplete="off" />
                    </div>
                    <div class="flex align-items-center gap-3 mb-3">
                        <label for="email" class="font-semibold w-6rem">Email</label>
                        <InputText id="Email" v-model="Email" class="flex-auto" autocomplete="off" />
                    </div>
                </div>
                <div class="flex align-items-center gap-3 mb-5">
                    <label for="email" class="font-semibold w-6rem">Phone Number</label>
                    <InputText id="phoneNumber" v-model="phoneNumber" class="flex-auto" autocomplete="off" />
                </div>
                <div class="flex gap-6"><!--firstとfamilyを横並びにする-->
                    <div class="flex align-items-center gap-3 mb-5">
                        <label for="email" class="font-semibold w-6rem">Company Name</label>
                        <InputText id="companyName" v-model="companyName" class="flex-auto" autocomplete="off" />
                    </div>
                    <div class="flex align-items-center gap-3 mb-5">
                        <label for="email" class="font-semibold w-6rem">Company Code</label>
                        <InputText id="companyCode" v-model="companyCode" class="flex-auto" autocomplete="off" />
                    </div>
                </div>
                <div class="flex gap-6"><!--firstとfamilyを横並びにする-->
                    <div class="flex align-items-center gap-3 mb-5">
                        <label for="email" class="font-semibold w-6rem">Country</label>
                        <InputText id="country" v-model="country" class="flex-auto" autocomplete="off" />
                    </div>
                    <div class="flex align-items-center gap-3 mb-5">
                        <label for="email" class="font-semibold w-6rem">Zip-Code</label>
                        <InputText id="zipCode" v-model="zipCode" class="flex-auto" autocomplete="off" />
                    </div>
                </div>
                <div class="flex justify-content-end gap-2">
                    <Button type="button" label="Cancel" severity="secondary" @click="$emit('close')"></Button>
                    <Button type="button" label="Save" @click="submitForm"></Button>
                </div>
            </div>
        </div>
    </Transition>
</template>


<script setup>
import axios from 'axios';
import { ref } from 'vue';


const firstName = ref('');
const familyName = ref('');
const userName = ref('');
const Email = ref('');
const phoneNumber = ref('');
const companyCode = ref('');
const country = ref('');
const zipCode = ref('');

const props = defineProps({
    show: Boolean
})

//axios postの用methods
const submitForm = async () => {
    try {
        // ユーザー情報をPOSTするためのデータ
        const userData = {
            firstName: firstName.value,
            familyName: familyName.value,
            userName: userName.value,
            email: Email.value,
            phoneNumber: phoneNumber.value,
            zipCode: zipCode.value,
            // 他のフォームフィールドのデータを追加
        };

        // 会社情報をPOSTするためのデータ
        const companyData = {
            companyCode: companyCode.value,
            country: country.value,
            zipCode: zipCode.value,
        };


        // ユーザー情報をPOST
        console.log("userData:", userData);
        const userResponse = await axios.post("http://localhost:3000/users", userData);
        console.log(userResponse.data);

        // 会社情報をPOST
        console.log("companyData:", companyData);
        const companyResponse = await axios.post("http://localhost:3000/company", companyData);
        console.log(companyResponse.data);

        // フォームを初期化
        resetForm();
        // フォームを閉じるイベントを発火
        $emit('close');
    } catch (error) {
        console.error("Error submitting form:", error.response ? error.response.data : error.message);
        // エラーが発生した場合でも、場合によってはフォームを閉じることが望ましいかもしれません
        $emit('close');
    }
};

// フォームの初期化関数
const resetForm = () => {
    firstName.value = '';
    familyName.value = '';
    userName.value = '';
    Email.value = '';
    phoneNumber.value = '';
    companyCode.value = '';
    zipCode.value = '';
    // 他のフィールドも初期化
};
</script>

<style>
.modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    transition: opacity 0.3s ease;
}

.modal-container {
    width: 800px;
    margin: auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    transition: all 0.3s ease;
}

.flex-auto {
    width: 100%;
    /* テキストエリアの幅を親要素の幅いっぱいに設定 */
}
</style>