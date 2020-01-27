
list1=[x for x in range(10)]

print(list1)

h_letter = [letter for letter in "HUMAN"]
print(h_letter)

#List comprhensions VS Lambda

letter1 = list(map(lambda x:x, "HUMAN"))
print("List using Lambda ", letter1)

#Lambda with Mapping list
test_lambda = list(map(lambda x:x, list1))
print("&&&&&&&&7 test lambda ",test_lambda)
#List Comprehensions using condtion
conditonList = [x for x in range(20) if x%2 == 0]
print("Condition with list Comprehension ", conditonList)

#nested if with List Comprehensions
num_list = [no for no in range(50) if no%2 == 0 if no%5 == 0]
print(num_list)

#if else with list Coprenhensions
even_odd_list = ["Even" if no%2 else "odd" for no in range(10)]
print("List Comprehension with If Else  ", even_odd_list)