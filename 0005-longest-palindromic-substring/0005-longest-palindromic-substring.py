class Solution:
    def longestPalindrome(self, s: str) -> str:

        substrings =[s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        cleaned = [string for string in substrings if string[0] == string[-1]]
        palindromic = [string for string in cleaned if string[::-1] == string]
        
        if palindromic: return max(palindromic, key=len)