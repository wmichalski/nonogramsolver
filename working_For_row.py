width_max = 10
width = [None] * (width_max+1)

row = [2, 4]


def recursion(no, it):
    try:
        row[no]
    except IndexError:
        try:
            width[it] = 0
        except IndexError:
            pass
        print(width[1:])
        #print("^bo probowalismy do 3")
        return

    try:
        width[it] = 0
    except IndexError:
        #print(width[1:])
        return
    it += 1
    recursion(no, it)

    for i in range(row[no]):
        try:
            width[it] = 1
        except IndexError:
            return
        it += 1
    recursion(no+1, it)



recursion(0, 0)