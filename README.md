# 🧮 SimpleCalc

A lightweight, console-based Python calculator that supports basic arithmetic, percentages (`%`), and modulus (`%%`) operations — built with clean object-oriented design and tested using `pytest`.

---

## 🚀 Features

- **Basic arithmetic**: `+`, `-`, `*`, `/`
- **Percent (%) support**: e.g. `200 * 12%` → `24.00`
- **Modulus (%%)**: e.g. `7 %% 3` → `1.00`
- **History tracking**: Stores up to 5 recent results
- **Formatted output**: Rounded to 2–4 decimal places
- **Friendly CLI** with commands:
  - `help` – show usage guide  
  - `history` – view recent calculations  
  - `clear` – clear the console  
  - `exit` – quit the program  

---

## 📦 Installation

### Clone the repository
```bash
git clone https://github.com/<YOUR_ID>/hojin-simplecalc.git
cd hojin-simplecalc
````

### Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS / Linux
# venv\Scripts\activate   # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, just install pytest manually:
>
> ```bash
> pip install pytest
> ```

---

## 🖥️ Usage

### Run the calculator

```bash
python -m simplecalc
```

### Example session

```
┌───────────────────────────────────────────┐
│               SimpleCalc v1               │
└───────────────────────────────────────────┘
Commands: help, history, clear, exit
Percent: 200*12% → 24.00 / Modulus: 7 %% 3 → 1.00
---------------------------------------------

› 5 * 3
= 15.00
› 200 * 12%
= 24.00
› 7 %% 3
= 1.00
› history
 1  7 %% 3                  1.00     2025-10-08 23:05:21
 2  200 * 12%               24.00    2025-10-08 23:04:58
 3  5 * 3                   15.00    2025-10-08 23:04:45
› exit
```

---

## 🧪 Testing

### Run all tests

```bash
pytest -v
```

Expected output:

```
==================== test session starts ====================
collected 13 items

tests/test_parser.py .....                         [ 38%]
tests/test_evaluator.py ...                        [ 61%]
tests/test_formatter.py ..                         [ 77%]
tests/test_history.py ..                           [ 92%]
tests/test_calculator.py ..                        [100%]
===================== 13 passed in 0.12s =====================
```

---

## 🧰 Project Structure

```
simplecalc/
│
├── simplecalc/
│   ├── __init__.py
│   ├── __main__.py
│   ├── calculator.py
│   ├── parser.py
│   ├── evaluator.py
│   ├── formatter.py
│   ├── history.py
│   └── cli.py
│
└── tests/
    ├── test_parser.py
    ├── test_evaluator.py
    ├── test_formatter.py
    ├── test_history.py
    └── test_calculator.py
```

---

## ⚙️ Requirements

* Python 3.12+
* pytest ≥ 7.0

---

## 🧑‍💻 Author

**Jo Hojin**
Department of Computer Science
💼 GitHub: [@<YOUR_ID>](https://github.com/<YOUR_ID>)

---

## 📄 License

This project is released under the MIT License.
You are free to modify and distribute it for both personal and commercial use.

---

## 🌟 Acknowledgements

This project was developed as a practical example for **Software Engineering** coursework — demonstrating requirement analysis, UML modeling, modular design, and automated testing.
