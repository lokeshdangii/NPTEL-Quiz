def remdup(m):
    seen = set()
    for i in range (len (m)-1, -1, -1):
        if m[i] in seen:
            del m[i]
        else:
            seen.add(m[i])
    return(m)