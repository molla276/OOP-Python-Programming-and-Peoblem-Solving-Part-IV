"""
8. Suppose you have a program that converts a string into Upper, Capitalized and Lower style using three different functions. Now create a test script for testing the three functionality of that program. Run using PyTest.

Write a function make_upper() to make the string in uppercase
Write a function make_capital() to make the string capitalized
Write a function make_lower() to make the string lowercase

Write a function named test_script() and write your code inside this function. 
"""
def test_script():
    make_upper(str)
    make_capital(str)
    make_lower(str)

def make_upper(str):
    output = ""
    for i in str:
        if ord(i) >= 97 and ord(i)<=120:
            output+=chr(ord(i)-32)
    return output

def make_lower(str):
    output = ""
    for i in str:
        if ord(i) >= 65 and ord(i)<=90:
            output+=chr(ord(i)+32)
    return output

def make_capital(str):
    output = ""
    if ord(str[0]>=97) and ord(str[0])<=120:
        letter = ord(str[0])-32
    return output

if __name__ == "main":
    res = test_script(str)
    print(res)