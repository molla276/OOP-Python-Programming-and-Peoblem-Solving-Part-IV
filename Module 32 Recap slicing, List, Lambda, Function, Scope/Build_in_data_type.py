# a = float(10)
# print(a)

#Example 1

# s = 'Phitron'
# new_string = lambda string : string.upper()[::]
# print(new_string)

# mx = lambda a,b : a if(a > b) else b
# print(mx(mx(6,5), max(3,4)))

#Example 6 
# lst = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in lst:
#     sum += i

# print(sum)

#Example - 6
# from functools import reduce
# lst = [1,2,3,4,5,6,7,8,9,10]

# sum = reduce(lambda x, y:x+y, lst)
# print(sum)

# lst = ['hello', 'world', 'python']

# new_list = [x.lower() for x in lst]
# print(new_list)

# lst = [[j for j in range(3)] for i in range(4)]
# print(lst)

# lst = [[0 for i in range(5)] for i in range(5)]
# print(lst)

#zip
# nums = [1,2,3]
# string = ['one', 'two', 'three']
# new_obj = zip(nums, string)
# # print(set(new_obj))
# # print(tuple(new_obj))
# print(list(new_obj))

# names = ['rahim', 'karim', 'halim']
# salaries = [1000, 2000, 30000]
# result = zip(names, salaries)
# # print(set(result))

# name, salary = zip(*result)
# print(name)
# print(salary)