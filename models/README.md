# 3D Models Folder

Upload your `.glb` files here and use the links to import them into the Bosch AR/VR Viewer.

## How to Add Your Models

### Step 1: Upload GLB File to GitHub
1. Go to: https://github.com/sileSpawns/GBL-Viewer
2. Click the `models` folder
3. Click **"Add file"** → **"Upload files"**
4. Drag and drop your `.glb` file
5. Click **"Commit changes"**

### Step 2: Get the Import URL
1. Open your uploaded file
2. Click the **"Raw"** button in the top-right
3. Copy the URL (it will look like the example below)

### Step 3: Import into Viewer
1. Go to https://share.streamlit.io/sileSpawns/GBL-Viewer/main/streamlit_app.py
2. Paste the URL into the import field
3. Add a custom name (optional)
4. Click **"+ Import Model"**

---

## URL Format Example

Once you upload a file named `my_model.glb`, your import URL will be:

```
https://raw.githubusercontent.com/sileSpawns/GBL-Viewer/main/models/my_model.glb
```

**Just paste this into the viewer's import field!**

---

## File Size Limit
- GitHub: Maximum 100MB per file
- For larger files, use external hosting (Sketchfab, AWS S3, etc.)

## Supported Format
- ✅ `.glb` files only
