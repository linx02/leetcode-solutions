class Solution:
    def romanToInt(self, s: str) -> int:
        """
        roman nums: dict
        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """

        roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sub_instances = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        instances = []
        for instance in sub_instances.keys():
            if instance in s:
                instances.append(sub_instances[instance])
                s = s.replace(instance, '')

        nums = [roman_nums[roman] for roman in s]

        return sum(nums) + sum(instances)