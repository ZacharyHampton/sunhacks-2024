<template>
  <div class="hero-frame">
    <div class="frame-content">
      <!-- Content for the frame will go here later -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeroFrame'
}
</script>

<style scoped>
.hero-frame {
  position: absolute;
  top: 50%;
  right: 5%;
  transform: translateY(-50%);
  height: 70%;
  width: 40%;
  max-width: 500px;
  aspect-ratio: 16 / 9;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.frame-content {
  width: 100%;
  height: 100%;
  background-color: white;
}
</style>