class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        for i in range(len(nums)):
            try:
                idx = nums.index(target - nums[i], i + 1)
                return [i, idx]
            except:
                continue

