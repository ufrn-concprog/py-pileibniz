from threading import Barrier, Thread
from time import perf_counter

from src.calc_thread import CalcThread
from src.sum_aggregator import SumAggregator

def main():
    precision = int(input("Enter the precision (number of terms): "))

    terms = [0.0] * precision
    barrier = Barrier(precision, action=SumAggregator(terms))
    threads = []

    print("Calculating the value of pi with", precision, "terms...")
    start = perf_counter()

    for i in range(precision):
        thread = CalcThread(i, terms, barrier)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    elapsed_milliseconds = (perf_counter() - start) * 1000
    print(elapsed_milliseconds, "milliseconds")


if __name__ == "__main__":
    main()
