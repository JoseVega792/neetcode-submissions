class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordering = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in ordering:
                ordering[key] = []
            ordering[key].append(s)
        return ordering.values()