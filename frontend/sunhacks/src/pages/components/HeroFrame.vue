<template>
  <div class="hero-frame">
    <div class="inner-frame">
      <div class="card-container">
        <div v-for="(card, index) in cards" :key="index" class="inner-card">
          <div class="avatar" :style="{ backgroundImage: `url(${card.avatarUrl})` }"></div>
          <div class="text-content">
            <p class="card-title">{{ card.title }}</p>
            <p class="card-subtext">{{ card.subtext }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeroFrame',
  data() {
    return {
      cards: [
        {
          avatarUrl: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-fe-r1.jpg',
          title: 'Samsung Galaxy S24',
          subtext: 'Subtext'
        },
        {
          avatarUrl: 'https://www.gutenberg.org/cache/epub/74490/pg74490.cover.medium.jpg',
          title: 'Gods of the Jungle',
          subtext: 'Subtext'
        },
        {
          avatarUrl: 'https://cdn11.bigcommerce.com/s-y84jjppazd/images/stencil/original/products/14271/46061/PNTL02071__22678.1723818623.jpg',
          title: 'Atomic Bent 100 Skis',
          subtext: 'Subtext'
        },
        {
          avatarUrl: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-watch-ultra.jpg',
          title: 'Samsung Galaxy Watch Ultra',
          subtext: 'Subtext'
        },
      ]
    }
  }
}
</script>

<style scoped>
* {
  font-family: "Proxima Nova", serif;
}

.hero-frame {
  position: absolute;
  top: 50%;
  right: 5%;
  transform: translateY(-50%);
  height: 70%;
  width: 28%;
  max-width: 400px;
  aspect-ratio: 16 / 9;
  background: radial-gradient(circle, rgba(235,235,235,1) 0%, rgba(232,232,232,1) 35%, rgba(219,219,219,1) 100%);
  border-radius: 12px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.inner-frame {
  width: calc(100% - 12px);
  height: calc(100% - 12px);
  border-radius: 8px;
  overflow: hidden;
  background-color: white;
}

.card-container {
  padding: 10px;
  border-radius: 8px;
  background-color: #ececec;
  width: calc(100% - 20px);
  margin: 10px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.inner-card {
  display: flex;
  align-items: center;
  padding: 25px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
}

.inner-card:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.avatar {
  background-color: #525252;
  background-size: cover;
  background-position: center;
  border-radius: 12px;
  height: 4rem;
  width: 4rem;
  flex-shrink: 0;
  margin: 2px 16px 2px 2px;
}

.text-content {
  display: flex;
  flex-direction: column;
}

.card-title {
  margin: 0;
  font-weight: bold;
  font-size: 1rem;
}

.card-subtext {
  margin: 0;
  font-size: 0.8rem;
  color: #666;
}
</style>