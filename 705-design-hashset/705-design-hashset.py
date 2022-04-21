class MyHashSet:

    def __init__(self):
        self.hash_dict = {}
        

    def add(self, key: int) -> None:
        self.hash_dict[key] = self.hash_dict.get(key, 0) + 1
        

    def remove(self, key: int) -> None:
        if self.hash_dict.get(key) is not None:
            self.hash_dict.pop(key)
        

    def contains(self, key: int) -> bool:
        if self.hash_dict.get(key) is not None:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)