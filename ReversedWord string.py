str1 = "I am python developer"
list1 = str1.split()
print("Reversed by slicing "+str1[::-1])
print(list1)
str2 = " ".join(list1[::-1])

print("Reversed string by word:"+str2)
# Reversed string by each and every charcter in word  without slicing
list2=[]
for word in list1:
    list2.append(word[::-1])
revStr = " ".join(list2[::-1])

print("Reversed string by each and every charcter in word  without slicing : "+revStr)

str3="test12"
str4="test12"
print("string index 7 :")
print("id of str3 :", id(str3))
print("id of str4 :", id(str4))
