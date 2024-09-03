<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';
import { useLayout } from '@/layout/composables/layout';
import { useRouter } from 'vue-router';
import Modal from '@/components/Modal/test.vue';

//modal test用
const showModal = ref(false)

const { layoutConfig, onMenuToggle } = useLayout();

const outsideClickListener = ref(null);
const topbarMenuActive = ref(false);
const router = useRouter();

onMounted(() => {
    bindOutsideClickListener();
});

onBeforeUnmount(() => {
    unbindOutsideClickListener();
});

const logoUrl = computed(() => {
    return `layout/images/${layoutConfig.darkTheme.value ? 'logo-white' : 'logo-dark'}.svg`;
});

const onTopBarMenuButton = () => {
    topbarMenuActive.value = !topbarMenuActive.value;
};
const onSettingsClick = () => {
    topbarMenuActive.value = false;
    router.push('/documentation');
};
const topbarMenuClasses = computed(() => {
    return {
        'layout-topbar-menu-mobile-active': topbarMenuActive.value
    };
});

const bindOutsideClickListener = () => {
    if (!outsideClickListener.value) {
        outsideClickListener.value = (event) => {
            if (isOutsideClicked(event)) {
                topbarMenuActive.value = false;
            }
        };
        document.addEventListener('click', outsideClickListener.value);
    }
};
const unbindOutsideClickListener = () => {
    if (outsideClickListener.value) {
        document.removeEventListener('click', outsideClickListener);
        outsideClickListener.value = null;
    }
};
const isOutsideClicked = (event) => {
    if (!topbarMenuActive.value) return;

    const sidebarEl = document.querySelector('.layout-topbar-menu');
    const topbarEl = document.querySelector('.layout-topbar-menu-button');

    return !(sidebarEl.isSameNode(event.target) || sidebarEl.contains(event.target) || topbarEl.isSameNode(event.target) || topbarEl.contains(event.target));
};

const newsItems = ref([
    'Breaking News: Market hits an all-time high!',
    'Weather Update: Sunny with a chance of rain.',
    'Sports: Local team wins championship!',
    'Event: Community festival this weekend.',
]);

</script>

<template>
    <div class="layout-topbar">
        <router-link to="/" class="layout-topbar-logo">
            <span>MECHPHAISTOS&nbsp;βver.
                <div class="subtitle">
                    Money,Equipment,People.&nbsp;The best maintenance tool.
                </div>
            </span>
        </router-link>

        <!--サイドバーメニューの開閉ボタン-->
        <button class="p-link layout-menu-button layout-topbar-button" @click="onMenuToggle()">
            <i class="pi pi-bars"></i>
        </button>

        <!-- ニュースティッカー -->
        <div class="ticker">
            <div class="ticker-content">
                <div class="ticker-item" v-for="(news, index) in newsItems" :key="index">
                    {{ news }}
                </div>
            </div>
        </div>

        <!-- トップバーメニューボタン -->
        <button class="p-link layout-topbar-menu-button layout-topbar-button" @click="onTopBarMenuButton()">
            <i class="pi pi-ellipsis-v"></i>
        </button>

        <div class="layout-topbar-menu" :class="topbarMenuClasses">
            <button id="show-modal" @click="showModal = true">Show Modal</button>
            <Teleport to="body">
                <!-- モーダルコンポーネントの使用 -->
                <modal :show="showModal" @close="showModal = false">
                </modal>
            </Teleport>
            <button @click="onTopBarMenuButton()" class="p-link layout-topbar-button">
                <i class="pi pi-calendar"></i>
                <span>Calendar</span>
            </button>
            <button @click="onTopBarMenuButton()" class="p-link layout-topbar-button">
                <i class="pi pi-user"></i>
                <span>Profile</span>
            </button>
            <button @click="onSettingsClick()" class="p-link layout-topbar-button">
                <i class="pi pi-cog"></i>
                <span>Settings</span>
            </button>
        </div>
    </div>
</template>

<style scoped>
.ticker {
    overflow: hidden;
    white-space: nowrap;
    width: 100%;
    height: 30px;
    background-color: black;
    color: white;
    display: flex;
    align-items: center;
    margin: 0 10px; /* ボタンとの間に少し余白を追加 */
}

.ticker-content {
    display: inline-block;
    white-space: nowrap;
    animation: ticker 10s linear infinite;
}

.ticker-item {
    display: inline-block;
    padding: 0 2rem;
}

@keyframes ticker {
    0% {
        transform: translateX(100%);
    }
    100% {
        transform: translateX(-100%);
    }
}

.layout-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.layout-topbar-logo {
    flex: 1;
}

.layout-menu-button,
.layout-topbar-menu-button {
    margin: 0 5px;
}

.layout-topbar-menu {
    display: flex;
    align-items: center;
}
</style>
