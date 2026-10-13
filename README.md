# Concurrent Calculation of the Leibniz Series using Barriers in Python

This project calculates an approximation of π using the [Leibniz infinite
series](https://en.wikipedia.org/wiki/Leibniz_formula_for_pi):

$$\pi = 4 \sum_{i=0}^{\infty} \frac{(-1)^i}{2i + 1}$$

It demonstrates coordinating one worker thread per term with Python's
[`threading.Barrier`](https://docs.python.org/3/library/threading.html#barrier-objects). The final worker to reach the barrier triggers a completion action that sums and prints the calculated terms.

## 📃 About

A **barrier** is a synchronization mechanism that causes multiple threads to wait at a designated synchronization point until a specified number of threads have arrived.

### Execution Workflow

1. **Decomposition and thread spawning**: The user inputs the number of terms (`precision`) to calculate . An independent worker thread ([`CalcThread`](src/calc_thread.py)) is spawned for each term $i \in [0, \text{precision}-1]$.
2. **Partial term calculation**: Each thread computes its $i$-th term:

   $$term_i = 4 \cdot \frac{(-1)^i}{2i + 1}$$

3. **Shared storage**: The computed partial term is stored into a shared list.
4. **Waiting at the barrier**: After appending its value, each [`CalcThread`](src/calc_thread.py) calls `barrier.wait()`, suspending execution until all other worker threads finish their computations.
5. **Barrier action execution**: When the last thread calls `wait()`, the barrier automatically triggers a [`SumAggregator`](src/sum_aggregator.py) object before releasing the threads.
6. **Result aggregation**: [`SumAggregator`](src/sum_aggregator.py) sums all partial values stored in the list and outputs the computed approximation of $\pi$.

## 📂 Repository structure

```text
py-pileibniz/
└── doc/                    # Generated HTML documentation
├── main.py                 # Main entry point; starts and joins worker threads
└── README.md
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
