import argparse
import numpy as np
from vecz import VecZCompressor

def main():
    parser = argparse.ArgumentParser(description="VecZ - Vector Compressor")
    subparsers = parser.add_subparsers(dest="command")

    compress_parser = subparsers.add_parser("compress")
    compress_parser.add_argument("--input", required=True, help="Path to .npy file containing vectors")
    compress_parser.add_argument("--output", required=True, help="Output path for .vecz.gz file")
    compress_parser.add_argument("--block", type=int, default=4, help="Block size for compression")

    decompress_parser = subparsers.add_parser("decompress")
    decompress_parser.add_argument("--input", required=True, help="Path to .vecz.gz file")
    decompress_parser.add_argument("--output", required=True, help="Output path for decompressed .npy file")

    args = parser.parse_args()

    if args.command == "compress":
        vectors = np.load(args.input)
        compressor = VecZCompressor(block_size=args.block)
        compressor.compress(vectors)
        compressor.save(args.output)
        print(f"Compressed and saved to {args.output}")

    elif args.command == "decompress":
        compressor = VecZCompressor()
        compressor.load(args.input)
        vectors = compressor.decompress_all()
        np.save(args.output, np.array(vectors))
        print(f"Decompressed and saved to {args.output}.npy")

if __name__ == "__main__":
    main()
