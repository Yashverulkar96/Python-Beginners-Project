import random
passlen=int(input("Enter the password length"))
allowedchars="abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p =''.join(random.sample(allowedchars,passlen))
print(p)
