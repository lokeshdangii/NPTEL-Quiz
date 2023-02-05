# What is h(53)-h(52), given the definition of h below?
def h(n):
    s = 0
    for i in range(1,n+1):
        if n%i > 0:
           s = s+1
    return(s)

var1 = h(53)-h(52)
print("answer is :",var1)