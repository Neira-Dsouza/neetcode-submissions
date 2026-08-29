class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]==".":
                    continue
                num=board[i][j]
                
                if num in row[i]:
                    return False
                row[i].add(num)
                if num in col[j]:
                    return False
                col[j].add(num)
                boxs=(i//3)*3+(j//3)
                if num in box[boxs]:
                    return False
                box[boxs].add(num)
        return True