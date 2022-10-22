# from functools import cache
# import time
# # 1, 1, 2, 3, 4, 5, 8,13,21.....

# @cache
# def fib(n):
#     if n <= 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# start = time.time()
# for i in range(37):
#     print(i, fib(1))

# end = time.time()
# mili_second = (end-start)*1000
# print('Time took', mili_second)

class Fruit:
    pass


print(Fruit.__name__)
