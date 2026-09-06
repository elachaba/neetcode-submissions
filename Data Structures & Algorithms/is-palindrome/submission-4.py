class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(char):
            return ord("a") <= ord(char) <= ord("z") \
            or ord("A") <= ord(char) <= ord("Z") \
            or ord("0") <= ord(char) <= ord("9")
        
        if len(s) < 2:
            return True
        i, j = 0, len(s) - 1

        while i < j:
            if not isAlphanumeric(s[i]):
                i += 1
                continue
            if not isAlphanumeric(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True