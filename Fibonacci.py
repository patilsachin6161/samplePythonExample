def fib(n) :
    a, b = 0,1
    while(a<n):
        print(a, end=' ')
        a, b = b, a+b

fib(10)

def fibb(n):
    a,b= 0,1
    result =[]
    while a<n :
        result.append(a)
        a,b = b, a+b
    return result

print("Fiboncci for 1 to 100 ",fibb(100))