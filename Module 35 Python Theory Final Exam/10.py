# #single inheritance
# class Nokia:
#     company = 'Nokia'
#     website = 'www.nokia.com'

#     def contact_details(self):
#         print('Address: Gulshan,Road-4,Dhaka')

# class Nokia1100(Nokia):
#     def __init__(self) -> None:
#         self.name = 'Nokia 1100'
#         self.year = 2000

#     def product_details(self):
#         print('Name     :', self.name)
#         print('Year     :', self.year)
#         print('Company  :', self.company)
#         print('Website  :', self.website)

# # Multiple Inheritance
# class Father:
#     def fishing(self):
#         print("Fishing in Rivers")
#     def chess(self):
#         print("Playing Chess From Father")

# class Mother:
#     def cooking(self):
#         print("Cooking Food")

#     def chess(self):
#         print("Playing Chess From Mother")

# class Son(Mother,Father):
#     def ride(self):
#         print("Riding Bicycle")
# cook = Son()
# cook.ride()
# cook.fishing()
# cook.cooking()
# cook.chess()

#Multilevel inheritance
# Multilevel Inheritance

class GrandFather:
    def ownHouse(self):
        print("Grandpa House")

class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike")

class Son(Father):
    def ownBook(self):
        print("Son Have a Book")

cook = Son()
cook.ownHouse()
cook.ownBike()
cook.ownBook()
