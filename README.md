# Explicit QLDPC Database

This repository serves as a database for explicit instances of finite-size Quantum Low-Density Parity-Check (QLDPC) codes.

Codes are categorized by construction method. Click on the Hx/Hz links to download the X or Z parity-check matrix directly.

> **File Format:** All matrices are in [Matrix Market format](https://math.nist.gov/MatrixMarket/formats.html) (`.mtx`).  
> **Need other formats?** Use `scripts/convert_format.py` to convert to NumPy, CSV, or alist.

---

## 1. Quantum Tanner Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| :- | - | - | - | - | - | - | - | - |

## 2. Lifted-Product Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| pk_code_169 | 416 | 18 | 22 | (8,4,8,4) | (8.0, 4.0, 8.0, 4.0) | [Hx](./codes/lifted_product/pk_code_169_n416_k18_d22_pcmX.mtx) | [Hz](./codes/lifted_product/pk_code_169_n416_k18_d22_pcmZ.mtx) | Panteleev-Kalachev (arXiv:2104.11340) |
| lp_B16_12 | 544 | 80 | 12 | (8,5,8,5) | (8.0, 3.53, 8.0, 3.53) | [Hx](./codes/lifted_product/lp_B16_12_n544_k80_d12_pcmX.mtx) | [Hz](./codes/lifted_product/lp_B16_12_n544_k80_d12_pcmZ.mtx) | arXiv:2308.08648 |
| lp_B21_16 | 714 | 100 | 16 | (8,5,8,5) | (8.0, 3.53, 8.0, 3.53) | [Hx](./codes/lifted_product/lp_B21_16_n714_k100_d16_pcmX.mtx) | [Hz](./codes/lifted_product/lp_B21_16_n714_k100_d16_pcmZ.mtx) | arXiv:2308.08648 |
| lcs_copies3 | 75 | 3 | 4 | (4,2,4,2) | (3.5, 1.68, 3.5, 1.68) | [Hx](./codes/lifted_product/lcs_copies3_n75_k3_d4_pcmX.mtx) | [Hz](./codes/lifted_product/lcs_copies3_n75_k3_d4_pcmZ.mtx) | - |
| lcs_copies5 | 125 | 5 | 4 | (4,2,4,2) | (3.5, 1.68, 3.5, 1.68) | [Hx](./codes/lifted_product/lcs_copies5_n125_k5_d4_pcmX.mtx) | [Hz](./codes/lifted_product/lcs_copies5_n125_k5_d4_pcmZ.mtx) | - |

## 3. Hypergraph Product (HGP) Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| hgp_16_4_6 | 377 | 25 | 5 | (7,4,7,4) | (6.75, 3.15, 6.75, 3.15) | [Hx](./codes/hgp/hgp_16_4_6_n377_k25_d5_pcmX.mtx) | [Hz](./codes/hgp/hgp_16_4_6_n377_k25_d5_pcmZ.mtx) | - |
| hgp_20_5_8 | 625 | 25 | 8 | (7,4,7,4) | (7.0, 3.36, 7.0, 3.36) | [Hx](./codes/hgp/hgp_20_5_8_n625_k25_d8_pcmX.mtx) | [Hz](./codes/hgp/hgp_20_5_8_n625_k25_d8_pcmZ.mtx) | - |
| hgp_24_6_10 | 900 | 36 | 10 | (7,4,7,4) | (7.0, 3.36, 7.0, 3.36) | [Hx](./codes/hgp/hgp_24_6_10_n900_k36_d10_pcmX.mtx) | [Hz](./codes/hgp/hgp_24_6_10_n900_k36_d10_pcmZ.mtx) | - |
| hamming_hgp_r4 | 241 | 121 | 3 | (12,8,12,8) | (10.13, 2.52, 10.13, 2.52) | [Hx](./codes/hgp/hamming_hgp_r4_n241_k121_d3_pcmX.mtx) | [Hz](./codes/hgp/hamming_hgp_r4_n241_k121_d3_pcmZ.mtx) | - |
| hamming_hgp_r3 | 58 | 16 | 3 | (7,4,7,4) | (5.71, 2.07, 5.71, 2.07) | [Hx](./codes/hgp/hamming_hgp_r3_n58_k16_d3_pcmX.mtx) | [Hz](./codes/hgp/hamming_hgp_r3_n58_k16_d3_pcmZ.mtx) | - |
| toric_hgp_n5 | 41 | 1 | 5 | (4,2,4,2) | (3.6, 1.76, 3.6, 1.76) | [Hx](./codes/hgp/toric_hgp_n5_n41_k1_d5_pcmX.mtx) | [Hz](./codes/hgp/toric_hgp_n5_n41_k1_d5_pcmZ.mtx) | Toric code on 5x5 grid |
| small_hgp_3_2_1 | 10 | 4 | 2 | (4,3,4,3) | (4.0, 1.2, 4.0, 1.2) | [Hx](./hgp_lp_matrices/hgp_codes/small_hgp_3_2_1_d2_pcmX.mtx) | [Hz](./hgp_lp_matrices/hgp_codes/small_hgp_3_2_1_d2_pcmZ.mtx) | - |

## 4. Bivariate Bicycle (BB) Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| bb_code_12_6 | 144 | 12 | 12 | (6,3,6,3) | (6.0, 3.0, 6.0, 3.0) | [Hx](./codes/bivariate_bicycle/bb_code_12_6_n144_k12_d12_pcmX.mtx) | [Hz](./codes/bivariate_bicycle/bb_code_12_6_n144_k12_d12_pcmZ.mtx) | - |
| bb_code_9_6 | 108 | 8 | 10 | (6,3,6,3) | (6.0, 3.0, 6.0, 3.0) | [Hx](./codes/bivariate_bicycle/bb_code_9_6_n108_k8_d10_pcmX.mtx) | [Hz](./codes/bivariate_bicycle/bb_code_9_6_n108_k8_d10_pcmZ.mtx) | - |
| bb_code_6_6 | 72 | 12 | 6 | (6,3,6,3) | (6.0, 3.0, 6.0, 3.0) | [Hx](./codes/bivariate_bicycle/bb_code_6_6_n72_k12_d6_pcmX.mtx) | [Hz](./codes/bivariate_bicycle/bb_code_6_6_n72_k12_d6_pcmZ.mtx) | - |

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
