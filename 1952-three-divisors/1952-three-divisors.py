class Solution:
    def isThree(self, n: int) -> bool:
        divisors = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i**2 == n:
                    divisors += 1
                else:
                    divisors += 2
        if divisors != 3:
            return False
        return True