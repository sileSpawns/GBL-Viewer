import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer — Multiple 3D Models")

# Use the same Astronaut GLB for all viewers (test)
test_url = "https://modelviewer.dev/shared-assets/models/Astronaut.glb"

# Model names
names = ["Astronaut 1", "Astronaut 2", "Astronaut 3", "Astronaut 4", "Astronaut 5", "Astronaut 6"]

# Load model-viewer script globally once
global_script = """
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@1.16.0/dist/model-viewer.min.js"></script>
"""
html(global_script, height=10)

# Create layout: 3 rows, 2 columns
for i in range(0, len(names), 2):
    col1, col2 = st.columns(2)
    
    # First viewer
    with col1:
        st.subheader(names[i])
        viewer_1 = f"""
        <style>
          model-viewer {{
            width: 100%;
            height: 400px;
            background: #1a1a1a;
            border-radius: 8px;
          }}
        </style>
        <model-viewer
          src="{test_url}"
          alt="3D Model"
          shadow-intensity="1"
          camera-controls
          auto-rotate
          ar>
        </model-viewer>
        """
        html(viewer_1, height=450)
    
    # Second viewer
    if i + 1 < len(names):
        with col2:
            st.subheader(names[i+1])
            viewer_2 = f"""
            <style>
              model-viewer {{
                width: 100%;
                height: 400px;
                background: #1a1a1a;
                border-radius: 8px;
              }}
            </style>
            <model-viewer
              src="{test_url}"
              alt="3D Model"
              shadow-intensity="1"
              camera-controls
              auto-rotate
              ar>
            </model-viewer>
            """
            html(viewer_2, height=450)

st.markdown("---")
st.markdown("**Repo:** https://github.com/sileSpawns/GBL-Viewer")
