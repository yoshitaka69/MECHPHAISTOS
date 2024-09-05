<template>
  <div>
    <label for="language-select">Select Language:</label>
    <select id="language-select" v-model="selectedLanguage" @change="changeLanguage">
      <option value="en">English</option>
      <option value="ja">日本語</option>
      <!-- 他の言語オプションを追加 -->
    </select>
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
      this.$i18n.locale = this.selectedLanguage;
      // 必要に応じてローカルストレージに保存するなど、選択言語を永続化できます
      localStorage.setItem('selectedLanguage', this.selectedLanguage);
    }
  },
  mounted() {
    // ページリロード時に選択言語を復元
    const savedLanguage = localStorage.getItem('selectedLanguage');
    if (savedLanguage) {
      this.selectedLanguage = savedLanguage;
      this.$i18n.locale = savedLanguage;
    }
  }
};
</script>
