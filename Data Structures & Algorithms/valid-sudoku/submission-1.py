class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(list)
        col_set = defaultdict(list)
        subgrid_set = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                num = board[r][c]
                
                if (num in row_set[r] or
                    num in col_set[c] or
                    num in subgrid_set[(r // 3, c // 3)]):
                    return False
                
                row_set[r].append(num)
                col_set[c].append(num)
                subgrid_set[(r // 3, c // 3)].append(num)

        return True