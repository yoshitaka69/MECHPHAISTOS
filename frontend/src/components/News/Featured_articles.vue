<template>
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
