import numpy as np
from vecz import VecZCompressor

def test_vecz_roundtrip():
    vectors = [np.round(np.random.rand(512), 3).astype(np.float16) for _ in range(10)]
    compressor = VecZCompressor(block_size=4)
    compressor.compress(vectors)
    reconstructed = compressor.decompress_all()
    for original, recon in zip(vectors, reconstructed):
        assert np.allclose(original, recon)
