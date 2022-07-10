<template>
    <span class = "flux">{{nowFlux}}</span>
</template>

<script>
    export default {
        name: 't_Flux',
        data() {
            return{
                nowFlux:"",
                flux: 0,
            }
        },
        created () {
            this.nowFlux = this.startFlux();
        },
        methods: {
            startFlux () {
                let that = this;
                fetch("/api/flux").then((res) => res.json().then((j) => {
                    that.flux = j.flux
                    that.nowFlux = this.flux+ "G"
                }))
            },
        }
    }
</script>