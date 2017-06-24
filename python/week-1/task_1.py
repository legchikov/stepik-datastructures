# Task 1

def check_brackets(seq):
    arr = []
    count = 0
    for x in seq:
        count += 1
        if x in '([{':
            arr.append(x)
        if x in ')]}':
            last = arr.pop()
            if x == ')':
                if last != '(':
                    return str(count)
            if x == ']':
                if last != '[':
                    return str(count)
            if x == '}':
                if last != '{':
                    return str(count)
    if len(arr) > 0:
        return str(count)

    return 'Success'
