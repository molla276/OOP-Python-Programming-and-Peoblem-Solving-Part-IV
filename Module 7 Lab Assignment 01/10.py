def create_new_string(s,a):
    output = ""
    from_s = s.replace(",", " ").split(" ")
    for i in a:
        for index_j, j in enumerate(from_s):
            if i.lower() == j.lower():
                output+=from_s[index_j+1]+" "
    with open('out.txt','w') as fileWriter:
        fileWriter.write(output)
        fileWriter.close()

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

create_new_string(s,a)


# a = ['oh', 'Emelia', 'to']

# s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."


# def create_new_string(s):
#     s = s.replace(',', "")
#     s = s.replace('.', "")

#     split_string = s.split()

#     filtered_words = [split_string[i + 1] for i in range(
#         len(split_string)) if split_string[i].lower() in a or split_string[i] in a]

#     return "".join([" " + i for i in filtered_words])[1:]


# output = create_new_string(s)

# with open('out.txt', 'w') as fileWriter:
#     fileWriter.write(output)
