""" 
1. Create a function exp(a, n) that returns the exponential result ( an ). 
Read user input a and n in a single line from the keyboard.

Example input:
>> enter numbers: 2 3

Example Output:
>> result is: 8
"""
from tkinter import N


# a,n
# result = input(f"enter numbers: {a}**{n}")
# print(result)

a, n = map(int, input().split())
print(a**n)

