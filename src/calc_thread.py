from threading import Barrier, Thread

class CalcThread(Thread):
    """Compute one Leibniz-series term and wait for the other workers.

    Attributes:
        index: Index of the term to compute.
        terms: Shared list in which this worker stores its term.
        barrier: Synchronization barrier shared by all worker threads.
    """

    def __init__(self, index: int, terms: list[float], barrier: Barrier):
        """Initialize a worker for one term.

        Args:
            index: Index of the Leibniz series term.
            terms: Shared list that receives the calculated term at ``index``.
            barrier: Barrier that this worker waits at after calculating.
        """
        super().__init__()
        self.index = index
        self.terms = terms
        self.barrier = barrier

    def run(self):
        """Compute the Leibniz series term and wait for the other workers."""
        term = 4 * (-1) ** self.index / (2 * self.index + 1)
        self.terms[self.index] = term
        self.barrier.wait()
