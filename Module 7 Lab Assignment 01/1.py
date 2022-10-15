""" 1. Create a string out of some words given in a list -

l = ["This", "is", "very", "fantastic"]


Expected Output:
"This is very fantastic"

Write a function named create_string() and write your code inside this function.
"""
def create_string(l):
    for i in l:
        print(i, end=" ")

l = ["This", "is", "very", "fantastic"]

create_string(l)