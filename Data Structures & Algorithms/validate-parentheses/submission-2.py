class Solution:
    def isValid(self, s: str) -> bool:
        freq = {'}':'{', ')': '(', ']':'['}
        stack = []
        for i in s:
            if i in '{[(':
                stack.append(i)
            elif i in '}])':
                if stack and stack[-1] == freq[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
