<script setup>
import { useLayout } from '@/layout/composables/layout';
import { computed } from 'vue';

const { layoutConfig } = useLayout();


const logoUrl = computed(() => {
    return `/layout/images/${layoutConfig.darkTheme.value ? 'logo-white' : 'logo-dark'}.svg`;
});
</script>

<template>
            <div class="bg-gray-900 px-4 py-8 md:px-6 lg:px-8">
                <div class="grid">
                    <div class="col-12 md:col-3 flex flex-wrap justify-content-start md:mb-0 mb-3">
                        <img src="" alt="Image" />
                    </div>
                    <div class="col-12 md:col-3">
                        <div class="text-white text-lg mb-4 flex flex-wrap" style="max-width: 290px">Jacob Obrechtstraat 5, 1071 KC Amsterdam The Netherlands</div>
                        <div class="text-white mb-3"><i class="pi pi-phone border-round p-1 mr-2"></i>(31) 20 779 8986</div>
                        <div class="text-white mb-3"><i class="pi pi-inbox border-round p-1 mr-2"></i>hello@alfred.co</div>
                    </div>
                    <div class="col-12 md:col-3 text-gray-200">
                        <div class="text-white font-bold line-height-3 mb-3">Company</div>
                        <a class="line-height-3 block cursor-pointer mb-2">About Us</a>
                        <a class="line-height-3 block cursor-pointer mb-2">News</a>
                        <a class="line-height-3 block cursor-pointer mb-2">Investor Relations</a>
                        <a class="line-height-3 block cursor-pointer mb-2">Careers</a>
                        <a class="line-height-3 block cursor-pointer">Media Kit</a>
                    </div>
                    <div class="col-12 md:col-3 text-gray-200">
                        <div class="text-white font-bold line-height-3 mb-3">Resourses</div>
                        <a class="line-height-3 block cursor-pointer mb-2">Get Started</a>
                        <a class="line-height-3 block cursor-pointer mb-2">Learn</a>
                        <a class="line-height-3 block cursor-pointer">Case Studies</a>
                    </div>
                </div>
            </div>

            <div class="surface-900 py-6 lg:py-4 md:px-6 lg:px-8 flex flex-column lg:flex-row justify-content-between align-items-center">
                <ul class="list-none p-0 mb-0 flex flex-column md:flex-row flex-order-1 lg:flex-order-0 mt-4 lg:mt-0">
                    <li class="mr-4 mt-3 lg:mt-0">
                        <a tabindex="0" class="cursor-pointer text-0">Investor Relations</a>
                    </li>
                    <li class="mr-4 mt-3 lg:mt-0">
                        <a tabindex="0" class="cursor-pointer text-0">Data Privacy</a>
                    </li>
                    <li class="mr-4 mt-3 lg:mt-0">
                        <a tabindex="0" class="cursor-pointer text-0">Terms of Service</a>
                    </li>
                    <li class="mr-4 mt-3 lg:mt-0">
                        <a tabindex="0" class="cursor-pointer text-0">Legal Information</a>
                    </li>
                </ul>

                <div class="flex align-items-center flex-order-0 lg:flex-order-1">
                    <a tabindex="0" class="cursor-pointer mr-3 lg:mt-0 block">
                        <i class="pi pi-facebook surface-section p-1 text-sm border-circle text-900"></i>
                    </a>
                    <a tabindex="0" class="cursor-pointer mr-3 lg:mt-0 block">
                        <i class="pi pi-twitter surface-section p-1 text-sm border-circle text-900"></i>
                    </a>
                    <a tabindex="0" class="cursor-pointer mr-3 lg:mt-0 block">
                        <i class="pi pi-youtube surface-section p-1 text-sm border-circle text-900"></i>
                    </a>
                    <a tabindex="0" class="cursor-pointer lg:mt-0 block">
                        <i class="pi pi-google surface-section p-1 text-sm border-circle text-900"></i>
                    </a>
                </div>
            </div>
</template>
<style lang="scss" scoped></style>
