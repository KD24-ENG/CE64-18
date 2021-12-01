<template>
  <v-app>
    <v-app-bar
      app
      color="#39A388"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="130"
          src="https://sv1.picz.in.th/images/2021/12/01/6R5keV.png"
          width="130"
        />
      </div>

      <v-spacer></v-spacer>
      <v-toolbar-title class="my-2">
        <h6 class="subheading font-weight-bold">Bangkok Traffic Reporting System</h6>
      </v-toolbar-title>

    </v-app-bar>

    <v-main class="text-center">
      <router-link to="/">ข้อมูลรวมการจราจร</router-link> |
      <router-link to="/stat">สถิติการจราจรรายพื้นที่</router-link> |
      <router-link to="/about">เกี่ยวกับ</router-link>
      <router-view/>
    </v-main>
    <v-footer color="#39A388">
        <p class="footer center">© 2021 Bangkok Traffic Reporting System</p>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style>

</style>