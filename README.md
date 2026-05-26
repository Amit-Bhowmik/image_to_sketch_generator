# Image to Sketch Converter

A Python desktop app that transforms any photo into a **hand-drawn pencil sketch**, rendered live using Turtle graphics — line by line, just like a real artist drawing it.

---

## ✨ Features

- 🎨 **Live drawing animation** — watch the sketch appear stroke by stroke
- 🔍 **Smart edge detection** — combines Canny + Adaptive Threshold for rich, detailed lines
- 🖼️ **CLAHE contrast enhancement** — works well on dark, bright, and low-contrast images
- ✏️ **Pencil jitter effect** — subtle randomness makes lines feel hand-drawn
- 📐 **Variable pen width** — thicker strokes for large shapes, thinner for fine detail
- 💾 **Edge preview export** — saves `sketch_edges_preview.png` for debugging
- ⚙️ **Fully configurable** — tweak every parameter in `config.py`

---

## 📁 Project Structure

```
image_to_sketch/
├── main.py              # Entry point — run this
├── config.py            # All tunable settings
├── core/
│   ├── processor.py     # Image preprocessing & edge detection
│   └── renderer.py      # Turtle graphics drawing engine
└── ui/
    └── dialogs.py       # File picker & message boxes (tkinter)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Amit-Bhowmik/image_to_sketch_generator.git
cd image_to_sketch_generator
```

### 2. Install dependencies

```bash
pip install opencv-python numpy
```

> `tkinter` and `turtle` come built-in with Python — no extra install needed.

### 3. Run the app

```bash
python main.py
```

A file picker will open. Choose any `.png`, `.jpg`, `.jpeg`, `.bmp`, or `.webp` image and watch it get sketched in real time.

---

## ⚙️ Configuration

All settings live in `config.py`. No need to touch any other file.

| Parameter | Default | Effect |
|---|---|---|
| `TARGET_WIDTH` | `800` | Resize width before processing — larger = more detail, slower |
| `CANNY_LOW` | `30` | Lower Canny threshold — decrease to catch finer edges |
| `CANNY_HIGH` | `100` | Upper Canny threshold — decrease to capture more detail |
| `MIN_CONTOUR_AREA` | `10` | Minimum contour size — lower keeps more fine detail |
| `APPROX_EPSILON` | `1.2` | Curve simplification — lower = more faithful to original edges |
| `PENCIL_JITTER` | `0.4` | Hand-drawn randomness — set to `0` for clean computer lines |
| `TRACER_N` | `50` | Screen refresh rate — higher = faster drawing |
| `SCREEN_W / SCREEN_H` | `1100 / 800` | Turtle window size |

---

## 🧠 How It Works

```
Image File
    │
    ▼
Resize  →  Grayscale  →  CLAHE Contrast Enhancement
    │
    ▼
Bilateral Filter (denoise, preserve edges)
    │
    ├──▶ Canny Edge Detection
    └──▶ Adaptive Thresholding
         │
         ▼
      OR Merge  →  Morphological Cleanup
         │
         ▼
   Extract Contours  →  Filter & Approximate
         │
         ▼
   Turtle Renders Contours (large → small)
```

---

## 🖼️ Supported Image Formats

| Format | Extension |
|---|---|
| JPEG | `.jpg`, `.jpeg` |
| PNG | `.png` |
| Bitmap | `.bmp` |
| WebP | `.webp` |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `opencv-python` | Image processing, edge detection, contours |
| `numpy` | Array operations for morphological kernels |
| `turtle` | Live sketch drawing (built-in) |
| `tkinter` | File picker and dialogs (built-in) |

---

## 🙌 Contributing

Pull requests are welcome! If you find a bug or want to suggest an improvement, feel free to open an issue.

1. Fork the repo
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request
---

## Author
Amit Bhowmik<br>
Dept of CSE<br>
`Feni University`
