<template>
    <div>
        <div class="surface-section px-4 py-8 md:px-6 lg:px-8 recent-posts">
            <div class="text-900 font-bold text-5xl mb-6">Recent Posts</div>
            <div class="flex flex-wrap">
                <div v-if="recentArticles.length" class="w-full flex">
                    <div class="w-full xl:w-6 pr-0 xl:pr-6">
                        <div v-if="recentArticles[0]">
                            <img :src="getImageUrl(recentArticles[0].urlToImage)" alt="Image" class="recent-post-image w-full" />
                            <div class="flex align-items-center mt-4">
                                <img :src="getImageUrl(recentArticles[0].urlToImage)" class="recent-post-thumbnail mr-3 flex-shrink-0" width="28" height="28" />
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
                            <button @click="openArticle(recentArticles[0].url)" class="p-button p-component mt-4">Read More</button>
                        </div>
                    </div>
                    <div class="w-full xl:w-6">
                        <div v-if="recentArticles[1]" class="mb-8">
                            <img :src="getImageUrl(recentArticles[1].urlToImage)" alt="Image" class="recent-post-image w-full" />
                            <div class="flex align-items-center mt-4">
                                <img :src="getImageUrl(recentArticles[1].urlToImage)" class="recent-post-thumbnail mr-3 flex-shrink-0" width="28" height="28" />
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
                            <button @click="openArticle(recentArticles[1].url)" class="p-button p-component mt-4">Read More</button>
                        </div>
                        <div v-if="recentArticles[2]">
                            <img :src="getImageUrl(recentArticles[2].urlToImage)" alt="Image" class="recent-post-image w-full" />
                            <div class="flex align-items-center mt-4">
                                <img :src="getImageUrl(recentArticles[2].urlToImage)" class="recent-post-thumbnail mr-3 flex-shrink-0" width="28" height="28" />
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
                            <button @click="openArticle(recentArticles[2].url)" class="p-button p-component mt-4">Read More</button>
                        </div>
                    </div>
                </div>
                <div v-else class="w-full xl:w-6 pr-0 xl:pr-6">
                    <p>No article</p>
                </div>
            </div>
        </div>
  
        <div class="surface-ground px-4 py-8 md:px-6 lg:px-8 featured-articles">
            <div class="font-bold text-5xl text-900 mb-5 text-center">Featured Articles</div>
            <div class="grid nogutter">
                <div v-for="(article, index) in articles.slice(3)" :key="article.title" class="col-12 lg:col-4 p-3">
                    <div class="shadow-2 border-round h-full surface-card">
                        <img :src="getImageUrl(article.urlToImage)" alt="Image" class="featured-article-image block w-full border-round-top" />
                        <div class="p-4">
                            <span class="block font-medium text-blue-600 mb-3">{{ article.source.name }}</span>
                            <div class="text-xl text-900 font-medium mb-3 line-height-3">{{ article.title }}</div>
                            <div class="line-height-3 mb-3 text-700">{{ article.description }}</div>
                            <button @click="openArticle(article.url)" class="p-button p-component mt-4">Read More</button>
                            <div class="flex mt-4">
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
  import noImage from '@/assets/no_image.jpg';
  
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
            try {
                const apiKey = '7ead76cf08e64727b0f29af95f89dc72';
                const response = await fetch(`https://newsapi.org/v2/top-headlines?country=${country}&apiKey=${apiKey}`);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                this.articles = data.articles;
                this.recentArticles = this.articles.slice(0, 3);
            } catch (error) {
                console.error('Error fetching news:', error);
            }
        },
        async getCountry() {
            try {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(async (position) => {
                        try {
                            const lat = position.coords.latitude;
                            const lon = position.coords.longitude;
                            const geocodeResponse = await fetch(`https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${lat}&longitude=${lon}&localityLanguage=en`);
                            if (!geocodeResponse.ok) {
                                throw new Error(`HTTP error! status: ${geocodeResponse.status}`);
                            }
                            const geocodeData = await geocodeResponse.json();
                            this.country = geocodeData.countryCode.toLowerCase();
                            this.fetchNews(this.country);
                        } catch (error) {
                            console.error('Error getting geocode data:', error);
                        }
                    }, (error) => {
                        console.error('Geolocation error:', error);
                    });
                } else {
                    console.error('Geolocation is not supported by this browser.');
                }
            } catch (error) {
                console.error('Error getting country:', error);
            }
        },
        getImageUrl(url) {
            return url && url !== null ? url : noImage;
        },
        openArticle(url) {
            window.open(url, '_blank');
        }
    },
    mounted() {
        this.getCountry();
    }
  };
  </script>
  
  <style scoped>
  .recent-posts .recent-post-image {
    max-width: 90%;
    max-height: 250px;
  }
  
  .recent-posts .recent-post-thumbnail {
    max-width: 50px;
    max-height: 50px;
  }
  
  .featured-articles .featured-article-image {
    max-width: 100%;
    max-height: 200px;
  }
  
  .p-button {
    background-color: #007bff;
    color: white;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .p-button:hover {
    background-color: #0056b3;
  }
  </style>
  