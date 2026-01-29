import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Bosch AR/VR Viewer", layout="wide", initial_sidebar_state="collapsed")

# Hide all Streamlit UI elements
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { padding: 0 !important; background: linear-gradient(135deg, #0f1e3a 0%, #1a2f52 100%) !important; }
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stToolbar"] { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; }
    .stPage { width: 100vw; margin: 0; padding: 0; }
    html, body { width: 100vw; height: 100vh; overflow: hidden !important; margin: 0; padding: 0; }
</style>
""", unsafe_allow_html=True)

# Sample models array
models = [
    {
        "name": "Astronaut",
        "description": "A detailed 3D astronaut with spacesuit",
        "url": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
        "emoji": "👨‍🚀"
    },
    {
        "name": "Tower",
        "description": "3D tower model",
        "url": "https://raw.githubusercontent.com/sileSpawns/GBL-Viewer/main/models/tower.glb",
        "emoji": "🏗️"
    },
    {
        "name": "Drone",
        "description": "High-tech quadcopter drone model",
        "url": "https://modelviewer.dev/shared-assets/models/Drone.glb",
        "emoji": "🚁"
    },
    {
        "name": "Candle",
        "description": "Realistic 3D candle with lighting",
        "url": "https://modelviewer.dev/shared-assets/models/candle.glb",
        "emoji": "🕯️"
    },
    {
        "name": "Damaged Helmet",
        "description": "Weathered combat helmet with details",
        "url": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
        "emoji": "⚔️"
    },
    {
        "name": "Flight Helmet",
        "description": "Classic aviation flight helmet",
        "url": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/FlightHelmet/glTF-Binary/FlightHelmet.glb",
        "emoji": "🛩️"
    },
    {
        "name": "Avocado",
        "description": "Smooth 3D rendered avocado fruit",
        "url": "https://modelviewer.dev/shared-assets/models/Avocado.glb",
        "emoji": "🥑"
    }
]

# Build HTML grid with all models
grid_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.js"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { 
        margin: 0; 
        padding: 0; 
        width: 100vw; 
        height: 100vh; 
        overflow: hidden;
        background: linear-gradient(135deg, #0f1e3a 0%, #1a2f52 100%);
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
      }
      body.modal-open { overflow: hidden !important; }
      
      .container { 
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding: 20px;
        box-sizing: border-box;
        overflow: hidden;
      }
      
      .page-title {
        font-size: 48px;
        font-weight: 700;
        color: #fff;
        margin-bottom: 20px;
        text-align: center;
        letter-spacing: 3px;
      }
      
      .bosch-brand {
        color: #e6001b;
        font-weight: 900;
      }
      
      .import-section {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
        background: rgba(230, 0, 27, 0.05);
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #e6001b66;
        width: 100%;
        max-width: 1800px;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        backdrop-filter: blur(10px);
      }
      
      .import-input {
        background: rgba(26, 47, 82, 0.9);
        border: 1px solid #e6001b;
        color: #ffffff;
        padding: 10px 12px;
        border-radius: 4px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 12px;
        min-width: 250px;
        transition: all 0.3s ease;
      }
      
      .import-input::placeholder {
        color: #888888;
      }
      
      .import-input:focus {
        border-color: #e6001b;
        box-shadow: 0 0 15px rgba(230, 0, 27, 0.3);
        outline: none;
      }
      
      .import-select {
        background: rgba(26, 47, 82, 0.9);
        border: 1px solid #e6001b;
        color: #ffffff;
        padding: 10px 12px;
        border-radius: 4px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 12px;
        cursor: pointer;
        min-width: 150px;
        transition: all 0.3s ease;
      }
      
      .import-select option {
        background: #1a2f52;
        color: #ffffff;
      }
      
      .import-select:focus {
        border-color: #e6001b;
        box-shadow: 0 0 15px rgba(230, 0, 27, 0.3);
        outline: none;
      }
      
      .import-btn {
        background: linear-gradient(135deg, #e6001b 0%, #ff1a33 100%);
        color: #ffffff;
        border: none;
        padding: 10px 16px;
        border-radius: 4px;
        cursor: pointer;
        font-weight: 600;
        font-size: 12px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(230, 0, 27, 0.3);
      }
      
      .import-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(230, 0, 27, 0.5);
      }
      
      .import-btn:active {
        transform: scale(0.98);
      }
      
      .grid-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        flex: 1;
        width: 100%;
      }
      
      .grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        width: 100%;
        max-width: 1800px;
        height: auto;
        max-height: calc(100vh - 160px);
      }
      
      .card {
        background: linear-gradient(135deg, #1a2f52 0%, #0f1e3a 100%);
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #e6001b44;
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px rgba(230, 0, 27, 0.1);
        display: flex;
        flex-direction: column;
        height: 100%;
      }
      
      .card:hover {
        transform: translateY(-8px);
        border-color: #e6001b88;
        box-shadow: 0 12px 48px rgba(230, 0, 27, 0.2);
      }
      
      .card-header {
        padding: 12px;
        background: linear-gradient(135deg, #e6001b22 0%, #ff1a3322 100%);
        border-bottom: 1px solid #e6001b44;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-shrink: 0;
      }
      
      .card-title {
        font-size: 16px;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
      }
      
      .card-emoji {
        font-size: 20px;
        margin-right: 8px;
      }
      
      .fullscreen-btn {
        background: linear-gradient(135deg, #e6001b 0%, #ff1a33 100%);
        color: #ffffff;
        border: none;
        padding: 6px 10px;
        border-radius: 4px;
        cursor: pointer;
        font-weight: 600;
        font-size: 11px;
        transition: all 0.2s ease;
        flex-shrink: 0;
        box-shadow: 0 2px 8px rgba(230, 0, 27, 0.3);
      }
      
      .fullscreen-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(230, 0, 27, 0.5);
      }
      
      model-viewer {
        width: 100%;
        flex: 1;
        min-height: 200px;
        background: linear-gradient(135deg, #081529 0%, #0f1e3a 100%);
        display: block;
      }
      
      /* Modal Styles - Clean Fullscreen Viewer */
      .modal {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        width: 100vw;
        height: 100vh;
        background: #000;
        z-index: 9999;
        margin: 0;
        padding: 0;
        overflow: hidden;
        align-items: center;
        justify-content: center;
      }
      
      .modal.active {
        display: flex;
      }
      
      .modal-header {
        position: absolute;
        top: 20px;
        right: 20px;
        display: flex;
        z-index: 10001;
      }
      
      .close-btn {
        background: linear-gradient(135deg, #e6001b 0%, #ff1a33 100%);
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s ease;
        box-shadow: 0 4px 15px rgba(230, 0, 27, 0.3);
      }
      
      .close-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(230, 0, 27, 0.5);
      }
      
      .modal-viewer-container {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
        padding: 0;
        margin: 0;
        overflow: hidden;
      }
      
      #fullscreenViewer {
        width: 90%;
        height: 90%;
        max-width: 1920px;
        max-height: 1080px;
        border-radius: 8px;
      }
    </style>
</head>
<body>
  <div class="container">
    <div class="page-title"><span class="bosch-brand">BOSCH</span> AR/VR</div>
    
    <div class="import-section">
      <select class="import-select" id="viewerPosition">
        <option value="append">➕ Add to End</option>
        <option value="1">Position 1 (Astronaut)</option>
        <option value="2">Position 2 (Tower)</option>
        <option value="3">Position 3 (Drone)</option>
        <option value="4">Position 4 (Candle)</option>
        <option value="5">Position 5 (Helmet 1)</option>
        <option value="6">Position 6 (Helmet 2)</option>
      </select>
      <input type="text" class="import-input" id="modelUrl" placeholder="Paste GLB file URL here">
      <input type="text" class="import-input" id="modelName" placeholder="Model name (optional)" style="max-width: 150px;">
      <button class="import-btn" onclick="importModel()">+ Import Model</button>
    </div>
    
    <div class="grid-wrapper">
      <div class="grid" id="modelGrid">
"""

for model in models:
    grid_html += f"""
      <div class="card" data-model-id="default-{model["name"]}">
        <div class="card-header">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span class="card-emoji">{model["emoji"]}</span>
            <span class="card-title">{model["name"]}</span>
          </div>
          <button class="fullscreen-btn" onclick="openFullscreen('{model["url"]}', '{model["name"]}')">⛶</button>
        </div>
        <model-viewer
          src="{model["url"]}"
          alt="{model["name"]}"
          shadow-intensity="1"
          camera-controls
          auto-rotate
          ar
          style="background: linear-gradient(135deg, #081529 0%, #0f1e3a 100%);"></model-viewer>
      </div>
"""

grid_html += """
      </div>
    </div>
  </div>

  <!-- Fullscreen Modal -->
  <div id="fullscreenModal" class="modal">
    <div class="modal-header">
      <button class="close-btn" onclick="closeFullscreen()">✕ Close</button>
    </div>
    <div class="modal-viewer-container">
      <model-viewer
        id="fullscreenViewer"
        alt="3D Model"
        shadow-intensity="1"
        camera-controls
        auto-rotate
        ar
        camera-orbit="0deg 45deg auto">
      </model-viewer>
    </div>
  </div>

  <script>
    function openFullscreen(modelUrl, modelName) {
      const modal = document.getElementById('fullscreenModal');
      const viewer = document.getElementById('fullscreenViewer');
      
      viewer.src = modelUrl;
      modal.classList.add('active');
      document.body.classList.add('modal-open');
    }

    function closeFullscreen() {
      const modal = document.getElementById('fullscreenModal');
      modal.classList.remove('active');
      document.body.classList.remove('modal-open');
    }

    // Close modal on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeFullscreen();
      }
    });

    // Close modal when clicking outside the viewer
    document.getElementById('fullscreenModal').addEventListener('click', (e) => {
      if (e.target.id === 'fullscreenModal') {
        closeFullscreen();
      }
    });

    // Import model function
    function importModel() {
      const urlInput = document.getElementById('modelUrl');
      const nameInput = document.getElementById('modelName');
      const positionSelect = document.getElementById('viewerPosition');
      const modelUrl = urlInput.value.trim();
      const modelName = nameInput.value.trim() || 'Custom Model';
      const position = positionSelect.value;
      
      if (!modelUrl) {
        alert('Please enter a model URL');
        return;
      }
      
      if (!modelUrl.toLowerCase().endsWith('.glb') && !modelUrl.toLowerCase().includes('.glb?')) {
        alert('Please provide a valid GLB file URL');
        return;
      }
      
      // Create unique ID for this model
      const modelId = 'custom-' + Date.now();
      
      // Create card HTML
      const cardHTML = `
        <div class="card" data-model-id="${modelId}">
          <div class="card-header">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span class="card-emoji">📦</span>
              <span class="card-title">${modelName}</span>
            </div>
            <div style="display: flex; gap: 6px;">
              <button class="fullscreen-btn" onclick="openFullscreen('${modelUrl}', '${modelName}')">⛶</button>
              <button class="fullscreen-btn" style="background: #ff3333; padding: 4px 8px;" onclick="removeModel('${modelId}')">✕</button>
            </div>
          </div>
          <model-viewer
            src="${modelUrl}"
            alt="${modelName}"
            shadow-intensity="1"
            camera-controls
            auto-rotate
            ar
            style="background: linear-gradient(135deg, #081529 0%, #0f1e3a 100%);"></model-viewer>
        </div>
      `;
      
      const grid = document.getElementById('modelGrid');
      const newCardWrapper = document.createElement('div');
      newCardWrapper.innerHTML = cardHTML;
      const newCard = newCardWrapper.firstElementChild;
      
      // Add to grid at selected position
      if (position === 'append') {
        grid.appendChild(newCard);
      } else {
        const posIndex = parseInt(position) - 1;
        const cards = grid.querySelectorAll('.card');
        if (posIndex < cards.length) {
          cards[posIndex].replaceWith(newCard);
        } else {
          grid.appendChild(newCard);
        }
      }
      
      // Clear inputs and reset position
      urlInput.value = '';
      nameInput.value = '';
      positionSelect.value = 'append';
      urlInput.focus();
    }

    // Remove model function
    function removeModel(modelId) {
      const card = document.querySelector(`[data-model-id="${modelId}"]`);
      if (card) {
        card.remove();
      }
    }

    // Allow Enter key to import
    document.getElementById('modelUrl').addEventListener('keypress', (e) => {
      if (e.key === 'Enter') importModel();
    });
    
    document.getElementById('modelName').addEventListener('keypress', (e) => {
      if (e.key === 'Enter') importModel();
    });
  </script>
</body>
</html>
"""

html(grid_html, height=1200)
