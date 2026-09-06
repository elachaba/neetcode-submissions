class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(c):
            return c in "abcdeghijklmnopqrstuvw012345789"
        
        start = 0
        end = len(s) - 1
        s = s.lower()
        
        while start < end:
            if isAlphanumeric(s[start]) and isAlphanumeric(s[end]): 
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            else:
                if not isAlphanumeric(s[start]):
                    start += 1
                if not isAlphanumeric(s[end]):
                    end -= 1
        
        return True
        