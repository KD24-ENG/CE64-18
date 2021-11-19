<template>
<div>
  <button>บริเวรจราจรหนาแน่นที่สุด</button>
  <button>บริเวณการจราจรปกติ</button>
  <button>ถนนที่มีความเร็วเฉลี่ยสูงที่สุด</button>
  <GMapMap
    :disableUI="false"
    :zoom="12"
    mapType="roadmap"
    :center="{ lat: 38.8977859, lng: -77.0057621 }"
  >
  </GMapMap>
  </div>
</template>

<script>
export default {
  name: 'GoogleMap',
};
</script>
