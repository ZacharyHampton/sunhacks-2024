<script>
  import NavBar from '@/pages/components/NavBar.vue';
  import GradientSection from '@/pages/components/GradientSection.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    GradientSection,
  },
}
</script>

<template>
  <div id="app">
    <section>
    <NavBar />
    <GradientSection />
      </section>
    <section>
    </section>
  </div>
</template>

<style>
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
}

#app {
  width: 100%;
  min-height: 100vh;
  font-family: 'Proxima Nova', sans-serif;
}
@font-face {
  font-family: 'Proxima Nova';
  src: url('components/ui/font/proxima-nova.ttf') format('opentype');
  font-weight: normal;
  font-style: normal;
}
</style>