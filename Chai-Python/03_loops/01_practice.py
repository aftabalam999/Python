numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_count = 0

for num in numbers:
    if num > 0:
        positive_num_count += 1

# print("Positive number count is", positive_num_count)

n = 10
sum_even = 0
for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1
# print(sum_even)

#### check the user input is it between 1 to 10
while True:
    number = int(input("Enter the number between 1 to 10: "))
    if 1<= number <=10:
        print('Thanks')
        break
    else:
        print("Invalid number, try again")