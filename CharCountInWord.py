str1 = "aaaabbbbzzzzrrqqqq"
#Output = 4a4b5z1w4q
c=1
i=1
previos =str1[0]
output =""
while i<len(str1) :
    if str1[i] == previos :
        c=c+1
        x = previos
    else:
        output = output +x+str(c)
        c=1
        previos=str1[i]

    if(i == len(str1)-1) :
        output = output+x+str(c)
    i=i+1

print("output :"+output)