# Factorial 
n=int(input("Enter a number :"))

def factorial (number):
    val=1
    for i in range(1,n+1):
     val*=i
    print("Factorial of ",n," is :",val)

factorial(n)


