class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=nums1+nums2
        m.sort()
        l=len(m)
        if l%2==1:
            return m[l//2]
        m1=m[l//2-1]
        m2=m[l//2]
        return (m1+m2)/2.0
        