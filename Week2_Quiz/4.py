# What is the value of list1 after the following lines are executed?

def mystery(l):
  l[0:2] = l[3:5]
  return()

list1 = [34,17,12,88,53,97,62]
mystery(list1)
# print(mystery(list1))