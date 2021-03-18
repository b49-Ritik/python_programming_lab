n = int(input("enter the number = "))
x = 0
y = 1
print(x, y)
for i in range(2, n):
    sum = x+y
    print(sum, end = " ")
    x = y
    y = sum
