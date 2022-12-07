# rows = int(input('Enter the rows: ')) 
# for i in range(1,rows+1):
#     for j in range(i,rows+1):
#         print(j,end="")
#     for j in range(1,i):
#         print(j,end="")
#     print()

# def swapPositions(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list

# n = int(input())
# my_list = [x for x in range(1,n+1)]

# for i in range(n):
#     for j in my_list:
#         print(j,end='')
#     if i < n-1:
#         swapPositions(my_list,i,i+1)
#     print('\n')

def swap_position(my_list, position1, position2):
    my_list[position1], my_list[position2] = my_list[position2], my_list[position1]
    return my_list

index = int(input())
my_list = [x for x in range(1, index+1)]

for i in range(index):
    for j in my_list:
        print(j,end="")
    if i < index - 1:
        swap_position(my_list, i, i+1)
    print()