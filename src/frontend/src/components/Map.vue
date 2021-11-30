<template>
    <div class="map">
        <h1>{{ msg }}</h1>
        <p>Hollo My Map</p>
    </div>
</template>

<script>
export default {
    name: 'Map',
    props: {
    msg: String
    }
}
</script>

<style scoped>
h1 {
    margin: 40px 0 0;
}
</style>