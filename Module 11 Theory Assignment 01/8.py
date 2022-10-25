"""
8. Write a Python class to find a pair of elements (indices of the two numbers) from a 
given array whose sum equals a specific target number.
Input:
numbers= [10,20,10,40,50,60,70]
target=50 
Output: 3, 4

"""
# class target_num:
#     def two_sum(self, numbers, target):
#         sum = {}
#         for index, number in enumerate(numbers, start=1):
#             if target - numbers in sum:
#                 return (sum[target - number], index)
#             sum[number] = index

# numbers= [10,20,10,40,50,60,70]
# target = 50

# index = target_num().two_sum(numbers, target)
# print(index)


class target_num:
    def two_sum(self, nums, target):
        index = {}
        for i, num in enumerate(nums,start=1):
            if target - num in index:
                return (index[target - num], i)
            index[num] = i

numbers= [10,20,10,40,50,60,70]
target = 50

print("%d %d" % target_num().two_sum((numbers), target))
