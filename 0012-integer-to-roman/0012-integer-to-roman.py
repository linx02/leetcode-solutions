class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        reversed_dict = {key: value for key, value in reversed(symbols.items())}

        string = []
        while not num == 0:
            for k, v in reversed_dict.items():
                if v <= num:
                    string.append(k)
                    num -= v
                    break
        
        return ''.join(string)