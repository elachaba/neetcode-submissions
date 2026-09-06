class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for i in range(9):
                val = board[r][i]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        for c in range(9):
            seen = set()
            for i in range(9):
                val = board[i][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (box // 3) * 3 + i
                    c = (box % 3) * 3 + j
                    val = board[r][c]
                    if val  == ".":
                        continue
                    if val in seen:
                        return False
                    seen.add(val)
        

        return True
