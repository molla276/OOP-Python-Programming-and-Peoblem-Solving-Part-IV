# with open('message.txt', 'w') as fileWrite:
#     fileWrite.write('I love Phitron')

with open('message.txt', 'r') as fileRead:
    text = fileRead.read()
    print(text)