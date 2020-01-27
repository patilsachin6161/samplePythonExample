#Count the No og charachter in the string
example = "ASFGHGJHKJHHGFD"
set1 = set(example)
print("Count by using Set ")
for chr in set1:
    print("{} occuers {} times ".format(chr, example.count(chr)))
d={}
for chr1 in example:
    d[chr1] = d.get(chr1, 0)+1

print("count by using dictionary")
for k,v in d.items():
    print("{} occures {} times in example string ".format(k, v))

print("Count by using list")
output = []
for ch in example:
    if ch not in output:
       output.append(ch)
print(output)
for ch1 in output :
    print('{} occures in {} times'.format(ch1, example.count(ch1)))

