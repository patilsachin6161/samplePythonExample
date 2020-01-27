str = input("Enter your string to dispaly add & even charachter")
i = 0
strlen = len(str)
oddCharachter, evenCharacter = "",""
while i < strlen-1 :
    #print("character form even index "+str[i])
    evenCharacter = evenCharacter+str[i]
    i = i+2

i = 1
while i < strlen :
    #print("chrachter from odd index "+str[i])
    oddCharachter = oddCharachter + str[i]
    i = i+2

print("Even index chrachter :"+evenCharacter + " Odd index Character : "+oddCharachter)

# Print character using slicing string functionality
print("Even index from string by using slicing :"+str[::2])
print("odd index from string by using slicing :"+str[1::2])