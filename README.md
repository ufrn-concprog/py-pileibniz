# Concurrent Calculation of the Leibniz Series using Barriers in Python

This project calculates an approximation of π using the [Leibniz infinite
series](https://en.wikipedia.org/wiki/Leibniz_formula_for_pi):

$$\pi = 4 \sum_{i=0}^{\infty} \frac{(-1)^i}{2i + 1}$$

It demonstrates coordinating one worker thread per term with Python's
[`threading.Barrier`](https://docs.python.org/3/library/threading.html#barrier-objects). The final worker to reach the barrier triggers a completion action that sums and prints the calculated terms.

## 📂 Repository structure

```text
py-pileibniz/
├── main.py                 # Main entry point; starts and joins worker threads
└── src/
    ├── calc_thread.py      # Worker thread that computes one series term
    └── sum_aggregator.py   # Barrier completion action that sums the terms
```

🚀 Getting Started

✅ Prerequisites

Python 3 is required. The program uses only the Python standard library.

▶️ Running

From the repository root:

```bash
python3 main.py
```

Enter the number of terms when prompted. For example:

```text
Enter the precision (number of terms): 4000
Calculating the value of pi with 4000 terms...
3.1413426535936995
1003.8097081705928 milliseconds
```

### ⚠️ Caveat

The program creates one operating system thread per term. Requesting a very
large number of terms can exhaust available thread resources.

## 📝 Generate Documentation

The source modules include docstrings that can be rendered with [`pdoc`](https://pdoc.dev/). Install `pdoc` and generate HTML documentation from the repository root:

```bash
python3 -m pip install pdoc
python3 -m pdoc -o doc src.calc_thread src.sum_aggregator main
```

To serve the documentation locally instead of writing HTML files:

```bash
python3 -m pdoc src.calc_thread src.sum_aggregator main
```
