<template>
		<div class="home-contents">
			<img src="@/assets/MECHPHAISTOS cover.jpg">
			<h1 class="title">Welcome to MECHPHASTOS</h1>
		</div>
</template>










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

.information {
	display: flex;
}
</style>