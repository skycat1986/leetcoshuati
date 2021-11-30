#原地算法解决问题
from typing import List

#可以通过，有些测试用例还可以优化

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nchuli=0 #新标
        while k != 0:
            print("pre",nums)
            # 循环组对换
            xunhuancishu=int((len(nums)-nchuli)/k-1)
            print("xunhuancishu",xunhuancishu)
            for i in range(xunhuancishu):
                print("jinru xunhuancishu")
                b=nchuli+i*k
                for ik in range(k):
                    nums[b + ik], nums[-k + ik] = nums[-k + ik], nums[b + ik]

            nchuli+=xunhuancishu*k

            moshu=(len(nums)-nchuli)%k
            print("moshu",moshu)
            if moshu!=0:
                b=nchuli
                for i1 in range(moshu):
                    nums[b+i1],nums[b+moshu+i1]=nums[b+moshu+i1],nums[b+i1]

            nchuli+=moshu
            k=(k-moshu)%k

            print("post",nums)

        print(nums)

s=Solution()
lista=[1,2,3,4,5,6,7]
lista=[-100,-1,3,99]
s.rotate(lista,3)













