import streamlit as st
from streamlit.components.v1 import html
from pathlib import Path
import base64

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer (model-viewer)")

# Load and encode local assets as data URIs for Streamlit's sandboxed iframe
base = Path(__file__).parent
glb_path = base / "test.glb"
poster_path = base / "poster.png"

def to_data_uri(path: Path, mime: str):
    """Convert file to base64 data URI."""
    if not path.exists():
        return None
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{b64}"

glb_uri = to_data_uri(glb_path, "model/gltf-binary")
poster_uri = to_data_uri(poster_path, "image/png")

if not glb_uri:
    st.error("❌ Local `test.glb` not found. Falling back to demo model.")
    glb_uri = "https://modelviewer.dev/shared-assets/models/Astronaut.glb"
else:
    st.success("✅ Loaded `test.glb` locally")

if not poster_uri:
    poster_uri = "https://modelviewer.dev/shared-assets/press-poster.png"

component_html = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@1.16.0/dist/model-viewer.min.js"></script>
  <style>
    * {{ margin: 0; padding: 0; }}
    body {{ background: #111; color: #fff; font-family: sans-serif; }}
    model-viewer {{
      width: 100%;
      height: 100vh;
      background: #222;
    }}
  </style>
</head>
<body>
  <model-viewer
    src="{glb_uri}"
    alt="3D Model"
    poster="{poster_uri}"
    shadow-intensity="1"
    camera-controls
    auto-rotate
    ar
    ar-modes="webxr scene-viewer quick-look">
  </model-viewer>
</body>
</html>'''

html(component_html, height=900)

st.markdown("---")
st.markdown("**Repo:** https://github.com/sileSpawns/GBL-Viewer")
st.markdown("**Deploy:** https://share.streamlit.io/sileSpawns/GBL-Viewer/main/streamlit_app.py")
