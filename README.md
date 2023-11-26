# Tugas Besar TBFO IF2124
<h1 align="center">HTML VALIDITY CHECKER<h1/>

## Overview
Berikut adalah repository program HTML Syntax checker. Program ini berfungsi untuk menentukan validitas suatu kode HTML. Program ini meninjau struktur elemen-elemen dari file HTML dan menggunakan pushdown automata untuk melakukan pengecekan.`

## Kontributor:
| NIM      | Name                      | Task Allocation  |
| -------- | ------------------------- | ---------------- |
| 13522031 | Zaki Yudhistira Candra        | Diagram state, PDA    |
| 13522039 | Edbert Eddyson Gunawan             | Diagram state, PDA              |
| 13522049 | Vanson Kurnialim | Tokenizer, Implementasi PDA |

## Cara Menggunakan Program
1. Clone repository ini terlebih dahulu
2. Pastikan direktori folder berada di folder utama
3. Masukkan command berikut di terminal
`python main.py pda.txt “Direktori inputAcc.html”`
5. Cermati output program

### Prasyarat

- [Python](https://www.python.org/) (3.6 atau lebih baru)
- Library python
  argparse `pip install argparse`
  colorama `pip install colorama`
  re `pip install re`

### Susunan Program

```
├── README.md
├── main.py
├── pda.txt
├── prototype # Versi-versi terdahulu program
│   ├── alstruk.txt
│   ├── lmao.txt
│   ├── mesin.py
│   ├── mesinV2.py
│   └── script.py
└── test
    └── index.html
```
