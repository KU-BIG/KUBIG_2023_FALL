# 1. Practice recursive functions
# https://www.programiz.com/python-programming/recursion
import math
import sys

def fac(num):
    """
    Recursive function of the factorial
    """

    if num == 0:
        return 1
    else:
        return (num*fac(num - 1))
    
# 1.1 Compare math.factorial(10) to fac(10)
print(math.factorial(50))
print(fac(50))
# 1.2 Include exceptions raise error given float, string, negative
# Maximum recursions
# https://help.acmicpc.net/judge/rte/RecursionError
print(sys.getrecursionlimit())
# print(fac(1000))

def fac2(num):
    """
    Recursive function of the factorial
    Input is nonnegative integer
    """
    # 
    if type(num) is not int:
        raise TypeError("Input must be nonnegative integer")
    
    if num < 0:
        raise ValueError("Input is negative")
    
    if num == 0:
        return 1
    elif num > 500:
        raise ValueError("Input too large. Use integer under 500")
    else:
        return (num*fac(num - 1))
    
        
# fac2("501")
# fac2(-2)
# fac2(502)

# 2. Practice map() function
# https://gonigoni.kr/posts/python-map-reduce-filter/
# make a map() with lambda() that makes the words in respective list of letters
l1 = ["apple", "banana", "kiwi", "grape", "watermelon"]

a = list(map(lambda x: list(x), l1))
print(a)

# 3. Practice filter() function
# Construct a 369 game checker
numbers = list(range(1, 1000))
a = lambda x: ("3" in str(x)) or ("6" in str(x)) or ("9" in str(x))
print(list(filter(a, numbers)))