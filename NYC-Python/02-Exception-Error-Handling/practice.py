a = int(input("type a number :- "))
b = int(input("type a number :- "))


try: 
    print(f"the value is {a/b}")
except Exception as err:
    print(f"the error is occured:- {err}")
else:
    print('this will only run if the try code execute without the error')
finally:
    print('this will run if the try code execute without the error or not')


input("To check is upper code give the error then aslo the rest code is working or not :- ")
