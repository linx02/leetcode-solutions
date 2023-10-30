class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y = str(x)
            y = int(y[::-1])
            
            return x == y