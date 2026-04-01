class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=0
        b=0
        while b<len(nums) and a<len(nums):
            if a==b:
                b+=1
            elif nums[a]==nums[b]:
                nums.pop(b)
                
            else:
                a+=1
        return len(nums)
        