
import pandas as pd
import numpy as np

# Problem 1

names = ['Michael Jordan', 'Charlie Puth', 'Bruno Mars', 'Minjae Kim', 'Otani Shohei', 'Virgil Abloh', 'Lebron James']
dl =  [True, False, False, False, True, True, True]
budget = [809, 731, 588, 180, 200, 700, 450]
wishlist = [1000, 900, 550, 250, 400, 680, 430]

# 1-1 Make a dictionary 'Cars_list' with variables 'person_name', 'drive_liscence', 'cars_budget', 'want_to_buy'

# 1-2 Build 'cars' DataFrame

# 1-3 change the index into below list
row_labels = ['MJ', 'CP', 'BM', 'MK', 'OS', 'VA', 'LJ']

# 1-4 What is the difference DataFrame and csv data about index perspective?

# 1-5 print the information about only person_name ,cars_budget and want_to_buy with Michael jordan, Bruno Mars, Otani Shohei


# 1-6 What is the difference of 'loc' and 'iloc'?

# 1-7 Compare cars_budget with want_to_buy with bool sereis. Who can buy a car?

# Problem 2

# 2-1 In for loop, what is the difference dictionary with numpy array?

# 2-2 Use for loop and DataFrame 'cars' in Problem 1 insert new column named 'budget_difference' which means the subtraction of 'cars_budget' from 'want_to_buy'