import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide", initial_sidebar_state="collapsed")

# Hide all Streamlit UI elements
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { padding: 0 !important; background: #0f0f1e !important; }
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
        background: #0f0f1e;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
        color: #00d4ff;
        margin-bottom: 30px;
        text-align: center;
        letter-spacing: 2px;
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
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #00d4ff44;
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
        display: flex;
        flex-direction: column;
        height: 100%;
      }
      
      .card:hover {
        transform: translateY(-8px);
        border-color: #00d4ff88;
        box-shadow: 0 12px 48px rgba(0, 212, 255, 0.2);
      }
      
      .card-header {
        padding: 12px;
        background: linear-gradient(135deg, #00d4ff22 0%, #0099ff22 100%);
        border-bottom: 1px solid #00d4ff44;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-shrink: 0;
      }
      
      .card-title {
        font-size: 16px;
        font-weight: 700;
        color: #00d4ff;
        margin: 0;
      }
      
      .card-emoji {
        font-size: 20px;
        margin-right: 8px;
      }
      
      .fullscreen-btn {
        background: #00d4ff;
        color: #0f0f1e;
        border: none;
        padding: 6px 10px;
        border-radius: 4px;
        cursor: pointer;
        font-weight: 600;
        font-size: 11px;
        transition: all 0.2s ease;
        flex-shrink: 0;
      }
      
      .fullscreen-btn:hover {
        background: #00ffff;
        transform: scale(1.05);
      }
      
      model-viewer {
        width: 100%;
        flex: 1;
        min-height: 200px;
        background: linear-gradient(135deg, #0a0a15 0%, #1a1a2e 100%);
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
        background: #ff3333;
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s ease;
      }
      
      .close-btn:hover {
        background: #ff5555;
        transform: scale(1.05);
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
    <div class="page-title">Bosch AR/VR</div>
    <div class="grid-wrapper">
      <div class="grid">
"""

for model in models:
    grid_html += f"""
      <div class="card">
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
          style="background: linear-gradient(135deg, #0a0a15 0%, #1a1a2e 100%);"></model-viewer>
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
        camera-orbit="0deg 75deg 2.5m"
        min-camera-orbit="auto auto auto"
        max-camera-orbit="auto auto auto">
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
  </script>
</body>
</html>
"""

html(grid_html, height=1200)
