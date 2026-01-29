import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer — Multiple 3D Models")

# List of preview models from modelviewer.dev
models = [
    {"name": "Astronaut", "url": "https://modelviewer.dev/shared-assets/models/Astronaut.glb", "poster": "https://modelviewer.dev/shared-assets/press-poster.png"},
    {"name": "Candle", "url": "https://modelviewer.dev/shared-assets/models/candle.glb", "poster": "https://modelviewer.dev/shared-assets/press-poster.png"},
    {"name": "Drone", "url": "https://modelviewer.dev/shared-assets/models/Drone.glb", "poster": "https://modelviewer.dev/shared-assets/press-poster.png"},
    {"name": "Helmet", "url": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb", "poster": "https://modelviewer.dev/shared-assets/press-poster.png"},
    {"name": "Flight Helmet", "url": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/FlightHelmet/glTF-Binary/FlightHelmet.glb", "poster": "https://modelviewer.dev/shared-assets/press-poster.png"},
    {"name": "Avocado", "url": "https://modelviewer.dev/shared-assets/models/Avocado.glb", "poster": "https://modelviewer.dev/shared-assets/press-poster.png"},
]

# Create a 3x2 grid
cols = st.columns(2)

for idx, model in enumerate(models):
    col = cols[idx % 2]
    
    with col:
        st.subheader(model["name"])
        
        viewer_html = f"""
        <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@1.16.0/dist/model-viewer.min.js"></script>
        <style>
          body, html {{ margin: 0; padding: 0; }}
          model-viewer {{
            width: 100%;
            height: 400px;
            background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
            border-radius: 8px;
          }}
        </style>
        <model-viewer
          src="{model['url']}"
          alt="{model['name']}"
          poster="{model['poster']}"
          shadow-intensity="1"
          camera-controls
          auto-rotate
          ar
          ar-modes="webxr scene-viewer quick-look">
        </model-viewer>
        """
        
        html(viewer_html, height=450)

st.markdown("---")
st.markdown("**Repo:** https://github.com/sileSpawns/GBL-Viewer | **Deploy:** https://share.streamlit.io/sileSpawns/GBL-Viewer/main/streamlit_app.py")
