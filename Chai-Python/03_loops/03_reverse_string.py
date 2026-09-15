string = "hello"
reverse_str = ""

for char in string:
    reverse_str = char + reverse_str

# print(reverse_str)

### non repeated char
input_str = "teeter"

for char in input_str:
    if input_str.count(char) == 1:
        print('char is', char)
        break

 