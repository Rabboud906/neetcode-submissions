class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for row in board:
            seen_rows = set()

            for element in row:
                if element == ".":
                    continue

                if element in seen_rows:
                    return False

                seen_rows.add(element)


        # check columns
        for i in range(9):
            seen_columns = set()

            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] in seen_columns:
                    return False

                seen_columns.add(board[j][i])


        # check 3 x 3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):

                box = set()

                for k in range(i, i + 3):
                    for l in range(j, j + 3):

                        if board[k][l] == ".":
                            continue

                        if board[k][l] in box:
                            return False

                        box.add(board[k][l])

        return True

