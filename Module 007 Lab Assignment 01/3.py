"""
3. Go to this repo: https://pypi.org/project/pyjokes/ and try to make a chat bot to tell you joke using pyjokes.
Write a function named tell_some_jokes() and write your code inside this function. 
"""
import pyjokes

def tell_some_jokes():
    my_jokes = pyjokes.get_joke(language="en", category="neutral")

    print(my_jokes)
tell_some_jokes()