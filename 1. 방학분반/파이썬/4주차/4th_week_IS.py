### 1. List comprehension
## Syntax
## newlist = [expression for item in iterable if condition == True]
## newlit = [expression if A else B for item in iterable]
## https://bbookman.github.io/Python-list-comprehension1/

## 1.1 Find all numbers from 1-100 that have 3, 6, 9 in them (369 game) by list comprehension
## 1.2 Using nested list comprehension, find all numbers from 1-100 that are divisible by any single digit (2-9) 


### 2. Generators
## https://www.geeksforgeeks.org/generators-in-python/
## Finish the generator function of the threee number Fibonacci sequence:
## F_{n} + F_{n+1} + F_{n+2} = F_{n+3}
def Fibonacci(n):
    '''Generator function of the three number Fibonacci sequence'''
    # Initials F_1, F_2, F_3
    a, b, c = 1
    i=0
    while i < n:
        temp = a + b + c
    yield















#####--------------------ANSWERS-------------------------###
## 1.1
l1 = [x for x in range(1, 101) if ("3" in str(x) or "6" in str(x) or "9" in str(x))]
print(l1)

## 1.2
l2 = [[y for y in range(1, 101) if y % x == 0] for x in range(2,10)]
print(l2)


## 2.
def Fibonacci(n):
    '''Generator function of the three number Fibonacci sequence'''
    # Initials F_1, F_2, F_3
    a, b, c = 1, 1, 1
    i=0
    while i < n:
        temp = a + b + c
        yield a
        i += 1
        a = b
        b = c
        c = temp

for i in Fibonacci(10):
    print(i)
