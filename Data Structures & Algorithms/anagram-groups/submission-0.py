class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            curr = ''.join(sorted(s))
            if curr not in anagrams:
                anagrams[curr] = []
            anagrams[curr].append(s)
        return list(anagrams.values())