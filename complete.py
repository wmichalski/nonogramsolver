w, h = 5, 5

matrix = [[None for x in range(w+1)] for y in range(h+1)] 
guaranteed = [[None for x in range(w+1)] for y in range(h+1)] 
to_be_guaranteed = [0 for x in range(max(w,h)+1)]

tbg_iter = 0

numbers_row = [[],[2],[2,1],[4],[1,1],[1,1]]
numbers_col = [[],[4],[2],[3],[3],[1]]


def recursion_row(no, it, row):
    # check if no is higher than the amount of numbers for this row..
    # ..so we don't keep recursing if we already placed all numbers on the board
    try:
        numbers_row[row][no]
    except IndexError:
        try:
            matrix[row][it] = 0
        except IndexError:
            pass
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
        try:
            matrix[it][col] = 0
        except IndexError:
            pass
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
    global tbg_iter
    tbg_iter += 1
    for i in range(h+1):
        to_be_guaranteed[i] += matrix[i][col]

def printN():
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
        for i in range(1,w+1):
            if (to_be_guaranteed[i] == tbg_iter):
                guaranteed[row][i] = 1
            if (to_be_guaranteed[i] == 0):
                guaranteed[row][i] = 0

        # clearing stuff:
        tbg_iter = 0
        for i in range(0, len(to_be_guaranteed)):
            to_be_guaranteed[i] = 0
        # ^^^
        printN()

    # COL LOOP
    for col in range(1,w+1):
        recursion_col(0, 0, col)
        for i in range(1,h+1):
            if (to_be_guaranteed[i] == tbg_iter):
                guaranteed[i][col] = 1
            if (to_be_guaranteed[i] == 0):
                guaranteed[i][col] = 0

        # clearing stuff:
        tbg_iter = 0
        for i in range(0, len(to_be_guaranteed)):
            to_be_guaranteed[i] = 0
        # ^^^
        printN()

    isBreak = 1
    for h1 in range(1,h+1):
        for w1 in range(1,w+1):
            if guaranteed[h1][w1] is None:
                isBreak = 0
    if isBreak:
        break

printN()
    
