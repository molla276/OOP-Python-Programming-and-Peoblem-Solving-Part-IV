"""

7. Complete the following code (without using the replace function)-

def replace_comma_with_space(text):
    …
    …

s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)


"""
def replace_comma_with_space(text):
    replaced_text = ' '.join(i for i in text.split(','))
    return replaced_text

s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)

