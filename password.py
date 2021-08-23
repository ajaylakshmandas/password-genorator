import random 
password = int(input("enter a no of charesters"))
s = "1234567890ABCDEFGHIJKNMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz@#$%^&*"
p = ''.join(random.sample(s,password))
print(p)
