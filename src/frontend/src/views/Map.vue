<template>
    <div class="map">
        <v-container fluid>
        <v-row>
            <v-col class="d-flex ml-10" elevation="3" cols="6" sm="3">
                <v-select :items="items" label="เลือกถนน" solo></v-select>
            </v-col>
            <v-checkbox v-model="checkbox">
                <template v-slot:label>
                    <div>
                        ปัจจุบัน
                    <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                <a
                target="_blank"
                href="https://vuetifyjs.com"
                @click.stop
                v-on="on"
                >
                
                </a>
            </template>
            Opens in new window
                </v-tooltip>
        </div>
                </template>
    </v-checkbox>
        </v-row>
    </v-container>
        <l-map class="buttom" style="height: 645px" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <l-marker :lat-lng="markerLatLng"></l-marker>
        <l-polyline :lat-lngs="polyline.latlngs" :color="polyline.color"></l-polyline>
        </l-map>
    </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>

<script>
import {LMap, LTileLayer, LPolyline} from 'vue2-leaflet';

export default {
    components: {
    LMap,
    LTileLayer,
    LPolyline,
    },
    data () {
    return {
        items: ['นครสวรรค์', 'พระราม5', 'ลาดพร้าว', 'ศรีอยุธยา', 'สามเสน', 'หลานหลวง'],
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        zoom: 15,
        center: [13.76492902071622, 100.53823436762788],
        polyline: {
        latlngs: [[47.334852, -1.509485], [47.342596, -1.328731], [47.241487, -1.190568], [47.234787, -1.358337]],
        color: 'green'
        }
        };
    }
}
</script>

<style type="text/css">
.buttom {
    z-index: 3;
}
</style>
