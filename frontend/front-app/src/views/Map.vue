<template>
    <div>
        <h1>Test one</h1>
        <p>{{ coordinates.lat }} Latitude, {{ coordinates.lng }} Longitude</p>
    </div>
</template>
<script>
export default {
    data() {
        return {
            coordinates: {
                lat: 0,
                lng: 0
            }
        }
    },
    create() {
        // get user's coordinates from browser request
    }
}
</script>