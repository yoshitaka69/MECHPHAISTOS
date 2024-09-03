<template>
    <div>
        <input v-model="userId" placeholder="ユーザーIDを入力してください">
        <button @click="getQiitaData">取得開始</button>
        <div v-if="isClick">
            <div v-for="(item, index) in displayQiitaDataList.slice(0, displayedCount)" :key="index" class="card">
                <h3>{{ item.title }}</h3>
                <p><a :href="item.url" target="_blank">{{ item.url }}</a></p>
                <p>LGTM: {{ item.likes_count }}</p>
                <p>投稿日時: {{ formatDate(item.created_at) }}</p>
            </div>
            <button v-if="displayedCount < displayQiitaDataList.length" @click="showMore">続きを表示</button>
            <div>
                <h3>記事数 {{ totalArticle }}コ</h3>
                <h3>LGTM数 {{ totalLGTM }}コ</h3>
            </div>
        </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
        return {
            userId: "",
            displayQiitaDataList: [],
            totalArticle: 0,
            totalLGTM: 0,
            isClick: false,
            displayedCount: 5,
        }
    },
    methods: {
        getQiitaData() {
            axios.get(`https://qiita.com/api/v2/users/${this.userId}/stocks?page=1&per_page=100`)
                .then(res => {
                    let allQiitaData = res.data;
  
                    let displayQiitaDataList = [];
                    let totalLGTM = 0;
                    allQiitaData.forEach(item => {
                        displayQiitaDataList.push(item);
                        totalLGTM += item.likes_count;
                    });
  
                    this.displayQiitaDataList = displayQiitaDataList;
                    this.totalLGTM = totalLGTM;
                    this.totalArticle = displayQiitaDataList.length;
                    this.isClick = true;
                })
                .catch(error => {
                    console.error("APIリクエストに失敗しました:", error);
                    alert("ユーザーIDが正しいか確認してください。");
                });
        },
        showMore() {
            this.displayedCount = Math.min(this.displayedCount + 5, this.displayQiitaDataList.length);
        },
        formatDate(date) {
            const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
            return new Date(date).toLocaleDateString('ja-JP', options);
        }
    }
  }
  </script>
  
  <style>
  .card {
    border: 1px solid #ddd;
    padding: 16px;
    margin-bottom: 16px;
    border-radius: 8px;
  }
  </style>
  