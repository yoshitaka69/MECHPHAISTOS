<template>
    <div class="base-content">
        <section class="content">
            <div class="card card-solid">
                this is user setting page.
                <div>
                    <UserSettingList />
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import UserSettingList from '@/components/User_setting/User_setting_list.vue';

export default {
    name: 'ParentComponent',
    components: {
        UserSettingList
    }
};
</script>

<style>
ul.list {
    font-size: 25px;
    line-height: 200%;
}
</style>
