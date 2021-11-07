def rot(num):
    c = ''
    a = [i for i in str(num)]
    if '6' in a:
        b = a.index('6')
        a.insert(b, '9')
        a.pop(b + 1)
    else:
        for i in a:
            c += i
    return print(c)
