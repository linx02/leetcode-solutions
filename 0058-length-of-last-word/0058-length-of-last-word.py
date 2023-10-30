class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ''
        for char in s.strip()[::-1]:
            if char == ' ':
                break
            word += char
        return len(word)