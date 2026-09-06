class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                elt = board[r][c]
                if elt == ".":
                    continue
                if (elt in rows[r]
                    or elt in cols[c]
                    or elt in squares[(r // 3, c // 3)]):
                    return False
                
                cols[c].add(elt)
                rows[r].add(elt)
                squares[(r // 3, c // 3)].add(elt)
        
        return True