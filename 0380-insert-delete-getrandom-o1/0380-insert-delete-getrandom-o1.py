import random

class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.hashMap[val] = True
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        del self.hashMap[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(list(self.hashMap.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()