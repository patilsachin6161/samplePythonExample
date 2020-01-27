str = input("enter your string to reverse ")
print("orignal string "+str)
print("Reverse string "+str[::-1])

#// check string is paildrone or not
print("String Casefold :"+str[::1].casefold())
#str1, str2 = str[::1].casefold(), str[::-1].casefold()

if(str[::1].casefold() == str[::-1].casefold()):
    print("Palindrone")
else :
    print("string not Palindrone")

print("Reversed string by using reversed function")
revstr = reversed(str)
print(type(revstr))
print(revstr)
str3 = "".join(revstr)
print("String Reversed by reversed function :"+str3)

print("String reversed with out slice and reversed function ")
strlen = len(str)
print("string length ", strlen)
output=""
while(strlen > 0) :
    output = output+(str[strlen-1])
    strlen = strlen - 1
print("without slice & reversed fun reveredstring ", output)


