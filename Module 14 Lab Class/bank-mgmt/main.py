""" Manages Bank Account """

class Account:
    accID = 1
    def __init__(self,name, age, nid_num, balance):
        self._name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance

        #update account id
        self.account_id = Account.accID
        Account.accID += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name

    

acc_1 = Account('Ariful Islam', 26,789000987, 15000)
acc_2 = Account('Mainul Islam', 36,789000977, 1500)
# print(acc_1.account_id)
# print(acc_2.account_id)

# acc_1.deposit(5000)
# print(acc_1.balance)

# acc_2.withdraw(500)
# print(acc_2.balance)

print(acc_2.name)