class Solution:
    def isValid(self, s: str) -> bool:
        """
        Last one to be opened must be first one to be closed
        """
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        temp = []

        for char in s:
            if len(s) < 2: return False
            if char in pairs.keys():
                temp.append(char)
            elif len(temp) > 0 and pairs[temp[-1]] == char:
                temp.pop()
            else:
                return False
        
        return len(temp) == 0