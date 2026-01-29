import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer — Test Single Model")

test_url = "https://modelviewer.dev/shared-assets/models/Astronaut.glb"

# Minimal single viewer HTML
viewer_html = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@1.16.0/dist/model-viewer.min.js"></script>
</head>
<body style="margin: 0; padding: 0; width: 100%; height: 100%;">
  <model-viewer
    src="{test_url}"
    alt="Test Model"
    style="width: 100%; height: 100%;"
    shadow-intensity="1"
    camera-controls
    auto-rotate>
  </model-viewer>
</body>
</html>
"""

html(viewer_html, height=600)
