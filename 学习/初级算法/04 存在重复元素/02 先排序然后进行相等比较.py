class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 遍历元素，存放在map内，如果存在则返回true
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False


