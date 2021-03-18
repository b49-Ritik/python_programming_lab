n = int(input("enter the number = "))
num1 = n
count = 0
while n!=0 :
    count +=1
    n = n // 10
n = num1
s = 0
while n!=0 :
    rem = n % 10
    s = s + pow(rem, count)
    n = n//10
if s == num1 :
    print("number is armstrong")
else :
    print("number is not a armstrong")




