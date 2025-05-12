e = input('would you like to find the average or the median: ')

if e == 'average' or e == 'avg':
    g = input('how many numbers to avg: ')
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
    print('the average is', avg)

elif e == 'median' or e == 'med':
    g = input('how many numbers to med: ')
    g = int(g)
    num =[]
    defined = 0
    while defined < g:
        a = input('define a number: ')
        a = int(a)
        num.append(a)
        a = 0
        defined = defined + 1
        num.sort()
        print(num)
    u = len(num)

    p = g % 2
    if p > 0:
        t = u / 2 + 0.5
        print('the median is', num[t])
    else:
        q = u / 2
        q = int(q)
        w = q - 1
        w = int(w)
        m = (num[q] + num[w]) / 2
        print ('the median is', m)
        
