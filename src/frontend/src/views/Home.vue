<template>
  <div class="home">
    <Map msg="Test map"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Map from '@/components/Map.vue'

export default {
  name: 'Home',
  components: {
    Map
  }
}
</script>

<style>

</style>
