p = eval(input("enter the amount = "))
r = eval(input("enter the rate = "))
t = eval(input("enter the time = "))
a = p * (pow((1+r)/100, t))
c = a - p
print("compound interst is = ", c)