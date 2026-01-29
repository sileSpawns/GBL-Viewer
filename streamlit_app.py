import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for better styling
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 100%); }
    [data-testid="stHeader"] { background: rgba(0,0,0,0.3); }
    .stTitle { color: #00d4ff !important; font-size: 2.5rem !important; font-weight: 700 !important; }
    .stMarkdown { color: #e0e0e0 !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("# 🎨 3D Model Viewer")
st.markdown("**Explore, rotate, and preview stunning 3D models in your browser**", unsafe_allow_html=True)
st.markdown("---")

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
      html, body { margin: 0; padding: 0; }
      body { background: #0f0f1e; padding: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; overflow-y: auto; }
      body.modal-open { overflow: hidden; }
      .container { max-width: 1400px; margin: 0 auto; }
      .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
        gap: 24px;
        padding: 20px 0;
      }
      .card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #00d4ff44;
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
      }
      .card:hover {
        transform: translateY(-8px);
        border-color: #00d4ff88;
        box-shadow: 0 12px 48px rgba(0, 212, 255, 0.2);
      }
      .card-header {
        padding: 16px;
        background: linear-gradient(135deg, #00d4ff22 0%, #0099ff22 100%);
        border-bottom: 1px solid #00d4ff44;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .card-title {
        font-size: 20px;
        font-weight: 700;
        color: #00d4ff;
        margin: 0 0 8px 0;
      }
      .card-emoji {
        font-size: 28px;
        margin-right: 8px;
      }
      .card-description {
        font-size: 13px;
        color: #b0b0b0;
        margin: 0;
      }
      .fullscreen-btn {
        background: #00d4ff;
        color: #0f0f1e;
        border: none;
        padding: 8px 12px;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 600;
        font-size: 12px;
        transition: all 0.2s ease;
        flex-shrink: 0;
      }
      .fullscreen-btn:hover {
        background: #00ffff;
        transform: scale(1.05);
      }
      model-viewer {
        width: 100%;
        height: 340px;
        background: linear-gradient(135deg, #0a0a15 0%, #1a1a2e 100%);
        display: block;
      }
      .controls {
        padding: 12px 16px;
        background: rgba(0, 0, 0, 0.3);
        border-top: 1px solid #00d4ff44;
        font-size: 12px;
        color: #80ff00;
      }
      
      /* Modal Styles */
      .modal {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.95);
        z-index: 9999;
        margin: 0;
        padding: 0;
        overflow: hidden;
      }
      .modal.active {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }
      .modal-header {
        position: absolute;
        top: 15px;
        left: 20px;
        right: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #00d4ff;
        z-index: 10001;
      }
      .modal-title {
        font-size: 22px;
        font-weight: 700;
        margin: 0;
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
      .modal-content {
        width: calc(100vw - 40px);
        height: calc(100vh - 70px);
        max-width: 1880px;
        max-height: 1010px;
      }
    </style>
</head>
<body>
  <div class="container">
    <div class="grid">
"""

for model in models:
    grid_html += f"""
      <div class="card">
        <div class="card-header">
          <div>
            <div class="card-title"><span class="card-emoji">{model["emoji"]}</span>{model["name"]}</div>
            <p class="card-description">{model["description"]}</p>
          </div>
          <button class="fullscreen-btn" onclick="openFullscreen('{model["url"]}', '{model["name"]}')">⛶ Fullscreen</button>
        </div>
        <model-viewer
          src="{model["url"]}"
          alt="{model["name"]}"
          shadow-intensity="1"
          camera-controls
          auto-rotate
          ar
          style="background: linear-gradient(135deg, #0a0a15 0%, #1a1a2e 100%);"></model-viewer>
        <div class="controls">💡 Drag to rotate • Scroll to zoom • Click Fullscreen for expanded view</div>
      </div>
"""

grid_html += """
    </div>
  </div>

  <!-- Fullscreen Modal -->
  <div id="fullscreenModal" class="modal">
    <div class="modal-header">
      <h2 class="modal-title" id="modalTitle">3D Model</h2>
      <button class="close-btn" onclick="closeFullscreen()">✕ Close</button>
    </div>
    <div id="modalContent" class="modal-content">
      <model-viewer
        id="fullscreenViewer"
        alt="3D Model"
        shadow-intensity="1"
        camera-controls
        auto-rotate
        ar
        camera-orbit="0deg 75deg 2.5m"
        min-camera-orbit="auto auto auto"
        max-camera-orbit="auto auto auto"
        style="width: 100%; height: 100%; border-radius: 8px;">
      </model-viewer>
    </div>
  </div>

  <script>
    function openFullscreen(modelUrl, modelName) {
      const modal = document.getElementById('fullscreenModal');
      const viewer = document.getElementById('fullscreenViewer');
      const title = document.getElementById('modalTitle');
      
      viewer.src = modelUrl;
      title.textContent = modelName;
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

    // Close modal when clicking outside
    document.getElementById('fullscreenModal').addEventListener('click', (e) => {
      if (e.target.id === 'fullscreenModal') {
        closeFullscreen();
      }
    });
  </script>
</body>
</html>
"""

html(grid_html, height=2400)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #80ff00; padding: 20px;">
  <p><b>✨ Tips:</b> Drag models to rotate • Scroll to zoom • Use AR for real-world placement</p>
  <p><small>🔗 <a href="https://github.com/sileSpawns/GBL-Viewer" target="_blank" style="color: #00d4ff;">GitHub Repo</a> | 
  <a href="https://modelviewer.dev/" target="_blank" style="color: #00d4ff;">Model Viewer Docs</a></small></p>
</div>
""", unsafe_allow_html=True)
