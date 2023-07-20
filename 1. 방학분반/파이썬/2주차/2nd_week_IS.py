import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### 1. ###
# Playing with dictionaries
d1 = {"A":[1,2,3], "B":[4,5,6], "C":[7,8,9]}

print(d1)
# print(d1[1])
print(d1["A"])
print(d1["A"][1]) # check that dictionary is not ordered

d1["A"].append(10)
d1["B"].append(11)
d1["C"].append(12)
print(d1)

d2 = {"A": True, "B":False}
print(d2)

### 2. ###
# https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/eb5072ea046760bb81e5ce6bc1c97b37_MIT6_042JF10_chap20.pdf
# from the Empire state game, the rules will be changed a bit
# There is a pit at sea level, and a cliff at 60th floor
# Die 1,2 -> 1 step down
# Die 3, 4, 5 -> 1 step up
# Die 6 -> throw die again -> move up the amount of steps
# Fumble probability 0.1% -> 5%
# If we step down at 0 or exceed 30 floors, we die
# What is the distribution of the turns until death?
# Let's try 1000 iterations

np.random.seed(123)

turns_death = []
for i in range(1000):
    state = "alive"
    turns = 1
    random_walk = [0]
    while state == "alive":
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = step - 1
        elif dice <=5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        
        # Fumble
        if np.random.rand() <= 0.05:
            step = 0
        
        # Test if death
        if step < 0:
            state = "dead"
            turns_death.append(turns)
        elif step > 30:
            state = "dead"
            turns_death.append(turns)
        else:
            random_walk.append(step)
            turns = turns + 1

print(turns_death)

plt.hist(turns_death)

plt.xlabel("Number of turns")
plt.ylabel("Frequency")

plt.show()

### 3. Pandas Dataframes ###
df = pd.DataFrame(d1)
print(df)

# Difference between single and double bracket subsetting
print(type(df["A"]))
print(type(df[["A"]]))

# Get value of second row, second column
print(df["A"].iloc[1])
print(df.iloc[1]["A"])

# Get row sums by apply() method
print(df.apply(np.sum, axis = 0)) # column sum
print(df.apply(np.sum, axis = 1)) # row sum