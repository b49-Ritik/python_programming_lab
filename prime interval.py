n1 = eval(input("enter the start = "))
n2 = eval(input("enter the stop = "))
for i in range(n1, n2+1):
    for j in range(2, i):
        if i % j == 0 :
            break
    else:
        print(i, end = " ")

