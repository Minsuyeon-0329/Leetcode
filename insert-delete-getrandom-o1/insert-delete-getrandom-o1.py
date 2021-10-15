class RandomizedSet:

    def __init__(self):
        self.hash={}
        self.list=[]

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.hash[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.hash:
            last_element, idx = self.list[-1], self.hash[val]
            self.list[idx], self.hash[last_element] = last_element, idx
            self.list.pop()
            del self.hash[val]
            
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()