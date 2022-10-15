"""
6. Complete the following code
def clean_string(text):
    ....
    ....
    print(output)
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)


If you face any errors, fix them. Get help from google. Do not ask others.

"""
def clean_string(output):
    output = "".join(i for i in output if i.isalpha() or i.isspace())
    print(output)
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)