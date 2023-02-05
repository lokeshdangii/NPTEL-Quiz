#  Consider the following function mys:
def mys(m):
    if m == 1:
        return(1)
    else:
        return(m*mys(m-1))
    
print(mys(5))

"""
Which of the following is correct, assuming we always pass an integer argument to mys?
 1). The function always terminates with mys(n) = factorial of n
 2). The function always terminates with mys(n) = 1+2+...+n
 3). The function terminates for non-negative n with mys(n) = factorial of n
 4). The function terminates for positive n with mys(n) = factorial of n      """
