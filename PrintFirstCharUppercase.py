string = "i am python developer"
str1 = string.capitalize()
print(string.capitalize())
print(id(string))
print(id(str1))
splitList = string.split(" ")
result = ""
for item in splitList:
    for ch in item:
        if(ch == item[0]) :
            result = result + ch.upper()
        else :
            result = result + ch
    result = result + " "

print(result)