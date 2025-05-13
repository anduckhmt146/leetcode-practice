from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)          # val -> freq
        self.group = defaultdict(list)        # freq -> list (stack of values)
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        self.group[f].append(val)

        if f > self.max_freq:
            self.max_freq = f

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val
