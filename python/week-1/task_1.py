# Task 1

def check_brackets(seq):
    stack = []
    error_stack = []

    for count, x in enumerate(seq, 1):
        if x in '([{':
            stack.append(x)
            error_stack.append(count)
        if x in ')]}':
            if stack:
                last = stack.pop()
                last_error = error_stack.pop()
                if x == ')':
                    if last != '(':
                        return str(count)
                if x == ']':
                    if last != '[':
                        return str(count)
                if x == '}':
                    if last != '{':
                        return str(count)
            else:
                return str(count)
    if error_stack:
        return str(error_stack.pop())

    return 'Success'
