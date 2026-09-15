list = [12,43,1,65,7,23,54,999,6,543]
largest = list[0]
index = 0

# for i in list :
#     print(i)
#     if i > largest :
#         largest = i
#         print("largest", i)
        
# for i in range(len(list)) :
#     if list[i] > largest :
#         largest = list[i]
#         index = i

# print("ans", index)
    
larg = list[0]
sLarge = list[0]
for i in list :
    if i > larg :
        sLarge = larg
        larg = i
    elif i > sLarge :
        sLarge = i

print(sLarge)
