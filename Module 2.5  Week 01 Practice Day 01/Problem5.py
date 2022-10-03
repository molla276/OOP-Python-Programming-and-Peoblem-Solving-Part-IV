""" Write a Python which iterates the integers from 1 to 50. For multiples of three print
"Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both
three and five print "FizzBuzz" """

def fizzbuzz(num):
    if num % 3 == 0  and num % 5 == 0:
        return 'fizzbuzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    return num

for num in range(0,51):
    print(fizzbuzz(num))
