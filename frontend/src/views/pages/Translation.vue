<template>
    <div>
      <label for="language-select">Select Language:</label>
      <select id="language-select" v-model="selectedLanguage" @change="changeLanguage">
        <option value="en">English</option>
        <option value="ja">日本語</option>
      </select>
  
      <!-- サンプルの文 -->
      <p>{{ $t('greeting') }}</p>
      <p>{{ $t('description') }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedLanguage: this.$i18n.locale // 現在の言語を初期値として設定
      };
    },
    methods: {
      changeLanguage() {
        console.log("Language changed to:", this.selectedLanguage); // 言語変更時にコンソール出力
        this.$i18n.locale = this.selectedLanguage;
        // 必要に応じてローカルストレージに保存するなど、選択言語を永続化できます
        localStorage.setItem('selectedLanguage', this.selectedLanguage);
      }
    },
    mounted() {
      // ページリロード時に選択言語を復元
      const savedLanguage = localStorage.getItem('selectedLanguage');
      if (savedLanguage) {
        console.log("Restoring saved language:", savedLanguage); // 言語復元時にコンソール出力
        this.selectedLanguage = savedLanguage;
        this.$i18n.locale = savedLanguage;
      } else {
        console.log("No saved language, using default:", this.selectedLanguage); // デフォルト言語の確認
      }
    }
  };
  </script>
  