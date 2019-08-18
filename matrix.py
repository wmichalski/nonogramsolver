w, h = 10, 2

matrix = [[None for x in range(w+1)] for y in range(h+1)] 

numbers = [3, 4]


def recursion(no, it, row):
    try:
        numbers[no]
    except IndexError:
        try:
            matrix[row][it] = 0
        except IndexError:
            pass
        print(matrix[row][1:])
        #print("^bo probowalismy do 3")
        return

    try:
        matrix[row][it] = 0
    except IndexError:
        #print(width[1:])
        return
    it += 1
    recursion(no, it, row)

    for i in range(numbers[no]):
        try:
            matrix[row][it] = 1
        except IndexError:
            return
        it += 1
    recursion(no+1, it, row)



recursion(0, 0, 1)