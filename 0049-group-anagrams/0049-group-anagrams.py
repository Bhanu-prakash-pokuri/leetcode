class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a = defaultdict(list)
        
        for w in strs:
            s = ''.join(sorted(w))
            a[s].append(w)
        
        return list(a.values())