<template>
 <div class="container">
    <div class="clock">
        <div class="date">
            <p>{{ year }}/{{ month }}/{{ day }}</p>
        </div>
        <div class="time">
            <p>
                {{ hours }}:{{ minute }}<span class="seconds">:{{ seconds }}</span>
            </p>
        </div>
    </div>
 </div>
</template>

<script>

export default{
 name:"ClockScreen",

 data(){
    return{
        //現在の日時を保持
        date: new Date(),
    };
},

computed:{
    //年
    year(){
        return this.date.getFullYear();
    },

    //月
    month(){
        return this.date.getMonth() +1;
    },

    day(){
        return this.dateTimePadding(this.date.getDate());
    },
    hours(){
        return this.dateTimePadding(this.date.gethours());

    },

    minute(){
        return this.dateTimePadding(this.date.getMinutes());
    },

    seconds(){
        return this.dateTimePadding(this.date.getSeconds());
    },

},

mounted(){
    //現在日時をセット
    this.setDate();
    //1秒ごとにsetDate()を実行
    setInterval(() => this.setDate(),1000);
},

methods:{
    //日時を2桁に変更
    dateTimePadding(num){
        return("0" + num).slice(-2);
    },

    //現在日時をセット
    setDate(){
        this.date = new Date();
    },
},
};

</script>



<style>

</style>
