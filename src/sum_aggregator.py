class SumAggregator:
    """Sum and print the terms when all workers reach the barrier."""

    def __init__(self, terms: list[float]):
        self.terms = terms

    def __call__(self):
        print(sum(self.terms))
