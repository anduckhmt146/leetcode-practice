import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}  # value -> index in list
        self.list = []  # stores values

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        # Index of element to remove
        idx = self.dict[val]
        last_val = self.list[-1]

        # Swap with last element
        self.list[idx] = last_val
        self.dict[last_val] = idx

        # Remove last element
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
