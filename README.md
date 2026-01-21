# Explicit QLDPC Database

This repository serves as a database for explicit instances of finite-size Quantum Low-Density Parity-Check (QLDPC) codes.

Codes are categorized by construction method. Click on the Hx/Hz links to download the X or Z parity-check matrix directly.

> **File Format:** All matrices are in [Matrix Market format](https://math.nist.gov/MatrixMarket/formats.html) (`.mtx`).  
> **Need other formats?** Use `scripts/convert_format.py` to convert to NumPy, CSV, or alist.

---

## 1. Quantum Tanner Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| qt_6-1_3-1_4-3 | 72 | 19 | 4 | (6,4,8,3) | (6, 3, 8, 2.7) | [Hx](./codes/quantum_tanner/G6-1_A3-1_T50bafbdc8820_B4-3_Tcb63a96ac777_rep7_perm1_pcmX.mtx) | [Hz](./codes/quantum_tanner/G6-1_A3-1_T50bafbdc8820_B4-3_Tcb63a96ac777_rep7_perm1_pcmZ.mtx) | Group Group(6,1), Pairs (3, 1), (4, 3) |
| qt_6-1_4-1_4-3 | 96 | 30 | 4 | (8,4,8,4) | (8, 3, 8, 3) | [Hx](./codes/quantum_tanner/G6-1_A4-1_T7ac9928020e0_B4-3_Tcb63a96ac777_rep5_perm1_pcmX.mtx) | [Hz](./codes/quantum_tanner/G6-1_A4-1_T7ac9928020e0_B4-3_Tcb63a96ac777_rep5_perm1_pcmZ.mtx) | Group Group(6,1), Pairs (4, 1), (4, 3) |
| qt_6-1_4-2_6-3 | 144 | 12 | 7 | (9,7,12,9) | (7.5, 3.8, 7.5, 3.8) | [Hx](./codes/quantum_tanner/G6-1_A4-2_T26ada56bb948_B6-3_T5c4d5f54d04e_rep9_perm10_pcmX.mtx) | [Hz](./codes/quantum_tanner/G6-1_A4-2_T26ada56bb948_B6-3_T5c4d5f54d04e_rep9_perm10_pcmZ.mtx) | Group Group(6,1), Pairs (4, 2), (6, 3) |
| qt_6-1_5-2_6-3 | 180 | 16 | 7 | (16,8,12,8) | (9.6, 3.9, 7.1, 4.2) | [Hx](./codes/quantum_tanner/G6-1_A5-2_T2eb81f1e0aa2_B6-3_T5c4d5f54d04e_rep4_perm1_pcmX.mtx) | [Hz](./codes/quantum_tanner/G6-1_A5-2_T2eb81f1e0aa2_B6-3_T5c4d5f54d04e_rep4_perm1_pcmZ.mtx) | Group Group(6,1), Pairs (5, 2), (6, 3) |
| qt_6-1_6-3_6-3 | 216 | 20 | 8 | (16,9,16,9) | (9.5, 4.8, 9.5, 4.8) | [Hx](./codes/quantum_tanner/G6-1_A6-3_T5c4d5f54d04e_B6-3_T5c4d5f54d04e_rep4_perm10_pcmX.mtx) | [Hz](./codes/quantum_tanner/G6-1_A6-3_T5c4d5f54d04e_B6-3_T5c4d5f54d04e_rep4_perm10_pcmZ.mtx) | Group Group(6,1), Pairs (6, 3), (6, 3) |
| qt_6-2_4-3_5-2 | 120 | 23 | 4 | (8,8,12,3) | (6.2, 3.8, 9.3, 2.8) | [Hx](./codes/quantum_tanner/G6-2_A4-3_Tcb63a96ac777_B5-2_T2eb81f1e0aa2_rep6_perm1_pcmX.mtx) | [Hz](./codes/quantum_tanner/G6-2_A4-3_Tcb63a96ac777_B5-2_T2eb81f1e0aa2_rep6_perm1_pcmZ.mtx) | Group Group(6,2), Pairs (4, 3), (5, 2) |
| qt_6-2_4-2_6-3 | 144 | 6 | 9 | (12,7,9,8) | (7.8, 3.9, 7.5, 3.8) | [Hx](./codes/quantum_tanner/G6-2_A4-2_T26ada56bb948_B6-3_T5c4d5f54d04e_rep3_perm4_pcmX.mtx) | [Hz](./codes/quantum_tanner/G6-2_A4-2_T26ada56bb948_B6-3_T5c4d5f54d04e_rep3_perm4_pcmZ.mtx) | Group Group(6,2), Pairs (4, 2), (6, 3) |
| qt_6-2_5-1_5-4 | 150 | 62 | 4 | (10,5,10,5) | (10, 3.2, 10, 3.2) | [Hx](./codes/quantum_tanner/G6-2_A5-1_Ta579ba8231b6_B5-4_T4bb76c2f3e95_rep4_perm1_pcmX.mtx) | [Hz](./codes/quantum_tanner/G6-2_A5-1_Ta579ba8231b6_B5-4_T4bb76c2f3e95_rep4_perm1_pcmZ.mtx) | Group Group(6,2), Pairs (5, 1), (5, 4) |
| qt_6-2_6-3_6-3 | 216 | 10 | 14 | (16,9,16,11) | (9.5, 4.7, 9.5, 4.8) | [Hx](./codes/quantum_tanner/G6-2_A6-3_T5c4d5f54d04e_B6-3_T5c4d5f54d04e_rep5_perm10_pcmX.mtx) | [Hz](./codes/quantum_tanner/G6-2_A6-3_T5c4d5f54d04e_B6-3_T5c4d5f54d04e_rep5_perm10_pcmZ.mtx) | Group Group(6,2), Pairs (6, 3), (6, 3) |
| qt_7-1_5-2_7-4 | 245 | 22 | 8 | (12,7,12,8) | (10.1, 4.6, 9.3, 4.8) | [Hx](./codes/quantum_tanner/G7-1_A5-2_T2eb81f1e0aa2_B7-4_Te2dec83aafa8_rep3_perm8_pcmX.mtx) | [Hz](./codes/quantum_tanner/G7-1_A5-2_T2eb81f1e0aa2_B7-4_Te2dec83aafa8_rep3_perm8_pcmZ.mtx) | Group Group(7,1), Pairs (5, 2), (7, 4) |
| qt_7-1_7-3_7-4 | 343 | 22 | 14 | (16,10,16,12) | (12.2, 6.0, 12.3, 6.0) | [Hx](./codes/quantum_tanner/G7-1_A7-3_T1b404206a637_B7-4_Te2dec83aafa8_rep1_perm5_pcmX.mtx) | [Hz](./codes/quantum_tanner/G7-1_A7-3_T1b404206a637_B7-4_Te2dec83aafa8_rep1_perm5_pcmZ.mtx) | Group Group(7,1), Pairs (7, 3), (7, 4) |
| qt_8-1_4-1_4-3 | 128 | 40 | 4 | (8,4,8,4) | (8, 3, 8, 3) | [Hx](./codes/quantum_tanner/G8-1_A4-1_T7ac9928020e0_B4-3_Tcb63a96ac777_rep1_perm1_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-1_A4-1_T7ac9928020e0_B4-3_Tcb63a96ac777_rep1_perm1_pcmZ.mtx) | Group Group(8,1), Pairs (4, 1), (4, 3) |
| qt_8-1_5-2_7-4 | 280 | 31 | 8 | (16,8,12,8) | (10.2, 4.7, 9.3, 4.8) | [Hx](./codes/quantum_tanner/G8-1_A5-2_T2eb81f1e0aa2_B7-4_Te2dec83aafa8_rep10_perm2_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-1_A5-2_T2eb81f1e0aa2_B7-4_Te2dec83aafa8_rep10_perm2_pcmZ.mtx) | Group Group(8,1), Pairs (5, 2), (7, 4) |
| qt_8-2_3-1_4-2 | 96 | 10 | 4 | (9,4,6,6) | (7.5, 2.5, 5, 3.3) | [Hx](./codes/quantum_tanner/G8-2_A3-1_T50bafbdc8820_B4-2_T26ada56bb948_rep7_perm1_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-2_A3-1_T50bafbdc8820_B4-2_T26ada56bb948_rep7_perm1_pcmZ.mtx) | Group Group(8,2), Pairs (3, 1), (4, 2) |
| qt_8-2_3-1_4-3 | 96 | 24 | 4 | (6,4,8,3) | (6, 3, 8, 2.7) | [Hx](./codes/quantum_tanner/G8-2_A3-1_T50bafbdc8820_B4-3_Tcb63a96ac777_rep1_perm1_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-2_A3-1_T50bafbdc8820_B4-3_Tcb63a96ac777_rep1_perm1_pcmZ.mtx) | Group Group(8,2), Pairs (3, 1), (4, 3) |
| qt_8-2_6-3_8-4 | 384 | 48 | 12 | (16,12,16,13) | (13.3, 6.7, 13.3, 6.6) | [Hx](./codes/quantum_tanner/G8-2_A6-3_T5c4d5f54d04e_B8-4_Te71519c717c8_rep8_perm12_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-2_A6-3_T5c4d5f54d04e_B8-4_Te71519c717c8_rep8_perm12_pcmZ.mtx) | Group Group(8,2), Pairs (6, 3), (8, 4) |
| qt_8-3_7-3_7-4 | 392 | 54 | 12 | (16,18,16,15) | (12.9, 6.3, 12.9, 6.3) | [Hx](./codes/quantum_tanner/G8-3_A7-3_T1b404206a637_B7-4_Te2dec83aafa8_rep1_perm6_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-3_A7-3_T1b404206a637_B7-4_Te2dec83aafa8_rep1_perm6_pcmZ.mtx) | Group Group(8,3), Pairs (7, 3), (7, 4) |
| qt_8-4_8-4_8-4 | 512 | 76 | 16 | (16,18,16,18) | (16, 8, 16, 8) | [Hx](./codes/quantum_tanner/G8-4_A8-4_Te71519c717c8_B8-4_Te71519c717c8_rep1_perm1_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-4_A8-4_Te71519c717c8_B8-4_Te71519c717c8_rep1_perm1_pcmZ.mtx) | Group Group(8,4), Pairs (8, 4), (8, 4) |
| qt_8-5_8-4_8-4 | 512 | 76 | 16 | (16,18,16,18) | (16, 8, 16, 8) | [Hx](./codes/quantum_tanner/G8-5_A8-4_Te71519c717c8_B8-4_Te71519c717c8_rep8_perm6_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-5_A8-4_Te71519c717c8_B8-4_Te71519c717c8_rep8_perm6_pcmZ.mtx) | Group Group(8,5), Pairs (8, 4), (8, 4) |
| qt_8-5_8-4_8-4 | 512 | 80 | 16 | (16,18,16,18) | (16, 8, 16, 8) | [Hx](./codes/quantum_tanner/G8-5_A8-4_Te71519c717c8_B8-4_Te71519c717c8_rep4_perm9_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-5_A8-4_Te71519c717c8_B8-4_Te71519c717c8_rep4_perm9_pcmZ.mtx) | Group Group(8,5), Pairs (8, 4), (8, 4) |
| qt_8-5_6-3_6-3 | 288 | 36 | 8 | (12,12,12,12) | (9.9, 5.0, 10.0, 5.0) | [Hx](./codes/quantum_tanner/G8-5_A6-3_T5c4d5f54d04e_B6-3_T5c4d5f54d04e_rep5_perm14_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-5_A6-3_T5c4d5f54d04e_B6-3_T5c4d5f54d04e_rep5_perm14_pcmZ.mtx) | Group Group(8,5), Pairs (6, 3), (6, 3) |
| qt_8-5_6-3_8-4 | 384 | 56 | 12 | (16,18,16,18) | (13.3, 6.6, 13.3, 6.7) | [Hx](./codes/quantum_tanner/G8-5_A6-3_T5c4d5f54d04e_B8-4_Te71519c717c8_rep6_perm11_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-5_A6-3_T5c4d5f54d04e_B8-4_Te71519c717c8_rep6_perm11_pcmZ.mtx) | Group Group(8,5), Pairs (6, 3), (8, 4) |
| qt_8-5_7-3_7-3 | 392 | 50 | 8 | (16,18,16,18) | (16, 5.9, 10.5, 6.9) | [Hx](./codes/quantum_tanner/G8-5_A7-3_T1b404206a637_B7-3_T1b404206a637_rep2_perm6_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-5_A7-3_T1b404206a637_B7-3_T1b404206a637_rep2_perm6_pcmZ.mtx) | Group Group(8,5), Pairs (7, 3), (7, 3) |
| qt_8-5_7-3_7-4 | 392 | 59 | 12 | (16,18,16,18) | (12.9, 6.3, 13, 6.4) | [Hx](./codes/quantum_tanner/G8-5_A7-3_T1b404206a637_B7-4_Te2dec83aafa8_rep2_perm11_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-5_A7-3_T1b404206a637_B7-4_Te2dec83aafa8_rep2_perm11_pcmZ.mtx) | Group Group(8,5), Pairs (7, 3), (7, 4) |
| qt_8-5_7-3_8-4 | 448 | 68 | 12 | (16,18,16,18) | (16, 6.9, 13, 7.4) | [Hx](./codes/quantum_tanner/G8-5_A7-3_T1b404206a637_B8-4_Te71519c717c8_rep7_perm3_pcmX.mtx) | [Hz](./codes/quantum_tanner/G8-5_A7-3_T1b404206a637_B8-4_Te71519c717c8_rep7_perm3_pcmZ.mtx) | Group Group(8,5), Pairs (7, 3), (8, 4) |
| qt_9-1_3-1_7-4 | 189 | 24 | 4 | (9,5,8,8) | (9, 3.4, 8, 4.6) | [Hx](./codes/quantum_tanner/G9-1_A3-1_T50bafbdc8820_B7-4_Te2dec83aafa8_rep1_perm2_pcmX.mtx) | [Hz](./codes/quantum_tanner/G9-1_A3-1_T50bafbdc8820_B7-4_Te2dec83aafa8_rep1_perm2_pcmZ.mtx) | Group Group(9,1), Pairs (3, 1), (7, 4) |
| qt_9-1_6-3_6-3 | 324 | 8 | 26 | (12,7,16,10) | (10, 5, 11.1, 5.5) | [Hx](./codes/quantum_tanner/G9-1_A6-3_T5c4d5f54d04e_B6-3_T5c4d5f54d04e_rep1_perm3_pcmX.mtx) | [Hz](./codes/quantum_tanner/G9-1_A6-3_T5c4d5f54d04e_B6-3_T5c4d5f54d04e_rep1_perm3_pcmZ.mtx) | Group Group(9,1), Pairs (6, 3), (6, 3) |
| qt_9-1_6-3_8-4 | 432 | 16 | 28 | (16,10,16,10) | (13.3, 6.7, 13.3, 6.7) | [Hx](./codes/quantum_tanner/G9-1_A6-3_T5c4d5f54d04e_B8-4_Te71519c717c8_rep1_perm12_pcmX.mtx) | [Hz](./codes/quantum_tanner/G9-1_A6-3_T5c4d5f54d04e_B8-4_Te71519c717c8_rep1_perm12_pcmZ.mtx) | Group Group(9,1), Pairs (6, 3), (8, 4) |

## 2. Lifted-Product Codes

| ID | n | k | d | Max Weights | Avg Weights | X-PCM | Z-PCM | Notes / References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| pk_code_169 | 416 | 18 | 22 | (8,4,8,4) | (8.0, 4.0, 8.0, 4.0) | [Hx](./codes/lifted_product/pk_code_169_n416_k18_d22_pcmX.mtx) | [Hz](./codes/lifted_product/pk_code_169_n416_k18_d22_pcmZ.mtx) |  |
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
