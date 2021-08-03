"""
Filename: Problem2.py

@ author: C0MPU73R
"""


# Generate and store fibonacci numbers
# The general algorithm is:
# 0, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, etc
# This can be written as: Xn+2 = Xn+1 + Xn
# In terms of a function: Fn = Fn-1 + Fn-2
# the current term is equivalent to the sum of the last two terms

def fibonacci(limit):
    seq = []
    a = 0
    b = 0
    temp = None
    for i in range(limit):
        b = b + a
        a = temp
        seq.append(b)

