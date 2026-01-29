import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer — 3D Model Viewer")

st.markdown("### Upload a GLB file or use the demo model below")

# File uploader for custom GLB
uploaded_file = st.file_uploader("Upload your GLB file", type="glb")

if uploaded_file:
    import base64
    glb_bytes = uploaded_file.read()
    glb_url = f"data:model/gltf-binary;base64,{base64.b64encode(glb_bytes).decode()}"
    st.success(f"✅ Loaded: {uploaded_file.name}")
else:
    glb_url = "https://modelviewer.dev/shared-assets/models/Astronaut.glb"
    st.info("📦 Using default demo model (Astronaut)")

poster_url = "https://modelviewer.dev/shared-assets/press-poster.png"

# Embed model-viewer
viewer_html = f"""
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@1.16.0/dist/model-viewer.min.js"></script>
<style>
  body, html {{ margin: 0; padding: 0; overflow: hidden; }}
  model-viewer {{
    width: 100%;
    height: 80vh;
    background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
  }}
</style>
<model-viewer
  src="{glb_url}"
  alt="3D Model"
  poster="{poster_url}"
  shadow-intensity="1"
  camera-controls
  auto-rotate
  ar
  ar-modes="webxr scene-viewer quick-look"
  exposure="1"
  tone-mapping="neutral">
</model-viewer>
"""

html(viewer_html, height=850)

st.markdown("---")
st.markdown("**GitHub:** https://github.com/sileSpawns/GBL-Viewer | **Deploy:** https://share.streamlit.io/sileSpawns/GBL-Viewer/main/streamlit_app.py")
