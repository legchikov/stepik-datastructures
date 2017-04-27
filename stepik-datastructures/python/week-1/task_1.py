# Task 1

def check_brackets(seq):
    l = str(len(seq))
    arr = []
    for x in seq:

        #print(arr)
        if x in '([{':
        #    print('append()')
            arr.append(x)
        if x in ')]}':
        #    print('pop()')
            last = arr.pop()
            #print(last)

            if x == ')':
                if last != '(':
                    return l
            if x == ']':
                if last != '[':
                    return l
            if x == '}':
                if last != '{':
                    return l

    return 'Success'
