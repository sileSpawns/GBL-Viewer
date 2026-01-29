import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer — Multiple 3D Models")

test_url = "https://modelviewer.dev/shared-assets/models/Astronaut.glb"

# Single combined HTML block with script and all 6 viewers
combined_html = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@1.16.0/dist/model-viewer.min.js"></script>
</head>
<body style="margin: 0; padding: 20px; background: #111; font-family: sans-serif;">
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
    
    <div>
      <h3 style="color: #fff; text-align: center;">Astronaut 1</h3>
      <model-viewer
        src="{test_url}"
        alt="Astronaut"
        style="width: 100%; height: 400px; background: #222; border-radius: 8px;"
        shadow-intensity="1"
        camera-controls
        auto-rotate>
      </model-viewer>
    </div>
    
    <div>
      <h3 style="color: #fff; text-align: center;">Astronaut 2</h3>
      <model-viewer
        src="{test_url}"
        alt="Astronaut"
        style="width: 100%; height: 400px; background: #222; border-radius: 8px;"
        shadow-intensity="1"
        camera-controls
        auto-rotate>
      </model-viewer>
    </div>
    
    <div>
      <h3 style="color: #fff; text-align: center;">Astronaut 3</h3>
      <model-viewer
        src="{test_url}"
        alt="Astronaut"
        style="width: 100%; height: 400px; background: #222; border-radius: 8px;"
        shadow-intensity="1"
        camera-controls
        auto-rotate>
      </model-viewer>
    </div>
    
    <div>
      <h3 style="color: #fff; text-align: center;">Astronaut 4</h3>
      <model-viewer
        src="{test_url}"
        alt="Astronaut"
        style="width: 100%; height: 400px; background: #222; border-radius: 8px;"
        shadow-intensity="1"
        camera-controls
        auto-rotate>
      </model-viewer>
    </div>
    
    <div>
      <h3 style="color: #fff; text-align: center;">Astronaut 5</h3>
      <model-viewer
        src="{test_url}"
        alt="Astronaut"
        style="width: 100%; height: 400px; background: #222; border-radius: 8px;"
        shadow-intensity="1"
        camera-controls
        auto-rotate>
      </model-viewer>
    </div>
    
    <div>
      <h3 style="color: #fff; text-align: center;">Astronaut 6</h3>
      <model-viewer
        src="{test_url}"
        alt="Astronaut"
        style="width: 100%; height: 400px; background: #222; border-radius: 8px;"
        shadow-intensity="1"
        camera-controls
        auto-rotate>
      </model-viewer>
    </div>
    
  </div>
</body>
</html>
"""

html(combined_html, height=1400)

st.markdown("---")
st.markdown("**Repo:** https://github.com/sileSpawns/GBL-Viewer")
