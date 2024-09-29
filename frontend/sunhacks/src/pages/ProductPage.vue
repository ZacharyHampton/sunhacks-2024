<template>
  <NavBar />
  <div class="gradient-corner"></div>
  <div class="bg"></div>
  <div class="center-box">
    <div class="inner-div chat">
      <div class="chat-title">findit.</div>
      <div class="chat-container">
        <div class="chat-messages" ref="chatMessages">
          <div v-for="(message, index) in messages" :key="index" class="message" :class="message.type">
            {{ message.text }}
          </div>
        </div>
        <div class="chat-input">
          <input
            type="text"
            v-model="newMessage"
            @keyup.enter="sendMessage"
            placeholder="Send message..."
            width = 80%;
          />
          <button class="send-button" @click="sendMessage">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
              <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z" />
            </svg>
          </button>
        </div>
      </div>
    </div>
    <div class="inner-div prod">
      <div class="prod-title">Top Results</div>
      <div class="prod-container">
        <div v-for="(card, index) in cards" :key="index" class="item">
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
import NavBar from '@/pages/components/NavBar.vue'


export default {
  name: 'ChatBox',
  components: {
    NavBar,

  },
  data() {
    return {
      cards: [
        {
          avatarUrl: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-fe-r1.jpg',
          title: 'Samsung Galaxy S24',
          subtext: 'Relevancy: 90%'
        },
        {
          avatarUrl: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-14-pro-plus-5g.jpg',
          title: 'Xiaomi Redmi Note 14 Pro+',
          subtext: 'Relevancy: 87%'
        },
        {
          avatarUrl: 'https://fdn2.gsmarena.com/vv/bigpic/microsoft-surface-duo.jpg',
          title: 'Microsoft Surface Pro',
          subtext: 'Relevancy: 84%'
        },
        {
          avatarUrl: 'https://fdn2.gsmarena.com/vv/bigpic/asus-zenfone-11-ultra.jpg',
          title: 'Zenfone 11 Ultra',
          subtext: 'Relevancy: 83%'
        },
        {
          avatarUrl: 'https://fdn2.gsmarena.com/vv/bigpic/zte-nubia-red-magic-nova.jpg',
          title: 'ZTE nubia Red Magic Nova',
          subtext: 'Relevancy: 79%'
        }

      ]
    }
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim()) {
        this.messages.push({ text: this.newMessage, type: 'sent' });
        this.newMessage = '';
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      }
    },
    scrollToBottom() {
      const chatMessages = this.$refs.chatMessages;
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }
  }
}
</script>

<style scoped>
* {
  font-family: "Proxima Nova", serif;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
input:hover {
  border: 1px solid #c9c9c9;
  transform: scale(1.009);
  transition: all ease 0.3s
}
input:focus {
  outline: none;
  border: 1px solid #635bff;

}
.message {
  max-width: 70%;
  padding: 10px 15px;
  border-radius: 20px;
  margin-bottom: 10px;
  animation: fadeIn 0.3s ease-out;
}
.diagonal-line {
  position: absolute;
  right: 0.1%;
  top: 100%;
  width: 300%;
  height: 100%;
  border-left: 2px solid rgba(255, 255, 255, 0.5);
  transform: rotate(10deg) translateY(-50%);
  z-index: 1;
}
.gradient-corner {
  position: absolute;
  top: 70%;
  left: -50%;
  right: -75%;
  height: 80%;
  width: 170%;
  transform-origin: top right;
  background: linear-gradient(124deg, #ff80b5 0%, #9089fc 50%, #80e9ff 100%);
  background-size: 400% 400%;
  animation: gradientAnimation 8s ease infinite;
  transform: rotate(7deg);
  z-index: 0;
}
.bg {
  position: relative;
  background-image: radial-gradient(rgba(0, 0, 0, 0) 1.8px, #fff 0.4px);
  background-size: 16px 16px;
  width: 100%;
  height: 100vh;
  top: 0;
  left: 0;
}

.center-box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80vw;
  height: 65vh;
  background-color: rgba(255,255,255,1);
  border-radius: 50px;
  box-shadow:
      0 0 30px rgba(0,0,0,0.2),
      0 100px 1000px rgba(245, 245, 245, 0.8),
      150px 0px 1000px rgba(245, 245, 245, 0.8),
      -100px 0 1000px rgba(245, 245, 245, 0.8);
  z-index: 2;
  display: flex;
  justify-content: space-between;
  padding: 20px;
}
.inner-div {
  height: 100%;
  border-radius: 50px;
}

.prod {
  width: 70%;
  background-color: white;
  position:relative;
  overflow: auto;
}
.prod-title {
  font-size: 30px;
  text-align: center;
  padding: 15px;
  border-bottom: 1.5px dashed gray;
}

.chat {
  width: 28%;
  box-shadow: 0 0 15px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.center-box::after {
  content: "";
  position: absolute;
  top: 10px;
  left: calc(28% + 16px);
  border-left: 1.5px dashed gray;
  height: calc(96%);
  z-index: 3;
}
.chat-title {
   background-color:#0a2540;
   color:white;
   padding:20px;
   border-top-left-radius:50px;
   border-top-right-radius:50px;
   text-align:center;
}
.chat-container {
   flex-grow:1;
   display:flex;
   flex-direction:column;
   overflow:hidden;
}

.chat-messages {
   flex-grow:1;
  background-color:white;
   overflow-y:auto;
   padding:20px;
   display:flex;
   flex-direction:column;
}

.message {
   max-width:70%;
   padding:10px	15px;
   border-radius:20px;
   margin-bottom:10px;
   animation:fadIn	0.3s	ease-out;
}

.sent {
   align-self:flex-end;
   background-color:#0a2540;
   color:white;
}

@keyframes fadeIn {
	from { opacity :0 ; transform :translateY(20px); }
	to { opacity :1 ; transform :translateY(0); }
}

.chat-input {
	display:flex;
	padding :20px ;
	border-top :1px solid #e0e0e0 ;
	background-color:white ;
}

input {
  min-width: 0;
	flex: 1;
	padding :10px ;
	border :1px solid #e0e0e0 ;
	border-radius :20px ;
	margin-right :10px ;
}

input :focus {
	outline:none ;
	border :1px solid #c9c9c9 ;
}

.send-button {
	background-color:#0a2540 ;
	color:white ;
	border:none ;
	border-radius :50% ;
	width :40px ;
	height :40px ;
	display:flex ;
	justify-content:center ;
	align-items:center ;
	cursor:pointer ;
	transition :all	0.3s	ease ;
}

.send-button:hover {
	background-color:#635bff ;
	transform :translateY(-1px) scale(1.04) ;
	box-shadow :0	7px	14px rgba(50,50,93 ,0.1),	0	3px	6px rgba(0 ,0 ,0 ,0.08) ;
}

.send-button svg {
	width :20px ;
	height :20px ;
}
.item-container {
  background-color: white;
  height : 121px;
  border-bottom: 1.5px dashed gray;
}
body {
  background-color: rgb(234, 234, 234)
}
.prod-container {
  border-radius: 10px;
  padding: 10px;
  background-color: rgb(240, 240, 240);
  margin: 10px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.item {
  background-color: white;
  padding-left: 25px;
  box-shadow: 0 0 8px rgba(0,0,0,0.2);
  border-radius: 10px;
  display: flex;
  height: 120px;
  align-items: center;
}
.item:hover {
  transform: scale(1.01);
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
  font-weight: 500;
  font-size: 1rem;
}

.card-subtext {
  margin: 0;
  font-size: 0.8rem;
  color: #666;
}
</style>

