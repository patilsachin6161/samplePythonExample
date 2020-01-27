dict1 = {x:x**2 for x in (2,4,6,8)}

print(dict1)
print(list(dict1))

# 0 to 100 squere by using dictinary comprehensions

dict2 = {x:x**2 for x in range(100) if x%2 == 0}
print("squere of numbers ", dict2)

#print("dictinary revesed :"+"".join(reversed(dict1)))
for k, v in reversed(dict1.items()):
    print("{} as kay and {} as value ".format(k,v))