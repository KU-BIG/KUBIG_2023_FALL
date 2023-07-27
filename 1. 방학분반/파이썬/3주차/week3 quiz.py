import pandas as pd
import numpy as np
from functools import reduce

# Problem 1

# 1-1
# Make the same Lambda function as the one below

def add(x,y):
    return  x + y

# 1-2
# Use map() with the Lambda function one above and the list one below and print with parameter 'result1'
list1 = [1,2,3,4,5,6,7,8,9]

# 1-3
# Use reduce() with the Lambda function, list above and print with parameter 'result2'


# 1-4 
# Use filter() with the Lambda function and print only odd included in the list one above

# Problem 2
# Use *args or **kwargs and make wrong code as right one

def three_shouts():
    def inner(name):
        return name
    return (inner())

name1 = 'michael jordan'
name2 = 'charlie puth'
name3 = 'margot robbie'

print("Their name is : " + three_shouts(name1, name2, 'Tom Cruise', name3))