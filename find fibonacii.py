#a = eval(input("enter the number ti be find =  "))
n = eval(input("enter the number to be find = "))
x = 0
y = 1
sum = 0
while sum <= n-1:
    sum = x + y
    x = y
    y = sum
if n == sum :
    print("it si fibonacii")
else :
    print("not")



