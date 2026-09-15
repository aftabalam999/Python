number = 3
end = 10


for i in range(1, end+1):
    if i == 5:
        continue
    print(number,"x",i ,"=",i*number)