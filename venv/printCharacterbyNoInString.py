str = "A4B3C4Z1D5"
output = ""
for ch in str:
    if(ch.isalpha()):
        x = ch
    else:
        d1 = int(ch)
        output = output+x*d1

print("Print output :"+output)