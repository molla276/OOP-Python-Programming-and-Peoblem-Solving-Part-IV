# data={1:[2,3,4,5],2:[1,3,4,5],3:[1,2,4,5],4:[1,2,3,5],5:[1,2,3,4]}

og_list = [1, 2, 3, 4, 5]
# # squared_num_list = [num*num for num in og_list]
# dict = {index+1:value for index, value in enumerate(og_list)}
# print(dict)

# from collections import defaultdict
# from math import floor
# def test(lst, fn):
#     d = defaultdict(list)
#     for el in lst:
#         d[fn(el)].append(el)
#         return dict(d)
# nums = [1,2,3,4,5]

# print(test(nums, floor))
# import itertools 
nums = [1,2,3,4,5]
data = {x:[y for y in nums if x!=y] for x in nums}
print(f'data={data}')

# nums = [1,2,3,4,5,6]
# data = {x:[y for y in nums if x!=y] for x in nums}
# print(data)
