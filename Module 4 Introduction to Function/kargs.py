# def full_name(f_name, l_name):
#     name = f'{f_name}{l_name}'
#     return name

# name = full_name(l_name="Islam",f_name='Ariful')
# print(name)

# def long_name(**kargs):
#     print(kargs)

# long_name(first= 'Dr.',last = 'chowdury', middle = 'Rahman') 


# def name_mixed(first,last,**name_parts):
#     print(first, last, name_parts)

# name = name_mixed(first='chowdury', last='Choto', middle='majari')
# print(name)

def all_type(first,*args,**Kargs):
    print(first)
    print(args)
    print(Kargs)

all_type('add','bbb','lll','bbb',name='Abdul',father='babul')