<script setup>
import { computed } from 'vue';

// ロゴ画像のパスを指定
const logoUrl = computed(() => {
    return '/src/assets/MECHPHAISTOS3.png';  // ロゴの相対パスを指定
});
</script>

<template>
    <div class="surface-900 py-6 lg:py-4 md:px-6 lg:px-8 flex flex-column lg:flex-row justify-content-between align-items-center">
        <ul class="list-none p-0 mb-0 flex flex-column md:flex-row flex-order-1 lg:flex-order-0 mt-4 lg:mt-0">
            <li class="mr-4 mt-3 lg:mt-0 flex items-end">
                <img :src="logoUrl" alt="MECHPHAISTOS ロゴ" style="width: 50px; height: auto;" class="mr-2" />
                <a tabindex="0" class="cursor-pointer text-0">Investor Relations</a>
            </li>
            <li class="mr-4 mt-3 lg:mt-0 flex items-end">
                <a tabindex="0" class="cursor-pointer text-0">Data Privacy</a>
            </li>
            <li class="mr-4 mt-3 lg:mt-0 flex items-end">
                <a tabindex="0" class="cursor-pointer text-0">Terms of Service</a>
            </li>
            <!-- ここに align-items-end を追加して a タグを下揃えに -->
            <li class="mr-4 mt-3 lg:mt-0 flex items-end">
                <a tabindex="0" class="cursor-pointer text-0 flex items-end">Legal Information</a>
            </li>
        </ul>

        <div class="flex align-items-end flex-order-0 lg:flex-order-1">
            <a tabindex="0" class="cursor-pointer mr-3 lg:mt-0 block flex items-end">
                <i class="pi pi-facebook surface-section p-1 text-sm border-circle text-900"></i>
            </a>
            <a tabindex="0" class="cursor-pointer mr-3 lg:mt-0 block flex items-end">
                <i class="pi pi-twitter surface-section p-1 text-sm border-circle text-900"></i>
            </a>
            <a tabindex="0" class="cursor-pointer mr-3 lg:mt-0 block flex items-end">
                <i class="pi pi-youtube surface-section p-1 text-sm border-circle text-900"></i>
            </a>
            <a tabindex="0" class="cursor-pointer lg:mt-0 block flex items-end">
                <i class="pi pi-google surface-section p-1 text-sm border-circle text-900"></i>
            </a>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.bg-gray-900 {
    background-color: #000000 !important; /* 背景色を黒に */
}

.surface-900 {
    background-color: #000000 !important; /* 背景色を黒に */
}

.text-0, .surface-section i {
    color: #ffffff !important; /* テキストとアイコンの色を白に */
}

a {
    color: #ffffff !important; /* リンクテキストの色を白に */
}

.flex.items-end {
    align-items: flex-end !important; /* フレックスアイテムを下揃えに */
}
</style>
