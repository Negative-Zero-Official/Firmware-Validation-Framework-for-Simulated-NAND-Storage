# NAND Firmware Validation Framework

This project simulates a simple NAND storage device and provides a Python-based validation framework for functional, edge-case, and stress testing. It's designed to demonstrate core skills required for a Firmware Validation Engineer role, such as test strategy design, automation, and debugging.

---

## 📦 Project Structure

```
nand_firmware_validation/
├── nand_simulator.py         # Simulates basic NAND behavior
├── test_cases/
│   ├── test_functional.py    # Functional tests (write, read, erase)
│   ├── test_edge_cases.py    # Bad blocks, write-before-erase, etc.
│   ├── test_stress.py        # Stress and regression tests
├── run_tests.py              # Runs all tests, logs results, generates summary
├── logs/
│   └── test_log.txt          # Test execution logs
├── report/
│   └── test_summary.md       # Markdown test summary
└── README.md                 # You are here
```

---

## 🚀 How to Run

1. Install Python 3.8+.
2. Clone the repository or copy the files into a folder.
3. Run the test suite:

```bash
python run_tests.py
```

Test logs will appear in `logs/test_log.txt`, and a summary report will be written to `report/test_summary.md`.

---

## 🧠 What It Does

- Simulates NAND operations: `read_page`, `write_page`, `erase_block`
- Enforces NAND rules: no overwrite before erase, bad block handling
- Provides unittest-based test scripts for:
  - Functional correctness
  - Edge-case handling (like writing to bad blocks)
  - Stress and regression testing
- Uses Python logging to track actions and debug failures

---

## 💡 Why It Matters

This project demonstrates:

- Firmware-aware testing logic (grey-box + black-box strategies)
- Low-level simulation of NAND-like constraints
- Python automation and structured test reporting
- Readable, maintainable validation code with logging and summaries

---

## 🧰 Technologies Used

- Python 3
- `unittest`
- `logging`
- Custom file-based simulation of NAND memory

---

## 🧭 Next Steps

- Simulate ECC and retry logic
- Add power-failure recovery simulation
- Integrate with pytest for more powerful testing
- Implement real bad block table (BBT) simulation
- Add GUI or CLI to trigger specific test suites