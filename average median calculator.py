b = 5
while b == 5:
    

    g = input('how many numbers to input: ')
    g = int(g)
    num =[]
    defined = 0
    while defined < g:
        a = input('define a number: ')
        a = int(a)
        num.append(a)
        a = 0
        defined = defined + 1
        print(num)
    u = len(num)
    s = sum(num)
    avg = s / u
    print('\nthe average is', avg)
    p = g % 2
    if p > 0:
             t = u / 2 + 0.5
             t = int(t)
             print('\nthe median is', num[t])
    else:
        q = u / 2
        q = int(q)
        w = q - 1
        w = int(w)
        m = (num[q] + num[w]) / 2
        print ('\nthe median is', m)

    r = num[g - 1] - num[0]
    r = int(r)
    print('\nthe range is', r)
