class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        if len(nums) % 2 == 0:
            index1 = int(len(nums) / 2 - 1)
            index2 = int(len(nums) / 2)
            return (nums[index1] + nums[index2]) / 2
        else:
            index = math.floor(len(nums) / 2)
            print(index)
            return nums[index]