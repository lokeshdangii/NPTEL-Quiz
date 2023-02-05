# For what integer value n would g(92,n) return 13?

def g(m,n):
    res = 0
    while m >= n:
        res = res+1
        m = m-n
    return(res)

print(g(92,7))