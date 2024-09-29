<template>
  <section class="gradient-section">
    <div class="gradient-corner"></div>
    <div class="diagonal-line"></div>
    <div class="content">
      <h1 class="main-text">Finding<br>your perfect<br><span id="typed-output"></span></h1>
    </div>
  </section>
</template>

<script>
import Typed from 'typed.js';

export default {
  name: 'GradientSection',
  mounted() {
    const options = {
      strings: ['phone', 'book', 'ski','anything...^3000'],
      typeSpeed: 50,
      backSpeed: 30,
      backDelay: 1000,
      loop: true,
    };
    new Typed('#typed-output', options);
  }
}
</script>

<style scoped>
.gradient-section {
  position: absolute;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  background-color: white;
}

.gradient-background {
  position: absolute;
  top: -50%;
  right: -50%;
  width: 200%;
  height: 200%;


  transform-origin: top right;
  z-index: 0;
}

.gradient-corner {
  position: absolute;
  top: -50%;
  left: -50%;
  right: -75%;
  height: 100%;
  width: 145%;
  transform-origin: top right;
  background: linear-gradient(135deg, #ff80b5 0%, #9089fc 50%, #80e9ff 100%);
  background-size: 400% 400%;
  animation: gradientAnimation 8s ease infinite;
  transform: rotate(-12deg);
  z-index: 0;
}

.diagonal-line {
  position: absolute;
  top: 0;
  left: 0;
  width: 200%;
  height: 200%;
  border-left: 2px solid rgba(255, 255, 255, 0.5);
  transform: rotate(45deg) translateY(-50%);
  z-index: 1;
}

.content {
  position: relative;
  z-index: 2;
  padding: 5% 10%;
  max-width: 60%;
}

.main-text {
  font-size: 7rem;
  font-weight: bold;
  color: #0a2540;
  line-height: 1.2;
  margin-bottom: 1rem;
}

.sub-text {
  font-size: 2rem;
  color: #425466;
  margin-bottom: 2rem;
}

.cta {
  display: flex;
  gap: 1rem;
}

.email-input {
  padding: 0.75rem 1rem;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  flex-grow: 1;
}

.start-button {
  padding: 0.75rem 1.5rem;
  background-color: #0a2540;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

@keyframes gradientAnimation {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>