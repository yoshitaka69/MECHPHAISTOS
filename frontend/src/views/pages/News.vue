<template>
    <div class="home-contents">
        <img src="@/assets/MECHPHAISTOS cover.jpg">
        <h1 class="title">Welcome to MECHPHASTOS</h1>
    </div>
    <section>
        <div class="row">
            <div>
                <News_content />
            </div>
        </div>
    </section>
</template>



<script>

import News_content from '@/components/News/News_content.vue';


export default {
    components: {

        News_content,
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