class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "$" + s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        output = []
        sep = "$"
        i = 0
        while i < len(s):
            j = i
            length = ""
            while s[j] != sep and j < len(s):
                length += s[j]
                j += 1
            length = int(length)
            if j < len(s) - 1:
                output.append(s[j + 1: j + length + 1])
            else:
                output.append("")
            i = j + length + 1
        
        return output
