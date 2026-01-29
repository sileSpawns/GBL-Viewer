import streamlit as st
from streamlit.components.v1 import html
import json
from pathlib import Path

st.set_page_config(page_title="GBL Viewer", layout="wide")
st.title("GBL Viewer — 3D Model Gallery")

st.markdown("Browse and preview 3D models from the database")

# Load models from JSON
models_file = Path(__file__).parent / "models.json"
with open(models_file) as f:
    data = json.load(f)
    models = data["models"]

st.info(f"📦 Loaded {len(models)} models from database")

# Generate grid HTML for all models
grid_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.js"></script>
    <style>
      body { margin: 0; padding: 20px; background: #111; font-family: sans-serif; }
      .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px; }
      .card { background: #1a1a1a; border-radius: 8px; overflow: hidden; }
      .card h3 { margin: 10px; color: #fff; font-size: 18px; }
      .card p { margin: 0 10px 10px; color: #ccc; font-size: 14px; }
      model-viewer { width: 100%; height: 350px; background: #222; display: block; }
    </style>
</head>
<body>
  <div class="grid">
"""

for model in models:
    usdz_attr = f'ios-src="{model["usdz"]}"' if model.get("usdz") else ""
    grid_html += f"""
    <div class="card">
      <h3>{model["name"]}</h3>
      <p>{model["description"]}</p>
      <model-viewer 
        src="{model["url"]}"
        {usdz_attr}
        alt="{model["name"]}"
        shadow-intensity="1"
        camera-controls
        auto-rotate
        ar>
      </model-viewer>
    </div>
    """

grid_html += """
  </div>
</body>
</html>
"""

html(grid_html, height=2000)

st.markdown("---")
st.markdown("""
### How to add more models:

1. **Edit `models.json`** and add a new entry:
```json
{
  "name": "Your Model Name",
  "description": "Model description",
  "url": "https://raw.githubusercontent.com/YourUser/GBL-Models/main/model.glb",
  "usdz": "https://raw.githubusercontent.com/YourUser/GBL-Models/main/model.usdz"
}
```

2. **Create a separate repo** for GLB files (e.g., `GBL-Models`)
3. **Push your .GLB files** to that repo
4. **Use raw GitHub URLs** to reference them (use `raw.githubusercontent.com`)

**Repo:** https://github.com/sileSpawns/GBL-Viewer
""")
