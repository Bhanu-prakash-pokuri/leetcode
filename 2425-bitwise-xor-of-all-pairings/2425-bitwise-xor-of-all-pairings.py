class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x1=0
        x2=0
        if len(nums1)%2!=0:
            for i in nums2:
                x2 ^= i
        if len(nums2)%2!=0:
            for i in nums1:
                x1 ^= i
        return x1^x2
        