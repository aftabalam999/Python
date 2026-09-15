"""
    x -> only for creating the file
"""
# open('03-file-handling/hello.txt', "x")

"""
    w, a -> for create if !exist and write in the file
    w -> overrides
    a -> concate
"""
# file = open('03-file-handling/hello.txt', "w")
# data = input("Write something that you want to save in the file :- ")
# file.write(data)

"""
    r -> only for reading the file is !exist the file throw the error
"""
# file = open('03-file-handling/hello.txt', "r")
# print(file.read())

"""
    with keyword -> always prefer to this, don't need to create the extra var as well clean syntax
"""

with open('03-file-handling/hello.txt', 'a') as f:
    f.write('\n checking that this with keyword and the append is working properly or not')
