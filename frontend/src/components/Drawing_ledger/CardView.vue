<template>
    <div class="card-view">
        <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
            <div class="text-900 font-bold text-3xl text-center">Project List view</div>
            <p class="text-600 font-normal text-xl text-center">Here you can view completed drawings and CAD data.</p>
            <Divider class="w-full"></Divider>
            <div class="flex flex-wrap lg:flex-nowrap">
                <div class="col-fixed lg:col-2 mr-4 flex p-0 flex-column w-full lg:w-3">
                    <div class="flex flex-column p-0">
                        <!-- Sidebar Links -->
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">Denim</a>
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">Sweaters</a>
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">T-Shirt</a>
                        <!-- More Links... -->
                    </div>
                    <Divider class="w-full m-0 p-0"></Divider>

                    <!-- Accordion for Filters -->
                    <Accordion :multiple="true" class="-mb-1 mt-3" :activeIndex="[0, 1, 2, 3]">
                        <AccordionTab header="Category ({{ selectedBrand_1.length }})">
                            <div>
                                <div class="mb-3">
                                    <span class="p-input-icon-right w-full">
                                        <i class="pi pi-search"></i>
                                        <InputText placeholder="Search" class="w-full" />
                                    </span>
                                </div>
                                <!-- Filter Items... -->
                            </div>
                        </AccordionTab>

                        <!-- Date Range Accordion -->
                        <AccordionTab header="Date Range">
                            <!-- 修正: v-model を使わずにバインディング -->
                            <Slider :model-value="rangeValues" @update:model-value="updateRangeValues" :min="minDate.getTime()" :max="maxDate.getTime()" :step="oneDay" :range="true" />
                            <div class="flex my-4">
                                <InputText :model-value="formattedStartDate" @update:model-value="updateFormattedStartDate" placeholder="Start Date" class="date-input mr-3" readonly />
                                <InputText :model-value="formattedEndDate" @update:model-value="updateFormattedEndDate" placeholder="End Date" class="date-input" readonly />
                            </div>
                        </AccordionTab>

                        <AccordionTab :header="'Category (' + selectedCategories.length + ')'">
                            <div class="transition-all transition-duration-400 transition-ease-in-out">
                                <div class="grid mb-3">
                                    <!-- Mechanical -->
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-gray-300 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedCategories.indexOf('Mechanical') == -1 ? selectedCategories.push('Mechanical') : selectedCategories.splice(selectedCategories.indexOf('Mechanical'), 1)"
                                        >
                                            <i class="pi pi-cog text-2xl" v-if="selectedCategories.indexOf('Mechanical') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Mechanical</p>
                                    </div>

                                    <!-- Electrical -->
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-blue-300 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedCategories.indexOf('Electrical') == -1 ? selectedCategories.push('Electrical') : selectedCategories.splice(selectedCategories.indexOf('Electrical'), 1)"
                                        >
                                            <i class="pi pi-bolt text-2xl" v-if="selectedCategories.indexOf('Electrical') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Electrical</p>
                                    </div>

                                    <!-- Software -->
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-green-300 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedCategories.indexOf('Software') == -1 ? selectedCategories.push('Software') : selectedCategories.splice(selectedCategories.indexOf('Software'), 1)"
                                        >
                                            <i class="pi pi-desktop text-2xl" v-if="selectedCategories.indexOf('Software') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Software</p>
                                    </div>

                                    <!-- Building -->
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-yellow-300 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedCategories.indexOf('Building') == -1 ? selectedCategories.push('Building') : selectedCategories.splice(selectedCategories.indexOf('Building'), 1)"
                                        >
                                            <i class="pi pi-home text-2xl" v-if="selectedCategories.indexOf('Building') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Building</p>
                                    </div>

                                    <!-- Utilities -->
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-orange-300 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedCategories.indexOf('Utilities') == -1 ? selectedCategories.push('Utilities') : selectedCategories.splice(selectedCategories.indexOf('Utilities'), 1)"
                                        >
                                            <i class="pi pi-water text-2xl" v-if="selectedCategories.indexOf('Utilities') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Utilities</p>
                                    </div>
                                </div>
                            </div>
                        </AccordionTab>

                        <AccordionTab header="Size">
                            <div class="transition-all transition-duration-400 transition-ease-in-out">
                                <div class="grid mb-3">
                                    <div v-for="(sizePage, index) in sizes" :key="index" class="flex flex-wrap w-full h-auto overflow-hidden justify-content-center" style="column-gap: 5px; row-gap: 5px">
                                        <div
                                            v-for="size in sizePage.page"
                                            :key="size.value"
                                            class="w-4rem h-2rem text-900 flex justify-content-center align-items-center text-sm cursor-pointer border-round p-ripple"
                                            @click="selectedSizes1.indexOf(size.value) == -1 ? selectedSizes1.push(size.value) : selectedSizes1.splice(selectedSizes1.indexOf(size.value), 1)"
                                            :class="{
                                                'surface-100': selectedSizes1.indexOf(size.value) == -1,
                                                'bg-blue-200': selectedSizes1.indexOf(size.value) !== -1
                                            }"
                                        >
                                            {{ size.value }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </AccordionTab>
                    </Accordion>
                </div>
                <!-- Cards Section -->
                <div class="w-full border-2 border-dashed border-round surface-border surface-section mt-3 lg:mt-0" style="min-height: 25rem">
                    <div class="grid -mt-3 -ml-3 -mr-3">
                        <div v-for="file in sortedFiles" :key="file.id" class="col-12 md:col-6 lg:col-4 xl:col-2 card-item">
                            <div class="p-2">
                                <div class="p-card custom-card">
                                    <div class="p-card-header">
                                        <h4>{{ file.name }}</h4>
                                    </div>
                                    <div class="p-card-body">
                                        <p>
                                            <strong>ファイル:</strong> <a :href="`/api/cad_files/${file.file}`" download>{{ file.file }}</a>
                                        </p>
                                        <p><strong>カテゴリ:</strong> {{ file.category }}</p>
                                        <p><strong>プロジェクト名:</strong> {{ file.project_name }}</p>
                                        <p><strong>登録日:</strong> {{ new Date(file.uploaded_at).toLocaleDateString() }}</p>
                                        <p><strong>登録者:</strong> {{ file.uploaded_by }}</p>
                                        <p><strong>タグ:</strong> {{ file.tag }}</p>
                                    </div>
                                    <div class="p-card-footer">
                                        <Button icon="pi pi-pencil" class="p-button-text custom-button edit-button" @click="editItem(file)" />
                                        <Button icon="pi pi-trash" class="p-button-text custom-button delete-button" @click="deleteItem(file)" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// Props from parent
const props = defineProps({
    files: {
        type: Array,
        default: () => []
    },
    selectedBrand_1: {
        type: Array,
        default: () => []
    },
    rangeValues: {
        type: Array,
        default: () => [0, 0]
    },
    minDate: {
        type: Date,
        default: () => new Date(2020, 0, 1)
    },
    maxDate: {
        type: Date,
        default: () => new Date(2024, 11, 31)
    },
    oneDay: {
        type: Number,
        default: () => 24 * 60 * 60 * 1000
    },
    formattedStartDate: {
        type: String,
        default: ''
    },
    formattedEndDate: {
        type: String,
        default: ''
    },
    selectedCategories: {
        type: Array,
        default: () => []
    },
    sizes: {
        type: Array,
        default: () => []
    },
    selectedSizes1: {
        type: Array,
        default: () => []
    }
});

// props.files のみを使用する
const sortedFiles = computed(() => {
    return props.files;
});

const editItem = (item) => {
    console.log('Editing item:', item);
};

const deleteItem = (item) => {
    console.log('Deleting item:', item);
};

const emit = defineEmits(['update:rangeValues', 'update:formattedStartDate', 'update:formattedEndDate']);

const updateRangeValues = (newRangeValues) => {
    emit('update:rangeValues', newRangeValues);
};

const updateFormattedStartDate = (newDate) => {
    emit('update:formattedStartDate', newDate);
};

const updateFormattedEndDate = (newDate) => {
    emit('update:formattedEndDate', newDate);
};
</script>

<style scoped>
/* テキストボックスのスタイル */
.date-input {
    width: 100px;
}

/* カードビューのレイアウト設定 */
.card-view {
    display: flex;
    flex-direction: column;
    width: 100%;
}

/* セクションのスタイル */
.surface-section {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* カードコンポーネントのスタイル */
.p-card {
    margin-bottom: 20px;
    border: 1px solid #d3d3d3;
    background-color: #e0f7fa; /* 薄い青色 */
}

.p-card-header {
    font-weight: bold;
    font-size: 1.25rem;
    color: #0277bd; /* 強調する濃い青色 */
}

.p-card-body {
    font-size: 1rem;
    color: #555; /* テキストの色 */
}

.p-card-footer {
    display: flex;
    justify-content: flex-end;
}

.p-card-footer button {
    margin-right: 10px; /* ボタン間のスペース */
}

.p-card-footer button:last-child {
    margin-right: 0;
}

/* ボタンのスタイル */
.edit-button {
    background-color: #1976d2; /* 青色の背景 */
    color: white;
}

.edit-button .pi-pencil {
    color: white;
}

.delete-button {
    background-color: #d32f2f; /* 赤色の背景 */
    color: white;
}

.delete-button .pi-trash {
    color: white;
}

/* 汎用スタイル */
.field-checkbox,
.align-items-center {
    display: flex;
    align-items: center;
}

.cursor-pointer {
    cursor: pointer;
}

.text-900 {
    color: #333;
}

.text-sm {
    font-size: 0.875rem;
}

.flex {
    display: flex;
}

.flex-column {
    flex-direction: column;
}

.w-3rem,
.h-3rem {
    width: 3rem;
    height: 3rem;
}

.border-circle {
    border-radius: 50%;
}

.bg-gray-300 {
    background-color: #e0e0e0;
}

.bg-blue-200 {
    background-color: #b3e5fc;
}

/* マージン設定 */
.mb-3 {
    margin-bottom: 1rem;
}

.mt-3 {
    margin-top: 1rem;
}

/* レイアウトとボーダースタイル */
.w-full {
    width: 100%;
}

.mx-auto {
    margin-left: auto;
    margin-right: auto;
}

.p-ripple {
    position: relative;
    overflow: hidden;
}

.border-none {
    border: none;
}

</style>
