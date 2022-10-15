"""
9. You need to make a positive story into a negative by changing some of its words automatically. Someone gave you a list `replace with’ and asked to find the words that are in that list in string ‘s’ and replace them with the next word of that list.

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."


Output example (one done for you): 
"I am the thief of Baghdad..........."


"""
from unittest import result


def replace_word(s, replace_word):
    result = ""
    from_s = s.split(" ")
    for index_j,j in enumerate(replace_with):
        for index_i,i in enumerate(from_s):
            if i == j and index_j % 2 == 0:
                from_s[index_i]=replace_with[index_j+1]
    for i in from_s:
        result+=i+" "
    return result

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

result = replace_word(s,replace_with)
print(result)



