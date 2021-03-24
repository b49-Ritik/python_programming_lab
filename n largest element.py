l1 = []
n = int(input("enter the no of elements = "))
for i in range(0, n):
    ele = int(input())
    l1.append(ele)
r = int(input("enter the number of largest elements  = "))
s = l1[0]
l2 = []
for i in range(0, r):
    max1 = max(l1)
    l2.append(max1)
    l1.remove(max1)
print(l2)







