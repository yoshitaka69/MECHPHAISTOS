<template>
    <BlockViewer header="Sidebar" :code="block1">
        <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
            <div class="text-900 font-bold text-3xl text-center">Category Title</div>
            <p class="text-600 font-normal text-xl text-center">Nullam faucibus, sem et bibendum finibus, sapien ipsum congue felis, sit amet pretium ex nisl ut eros.</p>
            <Divider class="w-full"></Divider>
            <div class="flex flex-wrap lg:flex-nowrap">
                <div class="col-fixed lg:col-2 mr-4 flex p-0 flex-column w-full lg:w-3">
                    <div class="flex flex-column p-0">
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">Denim</a>
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">Sweaters</a>
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">T-Shirt</a>
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">Pants & Shorts</a>
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">Outwear</a>
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">Shoes</a>
                        <a tabindex="0" class="cursor-pointer text-900 font-medium mb-3 hover:text-primary transition-duration-150">Accessories</a>
                    </div>
                    <Divider class="w-full m-0 p-0"></Divider>

                    <Accordion :multiple="true" class="-mb-1 mt-3" :activeIndex="[0, 1, 2, 3]">
                        <AccordionTab :header="'Brand (' + (selectedBrand_1.length !== 0 ? selectedBrand_1.length : '0') + ')'">
                            <div class="ransition-all transition-duration-400 transition-ease-in-out">
                                <div class="mb-3">
                                    <span class="p-input-icon-right w-full">
                                        <i class="pi pi-search"></i>
                                        <InputText placeholder="Search" class="w-full" />
                                    </span>
                                </div>
                                <div class="flex w-full justify-content-between">
                                    <div class="field-checkbox">
                                        <Checkbox value="Alfred" id="alfred" v-model="selectedBrand_1"></Checkbox>
                                        <label for="alfred" class="text-900">Alfred</label>
                                    </div>
                                    <Badge value="42" class="mr-2 bg-gray-200 text-gray-900 p-0 border-circle"></Badge>
                                </div>
                                <div class="flex w-full justify-content-between">
                                    <div class="field-checkbox">
                                        <Checkbox value="Hyper" id="hyper" v-model="selectedBrand_1"></Checkbox>
                                        <label for="hyper" class="text-900">Hyper</label>
                                    </div>
                                    <Badge value="18" class="mr-2 bg-gray-200 text-gray-900 p-0 border-circle"></Badge>
                                </div>
                                <div class="flex w-full justify-content-between">
                                    <div class="field-checkbox">
                                        <Checkbox value="Bastion" id="bastion" v-model="selectedBrand_1"></Checkbox>
                                        <label for="bastion" class="text-900">Bastion</label>
                                    </div>
                                    <Badge value="7" class="mr-2 bg-gray-200 text-gray-900 p-0 border-circle"></Badge>
                                </div>
                                <div class="flex w-full justify-content-between">
                                    <div class="field-checkbox">
                                        <Checkbox value="Peak" id="peak" v-model="selectedBrand_1"></Checkbox>
                                        <label for="peak" class="text-900">Peak</label>
                                    </div>
                                    <Badge value="36" class="mr-2 bg-gray-200 text-gray-900 p-0 border-circle"></Badge>
                                </div>
                                <a tabindex="0" class="block cursor-pointer my-3 text-primary font-medium">Show all...</a>
                            </div>
                        </AccordionTab>
                        <AccordionTab header="Price Range">
                            <div class="transition-all transition-duration-400 transition-ease-in-out">
                                <Slider v-model="rangeValues" :range="true" class="mt-3 mx-auto" style="{'max-width':'93%'}"></Slider>
                                <div class="flex my-4">
                                    <InputNumber placeholder="$10" v-model="rangeValues[0]" :min="10" inputClass="w-full mr-3"></InputNumber>
                                    <InputNumber placeholder="$10000" :max="10000" v-model="rangeValues[1]" inputClass="w-full"></InputNumber>
                                </div>
                            </div>
                        </AccordionTab>
                        <AccordionTab :header="'Color (' + selectedColors.length + ')'">
                            <div class="transition-all transition-duration-400 transition-ease-in-out">
                                <div class="grid mb-3">
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-gray-900 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedColors.indexOf('Black') == -1 ? selectedColors.push('Black') : selectedColors.splice(selectedColors.indexOf('Black'), 1)"
                                        >
                                            <i class="pi pi-check text-2xl text-white" v-if="selectedColors.indexOf('Black') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Black</p>
                                    </div>
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-orange-500 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedColors.indexOf('Orange') == -1 ? selectedColors.push('Orange') : selectedColors.splice(selectedColors.indexOf('Orange'), 1)"
                                        >
                                            <i class="pi pi-check text-2xl text-white" v-if="selectedColors.indexOf('Orange') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Orange</p>
                                    </div>
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-indigo-500 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedColors.indexOf('Indigo') == -1 ? selectedColors.push('Indigo') : selectedColors.splice(selectedColors.indexOf('Indigo'), 1)"
                                        >
                                            <i class="pi pi-check text-2xl text-white" v-if="selectedColors.indexOf('Indigo') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Indigo</p>
                                    </div>
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-gray-500 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedColors.indexOf('Gray') == -1 ? selectedColors.push('Gray') : selectedColors.splice(selectedColors.indexOf('Gray'), 1)"
                                        >
                                            <i class="pi pi-check text-2xl text-white" v-if="selectedColors.indexOf('Gray') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Gray</p>
                                    </div>
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-cyan-500 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedColors.indexOf('Cyan') == -1 ? selectedColors.push('Cyan') : selectedColors.splice(selectedColors.indexOf('Cyan'), 1)"
                                        >
                                            <i class="pi pi-check text-2xl text-white" v-if="selectedColors.indexOf('Cyan') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-center mt-1">Cyan</p>
                                    </div>
                                    <div class="col-4 flex flex-column align-items-center">
                                        <div
                                            class="w-3rem h-3rem border-circle bg-pink-500 cursor-pointer border-none flex justify-content-center align-items-center"
                                            @click="selectedColors.indexOf('Pink') == -1 ? selectedColors.push('Pink') : selectedColors.splice(selectedColors.indexOf('Pink'), 1)"
                                        >
                                            <i class="pi pi-check text-2xl text-white" v-if="selectedColors.indexOf('Pink') !== -1"></i>
                                        </div>
                                        <p class="text-900 text-sm text-center mt-1">Pink</p>
                                    </div>
                                </div>
                            </div>
                        </AccordionTab>
                        <AccordionTab header="Size">
                            <div class="transition-all transition-duration-400 transition-ease-in-out">
                                <Galleria :value="sizes" :responsiveOptions="responsiveOptions" containerClass="h-full" :numVisible="2" :showThumbnails="false" :showIndicators="true">
                                    <template #item="slotProps">
                                        <div class="flex flex-wrap w-full h-auto overflow-hidden justify-content-center" style="column-gap: 5px; row-gap: 5px">
                                            <div
                                                v-ripple
                                                class="w-4rem h-2rem text-900 flex justify-content-center align-items-center text-sm cursor-pointer border-round p-ripple"
                                                v-for="size of slotProps.item.page"
                                                :key="size"
                                                @click="selectedSizes1.indexOf(size.value) == -1 ? selectedSizes1.push(size.value) : selectedSizes1.splice(selectedSizes1.indexOf(size.value.toString()), 1)"
                                                :class="{
                                                    'surface-100': selectedSizes1.indexOf(size.value) == -1,
                                                    'bg-blue-200': selectedSizes1.indexOf(size.value) !== -1
                                                }"
                                            >
                                                {{ size.value }}
                                            </div>
                                        </div>
                                    </template>
                                </Galleria>
                            </div>
                        </AccordionTab>
                    </Accordion>
                </div>
                <!-- 統合されたCAD Drawing Ledgerセクション -->
                <div class="w-full border-2 border-dashed border-round surface-border surface-section mt-3 lg:mt-0" style="min-height: 25rem">
                    <section class="content">
                        <div class="card card-solid">
                            <p class="line-height-3 m-0 description-text">This table displays management information related to CAD design drawings.</p>
                            <CAD_Drawing_ledger />
                        </div>
                    </section>
                </div>
            </div>
        </div>
    </BlockViewer>
