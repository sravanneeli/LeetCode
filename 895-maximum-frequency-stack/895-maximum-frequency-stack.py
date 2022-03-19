class FreqStack:

    def __init__(self):
        self.freq_dict = {}
        self.group = collections.defaultdict(list)
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.freq_dict[val] = self.freq_dict.get(val, 0) + 1
        if self.freq_dict[val] > self.max_freq:
            self.max_freq = self.freq_dict[val]
        
        self.group[self.freq_dict[val]].append(val)

    def pop(self) -> int:
        # print(self.freq_dict, self.group, self.max_freq)
        x = self.group[self.max_freq].pop()
        self.freq_dict[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()