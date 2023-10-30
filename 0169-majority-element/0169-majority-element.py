class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = list(set(nums))

        unique_counts = []

        for val in unique:
            temp = []
            for num in nums:
                if num == val:
                    temp.append(num)
            unique_counts.append(temp)
        
        for list_ in unique_counts:
            if len(list_) > (len(nums) / 2):
                return list_[0]