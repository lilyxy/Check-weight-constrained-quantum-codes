"""
Convert Matrix Market (.mtx) files to other formats.

Supported output formats:
- NumPy dense array (.npy)
- Alist format (.alist) - common in classical LDPC decoders
- CSV format (.csv)
- Scipy sparse formats (CSR, COO)

Usage:
    python convert_format.py <input.mtx> <output_format>
    
Example:
    python convert_format.py QT_144_12_6_Hx.mtx npy
    python convert_format.py QT_144_12_6_Hx.mtx alist
"""

import numpy as np
from scipy.io import mmread
from scipy.sparse import csr_matrix, coo_matrix
import argparse
from pathlib import Path


def mtx_to_dense(mtx_path: str) -> np.ndarray:
    """Load MTX file and return as dense NumPy array."""
    sparse_matrix = mmread(mtx_path)
    return sparse_matrix.toarray()


def mtx_to_npy(mtx_path: str, output_path: str = None) -> str:
    """Convert MTX to NumPy .npy format."""
    dense = mtx_to_dense(mtx_path)
    if output_path is None:
        output_path = Path(mtx_path).with_suffix('.npy')
    np.save(output_path, dense)
    return str(output_path)


def mtx_to_csv(mtx_path: str, output_path: str = None) -> str:
    """Convert MTX to CSV format."""
    dense = mtx_to_dense(mtx_path)
    if output_path is None:
        output_path = Path(mtx_path).with_suffix('.csv')
    np.savetxt(output_path, dense, delimiter=',', fmt='%d')
    return str(output_path)


def mtx_to_alist(mtx_path: str, output_path: str = None) -> str:
    """
    Convert MTX to alist format.
    
    Alist format (used by many LDPC decoders):
    - Line 1: n m (columns, rows)
    - Line 2: max_col_weight max_row_weight
    - Line 3: column weights (n values)
    - Line 4: row weights (m values)
    - Next n lines: non-zero row indices for each column (1-indexed)
    - Next m lines: non-zero column indices for each row (1-indexed)
    """
    # TODO: Implement alist conversion
    raise NotImplementedError("Alist conversion not yet implemented")


def mtx_to_csr(mtx_path: str) -> csr_matrix:
    """Load MTX file and return as CSR sparse matrix."""
    return csr_matrix(mmread(mtx_path))


def mtx_to_coo(mtx_path: str) -> coo_matrix:
    """Load MTX file and return as COO sparse matrix."""
    return coo_matrix(mmread(mtx_path))


def main():
    parser = argparse.ArgumentParser(description='Convert MTX files to other formats')
    parser.add_argument('input', help='Input MTX file path')
    parser.add_argument('format', choices=['npy', 'csv', 'alist'], 
                        help='Output format')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    
    args = parser.parse_args()
    
    converters = {
        'npy': mtx_to_npy,
        'csv': mtx_to_csv,
        'alist': mtx_to_alist,
    }
    
    output = converters[args.format](args.input, args.output)
    print(f"Converted to: {output}")


if __name__ == '__main__':
    main()
