<template>
    <div>
        <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
            <div class="text-900 font-bold text-5xl mb-6">Recent Posts</div>
            <div class="flex flex-wrap">
                <div v-if="recentArticles.length" class="w-full flex">
                    <div class="w-full xl:w-6 pr-0 xl:pr-6">
                        <div v-if="recentArticles[0]">
                            <img :src="recentArticles[0].urlToImage" alt="Image" class="w-full" />
                            <div class="flex align-items-center mt-4">
                                <img :src="recentArticles[0].urlToImage" class="mr-3 flex-shrink-0" width="28" height="28" />
                                <span class="text-900 font-medium text-lg white-space-nowrap">{{ recentArticles[0].author }}</span>
                                <span class="text-500 font-medium text-lg mx-3">|</span>
                                <span class="text-500 font-medium text-lg white-space-nowrap">{{ recentArticles[0].publishedAt }}</span>
                            </div>
                            <div class="text-900 font-bold text-3xl mt-4">{{ recentArticles[0].title }}</div>
                            <p class="line-height-3 text-700 my-4">{{ recentArticles[0].description }}</p>
                            <div class="flex align-items-center">
                                <span class="text-600 text-sm font-medium">15 min read</span>
                                <span class="text-600 font-medium text-sm mx-3">|</span>
                                <span v-for="tag in recentArticles[0].tags" :key="tag" class="bg-indigo-100 text-indigo-600 text-sm block py-1 px-2 border-round mr-3">{{ tag }}</span>
                            </div>
                        </div>
                    </div>
                    <div class="w-full xl:w-6">
                        <div v-if="recentArticles[1]" class="mb-8">
                            <img :src="recentArticles[1].urlToImage" alt="Image" class="w-full" />
                            <div class="flex align-items-center mt-4">
                                <img :src="recentArticles[1].urlToImage" class="mr-3 flex-shrink-0" width="28" height="28" />
                                <span class="text-900 font-medium text-lg white-space-nowrap">{{ recentArticles[1].author }}</span>
                                <span class="text-500 font-medium text-lg mx-3">|</span>
                                <span class="text-500 font-medium text-lg white-space-nowrap">{{ recentArticles[1].publishedAt }}</span>
                            </div>
                            <div class="text-900 font-bold text-3xl mt-4">{{ recentArticles[1].title }}</div>
                            <p class="line-height-3 text-700 my-4">{{ recentArticles[1].description }}</p>
                            <div class="flex align-items-center">
                                <span class="text-600 text-sm font-medium">12 min read</span>
                                <span v-for="tag in recentArticles[1].tags" :key="tag" class="bg-indigo-100 text-indigo-600 text-sm block py-1 px-2 border-round mr-3">{{ tag }}</span>
                            </div>
                        </div>
                        <div v-if="recentArticles[2]">
                            <img :src="recentArticles[2].urlToImage" alt="Image" class="w-full" />
                            <div class="flex align-items-center mt-4">
                                <img :src="recentArticles[2].urlToImage" class="mr-3 flex-shrink-0" width="28" height="28" />
                                <span class="text-900 font-medium text-lg white-space-nowrap">{{ recentArticles[2].author }}</span>
                                <span class="text-500 font-medium text-lg mx-3">|</span>
                                <span class="text-500 font-medium text-lg white-space-nowrap">{{ recentArticles[2].publishedAt }}</span>
                            </div>
                            <div class="text-900 font-bold text-3xl mt-4">{{ recentArticles[2].title }}</div>
                            <p class="line-height-3 text-700 my-4">{{ recentArticles[2].description }}</p>
                            <div class="flex align-items-center">
                                <span class="text-600 text-sm font-medium">10 min read</span>
                                <span class="text-600 font-medium text-sm mx-3">|</span>
                                <span v-for="tag in recentArticles[2].tags" :key="tag" class="bg-indigo-100 text-indigo-600 text-sm block py-1 px-2 border-round mr-3">{{ tag }}</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-else class="w-full xl:w-6 pr-0 xl:pr-6">
                    <p>No article</p>
                </div>
            </div>
        </div>

        <div class="surface-ground px-4 py-8 md:px-6 lg:px-8">
            <div class="font-bold text-5xl text-900 mb-5 text-center">Featured Articles</div>
            <div class="grid nogutter">
                <div v-for="(article, index) in articles.slice(3)" :key="article.title" class="col-12 lg:col-4 p-3">
                    <div class="shadow-2 border-round h-full surface-card">
                        <img :src="article.urlToImage" alt="Image" class="block w-full border-round-top" />
                        <div class="p-4">
                            <span class="block font-medium text-blue-600 mb-3">{{ article.source.name }}</span>
                            <div class="text-xl text-900 font-medium mb-3 line-height-3">{{ article.title }}</div>
                            <div class="line-height-3 mb-3 text-700">{{ article.description }}</div>
                            <div class="flex">
                                <Avatar image="" shape="circle"></Avatar>
                                <div class="ml-2">
                                    <div class="text-sm font-bold text-900 mb-1">{{ article.author }}</div>
                                    <div class="text-sm flex align-items-center text-700">
                                        <i class="pi pi-calendar mr-1 text-sm"></i>
                                        <span>{{ new Date(article.publishedAt).toLocaleDateString() }}</span>
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

<script>
export default {
    data() {
        return {
            articles: [],
            recentArticles: [],
            country: ''
        };
    },
    methods: {
        async fetchNews(country) {
            const apiKey = '7ead76cf08e64727b0f29af95f89dc72';
            const response = await fetch(`https://newsapi.org/v2/top-headlines?country=${country}&apiKey=${apiKey}`);
            const data = await response.json();
            this.articles = data.articles;
            this.recentArticles = this.articles.slice(0, 3);
        },
        async getCountry() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(async (position) => {
                    const lat = position.coords.latitude;
                    const lon = position.coords.longitude;
                    const geocodeResponse = await fetch(`https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${lat}&longitude=${lon}&localityLanguage=en`);
                    const geocodeData = await geocodeResponse.json();
                    this.country = geocodeData.countryCode.toLowerCase();
                    this.fetchNews(this.country);
                });
            } else {
                console.error('Geolocation is not supported by this browser.');
            }
        }
    },
    mounted() {
        this.getCountry();
    }
};
</script>
