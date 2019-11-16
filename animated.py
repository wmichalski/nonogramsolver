import time

# SIZE OF THE NONOGRAM
w, h = 20, 20

matrix = [[0 for x in range(w+1)] for y in range(h+1)] 
guaranteed = [[None for x in range(w+1)] for y in range(h+1)] 
to_be_guaranteed = [0 for x in range(max(w,h)+1)]

tbg_iter = 0

# http://www.nonograms.org/nonograms/i/16326
# numbers_row = [[],[2],[2,1],[4],[1,1],[1,1]]
# numbers_col = [[],[4],[2],[3],[3],[1]]

# 7,6
# numbers_row = [[],[3],[1,1],[6],[5,1],[6],[3]]
# numbers_col = [[],[4],[1,4],[1,4],[1,4],[4],[1,1],[1]]

# 20, 20
# https://www.nonograms.org/nonograms/i/26044
numbers_row=[[],[1,3],[3,6],[4,8],[1,4,9],[1,6,6,1],[1,6,4],[3,5,4],[5,5,4],[3,8,4],[1,3,6,5],[4,7,4],[3,7,5],[13],[14],[14],[13],[11],[9],[9],[8]]
numbers_col=[[],[2,3],[3,1],[6,1],[2,3,2],[3,5,2],[1,2,1,4,2],[19],[19],[20],[17],[13],[2,11],[6,8],[9,6],[18],[17],[5,8],[3,7],[3,4],[3]]

# 15, 15
# http://www.nonograms.org/nonograms/i/8341
# numbers_row = [[],[5],[1,5],[3,1],[2,2],[3,3],[5,4],[2,4,2],[1,1,2],[1,4,1],[4,7],[4,2,2],[2,2,2,1],[1,1,1,1],[1,1,1,1],[1,1,1]]
# numbers_col = [[],[1,3],[2,2,1],[1,5],[3,2],[1,4],[1,1,3,3],[1,1,1,1],[1,2,2],[1,1,1,3],[1,1,1,3,1],[3,2,2],[5,1],[1,7],[2,4,2,1],[1,3]]

def recursion_row(no, it, row):
    # check if no is higher than the amount of numbers for this row..
    # .. so we don't keep recursing if we already placed all numbers on the board
    try:
        numbers_row[row][no]
    except IndexError:
        # if all numbers are already placed, we replace the past-the-end cell with 0..
        # .. to overwrite possible leftovers from previous iteration
        try:
            matrix[row][it] = 0
        except IndexError:
            pass
        # if this combination fits our solution so far, we are going to compare it to other combinations
        if do_they_match_row(row):
            add_tbg_row(row)
        return

    # we put a 0 and recurse again
    try:
        matrix[row][it] = 0
    except IndexError:
        return
    it += 1
    recursion_row(no, it, row)

    # if we cant put 0's any more, we try to fit out number in
    for i in range(numbers_row[row][no]):
        # if we can't fit the number, then we go back with our recursion:
        try:
            matrix[row][it] = 1
        except IndexError:
            return
        it += 1
    recursion_row(no+1, it, row) # after inserting the whole number, we repeat the process for the next one

def do_they_match_row(row):
    for i in range(w+1):
        if guaranteed[row][i] is not None:
            if guaranteed[row][i] is not matrix[row][i]:
                return 0
    return 1

def add_tbg_row(row):
    # tbg_iter counts how many combinations, fitting the partial solution, exist
    global tbg_iter
    tbg_iter += 1
    for i in range(w+1):
        to_be_guaranteed[i] += matrix[row][i]

# copypaste for columns
def recursion_col(no, it, col):
    # check if no is higher than the amount of numbers for this row..
    # ..so we don't keep recursing if we already placed all numbers on the board
    try:
        numbers_col[col][no]
    except IndexError:
        # if all numbers are already placed, we replace the past-the-end cell with 0..
        # .. to overwrite possible leftovers from previous iteration
        try:
            matrix[it][col] = 0
        except IndexError:
            pass
        # if this combination fits our solution so far, we are going to compare it to other combinations
        if do_they_match_col(col):
            add_tbg_col(col)
        return

    # we put a 0 and recurse again
    try:
        matrix[it][col] = 0
    except IndexError:
        return
    it += 1
    recursion_col(no, it, col)

    # if we cant put 0's any more, we try to fit out number in
    for i in range(numbers_col[col][no]):
        # if we can't fit the number, then we go back with our recursion:
        try:
            matrix[it][col] = 1
        except IndexError:
            return
        it += 1
    recursion_col(no+1, it, col) # after inserting the whole number, we repeat the process for the next one

def do_they_match_col(col):
    for i in range(h+1):
        if guaranteed[i][col] is not None:
            if guaranteed[i][col] is not matrix[i][col]:
                return 0
    return 1

def add_tbg_col(col):
    # tbg_iter counts how many combinations, fitting the partial solution, exist
    global tbg_iter
    tbg_iter += 1
    for i in range(h+1):
        to_be_guaranteed[i] += matrix[i][col]

def printN():
    time.sleep(0.1)
    for h1 in range(1,h+1):
        for w1 in range(1,w+1):
            if guaranteed[h1][w1] == 1:
                print('░', end='')
            elif guaranteed[h1][w1] == 0:
                print('█', end='')
            else:
                print('?', end='')    

        print('')
    print('----')

# MAIN LOOP

while(1):
    # ROW LOOP
    for row in range(1,h+1):
        recursion_row(0, 0, row)
        hasGuaranteedChanged = 0
        for i in range(1,w+1):
            # the following happens if in every single fitting combination a specific cell had a value of "1"
            if (to_be_guaranteed[i] == tbg_iter):
                if guaranteed[row][i] == None:
                    hasGuaranteedChanged = 1
                guaranteed[row][i] = 1
            # the following happens if in every single fitting combination a specific cell had a value of "0"
            if (to_be_guaranteed[i] == 0):
                if guaranteed[row][i] == None:
                    hasGuaranteedChanged = 1
                guaranteed[row][i] = 0

        # clearing stuff before next iteration:
        tbg_iter = 0
        for i in range(0, len(to_be_guaranteed)):
            to_be_guaranteed[i] = 0
        # ^^^
        if hasGuaranteedChanged == 1:
            printN()

    # COL LOOP
    for col in range(1,w+1):
        recursion_col(0, 0, col)
        hasGuaranteedChanged = 0
        for i in range(1,h+1):
            # the following happens if in every single fitting combination a specific cell had a value of "1"
            if (to_be_guaranteed[i] == tbg_iter):
                if guaranteed[i][col] == None:
                    hasGuaranteedChanged = 1
                guaranteed[i][col] = 1
            # the following happens if in every single fitting combination a specific cell had a value of "0"
            if (to_be_guaranteed[i] == 0):
                if guaranteed[i][col] == None:
                    hasGuaranteedChanged = 1
                guaranteed[i][col] = 0

        # clearing stuff:
        tbg_iter = 0
        for i in range(0, len(to_be_guaranteed)):
            to_be_guaranteed[i] = 0
        # ^^^
        if hasGuaranteedChanged == 1:
            printN()

    # if there is at least 1 cell that is not confirmed, we loop again
    isBreak = 1
    for h1 in range(1,h+1):
        for w1 in range(1,w+1):
            if guaranteed[h1][w1] is None:
                isBreak = 0
    if isBreak:
        break

printN()
    
