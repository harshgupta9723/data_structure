matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target = 13

def check_element(target, matrix):
    each_len = len(matrix[0])-1

    for i in range(len(matrix)):
        if target <= matrix[i][each_len]:
            if target in matrix[i]:
                return True
            else:
                return False
