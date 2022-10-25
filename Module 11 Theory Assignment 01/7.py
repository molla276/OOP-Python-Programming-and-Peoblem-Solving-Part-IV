"""
7. Write a Python class to get all possible unique subsets from a set of integers.
Input  : [4, 5, 6] 
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

"""

def subset(set, index):
    if index == len(set): return [[]]
    return subset(set, index+1)+[[set[index]] + x for x in subset(set, index+1)]

Input = [4, 5, 6]
Output = subset(Input, 0)
print(Output)
