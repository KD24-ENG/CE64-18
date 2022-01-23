<template>
  <div class="stat">
    <v-container fluid>
        <v-row>
            <v-col class="d-flex ml-10" elevation="3" cols="6" sm="3">
                <v-select :items="road" label="เลือกถนน" solo></v-select>
            </v-col>
            <v-col class="d-flex ml-10" elevation="3" cols="6" sm="3">
                <v-select :items="date" label="เลือกวัน" solo></v-select>
            </v-col>
            </v-row>
    </v-container>
      <l-map class="buttom" style="height: 645px" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      </l-map>
  </div>
</template>

<script>
import {LMap, LTileLayer} from 'vue2-leaflet';

export default {
  name: 'Stat',
    components: {
    LMap,
    LTileLayer
    },
    data () {
    return {
      road: ['ราชวิถี', 'นครสวรรค์', 'พระราม5', 'ลาดพร้าว', 'ศรีอยุธยา', 'สามเสน', 'หลานหลวง'],
      date: ['วันทำงาน', 'วันหยุด'],
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:
            '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [13.76492902071622, 100.53823436762788]
    }
}
}
</script>

<style type="text/css">
.buttom {
    z-index: 3;
}
</style>