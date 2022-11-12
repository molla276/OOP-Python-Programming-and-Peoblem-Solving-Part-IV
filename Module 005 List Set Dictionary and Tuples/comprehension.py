nums = {12,45,56,45,12,89,78,11}

# odd_numbers = []
# for i in nums:
#     if i % 2 == 1:
#         odd_numbers.append(i)
# # print(odd_numbers) 

odd_numbers = [i for i in nums if i % 2 == 1 if i % 5 == 0]
print (odd_numbers) 