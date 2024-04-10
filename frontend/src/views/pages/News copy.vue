<template>
	<div>
		<div class="home-contents">
			<img src="@/assets/MECHPHAISTOS cover.jpg">
			<h1 class="title">Welcome to MECHPHASTOS</h1>
		</div>

		<section>
			<div class="clock">
				<Clock />
			<div class="information">

				<information />
			</div>

			</div>

		</section>
		<section>
			<div class="weather">
				<Weather />
			     </div>

				 
			<div class="tab-wrap">
				<input id="TAB-01" type="radio" name="TAB" class="tab-switch" checked="checked" /><label class="tab-label"
					for="TAB-01">News</label>
				<div class="tab-content">
					<News />
				</div>

				<input id="TAB-02" type="radio" name="TAB" class="tab-switch" /><label class="tab-label"
					for="TAB-02">機械</label>
				<div class="tab-content">
					機械の関係
				</div>

				<input id="TAB-03" type="radio" name="TAB" class="tab-switch" /><label class="tab-label"
					for="TAB-03">電気</label>
				<div class="tab-content">
					電気関係
				</div>

				<input id="TAB-04" type="radio" name="TAB" class="tab-switch" /><label class="tab-label"
					for="TAB-04">プログラミング</label>
				<div class="tab-content">
					プログラミング
					<Qiita />
				</div>
			</div>
		</section>
		
	</div>
</template>


<script>
import Clock from '@/components/Clock/Clock.vue'
import News from '@/components/News/News.vue'
import Qiita from '@/components/Qiita_api/Qiita_api'
import Weather from '@/components/Weather/Weather.vue'
import information from '@/components/information.vue'



export default {
  components: {
    Clock,
	News,
	Qiita,
	Weather,
	information
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
.home-contents::before{
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0, 0.4);
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

.clock {
	display: flex;
	flex-direction: column;
	text-align: center;
}


.tab-wrap {
	background: White;
	box-shadow: 0 0 5px rgba(0, 0, 0, .1);
	display: flex;
	flex-wrap: wrap;
	-webkit-justify-content: center;
	justify-content: center;
	-webkit-align-items: center;
	align-items: center;
	overflow: hidden;
	padding: 10px 50px 20px;
}

.tab-label {
	color: Gray;
	cursor: pointer;
	flex: 1;
	font-weight: bold;
	order: -1;
	padding: 12px 24px;
	position: relative;
	text-align: center;
	transition: cubic-bezier(0.4, 0, 0.2, 1) .2s;
	user-select: none;
	white-space: nowrap;
	-webkit-tap-highlight-color: transparent;
}

.tab-label:hover {
	background: rgba(0, 191, 255, .1);
}

.tab-switch:checked+.tab-label {
	color: DeepSkyBlue;
}

.tab-label::after {
	background: DeepSkyBlue;
	bottom: 0;
	content: '';
	display: block;
	height: 3px;
	left: 0;
	opacity: 0;
	pointer-events: none;
	position: absolute;
	transform: translateX(100%);
	transition: cubic-bezier(0.4, 0, 0.2, 1) .2s 80ms;
	width: 100%;
	z-index: 1;
}

.tab-switch:checked~.tab-label::after {
	transform: translateX(-100%);
}

.tab-switch:checked+.tab-label::after {
	opacity: 1;
	transform: translateX(0);
}

.tab-content {
	height: 0;
	opacity: 0;
	padding: 0 20px;
	pointer-events: none;
	transform: translateX(-30%);
	transition: transform .3s 80ms, opacity .3s 80ms;
	width: 100%;
}

.tab-switch:checked~.tab-content {
	transform: translateX(30%);
}

.tab-switch:checked+.tab-label+.tab-content {
	height: auto;
	opacity: 1;
	order: 1;
	pointer-events: auto;
	transform: translateX(0);
}

.tab-wrap::after {
	content: '';
	height: 20px;
	order: -1;
	width: 100%;
}

.tab-switch {
	display: none;
}

/* ============================== */

body {
	background: WhiteSmoke;
	font-family: sans-serif;
	margin: 10px;
}

.information{
	display:flex;
}



</style>