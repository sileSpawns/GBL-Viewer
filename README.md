# GBL Viewer

A minimal viewer that uses `model-viewer` to display a GLB file with AR support.

Files:
- [index.html](index.html) — main viewer page.

Usage
-----

1. Place your `test.glb` and (optionally) `poster.webp` in the project root next to `index.html`.
2. Serve the folder from a local HTTP server (AR and some browser features require a secure context or localhost).

Quickstart with Python 3:

```bash
# from the workspace root
python3 -m http.server 8000
# then open http://localhost:8000/index.html
```

Or using Node (if you prefer):

```bash
# install http-server if you don't have it
npm install -g http-server
http-server -c-1 . -p 8000
```

Notes
-----
- `model-viewer` is loaded from CDN. If you need an offline copy, download the library and update the script tag in `index.html`.
- For iOS Quick Look AR, you need a `usdz` or let `model-viewer` generate it server-side; quick-look support is handled by `model-viewer` when `ar` is enabled.
- If you want, I can add a sample `test.glb` and `poster.webp`, or add a `package.json` with a local dev script. What would you like next?