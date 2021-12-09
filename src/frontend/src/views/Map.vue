<template>
    <div class="container">
        <v-btn text class="mx-3">
            <span>Sign Out</span>
        <v-icon right>logout</v-icon>
        </v-btn>
        <l-map class style="height: 650px" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <l-marker :lat-lng="markerLatLng"></l-marker>
        </l-map>
        
    </div>
</template>

<script>
import {LMap, LTileLayer, LMarker} from 'vue2-leaflet';

export default {
    components: {
    LMap,
    LTileLayer,
    LMarker
    },
    data () {
    return {
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:
            '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        zoom: 15,
        center: [13.756331, 100.501762],
        };
    }
}
</script>

<style>
/*.container {
    margin-right: 0;
    align-items: right;
}*/
</style>
