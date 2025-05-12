class StockSpanner:

    def __init__(self):
        self.prices = []       # Stores all prices seen so far
        self.stack = []        # Monotonic stack of indices of previous greater elements

    def next(self, price: int) -> int:
        index = len(self.prices)

        # Remove prices from stack that are less than or equal to current price
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()

        if not self.stack:
            span = index + 1   # No previous greater, span is full length
        else:
            span = index - self.stack[-1]  # Span is distance from previous greater

        self.prices.append(price)
        self.stack.append(index)
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)