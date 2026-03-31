class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can=None
        c=0
        for num in nums:
            if c==0:
                can=num
            if can==num:
                c+=1
            else:
                c-=1
        return can

        