class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bflag=False
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=0:
                bflag=True
            else:
                if bflag:
                    del nums[i]
                    nums.append(0)