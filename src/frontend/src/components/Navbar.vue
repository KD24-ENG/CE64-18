<template>
    <nav>
        <v-toolbar flat app>
            <v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title class="grey--text">
                <span class="display-1 font-weight-black green--text">BTRS</span>
                <span class="font-weight-bold">Bangkok Traffic Reporting System</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <!--v-btn text>
                <span>Sign Out</span>
            <v-icon right>logout</v-icon>
            </v-btn-->
        </v-toolbar>

        <!--absolute temporary, permanent cliped,  absolute temporary clipped-->
        <v-navigation-drawer app v-model="drawer" class="teal " absolute temporary>
            <v-list nav dense>
                <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-item-action>
                        <v-icon class="white--text">{{ link.icon }}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title class="white--text">{{ link.text }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>

    </nav>
</template>

<script>
export default {
    data: () => ({
            drawer: null,
            links: [
                { icon: 'home', text: 'Home', route: '/'},
                { icon: 'map', text: 'Map', route: '/map'},
                { icon: 'dashboard', text: 'Dashboard', route: '/dashboard'},
                { icon: 'equalizer', text: 'Stat', route: '/stat'},
                { icon: 'contacts', text: 'About', route: '/about'},
            ]
        }),
    }
</script>

<style>
.v-navigation-drawer--temporary {
    z-index: 1001;
}
</style>