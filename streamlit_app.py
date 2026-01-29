import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer")

st.markdown("Single test viewer using model-viewer.dev CDN")

# Follow official model-viewer.dev example exactly
viewer_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Roboto+Mono">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>
<body>
    <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.js"></script>
    
    <style>
      body { margin: 0; background: #f0f0f0; }
      model-viewer {
        width: 100%;
        height: 100vh;
      }
    </style>

    <model-viewer 
      src="https://modelviewer.dev/shared-assets/models/Astronaut.glb"
      ios-src="https://modelviewer.dev/shared-assets/models/Astronaut.usdz"
      alt="A 3D model of an astronaut"
      shadow-intensity="1"
      camera-controls
      auto-rotate
      ar>
    </model-viewer>

</body>
</html>
"""

html(viewer_html, height=900)

st.markdown("---")
st.markdown("**Debug Info:** Using official model-viewer.dev example code")
