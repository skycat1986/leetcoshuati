class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        index = 0  # 重新赋值下标
        lastnum = nums[0]  # 迭代的最后一个数值
        for i in range(len(nums)):
            if nums[i] != lastnum:
                index = index + 1
                nums[index] = nums[i]
                lastnum = nums[i]

        return index + 1