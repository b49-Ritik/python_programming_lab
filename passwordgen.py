
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%*!"
all = lower+upper+numbers+symbols
length = int(input("enter the length of the string = "))
password = "".join(random.sample(all, length))
print(password)