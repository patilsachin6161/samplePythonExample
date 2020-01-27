string = "a2d3z1f4"
#output = acdgzAfj"
output=""
for ch in string:
    if ch.isalpha():
        x=ch
        x_AsciVal = ord(ch)
    else:
        d = int(ch)
        output = output+x+(chr(x_AsciVal+d))

print("Output :"+output)