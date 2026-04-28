class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while not s[l].isalpha() and not s[l].isdigit() and l < len(s) - 1:
                l += 1
            while not s[r].isalpha() and not s[r].isdigit() and r > 0:
                r -= 1
             
            if l >= r:
                break
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True