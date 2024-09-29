<template>
  <NavBar/>
  <div class="chat-container">
    <div class="chat-box">
      <div class="chat-messages" ref="chatMessages">
        <div v-for="(message, index) in messages" :key="index" class="message" :class="message.type">
          {{ message.text }}
        </div>
        <div v-if="isLoading" class="message ai loading">
          <div class="loading-dots">
          <span class="dot"></span>
          <span class="dot"></span>
          <span class="dot"></span>
            </div>
        </div>
      </div>
      <div class="chat-input">
        <input
          type="text"
          v-model="newMessage"
          @keyup.enter="sendMessage"
          placeholder="Send message..."
          :disabled="isLoading"
        />
        <button class="send-button" @click="sendMessage" :disabled="isLoading">
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
      newMessage: '',
      isLoading: false
    }
  },
  methods: {
    async sendMessage() {
    if (this.newMessage.trim()) {
        this.messages.push({ text: this.newMessage, type: 'sent' });
        this.newMessage = '';
        this.$nextTick(() => {
            this.scrollToBottom();
        });

        // Get AI response
        this.isLoading = true;
        await this.getAIResponse(this.newMessage);
        this.isLoading = false;
    }
},
    scrollToBottom() {
      const chatMessages = this.$refs.chatMessages;
      chatMessages.scrollTop = chatMessages.scrollHeight;
    },

    async getAIResponse() {
    try {
        const response = await fetch('http://localhost:8000/api/v1/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: this.newMessage })
        });
        const data = await response.json();

        // Add AI response to messages
        this.messages.push({ text: data.response, type: 'ai' });
        this.$nextTick(() => {
            this.scrollToBottom();
        });
    } catch (error) {
        console.error('Error getting AI response:', error);
      }
    }
  }
}
</script>

<style scoped>
.message.ai {
  align-self: flex-start;
  background-color: #f0f0f0;
  color: #333;
}
* {
  font-family: "Proxima Nova", serif;
}
.chat-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
  z-index: 0;
}
.message.ai.loading {
  background-color: transparent;
  box-shadow: none;
}

.loading-dots {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 40px;
  padding: 10px 15px;
}

.dot {
  width: 8px;
  height: 8px;
  background-color: #0a2540;
  border-radius: 50%;
  margin: 0 4px;
  opacity: 0.6;
  animation: bounce 1.4s infinite ease-in-out both;
}

.dot:nth-child(1) { animation-delay: -0.32s; }
.dot:nth-child(2) { animation-delay: -0.16s; }

@keyframes bounce {
  0%, 80%, 100% {
    transform: scale(0);
  }
  40% {
    transform: scale(1);
  }
}

input:disabled, .send-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
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