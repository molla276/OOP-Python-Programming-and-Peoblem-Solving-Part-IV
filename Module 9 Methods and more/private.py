class User:
    def __init__(self, name, password, phone):
        self.name = name
        self.__password = password
        self.__phone = phone

    def __get_password(self):
        print(self.__password)

    def user_log(self, name, password):
        if(name == self.name and password == self.__password):
            return True
        return False

arif = User('Ariful Islma Arif', 'NODEABCD', '01675560811')
print(arif.__password)
print(arif.__phone)
