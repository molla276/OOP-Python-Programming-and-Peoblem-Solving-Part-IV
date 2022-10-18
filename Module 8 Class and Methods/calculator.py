class Calculator:
    def add(self,num1,num2):
        sum = num1 + num2
        return sum

    def subtraction(self,num1,num2):
        sub = num1 - num2
        return sub

    def multiply(self,num1,num2):
        mul = num1 * num2
        return mul

    def divide(self,num1,num2):
        div = num1/num2
        return div

    

make_cal = Calculator()

sum = make_cal.add(10,20)
sub = make_cal.subtraction(30,10)
mul = make_cal.multiply(5,4)
div = int(make_cal.divide(100,10))

print(f'sum:{sum},div:{div},mul:{mul},sub:{sub}')

