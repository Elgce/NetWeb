<template>
    <span class = "flux">{{nowFlux}}</span>
</template>
<!-- template for the flux num, show how much flux the user has used -->
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
            this.startFlux();
        },
        methods: {
            startFlux () {
                let that = this;
                fetch("/api/flux").then((res) => res.json().then((j) => {
                    that.flux = j.flux
                    that.nowFlux = parseFloat(this.flux).toFixed(2)+ " G"
                }))
            },
        }
    }
</script>