<template>
  <div class="app">
    <navbar/>
    <v-app-bar-title>
        <v-btn plain :to="{name: 'Home'}" class="text-h3">Bangkok Traffic Reporting System</v-btn>
      </v-app-bar-title>
    <div class="nav">
      <router-link to="/">ข้อมูลรวมการจราจร</router-link> |
      <router-link to="/stat">สถิติการจราจรรายพื้นที่</router-link> |
      <router-link to="/about">เกี่ยวกับ</router-link> 
    </div>
    <router-view/>
    <v-footer color="green">
        <p class="footer">© 2021 Bangkok Traffic Reporting System</p>
    </v-footer>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar
  }
}

</script>

<style>
#app {
  margin: 0px;
  width: 100%;
}

.nav {
  margin-left: auto;
  margin-right: auto;
  max-width: 1280px;
  
  flex-direction: row;
  align-items: center;
  gap: 20px;
}

.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #202020;
  color: white;
  text-align: center;
}
</style>
