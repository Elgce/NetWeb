<template>
    <span class = "clock">{{nowTime}}</span>
</template>
<!-- a template using single js to make a changing clock shown on the page -->
 <script>
    export default {
    name: 't_Clock',
    data () {
        return {
            timer: null,
            nowTime:"",
            hour: 0,
            minutes: 0,
            seconds: 0
        }
    },
    created () {
        this.timer = setInterval(this.startTimer, 1000);
    },
    methods: {
    startTimer () {
        if(!this.timer) {
            clearInterval(this.timer);
		}
        this.seconds += 1;
        if (this.seconds >= 60) {
            this.seconds = 0;
            this.minutes= this.minutes+ 1;
        }
        if (this.minutes>= 60) {
            this.minutes= 0;
            this.hour = this.hour + 1;
        }
        this.nowTime = this.toZero(this.hour)+':'+this.toZero(this.minutes)+':'+this.toZero(this.seconds)
    },
    toZero(timeNumber) {
        return timeNumber<10?"0"+timeNumber:timeNumber
    },
 }
}
</script>