</template>

<script>
import CAD_Drawing_ledger from '@/components/Drawing_ledger/Drawing_ledger.vue';

export default {
    components: {
        CAD_Drawing_ledger
    },
    data() {
        return {
            selectedBrand_1: [],
            selectedColors: [],
            selectedSizes1: [],
            sizes: [
                {
                    page: [
                        { value: '28x28' },
                        { value: '28x30' },
                        { value: '28x32' },
                        { value: '28x34' },
                        { value: '29x28' },
                        { value: '29x30' },
                        { value: '29x32' },
                        { value: '29x34' },
                        { value: '30x28' },
                        { value: '30x30' },
                        { value: '30x32' },
                        { value: '30x34' },
                        { value: '31x28' },
                        { value: '31x30' },
                        { value: '31x32' },
                        { value: '31x34' }
                    ]
                },
                {
                    page: [
                        { value: '32x28' },
                        { value: '32x30' },
                        { value: '32x32' },
                        { value: '32x34' },
                        { value: '33x28' },
                        { value: '33x30' },
                        { value: '33x32' },
                        { value: '33x34' },
                        { value: '34x28' },
                        { value: '34x30' },
                        { value: '34x32' },
                        { value: '34x34' },
                        { value: '35x28' },
                        { value: '35x30' },
                        { value: '35x32' },
                        { value: '35x34' }
                    ]
                },
                {
                    page: [
                        { value: '28x28' },
                        { value: '28x30' },
                        { value: '28x32' },
                        { value: '28x34' },
                        { value: '29x28' },
                        { value: '29x30' },
                        { value: '29x32' },
                        { value: '29x34' },
                        { value: '30x28' },
                        { value: '30x30' },
                        { value: '30x32' },
                        { value: '30x34' },
                        { value: '31x28' },
                        { value: '31x30' },
                        { value: '31x32' },
                        { value: '31x34' }
                    ]
                }
            ],
            responsiveOptions: [
                {
                    breakpoint: '1024px',
                    numVisible: 3,
                    numScroll: 3
                },
                {
                    breakpoint: '768px',
                    numVisible: 2,
                    numScroll: 2
                },
                {
                    breakpoint: '560px',
                    numVisible: 1,
                    numScroll: 1
                }
            ],
            rangeValues: [20, 80]
        };
    }
};
</script>

<style>
.description-text {
    font-size: 1.2rem; /* フォントサイズを一回り大きく設定 */
}
</style>
