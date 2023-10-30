class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(num) for num in digits]
        digits = ''.join(digits)
        digits = str(int(digits) + 1)
        digits = [char for char in digits]
        digits = (int(char) for char in digits)

        return digits