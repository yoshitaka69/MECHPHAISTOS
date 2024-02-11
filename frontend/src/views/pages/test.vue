<template>
    <div id="app" class="watch-body">
        <!-- 時刻 -->
        <div class="number">
            <div class="letter-wrapper"><span>12</span></div>
            <div class="letter-wrapper"><span>1</span></div>
            <div class="letter-wrapper"><span>2</span></div>
            <div class="letter-wrapper"><span>3</span></div>
            <div class="letter-wrapper"><span>4</span></div>
            <div class="letter-wrapper"><span>5</span></div>
            <div class="letter-wrapper"><span>6</span></div>
            <div class="letter-wrapper"><span>7</span></div>
            <div class="letter-wrapper"><span>8</span></div>
            <div class="letter-wrapper"><span>9</span></div>
            <div class="letter-wrapper"><span>10</span></div>
            <div class="letter-wrapper"><span>11</span></div>
        </div>

        <!-- 針 -->
        <div class="hands">
            <span class="dot"></span>
            <span class="hour-hand-wrapper" :style="{ transform: 'rotate(' + calcHourHandAngle + 'deg)' }">
                <span class="hour-hand"></span>
            </span>
            <span class="minute-hand-wrapper" :style="{ transform: 'rotate(' + calcMinuteHandAngle + 'deg)' }">
                <span class="minute-hand"></span>
            </span>
            <span class="second-hand-wrapper" :style="{ transform: 'rotate(' + calcSecondHandAngle + 'deg)' }">
                <span class="second-hand"></span>
            </span>
        </div>
    </div>
</template>

<script>



</script>


<style>
* {
        margin:0;
        box-sizing:border-box;
        font-family: 'Signika Negative', sans-serif;
    }

    html {
        height: 100%;
    }
    body {
        padding:50px;
        height:100%;
        display:flex;
        justify-content:center;
        align-items:center;
        background:#444;
    }

    /* 時計本体 */
    .watch-body {
        border:10px solid #444;
        border-radius:100%;
        display:block;
        position:relative;
        height:300px;
        aspect-ratio:1/1;
        background:#fff;
    }

    /* 盤面文字 */
    .watch-body .number {
        position:absolute;
        left:0;
        top:0;
        border-radius:100%;
        width:100%;
        height:100%;
    }

    .watch-body .number div.letter-wrapper {
        position:absolute;
        width:2em;
        height:2em;
        font-weight:bold;
        display:inline-flex;
        align-items:flex-start;
        justify-content:center;
        font-size:20px;
        height:100%;
        padding:10px 0;
        top:0;
        left:calc((100% - 2em) / 2);
    }
    
    .watch-body .number div.letter-wrapper:nth-of-type(2) {
        transform:rotate(30deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(2) span {
        transform:rotate(-30deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(3) {

        transform:rotate(60deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(3) span {
        transform:rotate(-60deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(4) {
        transform:rotate(90deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(4) span {
        transform:rotate(-90deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(5) {
        transform:rotate(120deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(5) span {
        transform:rotate(-120deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(6) {
        transform:rotate(150deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(6) span {
        transform:rotate(-150deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(7) {
        transform:rotate(180deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(7) span {
        transform:rotate(-180deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(8) {
        transform:rotate(210deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(8) span {
        transform:rotate(-210deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(9) {
        transform:rotate(240deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(9) span {
        transform:rotate(-240deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(10) {
        transform:rotate(270deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(10) span {
        transform:rotate(-270deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(11) {
        transform:rotate(300deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(11) span {
        transform:rotate(-300deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(12) {
        transform:rotate(330deg);
    }

    .watch-body .number div.letter-wrapper:nth-of-type(12) span {
        transform:rotate(-330deg);
    }

    /* 針 */
    .watch-body .dot {
        display: block;
        width: 8px;
        height: 8px;
        background: #fff;
        border-radius: 100%;
        position: absolute;
        left: calc((100% - 8px) / 2);
        top: calc((100% - 8px) / 2);
        z-index: 999;
    }

    .watch-body .hour-hand-wrapper {
        position:absolute;
        height:100%;
        width:15px;
        left:calc((100% - 15px) / 2);
        top:0;
    }

    .watch-body .hour-hand-wrapper .hour-hand {
        background: #444;
        width: 100%;
        height: 35%;
        position: absolute;
        left: 0;
        top: 20%;
        border-radius: 100px;
    }

    .watch-body .minute-hand-wrapper {
        position: absolute;
        height: 100%;
        width: 10px;
        left: calc((100% - 10px) / 2);
        top: 0;
    }

    .watch-body .minute-hand-wrapper .minute-hand {
        background: #444;
        width: 100%;
        height: 45%;
        position: absolute;
        left: 0;
        top: 10%;
        border-radius: 100px;
    }

    .watch-body .second-hand-wrapper {
        position: absolute;
        height: 100%;
        width: 5px;
        left: calc((100% - 5px) / 2);
        top: 0;
    }

    .watch-body .second-hand-wrapper .second-hand {
        background: #444;
        width: 100%;
        height: 45%;
        position: absolute;
        left: 0;
        top: 10%;
        border-radius: 100px;
    }

</style>