def splitsum (m):
    pos=0
    neg=0
    for v in m:
        if v >0:
            pos=pos+v*v
        if v< 0:
            neg=neg+v*v*v
    return ([pos, neg])