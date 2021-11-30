class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if i % 2 == 1:
                if nums[i] != nums[i - 1]:
                    return nums[i - 1]
        return nums[-1]
