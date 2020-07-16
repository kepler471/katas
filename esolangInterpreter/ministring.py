def interpreter(code):
    count = 0
    accum = ''
    for i in code:
        if i == '+':
            count = (count + 1) % 256
        elif i == '.':
            accum += chr(count)
    return accum
