<template>
    <div v-if="visible" :class="alertClass" :style="alertStyle">
        <i :class="iconClass"></i>
        <div class="mr-3">
            <div :class="titleClass" class="font-medium text-xl mb-2 line-height-1">{{ title }}</div>
            <p v-if="type === 'success'" :class="messageClass" class="m-0 p-0 line-height-3">{{ message }}</p>
            <ul v-if="type === 'error'" class="m-0 p-0 text-pink-700 ml-3">
                <li v-for="(error, index) in errorMessages" :key="index" class="p-1">{{ error }}</li>
            </ul>
        </div>
        <div class="ml-auto">
            <a
                v-ripple
                class="inline-flex align-items-center justify-content-center ml-auto border-circle no-underline cursor-pointer transition-colors transition-duration-150 p-ripple"
                :class="closeIconClass"
                style="width: 1.5rem; height: 1.5rem"
                @click="closeAlert"
            >
                <i :class="closeIconColor"></i>
            </a>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        type: {
            type: String,
            default: 'error' // 'success' または 'error' を指定
        },
        message: {
            type: String,
            default: 'Operation completed successfully.'
        },
        errorMessages: {
            type: Array,
            default: () => []
        }
    },
    data() {
        return {
            visible: true
        };
    },
    computed: {
        alertClass() {
            return this.type === 'success'
                ? 'flex align-items-start p-4 bg-green-100 border-round border-1 border-green-300'
                : 'flex align-items-start p-4 bg-pink-100 border-round border-1 border-pink-300';
        },
        alertStyle() {
            return {
                position: 'fixed',
                top: '10px',
                left: '50%',
                transform: 'translateX(-50%)',
                zIndex: '1000',
                width: '90%',
                maxWidth: '600px',
                boxShadow: '0px 2px 10px rgba(0, 0, 0, 0.1)',
                opacity: this.visible ? 1 : 0,
                transition: 'opacity 0.3s ease'
            };
        },
        iconClass() {
            return this.type === 'success'
                ? 'pi pi-check-circle text-green-900 text-2xl mr-3'
                : 'pi pi-times-circle text-pink-900 text-2xl mr-3';
        },
        title() {
            return this.type === 'success' ? 'Success' : 'Validation Errors';
        },
        titleClass() {
            return this.type === 'success' ? 'text-green-900' : 'text-pink-900 mb-3';
        },
        messageClass() {
            return this.type === 'success' ? 'text-green-700' : 'text-pink-700';
        },
        closeIconClass() {
            return this.type === 'success' ? 'hover:bg-green-50' : 'hover:bg-pink-50';
        },
        closeIconColor() {
            return this.type === 'success' ? 'pi pi-times text-green-900' : 'pi pi-times text-pink-900';
        }
    },
    methods: {
        closeAlert() {
            this.visible = false;
        }
    }
};
</script>
