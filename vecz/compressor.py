import numpy as np
import gzip
import pickle
from typing import List, Tuple

class VecZCompressor:
    def __init__(self, block_size: int = 4):
        self.block_size = block_size
        self.pattern_dict = {}
        self.reverse_dict = {}
        self.pattern_id_counter = 0
        self.compressed_vectors = []
        self.vector_dim = None

    def _break_vector(self, vector: np.ndarray) -> List[Tuple[float]]:
        return [tuple(vector[i:i + self.block_size]) for i in range(0, len(vector), self.block_size)]

    def _register_block(self, block: Tuple[float]) -> int:
        if block not in self.pattern_dict:
            self.pattern_dict[block] = self.pattern_id_counter
            self.reverse_dict[self.pattern_id_counter] = block
            self.pattern_id_counter += 1
        return self.pattern_dict[block]

    def compress(self, vectors: List[np.ndarray]):
        self.vector_dim = vectors[0].shape[0]
        self.compressed_vectors = []
        for vec in vectors:
            blocks = self._break_vector(vec)
            compressed = [self._register_block(block) for block in blocks]
            self.compressed_vectors.append(compressed)

    def decompress_vector(self, compressed: List[int]) -> np.ndarray:
        flat = []
        for pid in compressed:
            flat.extend(self.reverse_dict[pid])
        return np.array(flat, dtype=np.float16)

    def decompress_all(self) -> List[np.ndarray]:
        return [self.decompress_vector(comp) for comp in self.compressed_vectors]

    def save(self, path: str):
        with gzip.open(path, 'wb') as f:
            pickle.dump({
                "block_size": self.block_size,
                "vector_dim": self.vector_dim,
                "pattern_dict": self.pattern_dict,
                "compressed_vectors": self.compressed_vectors
            }, f)

    def load(self, path: str):
        with gzip.open(path, 'rb') as f:
            data = pickle.load(f)
            self.block_size = data["block_size"]
            self.vector_dim = data["vector_dim"]
            self.pattern_dict = data["pattern_dict"]
            self.reverse_dict = {v: k for k, v in self.pattern_dict.items()}
            self.compressed_vectors = data["compressed_vectors"]
            self.pattern_id_counter = len(self.pattern_dict)
