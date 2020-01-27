StringExm = "HELLLOHELLOHELLO"
list1 = []
for ch in StringExm:
    if ch not in list1:
        list1.append(ch)

print("Unique Char from String "+"".join(list1))