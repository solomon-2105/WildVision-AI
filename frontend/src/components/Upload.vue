<template>
  <div class="card">
    <h2>Upload Image</h2>

    <label 
      class="upload-box" 
      @dragover.prevent
      @drop.prevent="handleDrop"
      :class="{ 'is-loading': isLoading }"
    >
      <p v-if="isLoading">Processing image...</p>
      <p v-else>Drag or select an image</p>

      <input
        type="file"
        ref="fileInput"
        accept="image/*"
        @change="handleFileSelect"
        class="visually-hidden"
        :disabled="isLoading"
      />
    </label>

    <div v-if="errorMsg" class="error-badge">
      {{ errorMsg }}
    </div>

    <img v-if="preview" :src="preview" class="preview">

    <div v-if="result && !isLoading" class="result">
      <h3>Detection Result</h3>

      <div v-if="result.detections && result.detections.length === 0">
        <p>No objects detected.</p>
      </div>

      <div v-for="(d, index) in result.detections" :key="index" class="badge">
        {{ d.class }} | {{ d.confidence }}
      </div>

      <img
        v-if="result.image"
        :src="'http://localhost:8000' + result.image"
        class="result-img"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      preview: null,
      result: null,
      isLoading: false,
      errorMsg: null
    };
  },
  methods: {
    // Handle Drop from Drag-and-Drop
    handleDrop(event) {
      const file = event.dataTransfer.files[0];
      if (file && file.type.startsWith('image/')) {
        this.processFile(file);
      } else {
        this.errorMsg = "Please drop a valid image file.";
      }
    },

    // Handle standard file selection
    handleFileSelect(event) {
      const file = event.target.files[0];
      if (!file) return;
      this.processFile(file);
      
      // Reset input value so the exact same file can be uploaded again if needed
      event.target.value = ""; 
    },

    // Centralized upload logic
    async processFile(file) {
      this.errorMsg = null;
      this.result = null;
      this.isLoading = true;
      
      this.preview = URL.createObjectURL(file);

      const formData = new FormData();
      formData.append("file", file);

      try {
        const res = await axios.post(
          "http://localhost:8000/predict",
          formData,
          { headers: { "Content-Type": "multipart/form-data" } }
        );

        this.result = res.data;

        // Fetch history after successful prediction
        const history = await axios.get("http://localhost:8000/history");
        this.$emit("updateHistory", history.data);

      } catch (e) {
        console.error("Upload Error:", e);
        this.errorMsg = e.response?.data?.detail || "Error connecting to the server. Is localhost:8000 running?";
      } finally {
        this.isLoading = false;
        // The proper Vue way to reset the file input
        if (this.$refs.fileInput) {
          this.$refs.fileInput.value = ""; 
        }
      }
    }
  }
};
</script>

<style>
.card {
  background: #1e293b;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.4);
}

.card h2 {
  margin-top: 0;
  color: #39ff14;
}

.upload-box {
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px dashed #2b333a;
  border-radius: 10px;
  padding: 40px;
  margin-bottom: 20px;
  cursor: pointer;
  user-select: none;
  transition: .25s;
  width: 100%;
  box-sizing: border-box;
}

.upload-box:hover {
  border-color: #39ff14;
  background: rgba(57,255,20,0.05);
}

.upload-box.is-loading {
  cursor: not-allowed;
  opacity: 0.7;
  border-color: #888;
  animation: pulse 1.5s infinite;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.preview {
  width: 100%;
  margin-top: 15px;
  border-radius: 10px;
}

.result {
  margin-top: 20px;
}

.badge {
  display: inline-block;
  background: rgba(57,255,20,0.12);
  color: #39ff14;
  border: 1px solid #39ff14;
  padding: 8px 14px;
  border-radius: 20px;
  margin-right: 10px;
  margin-bottom: 10px;
  font-weight: 600;
}

.error-badge {
  background: rgba(255, 57, 57, 0.12);
  color: #ff3939;
  border: 1px solid #ff3939;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 15px;
  font-weight: 600;
  text-align: center;
}

.result-img {
  width: 100%;
  margin-top: 10px;
  border-radius: 10px;
  animation: fadeIn .6s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
  0% { background: rgba(255, 255, 255, 0); }
  50% { background: rgba(255, 255, 255, 0.05); }
  100% { background: rgba(255, 255, 255, 0); }
}
</style>