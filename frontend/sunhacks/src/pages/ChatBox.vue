<template>
  <NavBar/>
  <div class="chat-container">
    <div class="chat-box">
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
        />
        <button class="send-button" @click="sendMessage">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
            <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z" />
          </svg>
        </button>
      </div>
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
      newMessage: ''
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
.chat-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
}

.chat-box {
  width: 90%;
  max-width: 800px;
  height: 80vh;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.chat-messages {
  flex-grow: 1;
  overflow-y: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.message {
  max-width: 70%;
  padding: 10px 15px;
  border-radius: 20px;
  margin-bottom: 10px;
  animation: fadeIn 0.3s ease-out;
}

.sent {
  align-self: flex-end;
  background-color: #0a2540;
  color: white;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.chat-input {
  display: flex;
  padding: 10px;
  border-top: 1px solid #e0e0e0;
}

input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 20px;
  margin-right: 10px;
  transition: all 0.3s ease;

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

.send-button {
  background-color: #0a2540;
  color: white;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.send-button:hover {
  background-color: #635bff;
  transform: translateY(-1px) scale(1.04);
  box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
}

.send-button svg {
  width: 20px;
  height: 20px;
}
</style>