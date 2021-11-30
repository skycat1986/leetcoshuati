#原地算法解决问题
from typing import List

#可以通过，更加耗时了

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        if k != 0:
            # 循环组对换
            xunhuancishu=int(len(nums)/k-1)

            for i in range(xunhuancishu):
                b=i*k
                for ik in range(k):
                    nums[b + ik], nums[-k + ik] = nums[-k + ik], nums[b + ik]

            print("moshuqian   ",nums)
            moshu = len(nums) % k
            print("moshu",moshu)
            if moshu!=0:
                for im in range(moshu):
                    nums[xunhuancishu*k+im],nums[xunhuancishu*k+im+moshu]=nums[xunhuancishu*k+im+moshu],nums[xunhuancishu*k+im]
                newl=nums[xunhuancishu*k+moshu:len(nums)]
                self.rotate(newl,k-moshu)
                print("newl",newl)
                for i1 in range(len(newl)):
                    nums[xunhuancishu * k + moshu+i1]=newl[i1]

        print(nums)


s=Solution()
lista=[1,2,3,4,5,6,7]
s.rotate(lista,3)













