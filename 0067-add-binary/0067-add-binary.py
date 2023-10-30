class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = f'0b{a}'
        b = f'0b{b}'
        
        sum_ = int(a, 2) + int(b, 2)
        sum_ = str(bin(sum_)[2:])

        return sum_