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
      <div class="chat-title">Top Results</div>
      <div class="item-container">{{ product.title }}</div>
      <div class="item-container">aaadf</div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/pages/components/NavBar.vue'

export default {
  name: 'ChatBox',
  components: {
    NavBar
  },
  data() {
    return {
      messages: [],
      newMessage: '',
      product: {
        title: "abcd",
        image_url: "1234"
      }
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
  background-color: rgba(245,245,245,1);
  border-radius: 50px;
  box-shadow:
      0 100px 1000px rgba(245, 245, 245, 0.8),
      150px 0px 1000px rgba(245, 245, 245, 0.8),
      -100px 0 1000px rgba(245, 245, 245, 0.8);
  border: 1.3px dashed rgba(120, 120, 120, 1);
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
  border: 1.3px dashed rgba(120, 120, 120, 1);
  background-color: rgba(237,237,237,1);
}

.chat {
  width: 28%;
  box-shadow: 0 0 30px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
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
  height : 120px;
  border: 1px solid #0A2540;
}
</style>

