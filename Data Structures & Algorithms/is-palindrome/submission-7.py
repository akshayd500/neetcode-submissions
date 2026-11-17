class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1

        while l<r:
            if (s[l].isalnum() is not True):
                l += 1
                continue
            if (s[r].isalnum() is not True):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True

        