"""
5. Write a python program to read student_name and mark from keyboard and store the data in a text file
with an unique student_id .  
"""

# student_name = input("Enter the student_name: ")
# mark = input("Enter the mark: ")
# print(student_name,mark)

# with open('readme.txt', 'a') as f:
#     f.write(student_name)
#     f.write(mark('\n'))
#     f.close()

with open('readme.txt','a') as f:
    student_name = input("Enter the student_name: ")
    mark = input("Enter the mark: ")
    student_name = student_name + ' '+ mark + '\n'
    f.write(student_name)
    f.close()
