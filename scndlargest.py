l1 = []
n = int(input("enter the no of elements = "))
for i in range(0, n):
    ele = int(input())
    l1.append(ele)
s = l1[0]
for i in l1:
    if s < i:
        s = i
l2 = l1
l2.remove(s)
s2 = l2[0]
for i in l2:
    if s2 < i:
        s2 = i
print("the second largest element is", s2)