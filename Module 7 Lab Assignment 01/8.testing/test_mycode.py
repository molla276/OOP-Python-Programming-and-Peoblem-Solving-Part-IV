import my_code

def make_upper(string):
    return (string.upper())


def make_capital(string):
    return (string.capitalize())


def make_lower(string):
    return (string.lower())


string = 'Hello'
res = make_upper(string)
res1 = make_capital(string)
res2 = make_lower(string)


def test_script1():
    assert res == "HELLO"


def test_script2():
    assert res1 == "Hello"


def test_script3():
    assert res2 == "hello"