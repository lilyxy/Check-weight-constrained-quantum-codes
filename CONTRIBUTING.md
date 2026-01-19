# Contributing to Explicit-QLDPC-codes

Thank you for contributing to this database of explicit QLDPC code instances!

## How to Add a New Code Instance

### 1. File Naming Convention

All parity-check matrix files must follow this naming pattern:

```
{construction}_{n}_{k}_{d}_Hx.mtx   # X parity-check matrix
{construction}_{n}_{k}_{d}_Hz.mtx   # Z parity-check matrix
```

**Parameters:**
| Field | Description | Example |
|-------|-------------|---------|
| `{construction}` | Abbreviation for construction type | `QT`, `LP`, `HGP`, `BB` |
| `{n}` | Number of physical qubits | `144` |
| `{k}` | Number of logical qubits | `12` |
| `{d}` | Code distance | `6` |

**Construction Type Abbreviations:**
| Full Name | Abbreviation | Folder |
|-----------|--------------|--------|
| Quantum Tanner Codes | `QT` | `codes/quantum_tanner/` |
| Lifted-Product Codes | `LP` | `codes/lifted_product/` |
| Hypergraph Product Codes | `HGP` | `codes/hgp/` |
| Bivariate Bicycle Codes | `BB` | `codes/bivariate_bicycle/` |

### 2. File Format

Use **Matrix Market format** (`.mtx`) for all parity-check matrices.

Example header:
```
%%MatrixMarket matrix coordinate integer general
% Quantum Tanner Code, n=144, k=12, d=6, X-checks
72 144 432
1 1 1
1 3 1
...
```

### 3. Place Files in Correct Directory

Place your `.mtx` files in the appropriate subdirectory under `codes/`:
- `codes/quantum_tanner/` for QT codes
- `codes/lifted_product/` for LP codes
- `codes/hgp/` for HGP codes
- `codes/bivariate_bicycle/` for BB codes

### 4. Update README.md

Add a row to the appropriate table in `README.md`:

```markdown
| QT002 | 288 | 24 | 8 | 6, 6, 6, 6 | 5.5, 5.5, 5.5, 5.5 | [Hx](./codes/quantum_tanner/QT_288_24_8_Hx.mtx) | [Hz](./codes/quantum_tanner/QT_288_24_8_Hz.mtx) | [arXiv:xxxx.xxxxx](https://arxiv.org/abs/xxxx.xxxxx) |
```

**Compute weights using the provided script:**
```bash
python scripts/compute_weights.py codes/quantum_tanner/QT_288_24_8_Hx.mtx codes/quantum_tanner/QT_288_24_8_Hz.mtx
```

### 5. Adding a New Construction Type

To add an entirely new construction type:

1. Create a new folder under `codes/` (use snake_case)
2. Choose a short abbreviation (2-4 letters)
3. Add a new section to `README.md` with the standard table format
4. Update this CONTRIBUTING.md with the new abbreviation

## Utility Scripts

- **`scripts/convert_format.py`** - Convert MTX files to other formats (npy, csv, alist)
- **`scripts/compute_weights.py`** - Compute max/avg weights for README tables

## Questions?

Open an issue if you have questions about contributing.
