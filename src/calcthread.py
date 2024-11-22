from threading import Thread
from math import pow

class CalcThread(Thread):
    def __init__(self, i, terms, barrier):
        super().__init__()
        self.i = i
        self.terms = terms
        self.barrier = barrier

    def run(self):
        term = 4 * pow(-1, self.i) / (2 * self.i + 1)
        self.terms.append(term)
        self.barrier.wait()