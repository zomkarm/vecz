# 🧠 VecZ

**VecZ** is a lightweight, block-level compressor for high-dimensional ML vectors (like embeddings).  
Perfect for storing millions of vectors with repeated float patterns — lossless and blazing fast.

---

## 🚀 Features

- 🔹 Compresses repeated float vector patterns
- 🔹 Offline & fully lossless
- 🔹 Works great with audio/image/text embeddings
- 🔹 No ML or training required
- 🔹 Saves 60–90% storage in many real-world cases

---

## 📦 Installation

```bash
pip install vecz
```

---

## ⚙️ Usage

### ✅ In Python

```python
import numpy as np
from vecz import VecZCompressor

vectors = [np.random.rand(512).astype(np.float16) for _ in range(1000)]
compressor = VecZCompressor(block_size=4)
compressor.compress(vectors)
compressor.save("compressed.vecz.gz")

# Load and restore
c2 = VecZCompressor()
c2.load("compressed.vecz.gz")
restored = c2.decompress_all()
```

### ✅ CLI Usage

```bash
# Compress
vecz compress --input vectors.npy --output compressed.vecz.gz --block 4

# Decompress
vecz decompress --input compressed.vecz.gz --output restored.npy
```

---

## 🧪 Benchmark (example)

| Format      | Size (MB) | Compression |
|-------------|-----------|-------------|
| Raw .npy    | 160 MB    | ❌          |
| VecZ .gz    | 18 MB     | ✅ 8–10x     |
| Joblib      | 140 MB    | ❌          |
| Pickle      | 130 MB    | ❌          |

---

## 🔧 Roadmap

- [x] CLI tool
- [ ] Integration with FAISS
- [ ] Quantized modes (float8 / int8)
- [ ] PyTorch/TensorFlow embedding support

---

## 🧑‍💻 Author

**Omkar Zende**  
📫 [expertomkar@gmail.com](mailto:expertomkar@gmail.com)  
🌐 [github.com/zomkarm](https://github.com/zomkarm)

MIT Licensed · Built with ❤️ in Python
