# def square(x):
#     return x * x

# square = lambda x : x * x
# result = square(6)
# print(result)

nums = [12,45,56,45,12,89]

# def double_it(x):
#     return x * 2
# double_it2 = lambda x : x* 2

# doubled_numbers = map(double_it, nums)
# print(nums)
# print(list(doubled_numbers))

# square_numbers = map(lambda x: x*x, nums)
# print(list(square_numbers))

# bigger_numbers = filter(lambda num: num > 50, nums)

# print(tuple(bigger_numbers))

actors = [
    {'name': 'sakib', 'age': 35},
    {'name': 'bubli', 'age': 30},
    {'name': 'manna', 'age': 55},
    {'name': 'shabana', 'age': 50}
    ]

senior_artist = filter(lambda actor: actor['age'] > 35,actors)
junior_artist = filter(lambda actor: actor['age'] < 35,actors)

print(list(senior_artist))
print(list(junior_artist))