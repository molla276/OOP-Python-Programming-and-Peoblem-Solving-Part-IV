# rows = 6
# # if you want user to enter a number, uncomment the below line
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for x in range(rows):
#     # nested loop
#     for y in range(x):
#         # display number
#         print(x, end=' ')
#     # new line after each row
#     print('')

rows = 5
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for x in range(rows):
    # nested loop
    for y in range(x,rows,--1):
        # display number
        print("*", end=' ')
    # new line after each row
    print('')