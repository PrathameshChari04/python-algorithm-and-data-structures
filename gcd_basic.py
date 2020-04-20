n = int(input('Enter the n :'))
m = int(input('Enter the m :'))

def gcd(n,m):
    fm = []
    for i in range(1,m+1):
        if (m%i) == 0:
            fm.append(i)

    fn = []
    for j in range(1,n+1):
        if (n%j) == 0:
            fn.append(j)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    return(print(' GCD : ',cf[-1]))




gcd(n,m)

