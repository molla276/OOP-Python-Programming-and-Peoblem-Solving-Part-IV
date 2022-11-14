import math
def timer(fact):
    def inner(*args, **kwargs):
        print('Timer start')
        fact(*args, **kwargs)
        print('Time End')
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'factorial of {n} is :{result}')

# timer(get_factorial)()
get_factorial(n=5)
