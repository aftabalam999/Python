myList = [1,2,3,4,5,6]

myList.append(8)
myList.extend([20, 40])
myList.pop()
# myList.clear()
# print(myList)

numbers = [10, 20, 30]

numbers.insert(1, 15)

# print(numbers)

number = (10)
# print(type(number))

student = ("Jasin", 22, "Python")

name, age, language = student

# print(name)
# print(age)
# print(language)

student = {
    "name": "Jasin",
    "age": 22,
    "city": "Dharamshala"
}

# student.pop("city")
# print(student.get("city", "Not available"))

# print(student["city"])

# print(student.keys())
# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(value)


# for key, value in student.items():
#     print(key, value)

numbers = {10, 20, 30}

numbers.update([40, 50, 60])
numbers.update({70, 80})

print(numbers)

list = [1,2,3]
print(list*2 )