
<template>
  <div>
    <section class="navbar">
      <div class="logo">LOGO</div>
    </section>
    <section class="dynamic-text">
      <p>FIND</p>
      <div ref="typedElement">ANYTHING</div>
    </section>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  mounted() {
    new Typed(this.$refs.typedElement, {
      strings: ['BOOKS', 'SKIS', 'PHONES'],
      typeSpeed: 50,
      backSpeed: 50,
      loop: true
    })
  }
}
</script>

<style scoped>
.navbar {
  position: relative;
}
.logo {
  position: absolute;
  top: 10px;
  left: 10px;
}
.dynamic-text {
  text-align: center;
  padding: 20px;
}

@font-face {
  font-family: 'Proxima Nova';
  src: url('components/ui/font/proxima-nova.ttf') format('opentype');
  font-weight: normal;
  font-style: normal;
}
#app {
  font-family: 'Proxima Nova', sans-serif;
}
</style>
