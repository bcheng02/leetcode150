import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validValues = ['1', '2', '3', '4', '5','6', '7', '8', '9']
        subBoxes = {i:[] for i in range(len(board))}

        for i, row in enumerate(board):
            filteredRow = [val for val in row if val != "." and val in validValues]
            if  len(filteredRow) != len(set(filteredRow)):
                return False

            col = []
            for j in range(len(row)):
                col.append(board[j][i])
                boxNum = 3 * math.floor(i/3) + math.floor(j/3)
                subBoxes[boxNum].append(board[j][i]) 
            filteredCol = [val for val in col if val != "." and val in validValues]
            if  len(filteredCol) != len(set(filteredCol)):
                return False

        print(subBoxes)
        for box in subBoxes.values():
            filteredBox = [val for val in box if val != "." and val in validValues]
            if  len(filteredBox) != len(set(filteredBox)):
                return False


            
        return True