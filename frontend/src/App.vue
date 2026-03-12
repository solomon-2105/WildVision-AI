<template>
  <div class="app">

    <transition name="fade" mode="out-in">

      <div v-if="!hasEntered" class="landing-page" key="landing">
        <div class="landing-content">
          
          <img src="./assets/tiger.jpg" class="animal-img left-animal" alt="Night Vision tiger" />
          <img src="./assets/deer.jpg" class="animal-img right-animal" alt="Night Vision deer" />

          <h1 class="main-title">WildVision AI</h1>
          <p class="sub-title">Advanced Wildlife Detection System</p>
          
          <button class="enter-button" @click="enterApp">
            ENTER SYSTEM
          </button>
        </div>
      </div>

      <div v-else class="main-layout" key="main">
        <header class="navbar">
          <h1>WildVision AI</h1>
          <p>Wildlife Detection System</p>
        </header>

        <div class="container">
          <Upload @updateHistory="setHistory"/>
          <History :history="history"/>
        </div>

        <footer class="footer">
          <p>YOLOv8 Wildlife Detection</p>
        </footer>
      </div>

    </transition>

  </div>
</template>

<script>
import Upload from "./components/Upload.vue"
import History from "./components/History.vue"
import axios from "axios"

export default {
  components: { Upload, History },

  data() {
    return {
      history: [],
      hasEntered: false // <-- NEW: Controls which screen is shown
    }
  },

  methods: {
    setHistory(data) {
      this.history = data
    },
    // <-- NEW: Triggers the transition to the main app
    enterApp() {
      this.hasEntered = true;
    }
  },

  async mounted() {
    try {
      const res = await axios.get("http://localhost:8000/history")
      this.history = res.data
    } catch (error) {
      console.error("Could not fetch history. Is backend running?", error)
    }
  }
}
</script>

<style>
/* ---- YOUR EXISTING STYLES ---- */
body {
  margin: 0;
  font-family: Segoe UI, Arial;
  background: #0f172a;
  color: white;
}

.navbar {
  background: #1e293b;
  padding: 20px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.4);
}

.navbar h1 {
  margin: 0;
  font-size: 32px;
  color: #38bdf8;
}

.navbar p {
  margin-top: 5px;
  color: #94a3b8;
}

.container {
  width: 1100px;
  margin: auto;
  padding: 40px 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  position: relative;
  z-index: 10;
}

.footer {
  text-align: center;
  padding: 20px;
  background: #1e293b;
  margin-top: 40px;
  color: #64748b;
}

/* ==========================================
   NEW: LANDING PAGE STYLES 
   ========================================== */

.landing-page {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.landing-content {
  position: relative;
  z-index: 20;
}

.main-title {
  font-size: 80px;
  color: #39ff14; /* Using your nightvision green */
  margin: 0;
  text-shadow: 0 0 20px rgba(57, 255, 20, 0.5);
  letter-spacing: 4px;
}

.sub-title {
  font-size: 24px;
  color: #94a3b8;
  margin-bottom: 50px;
  letter-spacing: 2px;
}

/* The Glowing Enter Button */
.enter-button {
  background: transparent;
  color: #39ff14;
  border: 2px solid #39ff14;
  padding: 15px 50px;
  font-size: 20px;
  font-weight: bold;
  letter-spacing: 3px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 0 15px rgba(57, 255, 20, 0.2), inset 0 0 15px rgba(57, 255, 20, 0.1);
}

.enter-button:hover {
  background: rgba(57, 255, 20, 0.15);
  box-shadow: 0 0 30px rgba(57, 255, 20, 0.6), inset 0 0 20px rgba(57, 255, 20, 0.4);
  transform: scale(1.05);
}

/* Animal Image Positioning */
.animal-img {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 250px; /* Adjust based on your actual images */
  opacity: 0.6;
  transition: 0.5s ease;
  filter: drop-shadow(0 0 10px #39ff14);
}

.animal-img:hover {
  opacity: 1;
  filter: drop-shadow(0 0 20px #39ff14);
}

.left-animal {
  left: -300px;
}

.right-animal {
  right: -300px;
}

/* Smooth Fade Transition between screens */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.8s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>