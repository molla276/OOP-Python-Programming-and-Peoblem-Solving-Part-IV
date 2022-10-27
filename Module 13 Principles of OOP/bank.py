class Account:
    def __init__(self,holder, initial___balance):
        self.holder = holder #public attribute
        self.__balance = initial___balance #__balance is a private attribute

    def deposit(self,amount):
        print(f'adding {amount} to your account')
        self.__balance += amount

    def withdraw(self,amount):
        print(f'Withdrawing {amount} from your account')
        self.__balance -=amount

class StudentAccount(Account):
    def __init__(self, holder, initial___balance, school):
        self.school = school
        super().__init__(holder, initial___balance)

rafsan = StudentAccount('Rafsan', 150000, 'IUB')
print(rafsan.__balance)
rafsan.deposit(20000)
rafsan.deposit(10000)
rafsan.deposit(5000)
rafsan.__balance = 0
print(rafsan.__balance)
