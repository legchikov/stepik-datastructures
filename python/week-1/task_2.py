# Task 2

def height_tree(num, seq):
    i = 0
    while num:
        print(seq[i])
        num -= 1
        i += 1

arr = [1, 2, 3, 4, 5, 6, 7]
height_tree(3, arr)
