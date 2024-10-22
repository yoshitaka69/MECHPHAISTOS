<template>
    <div class="clock-container">
        <svg viewBox="0 0 100 100" class="clock-face">
            <defs>
                <mask id="clock-mask">
                    <rect x="0" y="0" width="100" height="100" fill="white" />
                    <circle cx="50" cy="50" r="45" fill="black" />
                </mask>
            </defs>
            <circle cx="50" cy="50" r="48" class="clock-border" />
            <g v-for="(zone, index) in warningZones" :key="index">
                <path :d="zone.path" :fill="zone.color" />
                <text v-if="zone.label" :x="getLabelTextX(zone)" :y="getLabelTextY(zone)" class="warning-text" dominant-baseline="middle" text-anchor="middle">
                    {{ zone.label }}
                </text>
            </g>
            <circle cx="50" cy="50" r="45" fill="white" mask="url(#clock-mask)" />
            <g v-for="hour in 12" :key="hour">
                <text :x="getHourTextX(hour)" :y="getHourTextY(hour)" class="hour-text" dominant-baseline="middle">
                    {{ hour }}
                </text>
            </g>
            <path :d="hourHandPath" class="hand hour-hand" :style="hourHandStyle" />
            <path :d="minuteHandPath" class="hand minute-hand" :style="minuteHandStyle" />
            <path :d="secondHandPath" class="hand second-hand" :style="secondHandStyle" />
            <circle cx="50" cy="50" r="1.5" class="center-dot" />
        </svg>
    </div>
</template>

<script>
export default {
    data() {
        return {
            time: new Date(),
            warningZones: [
                {
                    start: 7,
                    end: 10,
                    color: 'rgba(255, 0, 0, 0.2)',
                    label: 'Warning'
                },
                {
                    start: 15,
                    end: 17,
                    color: 'rgba(255, 0, 0, 0.2)',
                    label: 'Warning'
                }
            ]
        };
    },
    computed: {
        hourHandStyle() {
            const hours = this.time.getHours() % 12;
            const degrees = (hours + this.time.getMinutes() / 60) * 30;
            return { transform: `rotate(${degrees}deg)`, transformOrigin: '50% 50%' };
        },
        minuteHandStyle() {
            const minutes = this.time.getMinutes();
            const degrees = minutes * 6;
            return { transform: `rotate(${degrees}deg)`, transformOrigin: '50% 50%' };
        },
        secondHandStyle() {
            const seconds = this.time.getSeconds();
            const degrees = seconds * 6;
            return { transform: `rotate(${degrees}deg)`, transformOrigin: '50% 50%' };
        },
        hourHandPath() {
            return 'M50 50 L50 30 L48 30 L52 30 Z'; // Custom shape for hour hand
        },
        minuteHandPath() {
            return 'M50 50 L50 20 L49 20 L51 20 Z'; // Custom shape for minute hand
        },
        secondHandPath() {
            return 'M50 50 L50 15 L49.5 15 L50.5 15 Z'; // Custom shape for second hand
        }
    },
    methods: {
        calculateWarningZonePath(start, end) {
            const startAngle = start * 30 - 90;
            const endAngle = end * 30 - 90;
            const largeArcFlag = end - start <= 6 ? 0 : 1;
            const startCoords = this.polarToCartesian(50, 50, 45, startAngle);
            const endCoords = this.polarToCartesian(50, 50, 45, endAngle);

            return ['M', startCoords.x, startCoords.y, 'A', 45, 45, 0, largeArcFlag, 1, endCoords.x, endCoords.y, 'L', 50, 50, 'Z'].join(' ');
        },
        polarToCartesian(centerX, centerY, radius, angleInDegrees) {
            const angleInRadians = (angleInDegrees * Math.PI) / 180.0;
            return {
                x: centerX + radius * Math.cos(angleInRadians),
                y: centerY + radius * Math.sin(angleInRadians)
            };
        },
        getHourTextX(hour) {
            const angle = hour * 30 - 90;
            return 50 + Math.cos((angle * Math.PI) / 180) * 40;
        },
        getHourTextY(hour) {
            const angle = hour * 30 - 90;
            return 50 + Math.sin((angle * Math.PI) / 180) * 40;
        },
        getLabelTextX(zone) {
            const middleAngle = ((zone.start + zone.end) / 2) * 30 - 90;
            return 50 + Math.cos((middleAngle * Math.PI) / 180) * 25;
        },
        getLabelTextY(zone) {
            const middleAngle = ((zone.start + zone.end) / 2) * 30 - 90;
            return 50 + Math.sin((middleAngle * Math.PI) / 180) * 25;
        }
    },
    mounted() {
        setInterval(() => {
            this.time = new Date();
        }, 1000);

        this.warningZones = this.warningZones.map((zone) => ({
            ...zone,
            path: this.calculateWarningZonePath(zone.start, zone.end)
        }));
    }
};
</script>

<style scoped>
.clock-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}

.clock-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #fff9c4;
    position: relative;
    padding: 2%;
    flex-grow: 1;
    height: 100%; /* 親要素の高さに合わせる */
    width: auto; /* 高さに合わせて幅を自動調整（アスペクト比維持） */
}

.clock-face {
    height: 100%; /* 親要素に対して高さ100% */
    width: auto;  /* アスペクト比を保ちながら高さに合わせて横幅を調整 */
    background-color: #f0f0f0;
    border-radius: 50%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.clock-border {
    fill: none;
    stroke: #333;
    stroke-width: 2;
}

.hand {
    stroke-linecap: round;
    transform-origin: center;
}

.hour-hand,
.minute-hand,
.second-hand {
    fill: #333;
}

.center-dot {
    fill: #333;
}

.hour-text {
    font-size: 0.6em;
    text-anchor: middle;
    fill: #333;
}

.warning-text {
    font-size: 0.55em;
    fill: #ff0000;
    font-weight: bold;
}


</style>
