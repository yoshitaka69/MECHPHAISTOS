<template>
    <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
        <div class="text-900 font-bold text-5xl mb-6">Recent Posts</div>
        <div class="flex flex-wrap">
            <div v-if="articles.length" class="w-full xl:w-6 pr-0 xl:pr-6">
                <div v-for="(article, index) in articles" :key="article.title">
                    <div v-if="index === 0">
                        <!-- 最新の記事 -->
                        <img :src="article.urlToImage" alt="Image" class="w-full" />
                        <div class="flex align-items-center mt-4">
                            <img :src="article.urlToImage" class="mr-3 flex-shrink-0" width="28" height="28" />
                            <span class="text-900 font-medium text-lg white-space-nowrap">{{ article.author }}</span>
                            <span class="text-500 font-medium text-lg mx-3">|</span>
                            <span class="text-500 font-medium text-lg white-space-nowrap">{{ article.publishedAt }}</span>
                        </div>
                        <div class="text-900 font-bold text-3xl mt-4">{{ article.title }}</div>
                        <p class="line-height-3 text-700 my-4">{{ article.description }}</p>
                        <div class="flex align-items-center">
                            <span class="text-600 text-sm font-medium">15 min read</span>
                            <span class="text-600 font-medium text-sm mx-3">|</span>
                            <span v-for="tag in article.tags" :key="tag"
                                class="bg-indigo-100 text-indigo-600 text-sm block py-1 px-2 border-round mr-3">{{ tag }}</span>
                        </div>
                        <div class="w-full xl:w-6"></div>
                    </div>
                    <div v-else-if="index === 1">
                        <!-- 2番目に新しい記事 -->
                        <div class="flex flex-wrap align-items-start mb-8 mt-8 xl:mb-6 xl:mt-0">
                            <div class="w-full xl:w-6 pr-0 xl:pr-4 mb-4 xl:mb-0">
                                <img :src="article.urlToImage" alt="Image" class="w-full" />
                            </div>
                            <div class="w-full xl:w-6">
                                <div class="flex align-items-center">
                                    <img :src="article.urlToImage" class="mr-3 flex-shrink-0" width="28" height="28" />
                                    <span class="text-900 font-medium text-lg white-space-nowrap">{{ article.author }}</span>
                                    <span class="text-500 font-medium text-lg mx-3">|</span>
                                    <span class="text-500 font-medium text-lg white-space-nowrap">{{ article.publishedAt }}</span>
                                </div>
                                <div class="text-900 font-bold text-3xl mt-4">{{ article.title }}</div>
                                <p class="line-height-3 text-700 my-4">{{ article.description }}</p>
                                <div class="flex align-items-center">
                                    <span class="text-600 text-sm font-medium">12 min read</span>
                                    <span v-for="tag in article.tags" :key="tag"
                                class="bg-indigo-100 text-indigo-600 text-sm block py-1 px-2 border-round mr-3">{{ tag }}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-else-if="index === 2">
                        <!-- 3番目に新しい記事 -->
                        <div class="flex flex-wrap align-items-start">
                            <div class="w-full xl:w-6 pr-0 xl:pr-4 mb-4 xl:mb-0">
                                <img :src="article.urlToImage" alt="Image" class="w-full" />
                            </div>
                            <div class="w-full xl:w-6">
                                <div class="flex align-items-center">
                                    <img :src="article.urlToImage" class="mr-3 flex-shrink-0" width="28" height="28" />
                                    <span class="text-900 font-medium text-lg white-space-nowrap">{{ article.author }}</span>
                                    <span class="text-500 font-medium text-lg mx-3">|</span>
                                    <span class="text-500 font-medium text-lg white-space-nowrap">{{ article.publishedAt }}</span>
                                </div>
                                <div class="text-900 font-bold text-3xl mt-4">{{ article.title }}</div>
                                <p class="line-height-3 text-700 my-4">{{ article.description }}</p>
                                <div class="flex align-items-center">
                                    <span class="text-600 text-sm font-medium">10 min read</span>
                                    <span class="text-600 font-medium text-sm mx-3">|</span>
                                    <span v-for="tag in article.tags" :key="tag"
                                class="bg-indigo-100 text-indigo-600 text-sm block py-1 px-2 border-round mr-3">{{ tag }}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="w-full xl:w-6 pr-0 xl:pr-6">
                <p>No article</p>
            </div>
        </div>
    </div>
</template>



<script>
import axios from 'axios';

export default {
    data() {
        return {
            articles: [],
            apiKey: '7ead76cf08e64727b0f29af95f89dc72',
            apiUrl: 'https://newsapi.org/v2/top-headlines',
            params: {
                category: '',  // Default category (can be specified as needed)
                language: 'en',  // Default language
                country: 'us'  // Default country
            }
        };
    },
    methods: {
        fetchNews() {
            axios.get(this.apiUrl, {
                params: {
                    apiKey: this.apiKey,
                    category: this.params.category,
                    language: this.params.language,
                    country: this.params.country
                }
            })
                .then(response => {
                    this.articles = response.data.articles;
                    console.log('Response data:', response.data);  // Log the response data
                })
                .catch(error => {
                    console.error('Error fetching news:', error);
                });
        }
    },
    created() {
        this.fetchNews();  // Fetch news when the component is created
    }
}
</script>
