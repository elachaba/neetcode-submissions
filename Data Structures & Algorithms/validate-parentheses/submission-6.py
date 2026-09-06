class Solution:
    def isValid(self, s: str) -> bool:
        hashSet = {'{' : '}', '[' : ']', '(' : ')'}
        stack = []
        for elt in s:
            if elt in hashSet:
                stack.append(hashSet[elt])
            else:
                if not stack or stack[-1] != elt:
                    return False
                else:
                    stack.pop()
        
        return not stack