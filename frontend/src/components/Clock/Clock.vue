<template>
    <div class="container">
        <div class="clock_hou">
            <div class="date">
                <p>{{ year }}/{{ month }}/{{ day }}</p>
            </div>
            <div class="time">
                <p>
                    {{ hours }}:{{ minutes }}<span class="second">:{{ seconds }}</span>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name : "Clock",
    data(){
        return{
            date:new Date(),
        };
    },
    computed:{
        year(){
            return this.date.getFullYear();
        },

        month(){
            return this.date.getMonth() +1;
        },

        day(){
            return this.dateTimePadding(this.date.getDate());
        },
        hours(){
            return this.dateTimePadding(this.date.getHours());
        },
        minutes(){
            return this.dateTimePadding(this.date.getMinutes())
        },
        seconds(){
            return this.dateTimePadding(this.date.getSeconds())
        },
        },
        mounted(){
            this.setDate();
            setInterval(() => this.setDate(),1000);
        },

    methods:{
        dateTimePadding(num){
            return("0"+num).slice(-2);
        },
        setDate(){
            this.date = new Date();
        },
    }
}
</script>

<style scoped>
.container{
    height:100%;
    display:flex;
    flex-flow:column;
    justify-content: center;
    align-items:center;
    background-color: #262626;
}

p{
    margin:0px;
}

.date,
.time{
    font-weight: 700;
    color:#00ff01;
}
.date{
    font-size:16px;
    text-align: right;
}
.time{
    font-size: 70px;
}
.seconds{
    font-size: 30px;
}

</style>