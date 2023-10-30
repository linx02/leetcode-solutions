class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            for idx_, num_ in enumerate(nums):
                if idx == idx_:
                    continue
                else:
                    if num + num_ == target:
                        return [idx, idx_]