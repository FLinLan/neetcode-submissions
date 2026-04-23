class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(list)
        col_set = defaultdict(list)
        subgrid_set = defaultdict(list)

        # have a dict of list for each row
        # have a dict of list for each col
        # each subgrid
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                row_set[r].append(board[r][c])
                col_set[c].append(board[r][c])
                subgrid_set[(r//3, c//3)].append(board[r][c])
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (len(row_set[r]) != len(set(row_set[r])) or
                    len(col_set[c]) != len(set(col_set[c])) or
                    len(subgrid_set[(r//3, c//3)]) != len(set(subgrid_set[(r//3, c//3)]))):
                    return False

        print(row_set)
        print(col_set)
        print(subgrid_set)
        return True
                