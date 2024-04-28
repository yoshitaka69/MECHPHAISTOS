<template>
    <div class="home-contents">
        <img src="@/assets/MECHPHAISTOS cover.jpg">
        <h1 class="title">Welcome to MECHPHASTOS</h1>
    </div>

    <section>
        <div class="row">
            <div>
                <Clock />
            </div>
        </div>
    </section>

    <section>

        <div class="row">
            <div>
                <Emphasized_post />
            </div>
        </div>

    </section>

    <div class="row">
        <div>
            <Featured_articles />
        </div>
        </div>


</template>



<script>

import Clock from '@/components/Clock/Clock.vue';
import Emphasized_post from '@/components/News/Emphasized_post.vue';
import Featured_articles from '@/components/News/Featured_articles.vue';

export default {
    components: {

        Clock,
        Emphasized_post,
        Featured_articles,
    },
}


</script>




<style lang="css">
.home-contents {
    display: flex;
    flex-direction: column;
    text-align: center;
    position: relative;
    /*画像上の文字を中央に配置するため*/
}

.home-contents img {
    object-fit: cover;
    /*画像のトリミングのため*/
    width: 100%;
    height: 130px;
}

/*背景画像を暗くしてもwelcome to…を目立たせる*/
.home-contents::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    display: block;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.4);
}


/*welcome to MECHPHAISTOS*/
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
</style>