#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 18:01:22 2023

@author: nang
"""

# 1
# https://www.acmicpc.net/problem/2675
# making function for above problem

def repeating_characters(R, S):
    new_string = ''
    
    for i in range(len(_)):
        new_string += _ * _
        
    return new_string

# 2
# *args / **kwargs
# Answer that what's the difference of *args and **kwargs 
# and when could you possibly use them


# 3.
# Use lambda function, name it as ci_check
# and make a new list ci_list being composed of strings 
# that contains a string 'ci' 
# Upper/Lower case doesn't matter

str_lst = ['CIA', 'appericiate', 'Ciao','banana',
           'nonfiction','F1player','social']

ci_check = filter(lambda x: 'CI' in x.upper(), str_lst)
ci_list = list(ci_check)
print(ci_list)
