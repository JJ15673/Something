import random
znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dl = int(input("długość hasła:"))
password = ""
for i in range(dl):
    password += znaki[random.randint(0,len(znaki))] 
print(password)
