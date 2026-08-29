class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT= {}, {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False

        return True

        if sorted(s) == sorted(t) and len(s) == len(t):
            return True
        else:
            return False