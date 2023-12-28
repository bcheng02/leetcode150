class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows OK
        # check cols OK
        # check box ??
        
    
    
    
        # collect cols into arrOfCols
        # list comprehension needed?? YES!
        arrOfCols = [["."] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                arrOfCols[i][j] = board[j][i]
                

        # check no duplicates and 1-9 per row
        for i in range(9):
            arrOfNums = list(filter(lambda x: x.isnumeric() and int(x) >= 1 and int(x) <= 9 , board[i]))
            if (len(set(arrOfNums)) != len(arrOfNums)):
                return False

        # check no duplicates and 1-9 per col
        for i in range(9):
            arrOfNums = list( filter(lambda x: x.isnumeric() and int(x) >= 1 and int(x) <= 9 , arrOfCols[i]) )
            if (len(set(arrOfNums)) != len(arrOfNums)):
                return False
            
        
        # check 9 boxes?? this is STUPID
        box1 = ["."] * 9
        k = 0
        for i in range(0, 3):
            for j in range(0, 3):
                box1[k] = board[i][j]
                k+=1
                

        k = 0
        box2 = ["."] * 9
        for i in range(3, 6):
            for j in range(0, 3):
                box2[k] = board[j][i]
                k+=1

                
        k = 0        
        box3 = ["."] * 9
        for i in range(6, 9):
            for j in range(0, 3):
                box3[k] = board[j][i]
                k+=1
 
                
        k = 0        
        box4 = ["."] * 9
        for i in range(0, 3):
            for j in range(3, 6):
                box4[k] = board[j][i]
                k+=1

        
        k = 0
        box5 = ["."] * 9
        for i in range(3, 6):
            for j in range(3, 6):
                box5[k] = board[j][i]
                k+=1
        
        k = 0
        box6 = ["."] * 9
        for i in range(6, 9):
            for j in range(3, 6):
                box6[k] = board[j][i]
                k+=1
        
        k = 0
        box7 = ["."] * 9
        for i in range(0, 3):
            for j in range(6, 9):
                box7[k] = board[j][i]
                k+=1
                
        k = 0
        box8 = ["."] * 9
        for i in range(3, 6):
            for j in range(6, 9):
                box8[k] = board[j][i]
                k+=1
        
        k = 0
        box9 = ["."] * 9
        for i in range(6, 9):
            for j in range(6, 9):
                box9[k] = board[j][i]
                k+=1


        arrOfBoxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
        
        print(arrOfBoxes)
        
        for i in range(9):
            arrOfNums = list( filter(lambda x: x.isnumeric() and int(x) >= 1 and int(x) <= 9 , arrOfBoxes[i]) )
            if (len(set(arrOfNums)) != len(arrOfNums)):
                return False
            
        return True
        
        
    