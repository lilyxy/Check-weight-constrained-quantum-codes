"""
Compute row/column weights from parity-check matrices.

For CSS codes, computes max and average weights for both X and Z PCMs.
Output is formatted for easy copy-paste into README.md tables.

Usage:
    python compute_weights.py <Hx.mtx> <Hz.mtx>
    python compute_weights.py codes/quantum_tanner/QT_144_12_6_Hx.mtx codes/quantum_tanner/QT_144_12_6_Hz.mtx
"""

import numpy as np
from scipy.io import mmread
from scipy.sparse import issparse
import argparse
from pathlib import Path


def compute_weights(matrix) -> dict:
    """
    Compute row and column weights from a parity-check matrix.
    
    Returns:
        dict with keys: max_row, max_col, avg_row, avg_col
    """
    if issparse(matrix):
        matrix = matrix.toarray()
    
    row_weights = np.sum(matrix != 0, axis=1)
    col_weights = np.sum(matrix != 0, axis=0)
    
    return {
        'max_row': int(np.max(row_weights)),
        'max_col': int(np.max(col_weights)),
        'avg_row': float(np.mean(row_weights)),
        'avg_col': float(np.mean(col_weights)),
    }


def compute_css_weights(hx_path: str, hz_path: str) -> dict:
    """
    Compute weights for a CSS code from X and Z parity-check matrices.
    
    Returns:
        dict with max and avg weights for both X and Z
    """
    hx = mmread(hx_path)
    hz = mmread(hz_path)
    
    x_weights = compute_weights(hx)
    z_weights = compute_weights(hz)
    
    return {
        'hx': x_weights,
        'hz': z_weights,
        'max_weights': f"{x_weights['max_row']}, {x_weights['max_col']}, {z_weights['max_row']}, {z_weights['max_col']}",
        'avg_weights': f"{x_weights['avg_row']:.1f}, {x_weights['avg_col']:.1f}, {z_weights['avg_row']:.1f}, {z_weights['avg_col']:.1f}",
    }


def main():
    parser = argparse.ArgumentParser(
        description='Compute row/column weights from PCMs for README table'
    )
    parser.add_argument('hx', help='Path to X parity-check matrix (MTX format)')
    parser.add_argument('hz', help='Path to Z parity-check matrix (MTX format)')
    
    args = parser.parse_args()
    
    weights = compute_css_weights(args.hx, args.hz)
    
    print("=" * 50)
    print("Weights for README.md table:")
    print("=" * 50)
    print(f"Max Weights (wrX, wcX, wrZ, wcZ): {weights['max_weights']}")
    print(f"Avg Weights (wrX, wcX, wrZ, wcZ): {weights['avg_weights']}")
    print("=" * 50)
    print("\nDetailed breakdown:")
    print(f"  X-checks: max_row={weights['hx']['max_row']}, max_col={weights['hx']['max_col']}, "
          f"avg_row={weights['hx']['avg_row']:.2f}, avg_col={weights['hx']['avg_col']:.2f}")
    print(f"  Z-checks: max_row={weights['hz']['max_row']}, max_col={weights['hz']['max_col']}, "
          f"avg_row={weights['hz']['avg_row']:.2f}, avg_col={weights['hz']['avg_col']:.2f}")


if __name__ == '__main__':
    main()
