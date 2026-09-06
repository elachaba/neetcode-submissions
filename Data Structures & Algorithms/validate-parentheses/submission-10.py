class Solution:
    def isValid(self, s: str) -> bool:
        combos = {
            '{':'}',
            '(': ')',
            '[': ']',
        }

        stack = []
        for c in s:
            if c in combos:
                stack.append(c)
            elif c in combos.values():
                if not stack or c != combos[stack.pop()]:
                    return False
        
        return True if not stack else False