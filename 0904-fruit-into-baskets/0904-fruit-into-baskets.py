from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        max_len=0
        
        arr=defaultdict(int)
        for i in range(len(fruits)):
            arr[fruits[i]]+=1

            while len(arr)>2:
                arr[fruits[l]]-=1
                if arr[fruits[l]]==0:
                    del arr[fruits[l]]
                l+=1
            max_len=max(max_len,i-l+1)
        return max_len


            




        