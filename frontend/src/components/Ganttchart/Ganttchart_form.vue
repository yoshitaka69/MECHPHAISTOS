<template>
    <div class="base" v-show="show">
        <div class="overlay" @click="show = false"></div>
        <div class="content">
            <h2 class="font-bold">{{ updateMode ? 'タスクの更新' : 'タスクの追加' }}</h2>
            <div class="my-4">
                <label class="text-xs">カテゴリーID:</label>
                <select v-model="form.category_id" class="text-xs border px-4 py-2 rounded-lg">
                    <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
                </select>
            </div>
            <div class="my-4">
                <label class="text-xs">ID:</label>
                <input type="number" class="text-xs border rounded-lg px-4 py-2" v-model.number="form.id" />
            </div>
            <div class="my-4">
                <label class="text-xs">タスク名:</label>
                <input type="text" class="text-xs border rounded-lg px-4 py-2" v-model="form.name" />
            </div>
            <div class="my-4">
                <label class="text-xs">担当者:</label>
                <input type="text" class="text-xs border rounded-lg px-4 py-2" v-model="form.incharge_user" />
            </div>
            <div class="my-4">
                <label class="text-xs">開始日:</label>
                <input type="date" class="text-xs border rounded-lg px-4 py-2" v-model="form.start_date" />
            </div>
            <div class="my-4">
                <label class="text-xs">完了期限日:</label>
                <input type="date" class="text-xs border rounded-lg px-4 py-2" v-model="form.end_date" />
            </div>
            <div class="my-4">
                <label class="text-xs">進捗度:</label>
                <input type="number" class="text-xs border rounded-lg px-4 py-2" v-model="form.percentage" />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['show', 'updateMode', 'form', 'categories'],
    methods: {
        close() {
            this.$emit('update:show', false);
        }
    }
};
</script>
