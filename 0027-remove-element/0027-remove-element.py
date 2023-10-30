class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def remove(nums, val):
            if val in nums:
                del nums[nums.index(val)]
                remove(nums, val)
        remove(nums, val)