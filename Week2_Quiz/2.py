# Consider the following lines of Python code.

x = [589,'big',397,'bash']
y = x[2:]
u = x
w = y
w = w[0:]
w[0] = 357
x[2:3] = [487]

'''
After these execute, which of the following is correct?
 x[2] == 487, y[0] == 397, u[2] == 487, w[0] == 357
 x[2] == 487, y[0] == 357, u[2] == 487, w[0] == 357
 x[2] == 487, y[0] == 397, u[2] == 397, w[0] == 357
 x[2] == 487, y[0] == 357, u[2] == 397, w[0] == 357
 '''