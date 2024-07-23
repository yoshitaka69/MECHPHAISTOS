<template>
    <div>
        <div header="With Galleria, Tabs and Single Column Reviews">
            <div class="surface-overlay px-4 md:px-6 lg:px-8 flex align-items-stretch relative" style="min-height: 80px">
                <a v-ripple class="cursor-pointer flex align-items-center lg:hidden text-700 mr-3 sm:mr-5 p-ripple">
                    <i class="pi pi-bars text-4xl"></i>
                </a>
                <div class="flex align-items-center justify-content-center">
                    <img src="" alt="Logo" class="lg:mr-6 h-2rem sm:h-3rem" />
                </div>
                <div id="nav-1" class="surface-overlay hidden lg:flex absolute lg:static left-0 top-100 z-1 shadow-2 lg:shadow-none w-full lg:w-auto py-3 lg:py-0">
                    <ul class="list-none p-0 m-0 flex flex-column lg:flex-row">
                        <!-- Navigation items can be added here -->
                    </ul>
                </div>
                <div class="flex ml-auto">
                    <ul class="list-none p-0 m-0 flex">
                        <li class="flex">
                            <a v-ripple class="text-900 font-medium inline-flex align-items-center cursor-pointer px-2 sm:px-3 hover:text-primary p-ripple">
                                <i class="pi pi-search mr-2 lg:mr-3 text-xl sm:text-base"></i>
                                <span class="hidden lg:inline">Search</span>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="surface-section px-4 md:px-6 lg:px-8">
                <ul class="list-none py-3 px-0 m-0 border-y-1 surface-border flex flex-wrap align-items-center font-medium overflow-x-auto">
                    <li class="lg:pr-3">
                        <a class="cursor-pointer text-900 white-space-nowrap">Home</a>
                    </li>
                    <li class="lg:px-2">
                        <span class="text-900">/</span>
                    </li>
                    <li class="lg:px-2">
                        <a class="cursor-pointer text-900 white-space-nowrap">Women</a>
                    </li>
                </ul>

                <div class="grid my-4">
                    <div class="col-12 lg:col-6">
                        <div class="flex">
                            <div class="image-container">
                                <div class="small-images">
                                    <div v-for="(img, index) in smallImages" :key="index" class="small-image" @click="setLargeImage(img)">
                                        <img :src="img" alt="Small Spare Part Image" class="w-full h-auto" />
                                    </div>
                                </div>
                                <div class="large-image">
                                    <img :src="largeImage" alt="Large Spare Part Image" class="w-full h-auto" />
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 lg:col-6 py-3 lg:pl-6">
                        <div class="flex align-items-center text-xl font-medium text-900 mb-4">{{ sparePart.partsName }}</div>
                        <div class="flex align-items-center justify-content-between mb-5">
                            <span class="text-900 font-medium text-3xl block">{{ sparePart.partsCost }}</span>
                            <div class="flex align-items-center">
                                <span class="mr-3">
                                    <i class="pi pi-star-fill text-yellow-500 mr-1"></i>
                                    <i class="pi pi-star-fill text-yellow-500 mr-1"></i>
                                    <i class="pi pi-star-fill text-yellow-500 mr-1"></i>
                                    <i class="pi pi-star-fill text-yellow-500 mr-1"></i>
                                    <i class="pi pi-star text-700 mr-1"></i>
                                </span>
                                <span class="text-sm"><b class="text-900 mr-1">24</b> <span class="text-500"></span>reviews</span>
                            </div>
                        </div>

                        <div class="font-bold text-900 mb-3">Details</div>
                        <ul class="details-list">
                            <li><strong>Parts No:</strong> {{ sparePart.partsNo }}</li>
                            <li><strong>BOM Code:</strong> {{ sparePart.bomCode }}</li>
                            <li><strong>Category:</strong> {{ sparePart.category }}</li>
                            <li><strong>Model:</strong> {{ sparePart.partsModel }}</li>
                            <li><strong>Serial Number:</strong> {{ sparePart.serialNumber }}</li>
                            <li><strong>Task Code:</strong> {{ sparePart.taskCode }}</li>
                            <li><strong>Price:</strong> {{ sparePart.partsCost }}</li>
                            <li><strong>Number of:</strong> {{ sparePart.numberOf }}</li>
                            <li><strong>Unit:</strong> {{ sparePart.unit }}</li>
                            <li><strong>Location:</strong> {{ sparePart.location }}</li>
                            <li><strong>Delivery Time:</strong> {{ sparePart.partsDeliveryTime }}</li>
                            <li><strong>Alert Order:</strong> {{ sparePart.orderAlert }}</li>
                            <li><strong>Order Situation:</strong> {{ sparePart.orderSituation }}</li>
                            <li><strong>Classification:</strong> {{ sparePart.classification }}</li>
                            <li><strong>Inventory Turnover:</strong> {{ sparePart.inventoryTurnover }}</li>
                            <li><strong>Description:</strong> {{ sparePart.partsDescription }}</li>
                        </ul>

                        <div class="font-bold text-900 mb-3">Quantity</div>
                        <div class="flex flex-column sm:flex-row sm:align-items-center sm:justify-content-between">
                            <i
                                class="pi text-2xl cursor-pointer"
                                :class="{
                                    'pi-heart text-600': !liked,
                                    'pi-heart-fill text-orange-500': liked
                                }"
                                @click="liked = !liked"
                            ></i>
                        </div>
                    </div>
                </div>
            </div>

            <TabView>
                <TabPanel header="Reviews">
                </TabPanel>
                <TabPanel header="Shipping and Returns">
                </TabPanel>
            </TabView>

            <div class="grid -mr-3 -ml-3 py-8">
                <span class="text-900 p-2 text-4xl font-medium w-full">You may also like</span>
                <div class="col-12 md:col-6 lg:col-3 mb-3 lg:mb-0" v-for="product in relatedProducts" :key="product.partsNo">
                    <div class="p-2">
                        <div class="relative">
                            <img :src="product.image || noImage" class="w-full" />
                            <button
                                v-ripple
                                class="p-link w-3rem h-3rem surface-0 hover:surface-200 border-circle shadow-2 inline-flex align-items-center justify-content-center absolute transition-colors transition-duration-300 p-ripple"
                                style="top: 1rem; right: 1rem"
                            >
                                <i class="pi pi-heart text-2xl text-500"></i>
                            </button>
                        </div>
                        <div class="flex align-items-center justify-content-between mt-3 mb-2">
                            <span class="text-900 font-medium text-xl">{{ product.partsName }}</span>
                        </div>
                        <span class="text-600">{{ product.partsModel }}</span>
                        <span class="text-600">{{ product.serialNumber }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import noImage from '@/assets/no_image.jpg';

export default {
    data() {
        return {
            sparePart: {},
            relatedProducts: [],
            liked: false,
            noImage,
            largeImage: null,
            smallImages: []
        };
    },
    created() {
        this.fetchSparePartDetails();
    },
    methods: {
        fetchSparePartDetails() {
            const partsNo = this.$route.params.partsNo;
            const userStore = useUserStore();
            const companyCode = userStore.companyCode;
            const url = `http://127.0.0.1:8000/api/spareParts/sparePartsByCompany/?companyCode=${companyCode}`;

            console.log('Fetching spare part details from:', url);

            axios.get(url)
                .then(response => {
                    console.log('API response:', response);
                    const companyData = response.data.find(company => company.companyCode === companyCode);
                    if (companyData && companyData.sparePartsList) {
                        this.sparePart = companyData.sparePartsList.find(part => part.partsNo === partsNo);
                        this.processImages(this.sparePart.image);
                        this.fetchRelatedProducts(companyData.sparePartsList);
                        if (!this.sparePart) {
                            console.error('Spare part not found');
                        }
                    } else {
                        console.error('Company data or spare parts list not found');
                    }
                })
                .catch(error => {
                    console.error('Error fetching spare part details:', error);
                });
        },
        processImages(image) {
            const images = [image || this.noImage];
            this.largeImage = images[0];
            this.smallImages = images.concat(Array(4 - images.length).fill(this.noImage));
        },
        setLargeImage(image) {
            this.largeImage = image;
        },
        fetchRelatedProducts(sparePartsList) {
            const bomCode = this.sparePart.bomCode;
            this.relatedProducts = sparePartsList.filter(part => part.bomCode === bomCode && part.partsNo !== this.sparePart.partsNo);
        }
    }
};
</script>

<style scoped>
.block-category-title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
}

.image-container {
    display: flex;
}

.large-image {
    flex: 3;
    margin-left: 10px;
}

.small-images {
    display: flex;
    flex-direction: column;
    gap: 10px;
    flex: 1;
}

.small-image img {
    width: 50px;
    height: 50px;
    object-fit: cover;
}

.large-image img {
    width: 100%;
    height: auto;
    object-fit: cover;
}

.details-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.details-list li {
    padding: 10px 0;
    border-bottom: 1px solid #ccc;
}

.details-list li strong {
    font-weight: bold;
    color: #333;
}
</style>
