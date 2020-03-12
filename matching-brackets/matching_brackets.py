def is_paired(input_string):
    pairs = {'}': '{', ']': '[', ')': '('}
    stack = []
    for x in input_string:
        if x in pairs.values():
            stack.append(x)
        elif x in pairs.keys():
            if len(stack) and stack[-1] == pairs[x]:
                stack.pop()
            else:
                return False
    return not stack
