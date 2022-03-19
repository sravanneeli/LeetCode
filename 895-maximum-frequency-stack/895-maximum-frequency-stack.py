class FreqStack:

    def __init__(self):
        self.freq_dict = {}
        self.stck = []
        

    def push(self, val: int) -> None:
        self.freq_dict[val] = self.freq_dict.get(val, 0) + 1
        self.stck.append(val)

    def pop(self) -> int:
        max_freq = max(self.freq_dict.values())
        popped_values = []
        ans = None
        while True:
            # print(max_freq, self.stck)
            pop_value = self.stck.pop()
            if self.freq_dict[pop_value] == max_freq:
                self.freq_dict[pop_value] -= 1
                ans = pop_value
                break
            else:
                popped_values.append(pop_value)
        self.stck.extend(popped_values[::-1])
        
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()