import numpy as np

# Problem 1 
# From the code in lecture <Numpy: Basic Statistics>
height = np.round(np.random.normal(1.75, 0.20, 10), 2)
weight = np.round(np.random.normal(60.32, 15, 10), 2)
arr = np.column_stack((height, weight))

# why is "height" and "weight" within parenthesis? 
print(arr)
# help(np.column_stack)
# help(np.random.normal)
print((height, weight))
print(type((height, weight))) # <class 'tuple'>

# Problem 2
a = np.random.normal(0, 1, 10)
b = np.random.normal(0, 1, 10)
c = np.random.normal(0, 1, 10)
d = np.random.normal(0, 1, 10)
e = np.random.normal(0, 1, 10)

arr = np.column_stack((a, b, c, d, e))

# get row sum and column sum for arr
# help(np.sum)
print(arr)
print(np.sum(arr, axis = 0))
print(np.sum(arr, axis = 1))

# Problem 3
# Using methods
c = [1, 2, 3, 4, 5]
d = [6, 7, 8]
c.append(d)
print(c)


# Problem 4
x = [1, 2, 3]
y = x
z = y

print(x)
print(y)
print(z)

# What happens if you alternate the disabling?
# z.append(0)
# print(x)
# print(y)
# print(z)


# x.append(6)
# print(x)
# print(y)
# print(z)

y.append(9)
print(x)
print(y)
print(z)

