import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer (model-viewer)")

st.markdown("Replace the `src` in the embedded viewer with your own GLB URL (or ask me to add `test.glb`).")

component_html = '''
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@1.16.0/dist/model-viewer.min.js"></script>
  <style>body{margin:0;background:#111;color:#fff}model-viewer{width:100%;height:70vh}</style>
</head>
<body>
  <model-viewer src="test.glb"
    alt="A 3D model"
    ar ar-modes="webxr scene-viewer quick-look"
    camera-controls
    poster="poster.png"
    shadow-intensity="1">
  </model-viewer>
</body>
</html>
'''

html(component_html, height=700)

st.markdown("**Repo file:** https://github.com/sileSpawns/GBL-Viewer/blob/main/streamlit_app.py")
st.markdown("**Deploy URL (Streamlit Share):** https://share.streamlit.io/sileSpawns/GBL-Viewer/main/streamlit_app.py")
