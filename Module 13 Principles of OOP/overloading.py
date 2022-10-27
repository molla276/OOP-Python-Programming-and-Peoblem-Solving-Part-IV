# print(max(17,55,48,78,100))
# print(max([13,45,87]))
# print(max('A','B','C','R'))

# def add(num1,num2,num3):
#     return num1 + num2 + num3

# print(add(10,20,30))
# print(add(200,300,500))

# def add(*args):
#     sum = 0

#     for i in args:
#         sum = sum + i
#     print('sum:',sum)

# add(10,20,30,50,40)

# def info(**kwargs):
#     for key, value in kwargs.items():
#         print("{} is {}".format(key,value))

# info(Firstname="Ariful", Lastname= "Islam", Age=26, Phone= 1675560811)

class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def __add__(self, other):
        return self.__balance + other.__balance

    def __eq__(self, __o: object) -> bool:
        return self.__balance == __o.__balance

my_Account = Account("Shakib", 15000)
her_account = Account("Shishir", 20000)

result = my_Account + her_account
result2 = my_Account == her_account
print(result)
print(result2)