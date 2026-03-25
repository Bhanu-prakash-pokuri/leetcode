class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n = {} 

        for num in nums2:
            while stack and stack[-1] < num:
                n[stack.pop()] = num
            stack.append(num)
            
        for num in stack:
            n[num] = -1

        return [n[num] for num in nums1]


                    
        