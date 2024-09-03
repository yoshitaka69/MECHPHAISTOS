<template>
	<div class="name-notebook">
	  <div class="a4-paper" v-for="index in 3" :key="index">
		<div class="content-left">
		  <textarea placeholder="Left side content..."></textarea>
		</div>
		<div class="divider"></div>
		<div class="content-right">
		  <textarea placeholder="Right side content..."></textarea>
		</div>
	  </div>
	</div>
  </template>
  
  <script lang="ts" setup>
  // 特にJavaScript部分が必要なければ、ここにはコードはありません。
  </script>
  
  <style scoped>
  .name-notebook {
	display: flex;
	flex-direction: column;
	align-items: center;
	padding: 20px;
	background-image: 
	  url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" width="150" height="50"><text x="0" y="25" font-size="16" fill="%23999" transform="rotate(-20)">daily report</text></svg>');
	background-size: 280px 50px;
	background-repeat: repeat;
	opacity: 0.5;
  }
  
  .a4-paper {
	width: 297mm;    /* A4の幅 (横向き) */
	height: 210mm;   /* A4の高さ (横向き) */
	background: white; 
	padding: 20mm;   
	border: 1px solid #000; 
	box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); 
	margin-bottom: 20px; /* 各用紙の間のスペース */
	display: flex;
	position: relative;
  }
  
  .content-left, .content-right {
	padding: 10px;
	height: 100%;
  }
  
  .content-left {
	width: 33%;
  }
  
  .content-right {
	width: 67%; /* 黒線の分だけ右側を広く */
  }
  
  .divider {
	width: 1px;
	background-color: black;
	height: calc(100% - 40mm); /* A4用紙の縦全体に黒線を表示 */
	position: absolute;
	left: 33%;
	top: 20mm; /* パディングの影響を考慮 */
  }
  
  textarea {
	width: 100%;
	height: calc(100% - 20px);
	border: none; /* ボーダーなしにして区切り線のみ使用 */
	resize: none;
	padding: 10px;
	box-sizing: border-box;
	font-size: 14px;
	outline: none; /* フォーカス時のアウトラインを非表示 */
  }
  </style>
  