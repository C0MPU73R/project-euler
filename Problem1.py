"""
@author: C0MPU73R
"""
# Step 1: Generate and store all natural numbers

"""
What are natural numbers?
Positive integerrs from 1 to inf
"""




# generated and stored
# now for arith
def getNumbers():
    natNums = []
    for i in range(1,1000):
        natNums.append(i)
    filtered = []
    for i in natNums:
        if i % 3 == 0 or i % 5 == 0:
            filtered.append(i)
    r = 0
    for i in filtered:
        r = r + i
    return r

x = getNumbers()
print(x)