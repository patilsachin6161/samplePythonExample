str = "2D6fGA7CC1Z4E3"
print(sorted(str)) #sorted the digit first and alphabet next, return list object as result
alphabet =[]
digit=[]
for ch in str:
    if(ch.isalpha()):
        alphabet.extend(ch)
    else:
        digit.append(ch)

print("Sorted string :"+"".join(sorted(alphabet)+sorted(digit)))
