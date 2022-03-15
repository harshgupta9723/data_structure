board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

def check_list(test_list):
        
    res = [i for i in test_list if i != '.']
    
    if len(res) == len(set(res)):
        return True
    else:
        return False
        
# single box
def get_single_box(a,b):
    sq_board = []

    for i in range(a,a+3):
        for j in range(b,b+3):
            sq_board.append(board[i][j])

    return sq_board

def isValidSudoku(board):
    # verifier
    for j in range(9):
        
        row = board[j]
        #check row
        
        if check_list(row) == False:
            return 'false'
        
        column = []
        for i in range(9):
            column.append(board[i][j])
            
        #check column
        if check_list(column) == False:
            return 'false'
        
    samp_list = [0, 3, 6]
    for i in samp_list:
        for j in samp_list:
            square_box = get_single_box(i, j)
            
            if check_list(square_box) == False:
                return 'false'
            
    return 'true'

x = isValidSudoku(board)
print(x)