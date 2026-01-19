# Explicit QLDPC Database

This repository serves as a database for explicit instances of finite-size Quantum Low-Density Parity-Check (QLDPC) codes.

Codes are categorized by construction method. Click on the Hx/Hz links to download the X or Z parity-check matrix directly.

> **File Format:** All matrices are in [Matrix Market format](https://math.nist.gov/MatrixMarket/formats.html) (`.mtx`).  
> **Need other formats?** Use `scripts/convert_format.py` to convert to NumPy, CSV, or alist.

---

## 1. Quantum Tanner Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *coming soon* | - | - | - | - | - | - | - | - |

## 2. Lifted-Product Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *coming soon* | - | - | - | - | - | - | - | - |

## 3. Hypergraph Product (HGP) Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *coming soon* | - | - | - | - | - | - | - | - |

## 4. Bivariate Bicycle (BB) Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *coming soon* | - | - | - | - | - | - | - | - |

---

## Legend

| Symbol | Description |
|--------|-------------|
| n | Number of physical qubits |
| k | Number of logical qubits |
| d | Code distance |
| Max Weights | (w_rX, w_cX, w_rZ, w_cZ) - max row/col weights for X and Z checks |
| Avg Weights | Average row/col weights |

---

## Utility Scripts

| Script | Description |
|--------|-------------|
| [`compute_weights.py`](./scripts/compute_weights.py) | Compute max/avg weights from PCM files |
| [`convert_format.py`](./scripts/convert_format.py) | Convert MTX to NumPy, CSV, alist formats |

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- File naming convention: `{construction}_{n}_{k}_{d}_Hx.mtx`
- How to add new code instances
- How to add new construction types
