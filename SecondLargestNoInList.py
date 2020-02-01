list1 = [2,3,6,8,25,10,23, 24, 50]
largest = list1[0]
largest2 = None
for item in list1[1:] :
    if item > largest :
        largest2 = largest
        largest = item
    elif largest2 == None or largest2 < item :
        largest2 = item

print("2nd laregest no in list ", largest2)
