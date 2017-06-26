# Task 1

def check_brackets(seq):
    arr = []
    count = 0
    for count, x in enumerate(seq):
        if x in '([{':
            arr.append(x)
        if x in ')]}':
            if arr:
                last = arr.pop()
                if x == ')':
                    if last != '(':
                        return str(count+1)
                if x == ']':
                    if last != '[':
                        return str(count+1)
                if x == '}':
                    if last != '{':
                        return str(count+1)
            else:
                return str(count+1)
    if arr:
        return str(count+1)

    return 'Success'
