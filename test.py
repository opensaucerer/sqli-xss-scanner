def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def converter(str):
    res = 0
    i = 0

    while (i < len(str)):

        # Getting value of symbol s[i]
        s1 = value(str[i])

        if (i + 1 < len(str)):

            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])

            # Comparing both values
            if (s1 >= s2):

                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:

                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res


def sortRoman(names):
    # Write your code here
    sort = []
    value = []
    p = []
    vi = []
    rn = []
    for index, name in enumerate(names):
        r = name.split(' ')[1].rstrip()
        n = name.split(' ')[0].rstrip()
        i = converter(r)
        value.append(i)
        p.append(n)
        vi.append(index)
        vi.append(n)
        rn.append(r)

    print(value)
    print(rn)
    p.sort()
    print(p)
    print(vi)
    for a in p:
        d = a + ' '
        o = [i for i, x in enumerate(vi) if x == a]
        print(o)
        for c in o:
            print(vi[c - 1])


sortRoman(['Steven XL', 'Steven XVI', 'David IX',
          'Mary XV', 'Mary XIII', 'Mary XX'])
