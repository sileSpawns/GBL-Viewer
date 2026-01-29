import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer — Multiple 3D Models")

# List of preview models from modelviewer.dev
models = [
    {"name": "Astronaut", "url": "https://modelviewer.dev/shared-assets/models/Astronaut.glb"},
    {"name": "Candle", "url": "https://modelviewer.dev/shared-assets/models/candle.glb"},
    {"name": "Drone", "url": "https://modelviewer.dev/shared-assets/models/Drone.glb"},
    {"name": "Helmet", "url": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb"},
    {"name": "Flight Helmet", "url": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/FlightHelmet/glTF-Binary/FlightHelmet.glb"},
    {"name": "Avocado", "url": "https://modelviewer.dev/shared-assets/models/Avocado.glb"},
]

# Create layout: 3 rows, 2 columns
for i in range(0, len(models), 2):
    col1, col2 = st.columns(2)
    
    # First model in row
    with col1:
        st.subheader(models[i]["name"])
        viewer_html_1 = f"""
        <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@1.16.0/dist/model-viewer.min.js"></script>
        <style>
          model-viewer {{
            width: 100%;
            height: 400px;
            background: #222;
            border-radius: 8px;
            display: block;
          }}
        </style>
        <model-viewer
          src="{models[i]['url']}"
          alt="{models[i]['name']}"
          shadow-intensity="1"
          camera-controls
          auto-rotate
          ar>
        </model-viewer>
        """
        html(viewer_html_1, height=450)
    
    # Second model in row (if it exists)
    if i + 1 < len(models):
        with col2:
            st.subheader(models[i+1]["name"])
            viewer_html_2 = f"""
            <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@1.16.0/dist/model-viewer.min.js"></script>
            <style>
              model-viewer {{
                width: 100%;
                height: 400px;
                background: #222;
                border-radius: 8px;
                display: block;
              }}
            </style>
            <model-viewer
              src="{models[i+1]['url']}"
              alt="{models[i+1]['name']}"
              shadow-intensity="1"
              camera-controls
              auto-rotate
              ar>
            </model-viewer>
            """
            html(viewer_html_2, height=450)

st.markdown("---")
st.markdown("**Repo:** https://github.com/sileSpawns/GBL-Viewer | **Deploy:** https://share.streamlit.io/sileSpawns/GBL-Viewer/main/streamlit_app.py")
