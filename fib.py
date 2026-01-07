
#fibonacci series using iterators

n=int(input("enter an integer: "))
print("fibonacci series using iterators")
def fib(n):
    a,b=0,1

    for i in range(n):
        print(a,end=" ")

        a,b=b,a+b
    print()
fib(n)

#fibonacci series using recursion
print("fibonacci series using recursion")
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
   
for i in range(n):
   
    print(fib(i),end=" ")
print()

