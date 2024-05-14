<template>
    <div class="home-contents">
      <div class="header">
        <img src="@/assets/MECHPHAISTOS cover.jpg" />
        <h1 class="title">Welcome to MECHPHASTOS</h1>
      </div>
      <div class="section">
        <WorldClock />
      </div>
      <div class="section">
        <Weather />
      </div>
      <div class="section">
        <InformationBox message="これは管理人からのお知らせです。" />
      </div>
      <div class="section">
        <News_content />
      </div>
    </div>
  </template>
  
  <script>
  import News_content from '@/components/News/News_content.vue';
  import WorldClock from '@/components/Clock/WorldClock.vue';
  import Weather from '@/components/Weather/Weather.vue';
  import InformationBox from '@/components/Information_box/Information_box.vue';
  
  export default {
    components: {
      News_content,
      WorldClock,
      Weather,
      InformationBox,
    },
  };
  </script>
  
  <style scoped>
  .home-contents {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 20px; /* セクション間のスペース */
  }
  
  .header {
    position: relative;
    width: 100%;
  }
  
  .header img {
    object-fit: cover;
    width: 100%;
    height: 130px;
  }
  
  /* 背景画像を暗くしても welcome to… を目立たせる */
  .header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    display: block;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.4);
  }
  
  .title {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 0;
    margin: 0;
    font-size: 30px;
    color: #fff;
  }
  
  .section {
    width: 100%;
    max-width: 1000px; /* 各セクションの最大幅を広げる */
    margin: 0 10px; /* 両サイドのスペースを調整 */
  }
  </style>
  