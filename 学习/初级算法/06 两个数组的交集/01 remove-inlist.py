class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            lnums = nums1
            bnums = nums2
        else:
            lnums = nums2
            bnums = nums1
        nnums = []
        for num in lnums:
            if num in bnums:
                nnums.append(num)
                bnums.remove(num)

        return nnums



