class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            arranged = ''.join(sorted(s))
            if arranged not in anagrams:
                anagrams[arranged] = []
            anagrams[arranged].append(s)
        return list(anagrams.values())