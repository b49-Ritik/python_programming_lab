n = int(input("enter the length = "))
for i in range(0, n+1):
    ch = 65
    for j in range(0, i+1):
        print(chr(ch), end = " ")
        ch += 1
    print("\r")