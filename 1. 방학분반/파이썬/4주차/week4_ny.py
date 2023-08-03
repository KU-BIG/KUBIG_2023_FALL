#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:23:12 2023

@author: nang
"""

'''
1.
make dictionary with index as key and value as value in the list using iterator and list comprehension
'''
lst = ['goofy','bubbly','ick','quirky','disgusting','cocky','generous','modest','snobby']
ans = ___
print(ans)

'''
2.
using lst in question 1 and if lengths of the word is 6, save it in lst2
and make generator function length6 with single parameter input_list
to return the words having length of 6.
'''
lst2 = 
def length6(input_list):
    for word in _:
        ____
        
for word in __:
    print(word)


'''
3.
what's the difference betw the generator and iterator?
'''



'''
=========
ANSWER
=========
# 1. ans = {idx, value for idx, value in enumerate(lst)}

# 2.
lst2 = [wrd for wrd in lst if len(wrd)==6]
def length6(input_list):
    for word in input_list:
        yield word
        
for word in length6(input_list):
    print(word)


# 3.
iterable객체는 값을 지속적으로 호출하는 것이 가능하지만
generator은 그렇지 않다. 한 번 정보를 소비하고 나면 더이상 값을 기억하고 있지 않기 때문에 여러번 값을 호출하는 것이 불가능하다.
예를 들어, generator의 일종인 next나 생성한 generator을 yield를 사용해 리턴하는 경우 
더이상 리턴할 값이 없으면 StopIteration에러를 발생시킨다. 
제너레이터는 필요할 때만 값을 생산하여 메모리를 더 효율적으로 쓸 수 있다. 
모든 generator는 iterator지만 그 역은 성립하지 않는다.
'''