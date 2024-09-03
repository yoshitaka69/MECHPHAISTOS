<template>
    <div class="clock">
      <div class="digital">
        <span>{{ time.format('HH:mm') }}</span>
      </div>
      <div class="date">{{ time.format('YYYY-MM-DD') }}</div>
      <div class="greeting">{{ greeting }}</div>
      <div class="offset">{{ offset }}</div>
    </div>
  </template>
  
  <script>
  import moment from 'moment-timezone';
  
  export default {
    props: ['timezone'],
    data() {
      return {
        time: moment().tz(this.timezone),
        localTime: moment()
      };
    },
    computed: {
      greeting() {
        const hours = this.time.hours();
        if (hours >= 5 && hours < 12) {
          return 'Morning';
        } else if (hours >= 12 && hours < 17) {
          return 'Afternoon';
        } else if (hours >= 17 && hours < 21) {
          return 'Evening';
        } else {
          return 'Night';
        }
      },
      offset() {
        const offsetMinutes = this.time.utcOffset() - this.localTime.utcOffset();
        const offsetHours = offsetMinutes / 60;
        const sign = offsetHours >= 0 ? '+' : '-';
        return `UTC ${sign}${Math.abs(offsetHours)}`;
      }
    },
    methods: {
      updateTime() {
        this.time = moment().tz(this.timezone);
        this.localTime = moment();
      }
    },
    mounted() {
      this.updateTime();
      setInterval(this.updateTime, 1000);
    }
  };
  </script>
  
  <style scoped>
  .clock {
    width: 150px; /* ここを修正 */
    height: 75px; /* ここを修正 */
    position: relative;
    margin: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 2px solid #333;
    border-radius: 10px;
    background-color: #1a1a1a;
    color: #f0f0f0;
    padding: 10px;
  }
  
  .digital {
    font-size: 2em;
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
  }
  
  .date {
    position: absolute;
    top: 5px;
    left: 10px;
    font-size: 0.8em;
  }
  
  .greeting {
    position: absolute;
    bottom: 5px;
    right: 10px;
    font-size: 0.8em;
  }
  
  .offset {
    position: absolute;
    top: 5px;
    right: 10px;
    font-size: 0.8em;
  }
  </style>
